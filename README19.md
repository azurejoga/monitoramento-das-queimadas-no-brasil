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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39e71408-9254-3b10-9dad-4a28f179f84f | -15.8955 | -43.4523 | 2025-05-27 05:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a85954ea-3962-3720-91ec-032ae6334e53 | -15.8955 | -43.4523 | 2025-05-27 05:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 68c8e099-bb31-3b61-bc9f-1f7616972db6 | -18.8484 | -53.6035 | 2025-05-27 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 434.8 |
| 1710643d-9199-3db5-8fc9-fd9257f4f2fd | -18.8284 | -53.6067 | 2025-05-27 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 43385136-25b8-39f6-b1d4-370aff40fe32 | -18.8479 | -53.6251 | 2025-05-27 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 307.9 |
| cfee81dd-9730-3fb2-bfed-a5513ae4df23 | -18.8488 | -53.582 | 2025-05-27 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 7abef876-d71d-3f18-9fe7-08542a0e1669 | -18.8679 | -53.6218 | 2025-05-27 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 275.5 |
| 9ea1e4ae-74e8-3101-8750-3c31e55dfb63 | -18.8684 | -53.6003 | 2025-05-27 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 359.4 |
| 6b3dc99d-18a3-3739-9c94-652c1a8ef216 | -18.8484 | -53.6035 | 2025-05-27 05:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 283.2 |
| 8b95e313-02de-38f8-8c7e-6f8030e98414 | -18.8684 | -53.6003 | 2025-05-27 05:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 242.8 |
| ab89e8df-772c-3d44-b034-ec3146aa1dce | -18.8679 | -53.6218 | 2025-05-27 05:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 712fd77e-e30e-394f-a1f2-27f7dbf03835 | -18.8479 | -53.6251 | 2025-05-27 05:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 539d4c1a-441f-333e-bd79-ff838ded28f4 | -18.8488 | -53.582 | 2025-05-27 05:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 82f08ea4-3ea6-3c85-90ae-43371173bd76 | -8.31887 | -55.11812 | 2025-05-27 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3ac8aa8-6868-3d3c-923b-61a112896220 | -11.81581 | -55.07518 | 2025-05-27 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d035f03-50ce-3577-b892-3a333dcfe700 | -10.84339 | -54.01748 | 2025-05-27 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 231fb97d-73d7-3e82-b1fc-23f858bba4db | -14.03959 | -55.13297 | 2025-05-27 05:44:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 998c249a-a042-313f-b1a4-58c9f7b8ab83 | -10.82768 | -56.95522 | 2025-05-27 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17b309c3-b27b-3008-903f-20da0de2bb70 | -12.13013 | -54.66926 | 2025-05-27 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83b34cd0-386b-33e4-be14-dc7a85e73bc9 | -14.04535 | -55.13869 | 2025-05-27 05:44:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd027742-62c4-38f6-84b3-00d7dcc1f1f4 | -10.84276 | -54.02291 | 2025-05-27 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94a83894-ef1e-38fe-b1cd-853b8b81a71f | -14.0428 | -55.13304 | 2025-05-27 05:44:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bcbe2218-8bcf-3d53-8e61-f3770f3ee0c9 | -12.11747 | -54.66737 | 2025-05-27 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20cb5e4f-c7a7-3cda-a32c-2c99ba1c34ca | -11.63155 | -54.94162 | 2025-05-27 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 475c65e6-e36a-3736-ad6d-6e1211711e40 | -11.81549 | -55.08051 | 2025-05-27 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9096db82-82bc-38b4-8b3b-80070e5d4951 | -11.62536 | -54.94074 | 2025-05-27 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb4587d0-435f-3fad-8586-ce293a79c81c | -10.82913 | -54.02663 | 2025-05-27 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e585e33-a2a9-3bbd-b41a-0079fc1514f3 | -11.62591 | -54.93585 | 2025-05-27 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d30d3502-85db-371f-81e7-5d6a053d5001 | -10.82326 | -54.0203 | 2025-05-27 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b12e622-e8f1-336e-97fd-9f3034cfb233 | -11.81607 | -55.07568 | 2025-05-27 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a286798d-5989-372c-b7a2-b94960a68724 | -11.13863 | -53.9189 | 2025-05-27 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2392f00-670f-39be-9888-64f9a182cdac | -12.1238 | -54.66827 | 2025-05-27 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 296f1f0a-7f80-3c09-be92-6d9c75d49f49 | -11.81527 | -55.08003 | 2025-05-27 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c5bf397-2f24-388b-abfc-f18ed3e6f208 | -10.83563 | -54.02745 | 2025-05-27 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29106692-4a4e-30f7-9a74-95414c2af845 | -14.04335 | -55.12774 | 2025-05-27 05:44:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50460eca-83cc-35b3-80ed-0989e3e5da62 | -11.82197 | -55.0761 | 2025-05-27 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fe4fe88-6235-3408-b3c0-a9a34bfb36c8 | -11.82222 | -55.07657 | 2025-05-27 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 038b22b4-d716-3ae3-b6f5-0100de843848 | -11.63222 | -54.94426 | 2025-05-27 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 528a1414-a1f8-350d-93ef-c9d408570e91 | -11.13798 | -53.92462 | 2025-05-27 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb812abb-002c-3d43-aa79-9e5d90e5576b | -14.04859 | -55.13892 | 2025-05-27 05:44:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64b1ffe7-d645-365c-b077-d72e35d2c2d7 | -11.39999 | -52.95251 | 2025-05-27 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2ecbb4a-ac1d-3b55-b7c9-cb7e7680e86b | -10.83307 | -56.956 | 2025-05-27 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfb9087e-05eb-3f0b-b165-75b8792e6bf4 | -11.62659 | -54.93862 | 2025-05-27 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bd8ea2b1-a4f8-301c-ae85-09c1f52940d3 | -10.82724 | -56.95869 | 2025-05-27 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fbc0547-ab12-35f2-a437-290156ae34f0 | -10.83501 | -54.03277 | 2025-05-27 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abcdd321-99d0-3ff3-bbf9-89e1b06dcba8 | -14.04018 | -55.12765 | 2025-05-27 05:44:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2f1ece4-9adf-31ed-9e2d-096495857e6e | -11.82142 | -55.08099 | 2025-05-27 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef8da5ac-f068-327f-8d30-eec6980f33f1 | -10.82264 | -54.02572 | 2025-05-27 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e448428a-2f2e-32df-a4e6-44f4f228c96b | -12.16896 | -54.26334 | 2025-05-27 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d718934-f0d5-306b-8a09-f1b4e2172c47 | -22.439 | -48.4226 | 2025-05-27 05:50:00 | GOES-19 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 5ff3092b-f7d1-34b9-af87-aaa86bd025f8 | -22.4181 | -48.4278 | 2025-05-27 05:50:00 | GOES-19 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 59ac4f7d-94e7-39a0-995b-a6345b680de6 | -22.4174 | -48.4514 | 2025-05-27 05:50:00 | GOES-19 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 1bd72d17-a1f7-3563-a90f-031e8f168dfb | -22.4383 | -48.4462 | 2025-05-27 05:50:00 | GOES-19 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 105.1 |
| f496e920-21c6-3373-a073-51f2cae79f7f | -18.8479 | -53.6251 | 2025-05-27 06:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 186.1 |
| d9509a0e-9cc8-3862-9952-bc498a8a0a1b | -18.8488 | -53.582 | 2025-05-27 06:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 507aef28-4a48-3922-8750-5ee183f01b0d | -18.8684 | -53.6003 | 2025-05-27 06:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 04fa1b91-0bb1-3b1a-affa-5d4061789aeb | -18.8688 | -53.5788 | 2025-05-27 06:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 3c7c09ac-48bb-35f3-bfc9-50af6bf92572 | -18.8679 | -53.6218 | 2025-05-27 06:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 131.4 |
| df426c51-ab48-3d0f-b032-369106e4d76e | -18.8484 | -53.6035 | 2025-05-27 06:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 344.9 |
| f94ce7b6-36ed-39ff-9b4d-9ffd43552bad | -18.8484 | -53.6035 | 2025-05-27 06:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 144.6 |
| db6f3cd1-1ead-3ccf-9cca-fb11e3d4f234 | -18.8479 | -53.6251 | 2025-05-27 06:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f0507432-b57e-3055-83b2-b9d89a32674c | -18.8284 | -53.6067 | 2025-05-27 06:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 3732b082-8797-3549-9a7d-5427a795b140 | -18.8684 | -53.6003 | 2025-05-27 06:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 66.8 |
| fd79b241-dea4-3dfb-b577-20ce13b02bbd | -18.8484 | -53.6035 | 2025-05-27 06:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8b67e27c-c023-3836-aaf4-5fc4df8a0562 | -18.8484 | -53.6035 | 2025-05-27 06:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 82.7 |
| bfb8589d-7d8c-3b51-8554-7ba77bc513a7 | -18.8684 | -53.6003 | 2025-05-27 06:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 73.4 |
| decc65dd-d8f8-3189-8bdd-f6b264586330 | -18.8484 | -53.6035 | 2025-05-27 06:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 143.1 |
| bf7860ea-0d0c-3241-bac9-99ba289a2f67 | -18.8684 | -53.6003 | 2025-05-27 07:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 4f039404-7ccf-3763-adf0-2a743963390e | -18.8484 | -53.6035 | 2025-05-27 07:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 70.6 |
| bb29d3ca-dc3b-3dc7-8be1-4c2230dbb02d | -19.444 | -54.7708 | 2025-05-27 07:30:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 78bd6529-beae-3e71-9016-8aa43886aab0 | -19.444 | -54.7708 | 2025-05-27 07:40:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 78615723-4985-3f18-b830-0db7b3cd4251 | -19.444 | -54.7708 | 2025-05-27 07:50:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 0eb7a103-c257-3e40-842f-cfaa17e3d915 | -19.444 | -54.7708 | 2025-05-27 08:00:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 3d7b01aa-73cf-3a53-b332-b9d864767fd9 | -18.8684 | -53.6003 | 2025-05-27 08:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7c1216d0-8635-39bc-9518-2eaa12e19b55 | -18.8479 | -53.6251 | 2025-05-27 08:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 57.6 |
| cbd38c8e-a603-314c-a6a6-958ee3355618 | -18.8679 | -53.6218 | 2025-05-27 08:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 68.3 |
| bafa79f9-3023-3c91-808a-c0a31de0d68e | -18.8484 | -53.6035 | 2025-05-27 08:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 87.3 |
| e85f279e-64ba-3918-bc31-f647ab11400a | -18.8684 | -53.6003 | 2025-05-27 08:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1131e953-eadb-3949-878a-6d6454123724 | -18.8679 | -53.6218 | 2025-05-27 08:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 301.9 |
| 354f720a-ca80-3cdd-b835-7f05ea0490ef | -18.8684 | -53.6003 | 2025-05-27 08:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 337.6 |
| e7bc6dae-f0c4-3c22-a4f2-5b01e32a8b64 | -19.444 | -54.7708 | 2025-05-27 08:40:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 20f3a1fe-50f4-3679-aae8-c4cbee41d6bb | -18.8479 | -53.6251 | 2025-05-27 08:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 842c034e-6a51-3018-ab8b-f296d48171ae | -18.8488 | -53.582 | 2025-05-27 08:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 76.3 |
| fcd46cb2-fea8-3a16-9113-2b36d3394470 | -18.8284 | -53.6067 | 2025-05-27 08:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 60.0 |
| c365783d-c73c-3d32-9d33-0c66fe8c0970 | -18.8484 | -53.6035 | 2025-05-27 08:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 346.9 |
| ae89e89d-7bf8-335c-9080-b2e9a34e46ba | -18.8284 | -53.6067 | 2025-05-27 08:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 28d9042b-4d87-32f6-bc11-4f676f613c7a | -18.8484 | -53.6035 | 2025-05-27 08:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 421.2 |
| e7bea28a-b58c-3c76-9a84-f70743b5d6e1 | -18.8679 | -53.6218 | 2025-05-27 08:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 406.4 |
| 8efdaf17-df8b-3087-b502-cc4efe559bf6 | -18.8479 | -53.6251 | 2025-05-27 08:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 290.5 |
| 54128dee-8da2-3b74-9428-8c7a2d068267 | -18.8684 | -53.6003 | 2025-05-27 08:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 324.2 |
| 54a01f1c-bad4-360a-b52a-ff994191824b | -18.8488 | -53.582 | 2025-05-27 08:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 46856678-238a-3648-94d8-20e6a2b700f1 | -18.8484 | -53.6035 | 2025-05-27 11:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 696.3 |
| ab94e51d-f03f-3f67-b72f-73bd3cacac60 | -18.8284 | -53.6067 | 2025-05-27 11:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 88179cf2-5610-3cfc-9248-e4a5903cf8f3 | -18.8479 | -53.6251 | 2025-05-27 11:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 479.8 |
| cf951a3b-218a-3417-8395-0d2a48f43cc0 | -18.8684 | -53.6003 | 2025-05-27 11:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 511.3 |
| 36a7d21d-c979-31a6-b200-8d66a4991b5f | -18.8284 | -53.6067 | 2025-05-27 11:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 4c0b3e44-cea4-3b4d-9a04-7c39cc491095 | -18.8484 | -53.6035 | 2025-05-27 11:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 949.2 |
| 44e0d558-5941-3ee4-accc-150f9ed7347c | -7.9827 | -50.7201 | 2025-05-27 11:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 7b5fc848-5613-3c4f-9026-5004806d1444 | -18.8479 | -53.6251 | 2025-05-27 11:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 560.4 |
| 86bfb4ed-59d7-33a8-abc2-f2695ba7eef6 | -18.8679 | -53.6218 | 2025-05-27 11:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 589.0 |


[Clique aqui para ver as próximas entradas](README20.md)
