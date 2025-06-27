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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e033f82-391b-3a7d-bdf7-cca89b340855 | -6.9602 | -42.9052 | 2025-06-27 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 372.1 |
| 57e4cc41-1f99-389d-b99b-98e81fb15a5e | -12.424 | -43.7274 | 2025-06-27 00:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 1d586b7d-a24c-3af1-a4d6-83de8c75b20f | -11.559 | -52.117 | 2025-06-27 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 207.1 |
| 9cfddd7c-a558-3a6d-8d6c-ab5e46c2715c | -6.1789 | -48.0929 | 2025-06-27 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 332.1 |
| 3a9e7e1b-70b2-3210-aea5-5a0ae42cf86b | -8.6284 | -51.5716 | 2025-06-27 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| c0bd41e6-0678-3ce9-91c4-411e7971fcc5 | -10.2942 | -57.1182 | 2025-06-27 00:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 1a7c34da-e2cc-3282-8ca4-f8f557c3ecca | -6.1602 | -48.0941 | 2025-06-27 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 5f9e7daa-15cf-3b24-b7ba-40ba7bf3156c | -6.9793 | -42.8798 | 2025-06-27 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.1 |
| 9944fe3b-bc39-37a4-aafc-7e596fa5cb49 | -11.5776 | -52.136 | 2025-06-27 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 632f841c-303c-3fbc-8b39-a9f64c21dad3 | -9.0651 | -49.4151 | 2025-06-27 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8968bdd4-a157-359e-baa6-eb02ea65d520 | -11.5779 | -52.115 | 2025-06-27 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 517.9 |
| 4e80fe56-32ba-3812-b298-7a32b32641ba | -8.6097 | -51.5731 | 2025-06-27 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 209.2 |
| 9a263a5b-7a14-38bf-92d9-5fe5391d44f1 | -7.2217 | -43.0917 | 2025-06-27 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 383a9b3f-bcca-34be-a486-844653b85819 | -6.9416 | -42.8834 | 2025-06-27 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 779335e8-0b59-3ba0-a2b1-94ff33ececa9 | -6.9414 | -42.907 | 2025-06-27 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 8ff8888f-7b03-38e0-a3e7-4519f8127ca1 | -11.5592 | -52.096 | 2025-06-27 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 24f55253-387f-3d40-a543-e826687d7f79 | -11.5782 | -52.094 | 2025-06-27 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 154.9 |
| aeedb1c5-30e3-30a7-b7d8-8db12bdd1e5a | -10.2941 | -57.138 | 2025-06-27 00:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 2c27346c-fbbd-30a3-96b9-8a5bff4b0c00 | -11.3616 | -48.7142 | 2025-06-27 00:40:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 32aa1c30-0951-3d62-bbf2-aa286a2f53b4 | -11.0644 | -55.3757 | 2025-06-27 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 4a69263f-d297-3fee-8f3a-5684fc790ad4 | -11.5969 | -52.113 | 2025-06-27 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 5a0e8894-544b-33cc-8cb9-75140b5e402f | -12.0248 | -47.7702 | 2025-06-27 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 4a559028-0377-3f55-b42e-331d687bd604 | -6.9605 | -42.8816 | 2025-06-27 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 289.5 |
| 411a1010-f7fd-3ea8-a0a6-57e82e073aaf | -12.424 | -43.7274 | 2025-06-27 00:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 51ce9b71-3ce4-3650-a315-019dd21f3e96 | -6.9602 | -42.9052 | 2025-06-27 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 368.3 |
| fd03a8f3-f57c-3803-9132-bcde34abfee0 | -7.2217 | -43.0917 | 2025-06-27 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| f5e70135-d8dc-374f-b343-99649ab7486b | -6.1602 | -48.0941 | 2025-06-27 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| a27675d2-085c-325e-b091-5686d2d87705 | -6.9791 | -42.9034 | 2025-06-27 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| af643697-0163-3ff7-ac23-9e9cf35d645c | -6.9414 | -42.907 | 2025-06-27 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| eaab22ed-3dae-387d-9a45-664801c00fa5 | -6.1791 | -48.0712 | 2025-06-27 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 219.2 |
| 30287da3-f35e-3f35-bf29-df1913ff258c | -9.0648 | -49.4366 | 2025-06-27 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 046c1712-32a8-30b8-9866-dbfad8fdbb97 | -8.6284 | -51.5716 | 2025-06-27 00:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 169.1 |
| 81a3e8db-f42f-32fe-a579-dd577c24c40a | -11.0644 | -55.3757 | 2025-06-27 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 725b3262-e172-3b57-890d-0b62bde31662 | -8.6097 | -51.5731 | 2025-06-27 00:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 273.8 |
| f12801d6-4b11-3938-9989-00e2889af481 | -6.9793 | -42.8798 | 2025-06-27 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| cbea496b-763c-3471-8652-2ae4ea2cc138 | -6.9605 | -42.8816 | 2025-06-27 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 301.1 |
| 1a69b0f3-e6f0-3dad-9424-7e8dd8ae8509 | -10.2941 | -57.138 | 2025-06-27 00:50:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 95f36aa9-6301-3cb5-80bd-f8bbf23a2c3d | -8.6094 | -51.594 | 2025-06-27 00:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 3ab8d58f-2ce4-36ef-8efb-fd2d7ba5d36c | -9.0651 | -49.4151 | 2025-06-27 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 9c0a226c-adc6-3963-866f-9fa8591c6510 | -6.9416 | -42.8834 | 2025-06-27 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| e3de9865-4898-3905-9f18-889bc93afafc | -14.4476 | -48.8619 | 2025-06-27 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| fcb6040d-a341-31d9-930c-629f08624a34 | -7.2219 | -43.0682 | 2025-06-27 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| e9ddfd37-ea33-3cc1-917b-3c0a59ec65b2 | -6.1975 | -48.0916 | 2025-06-27 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1ef072bf-1d92-3b00-9dd3-00b6cd45d6d9 | -6.1789 | -48.0929 | 2025-06-27 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 341.8 |
| 2c89c82f-2a32-3d15-990f-4ad82fa399b7 | -10.2942 | -57.1182 | 2025-06-27 00:50:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 078d4f54-f151-35b9-990d-a6f40f2421d0 | -7.2031 | -43.0701 | 2025-06-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 5d791f68-c296-39c1-a281-d31f1c9bc19f | -12.424 | -43.7274 | 2025-06-27 01:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 17a794dd-7d69-3653-90e2-556c87c19f13 | -6.1604 | -48.0724 | 2025-06-27 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| db61c2f5-0a3c-3935-ab83-cf0580fcaf24 | -6.9414 | -42.907 | 2025-06-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| cadccca9-57aa-380b-b7b9-f2926638428c | -6.9416 | -42.8834 | 2025-06-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| b6a02cb4-d15a-3709-ad04-91e5c4853a73 | -6.1791 | -48.0712 | 2025-06-27 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 182.0 |
| e8a6d0f1-46af-3da8-bcdd-3c476135fe54 | -6.9605 | -42.8816 | 2025-06-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 324.6 |
| 1f8d8226-d5a7-34c5-8737-63fd73959b5c | -6.9602 | -42.9052 | 2025-06-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 332.3 |
| 7a3b0b8b-1688-32f1-82fb-1e746ca99e6e | -8.6286 | -51.5507 | 2025-06-27 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| eec73ae4-2fb5-3858-9d47-d0c67b373bbf | -10.2942 | -57.1182 | 2025-06-27 01:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| f1571cb2-0405-3ba6-9709-d2e8a180cdd0 | -10.2941 | -57.138 | 2025-06-27 01:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 22cf7dc2-1ab4-3508-84d9-7784d7b7ef1c | -7.2219 | -43.0682 | 2025-06-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 68ed732f-962a-3815-ad79-7b255ecae2d8 | -8.6094 | -51.594 | 2025-06-27 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4003ea59-54ac-3bcb-b308-83e0e0d4211a | -6.1602 | -48.0941 | 2025-06-27 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| a9078bcd-9c1e-3f90-a1a6-4f5fcad6b9ed | -6.1789 | -48.0929 | 2025-06-27 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 330af1ce-3078-39e3-a0b8-04cb067e32bc | -6.1975 | -48.0916 | 2025-06-27 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 88fad597-def3-3d1c-b395-7d9d126fde5c | -7.2028 | -43.0936 | 2025-06-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 651fd986-2b41-3591-ba81-1ae347e4801e | -6.9793 | -42.8798 | 2025-06-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| 91d48297-3ffb-317c-a9ff-bd2630e787f6 | -9.0648 | -49.4366 | 2025-06-27 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 3f3aaa6d-4e05-3233-b955-da19dd66480d | -8.6284 | -51.5716 | 2025-06-27 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 177.0 |
| 534a2818-8dcf-348c-bd80-46a4cd22f98c | -6.9791 | -42.9034 | 2025-06-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.5 |
| eb58f3fe-178c-36cc-b6b3-cb75415c0047 | -11.0644 | -55.3757 | 2025-06-27 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 054b89eb-94a7-38ea-8862-dc95773fc063 | -8.6097 | -51.5731 | 2025-06-27 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 270.1 |
| 428cc2ac-f585-3c3b-8d91-168e53f82fc2 | -9.0651 | -49.4151 | 2025-06-27 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| dccebb14-6f4b-32c7-93c3-611e77a0bd68 | -8.6099 | -51.5522 | 2025-06-27 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| b9e5fc5c-d8f4-3c0f-8ad3-720686eb32de | -7.2217 | -43.0917 | 2025-06-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 2de2e25b-5f3d-350d-9288-f1acc4bcaf78 | -6.9605 | -42.8816 | 2025-06-27 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 286.0 |
| f00c194a-51b9-34a8-b8ca-caef5ba3cdeb | -7.2219 | -43.0682 | 2025-06-27 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 3b7a13b5-2834-320b-b6a7-9a41427dac74 | -6.1604 | -48.0724 | 2025-06-27 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 96937706-d741-3817-b67a-412950a7d298 | -6.9414 | -42.907 | 2025-06-27 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| f0de925f-f994-3d54-95db-5c022c62d153 | -11.5782 | -52.094 | 2025-06-27 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 189.0 |
| 0ffd6cde-6ca3-3d42-bcd7-19eb5e6bb323 | -11.5969 | -52.113 | 2025-06-27 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| deb4a5c5-96d9-359a-a523-86a024c4b593 | -11.559 | -52.117 | 2025-06-27 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 7dda4486-abce-31e1-b5f2-c28dfea5b9aa | -11.5779 | -52.115 | 2025-06-27 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 586.4 |
| cf50b8ac-8046-3055-a38f-5e2433636e82 | -11.0644 | -55.3757 | 2025-06-27 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 69ac0c0e-9d15-3431-baf4-b7e85bd04d5d | -6.9602 | -42.9052 | 2025-06-27 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 343.8 |
| 38a3e00c-3af4-3ead-8f73-bad7e5e68da6 | -8.6097 | -51.5731 | 2025-06-27 01:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 199.8 |
| 66b65c4a-b117-3d09-91cf-db374b878aba | -6.1602 | -48.0941 | 2025-06-27 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| c074b912-ec5e-3d2b-858b-aaeb073fc5ff | -9.0837 | -49.4348 | 2025-06-27 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 09792af5-11d4-3d3d-a355-e1d0d38d1d31 | -14.4476 | -48.8619 | 2025-06-27 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| d4cd24cf-16f2-36c5-96b6-d8d95d0a4335 | -7.2031 | -43.0701 | 2025-06-27 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| fea32bd1-484b-3beb-bdc4-e9cc6e46214c | -7.2028 | -43.0936 | 2025-06-27 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| ede0c968-2712-3c20-b9fa-79d67d729ca5 | -6.9791 | -42.9034 | 2025-06-27 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 167.7 |
| d7914ad8-2bbc-3b3a-98a3-5134736ecf03 | -9.0648 | -49.4366 | 2025-06-27 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ed7c4baf-b5af-3cf1-b23d-e220ec051b1b | -8.6094 | -51.594 | 2025-06-27 01:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 308e949d-bd7c-3a26-bbbc-b74bad25c395 | -11.5592 | -52.096 | 2025-06-27 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| a577262f-8363-3105-8789-a2a5338e7fb6 | -6.1789 | -48.0929 | 2025-06-27 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 230.5 |
| 88739817-a987-303e-b582-e0c16d9c6810 | -11.5776 | -52.136 | 2025-06-27 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 588968cc-83d5-338f-91f4-58ca7180b55e | -6.1791 | -48.0712 | 2025-06-27 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 167.8 |
| f26cc560-8645-3c9c-b095-45cf7cdd640c | -8.6284 | -51.5716 | 2025-06-27 01:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 191.9 |
| 545c3429-cd8a-3939-abff-434358ba5a75 | -7.2217 | -43.0917 | 2025-06-27 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| b9987951-eb20-3585-81dc-ed7bc944e190 | -6.9416 | -42.8834 | 2025-06-27 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| e42b3660-b1d7-380f-902a-169e46ba56b1 | -6.9793 | -42.8798 | 2025-06-27 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| 067679b5-c10f-3780-9a18-d735ca8acb90 | -8.6284 | -51.5716 | 2025-06-27 01:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 265e3110-71e1-3dfc-97b2-5ac170eb899a | -6.1975 | -48.0916 | 2025-06-27 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |


[Clique aqui para ver as próximas entradas](README5.md)
