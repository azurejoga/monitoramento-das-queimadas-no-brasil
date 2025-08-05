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
| 2edf39d0-07e6-33af-baaa-e27447fc5a01 | -17.2256 | -44.817 | 2025-08-05 03:40:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 99.7 |
| d272d72f-6b2f-37a6-b94f-187d4e941ba3 | -13.0726 | -56.893 | 2025-08-05 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 495e8d0a-fc8e-3d0a-b8bd-27ef90c9a23e | -14.466 | -52.0899 | 2025-08-05 03:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 688bfac1-e038-371f-8ba9-c852938ede2a | -8.9478 | -46.7354 | 2025-08-05 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| b3f0714c-f65d-3e30-b584-b344eb41f780 | -17.2056 | -44.8214 | 2025-08-05 03:40:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f45a53b2-e1b7-350d-9855-0bc90fef12c4 | -8.9228 | -60.5376 | 2025-08-05 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 9f94c29c-c8aa-36ee-9e41-25d09c936fb5 | -5.10578 | -42.92063 | 2025-08-05 03:47:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92558fa0-f729-3391-8a22-0b5589e83d6e | -2.90708 | -40.132 | 2025-08-05 03:47:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 9f8dd425-1cda-3509-83bb-807099edad13 | -5.888 | -43.73816 | 2025-08-05 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4ebdfd8-f4ec-37ee-98d5-dc9b70a97015 | -5.14072 | -36.3684 | 2025-08-05 03:47:00 | NOAA-21 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5da7869d-28c4-3a33-9c03-4c46de896a23 | -5.7885 | -43.60747 | 2025-08-05 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7414c7c6-831f-33ed-8538-9af387474787 | -5.4927 | -36.46601 | 2025-08-05 03:47:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1df37d2b-758d-3e8a-8e9a-611e4bec7435 | -5.48677 | -42.16161 | 2025-08-05 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 24b6f8e9-6edf-3f3e-9c77-cf95ea4ea7c9 | -5.88876 | -43.73598 | 2025-08-05 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6aa5676f-b307-3c6d-a1d6-8abab1f21c1a | -4.77675 | -45.33405 | 2025-08-05 03:47:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 197d51f4-7c02-3400-9a4d-f7644aa4bec6 | -3.7814 | -41.68392 | 2025-08-05 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 120191f0-7edc-3f39-a108-56a695251e6e | -5.48265 | -42.16088 | 2025-08-05 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9f0f0f32-b1fc-3251-bb59-c0746a2aa254 | -4.13023 | -38.18457 | 2025-08-05 03:47:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| bca0fe32-ea82-3475-af14-e108d4877f57 | -3.421 | -43.16663 | 2025-08-05 03:47:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8529df8a-8e22-3046-92df-b26b1fe8e5f1 | -6.558 | -39.01191 | 2025-08-05 03:47:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0f319baf-0d56-3d53-b4db-31eea61698f6 | -4.77152 | -45.33339 | 2025-08-05 03:47:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6ab0c855-5409-3947-b8cc-0ed61cf497a8 | -5.78687 | -43.60928 | 2025-08-05 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 94755f78-cc46-32c9-b473-c1d6858442b0 | -5.67211 | -35.72458 | 2025-08-05 03:47:00 | NOAA-21 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 96a7e79c-9ad4-35d1-aa7f-bcd46042675c | -3.77668 | -41.68696 | 2025-08-05 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 51b2ed74-1fed-36b2-9569-59c0739a7dcd | -5.88878 | -43.73345 | 2025-08-05 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc1d4513-05c9-38b2-a8c5-cfbfb52b4d35 | -3.78551 | -41.68454 | 2025-08-05 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 65af240a-52d2-3255-ba8e-9bb05a3980ff | -4.35496 | -46.56113 | 2025-08-05 03:47:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d3325cb-70d2-3675-8c74-c42e935372fd | -5.88253 | -43.74482 | 2025-08-05 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e53758af-8dc3-3f2b-a776-a4e379e35c5a | -5.14126 | -36.36494 | 2025-08-05 03:47:00 | NOAA-21 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 8be547d6-37c4-3fe6-8e72-f0c6a7ff7b85 | -4.38593 | -41.91803 | 2025-08-05 03:47:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7b497adb-4cb8-3b4a-93c5-7048a343384b | -5.13795 | -36.36443 | 2025-08-05 03:47:00 | NOAA-21 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5afaacd8-addb-3c16-8879-032021f81cb3 | -3.48156 | -43.25605 | 2025-08-05 03:47:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcef4a7d-f817-3e9d-a1b7-9598ab577092 | -5.88957 | -43.7313 | 2025-08-05 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42739922-746b-3824-b6f5-01bc4b328ccf | -2.93224 | -40.19233 | 2025-08-05 03:47:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e5920d9-e491-3239-be71-aaed89b4f3f2 | -3.47775 | -43.2506 | 2025-08-05 03:47:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34ea870a-71c6-3fe3-af34-f6c7af5af0c5 | -5.65639 | -42.58328 | 2025-08-05 03:47:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 72ae461b-4044-3123-9e81-95b0d3da26bf | -5.80199 | -43.63064 | 2025-08-05 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 255ed007-4a0f-3bf5-b69b-06f56606cb7f | -5.80348 | -43.62873 | 2025-08-05 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ded246cf-be1f-3243-bd51-2bcd274c1d6f | -5.69261 | -43.83472 | 2025-08-05 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fe3669a-1152-3aa7-ae91-de24609698b7 | -2.4964 | -47.57089 | 2025-08-05 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 416eace3-c1a0-3ced-8fcb-8cbc108c9e61 | -4.12965 | -38.18823 | 2025-08-05 03:47:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 663935f8-f8d1-3856-a916-5196b5a833fe | -5.78772 | -43.61195 | 2025-08-05 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0836f4c5-b880-3e92-9b44-398f65e0f71b | -4.77099 | -45.33648 | 2025-08-05 03:47:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 16d1b305-fe45-3dfa-9e24-e0abb38dc10e | -3.77728 | -41.6833 | 2025-08-05 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5260e3cd-9532-3586-b046-fc05f607bfa3 | -4.7762 | -45.33721 | 2025-08-05 03:47:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cdb1de12-4b8a-3cc4-9f4c-49be7e52c216 | -5.24546 | -46.779 | 2025-08-05 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54b12fa3-1852-328e-b899-9c4b8bb3ab55 | -3.47854 | -43.24589 | 2025-08-05 03:47:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c210800-080f-3368-a5fc-d5de545e2991 | -3.21257 | -41.84472 | 2025-08-05 03:47:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee9b91b7-28df-3a01-819c-f3aca8074bb4 | -4.12683 | -38.18405 | 2025-08-05 03:47:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5bd8f322-2a3d-3a1e-9eba-b50ab6b541d6 | -10.91499 | -48.37544 | 2025-08-05 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67e6ee67-f0c0-3bd7-8246-e20ede60f7cd | -9.18361 | -48.84634 | 2025-08-05 03:49:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 91e76b5d-ed7c-3d70-972d-91fe771de059 | -8.11327 | -45.52109 | 2025-08-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6e882907-c5a6-31c6-9fd7-3f3d14606753 | -12.6928 | -48.11942 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c8bb6674-9916-3c00-bd25-5e3d7f275037 | -7.57314 | -44.89906 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df15df35-bf9f-3b27-bad5-3cd5bae51ca3 | -7.76077 | -45.23632 | 2025-08-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 478a1a14-61dd-325c-a772-46976334ee5f | -7.39303 | -44.63371 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c711e2d9-7947-323f-ac79-c797fb954c7d | -9.39111 | -45.50851 | 2025-08-05 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4d7e249-e064-3199-9d1c-e0bf289321da | -7.08647 | -44.69553 | 2025-08-05 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b7bf974-d019-3fb0-a7c7-3179ab457c08 | -11.32694 | -47.30859 | 2025-08-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 539b9964-fdb3-3fe9-9a41-6a6ddaa21131 | -10.46469 | -44.37856 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7fb3b51-6e90-33aa-8e59-3be515728d8b | -7.77343 | -45.22158 | 2025-08-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae24b318-02c0-3e83-a1e9-0b1b3737b68e | -12.22595 | -44.19404 | 2025-08-05 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 117a68cf-0c2e-3c4e-821a-63f1fac1a6a4 | -11.01436 | -47.1896 | 2025-08-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61cef60b-007a-3f4a-ab2c-a3d5f5b7bc7e | -12.68065 | -48.12379 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 62783053-18a8-3fdf-b022-64d6064773f1 | -11.01499 | -47.18618 | 2025-08-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19e0a587-83b3-3819-9c73-f9199115f15f | -14.05168 | -41.98962 | 2025-08-05 03:49:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8f57e4ed-2fca-33fa-84fc-eccce13763d7 | -7.98604 | -43.16911 | 2025-08-05 03:49:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 4ecf22e6-deaa-3fa6-adb9-e0823f990654 | -8.00851 | -43.13964 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b00e16ab-5c86-3855-866e-248a2a2e55d4 | -10.78461 | -46.64217 | 2025-08-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 421f46e4-92c2-3fe4-a71c-368c0da3345a | -10.44957 | -44.36369 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c5849d1-c04f-3c1b-a29e-06bde57da73c | -11.92277 | -44.96449 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9d0903fc-1063-3fa8-a0d8-cabd3c518fd9 | -7.94631 | -43.89808 | 2025-08-05 03:49:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 760c319f-b35a-3c80-b24f-8fac388f2408 | -10.47355 | -44.37995 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94c7c724-9ab5-30d3-9757-eff481369b25 | -13.29524 | -39.86559 | 2025-08-05 03:49:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a6363642-0be6-3462-a7b1-5fcab5c901c4 | -11.03907 | -47.619 | 2025-08-05 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f00d5eb7-ebe9-307a-adda-a2e692eadf2a | -6.57871 | -43.49274 | 2025-08-05 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11e87868-24e3-3c82-8a6a-029261669cd4 | -11.74424 | -45.0066 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f34be1ef-05a9-3497-82af-cbed9c033efb | -6.96463 | -42.86407 | 2025-08-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 5aed6cf9-8db7-33d5-adcf-e6e704a34614 | -11.75419 | -45.01245 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16973341-b81a-361b-801b-a0f6037b76a4 | -7.38961 | -44.65321 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 389d24e7-86b4-3e4b-8a1d-26ea40170f8f | -12.70612 | -48.08051 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2336271e-f78b-3ab5-9381-c566880fdf25 | -8.01868 | -43.18262 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1f58f55a-9491-3391-9a16-4602b081b4a9 | -6.54838 | -44.0137 | 2025-08-05 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28a389c6-17f1-355e-88f0-15662f179d68 | -12.54975 | -44.72766 | 2025-08-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22f73269-de83-378b-b6d8-ace531b35d43 | -10.44723 | -44.37718 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 763d25ef-afef-3e2f-8dc0-27148534f491 | -10.91085 | -48.36634 | 2025-08-05 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec4e9395-b1d3-3631-946d-5a3e45b57026 | -8.93829 | -46.73335 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 06f73484-a581-37ee-8156-d939433d6edb | -12.67519 | -48.12282 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6cfed2c0-f007-3a07-8cf7-a143d4aba957 | -12.54539 | -44.72689 | 2025-08-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dd93be3-74ae-33bf-b639-59c944fc2495 | -6.73826 | -45.30722 | 2025-08-05 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fb753bc-ca1c-341d-899c-a8d029d9385d | -6.20281 | -43.74878 | 2025-08-05 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92f466d5-0e79-39ff-8a73-2f29fac968bb | -11.91747 | -44.96826 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dfb1c12d-af56-3fb8-b57a-dc18f62b53c5 | -7.0556 | -47.46687 | 2025-08-05 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dc3f81e-30ef-3bae-94d0-f0f1cd2c49c6 | -2.89729 | -40.01989 | 2025-08-05 03:49:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b3891dc5-7ef9-31fd-8cb4-7901205b2473 | -8.25792 | -45.06606 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88d8f77a-337c-3bb0-ae6e-6ca57da992ed | -10.45059 | -44.38096 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8684feb7-aa18-333c-922e-0f83839d8d1e | -6.46606 | -43.03561 | 2025-08-05 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a32e8c9-0937-3099-871b-2e6be2fba8f7 | -12.73044 | -45.08051 | 2025-08-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08eb6234-d87f-370c-b621-263101f76a07 | -10.46829 | -44.38385 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e369488-f966-334a-b04b-6c435208d759 | -12.71463 | -47.79478 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README8.md)
