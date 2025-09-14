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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf96dc65-20dd-3aba-92dd-8e42ced26706 | -13.89805 | -48.30582 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c03aadd9-29f9-330b-99de-4b41134fb8d3 | -19.26155 | -51.4291 | 2025-09-14 04:42:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc0230be-cee8-35d7-baa8-1fc108015107 | -18.98019 | -48.59397 | 2025-09-14 04:42:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97a22ef9-2d8f-3e46-9d7c-1cc28c868204 | -18.95238 | -46.31451 | 2025-09-14 04:42:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53694fcc-bb77-389d-a0cf-5af671012ca2 | -15.58855 | -54.73797 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4606a123-2d61-370e-b798-0f7eaa32187f | -14.20037 | -46.17584 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 09c03e75-148d-364d-b755-6abcae7ab6f5 | -15.09302 | -52.49727 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5d654b9-eaef-373b-8894-ded28587a915 | -17.83753 | -50.41619 | 2025-09-14 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d09d7f2c-a76e-3203-ba36-ccc47f488072 | -12.66631 | -54.69016 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0032bf16-8d41-3938-a822-2d5e5ee773f1 | -15.08373 | -52.47005 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3899b7f-0c12-3e1c-b66c-47a8cae79255 | -18.15774 | -49.19405 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2c09f100-b008-3012-be65-9c83851f8a22 | -16.44498 | -45.68776 | 2025-09-14 04:42:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2cd8601-5902-3791-9db1-011b3651fdc0 | -15.76657 | -52.22411 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ed65ca06-9c39-3471-9b27-d8304101f852 | -16.65929 | -49.78371 | 2025-09-14 04:42:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 40c276c1-bcfd-3f56-9739-1864dca6b24f | -14.48285 | -47.33533 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| daffa8aa-cbf2-35fb-b0d4-9b7f6d35ec87 | -16.54656 | -49.22079 | 2025-09-14 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71025b1f-9c10-3d95-b568-d288b2056637 | -15.77706 | -52.22219 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab997812-b9f5-347c-8161-edf5f357349f | -12.68915 | -54.68967 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 29a87dad-840c-3088-8f12-17e56b744031 | -12.94709 | -54.73941 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e63e167f-7252-3723-8672-1ab4c8e4d219 | -17.94337 | -42.8395 | 2025-09-14 04:42:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50e8ad78-561e-3e69-a4b5-79e76f87d270 | -14.15652 | -46.259 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 19456b46-eb5d-360f-928c-afc06baa63e5 | -14.82717 | -48.40068 | 2025-09-14 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 648784ca-7bc5-3da9-aeee-cdc0323ce10f | -15.63861 | -51.3465 | 2025-09-14 04:42:00 | NOAA-21 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22256280-6312-3eb4-bb11-96be6c97e2eb | -16.50236 | -42.1299 | 2025-09-14 04:42:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c58f5cb0-5129-357e-b342-648008f00b26 | -15.30182 | -49.53649 | 2025-09-14 04:42:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e9d2f85-d940-3398-aa89-1168d6a3d638 | -14.62156 | -52.03951 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 918157c7-cd9b-3454-8aed-3149070c25fa | -18.59255 | -47.19765 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 42db8c65-bd79-31b6-aa3b-ddcb1f9f0e75 | -15.80251 | -52.21172 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8388e7d8-37ca-3990-b14b-ad120ae618ed | -16.66039 | -49.77621 | 2025-09-14 04:42:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 576dfc2f-bdfc-30d2-9e35-831a6c8e4678 | -16.30402 | -50.52657 | 2025-09-14 04:42:00 | NOAA-21 | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2146a3c1-5cff-34ef-9600-2556d87acc64 | -14.47044 | -47.31347 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b780b9e3-7931-368b-9a5f-0d11975a1660 | -14.43911 | -43.2084 | 2025-09-14 04:42:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9b050399-286e-3b23-be3b-498e07707345 | -12.66858 | -54.67691 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a76a68cc-46ad-34ce-88cd-29ac0a452e52 | -15.77212 | -53.48015 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38757e52-309f-31ba-aded-6a9b650a4484 | -12.68765 | -54.69849 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| e6c9611a-db61-3f9d-9ef1-5b2d0eb85eba | -15.00724 | -50.13368 | 2025-09-14 04:42:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 97c6d7b6-cce5-39f7-a631-9b8513dd3962 | -15.77951 | -53.4776 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 49334e40-f5c9-3dff-911d-ae7ef27f5cb3 | -15.76133 | -53.48221 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8cfff05-52c3-38d0-bc38-db9377054fe0 | -15.14857 | -55.75978 | 2025-09-14 04:42:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce2bb800-b071-384a-ac44-4ff4910ea618 | -15.103 | -52.49895 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0b5d6d3-de47-3b1d-924d-f62ee5f5667f | -17.83357 | -50.41947 | 2025-09-14 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 425a00db-595d-336f-8a21-78118b931a67 | -15.91656 | -49.97739 | 2025-09-14 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f822140e-99c7-3681-98c1-8b1292c8aee7 | -15.58407 | -47.1311 | 2025-09-14 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 816cf0f7-caba-3fa8-9f5b-662c329072c5 | -17.1338 | -48.50948 | 2025-09-14 04:42:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b63cf457-edc1-3669-8b3a-62e4e19e7388 | -15.15918 | -52.46795 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4f50a8af-b088-338c-9622-7e97b61df442 | -16.65809 | -49.76797 | 2025-09-14 04:42:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e64c676-490e-3ac4-94b3-e62711d18c5c | -15.77612 | -53.47701 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5ea4cf8e-e4c7-32bd-a814-0e53afc718fb | -17.34337 | -46.65713 | 2025-09-14 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29ceeab7-122a-3e82-8bf3-0445448916c0 | -15.68829 | -49.91114 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe1185b5-59d7-3c73-887e-d5eb3a3303d2 | -14.51017 | -53.88651 | 2025-09-14 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b9896b5-2fd0-30c6-bcb0-374f9e1c64a0 | -14.19586 | -46.17884 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2c70384-4afd-36f6-a176-651a588f11a3 | -14.31298 | -46.07926 | 2025-09-14 04:42:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ecfe58a6-3043-369a-9058-e7d3ebe98354 | -15.8638 | -51.84472 | 2025-09-14 04:42:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7568b128-e4b5-3833-aea6-a7afe1316b54 | -13.90878 | -48.30715 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca8a317b-78c7-3212-9f5d-65013192d154 | -18.08722 | -42.93441 | 2025-09-14 04:42:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 99573410-b403-3dfe-918c-96172556c3dd | -18.16013 | -49.20294 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| dc9832e6-51a7-3684-a946-b8feb8e9493b | -17.29923 | -46.11342 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 042d9802-9a18-398c-a2aa-057cc19eeea8 | -14.43484 | -43.20201 | 2025-09-14 04:42:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5cd1c005-8a42-3a83-9599-bd24a3124fe8 | -15.18501 | -50.10895 | 2025-09-14 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 28dcee00-618e-3113-9e34-0e821a3ef714 | -16.70865 | -54.95265 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f238743d-2195-3a05-a677-75721f776aa5 | -15.80753 | -52.2015 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6093b332-5360-35ee-9bc4-5700d3887296 | -16.54928 | -49.19747 | 2025-09-14 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de4c0f9d-9385-3c3c-a143-c15973a1d100 | -14.99626 | -50.12501 | 2025-09-14 04:42:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f683407-ca56-3cef-a593-5fb7aa958ab5 | -16.87185 | -49.34681 | 2025-09-14 04:42:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcd72d00-f304-3209-99e8-e923fc67c357 | -14.81926 | -48.76274 | 2025-09-14 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3aa1a2cb-da40-3f92-8f02-d506e79a50c3 | -15.11756 | -52.47204 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fa5c2ff-64b1-3bad-9849-98b71f92035d | -17.31912 | -46.09208 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c13cb0a6-2eca-3510-bc97-4333908c0240 | -12.66122 | -54.6756 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4ecf1a85-a58e-33e9-97cd-05a8bb1b6f5a | -15.75897 | -49.78565 | 2025-09-14 04:42:00 | NOAA-21 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9b55b1c-9977-34e4-9c3a-0bd8823f1698 | -14.99682 | -50.12133 | 2025-09-14 04:42:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4135e703-6b88-32f6-9a97-3e9adfc23d07 | -18.02148 | -46.96112 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7c206ea-7c44-3909-a781-d7302f274659 | -14.76217 | -60.21849 | 2025-09-14 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e845a34f-7deb-3eb2-8de8-8d62d9a4230a | -12.69576 | -54.69541 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| af92bb67-516f-3295-ade6-c3beb267328d | -14.31249 | -46.08297 | 2025-09-14 04:42:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df6a2076-dda2-3147-b38a-39cbb5f53797 | -18.26438 | -46.94339 | 2025-09-14 04:42:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f6a7dffe-8b4f-349c-a919-06925e068bda | -12.68547 | -54.68902 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 0e9880c6-17ca-3d44-8757-d37ae81a6eda | -18.01489 | -46.94844 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ec123d1-e34f-317f-9230-20477d2012e0 | -18.47305 | -46.93174 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14b17baa-cf0e-3d86-b367-fb62cba90271 | -14.63149 | -52.04117 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e48000fe-1af0-3723-8aa9-d854f8992d09 | -16.52992 | -43.75431 | 2025-09-14 04:42:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7ac16b9-2557-3c3b-a348-a0d02cc148ad | -17.35061 | -46.66572 | 2025-09-14 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a871678-dfef-31df-a7b2-5c96f37af85f | -12.70462 | -54.68791 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b2159731-b1a3-34e7-917a-ab7da196d64f | -12.68991 | -54.68525 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 2c5e9f76-2251-3cf1-b4a1-c1b2abb7a8c3 | -15.93184 | -49.96802 | 2025-09-14 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a555aef2-e790-3d24-98f9-bb65a9f194af | -17.34699 | -46.66149 | 2025-09-14 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a856e472-d8ae-3ee3-ad73-0f08bb12e592 | -17.94375 | -42.83595 | 2025-09-14 04:42:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61783f3c-bfe6-3d9e-8e12-d348375c7c3a | -16.32838 | -51.52656 | 2025-09-14 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6fccfcf-6c1b-37fa-b732-a6dfe5f177db | -16.71146 | -54.95764 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 831ab0c2-79e1-33c0-b7e9-62b48325c951 | -14.95504 | -55.95065 | 2025-09-14 04:42:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccdc801e-2455-3fae-8093-bbd8aefe104d | -15.13465 | -52.49319 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0c9d1c7-bcec-31bd-9245-b93693d34f65 | -18.84901 | -50.96719 | 2025-09-14 04:42:00 | NOAA-21 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 408a4975-b0ae-3d35-8c60-68a45ab5f4b7 | -12.67518 | -54.68267 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 56c93d1c-f1ae-351e-bdad-88822c059b6e | -12.68113 | -54.67004 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e074c84f-2f22-3de0-9bc1-91ea26ceaf6a | -14.75717 | -60.21724 | 2025-09-14 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9aab6b3-1d1c-3665-9647-0dd82ce19333 | -12.6869 | -54.70291 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a7d88477-faa5-38b0-87d5-c4a26ce8212c | -15.41202 | -52.97068 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0cbb6a1-e62e-3e51-8fa8-f269c1f79ae8 | -17.83413 | -50.41563 | 2025-09-14 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71d7c6ce-3710-3e13-a0d8-97e9a1669608 | -12.70529 | -54.70631 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e8c85dfb-1009-3924-a728-572bab5de7af | -15.78618 | -52.27159 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 826d5c86-3768-34fa-b7bb-4ac652394459 | -15.66425 | -44.69113 | 2025-09-14 04:42:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README47.md)
