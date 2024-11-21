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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c37575e6-b9d6-37ab-8837-a4a8bb16458a | -3.75236 | -50.00154 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d648ec7-c6aa-3761-9cf3-61b8385d36c4 | -2.75589 | -54.06844 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3e094d0-a948-3ba4-87e8-da25213f90a0 | -4.25348 | -46.11196 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66cc9a72-df8e-3d05-be32-778b3d3eff63 | -2.82321 | -54.00829 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4d0e405-c2af-36fd-9af6-6579556043b0 | -3.10915 | -53.70303 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c952db2b-22d9-38b4-8a8d-b185ccfdc678 | -3.28853 | -53.83723 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1bfe3cae-b73f-3aeb-ba79-09af2bce08f4 | -3.25189 | -50.56063 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e4b7ce2f-f6e3-3ee7-a561-ddcfdaa73796 | -4.10063 | -48.4818 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 863bb6a6-c8f4-35d1-b2b2-5ec06d7e61f9 | -2.81439 | -54.0211 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30cf74f7-52c2-3ed9-ae2d-dfd88b14b554 | -3.4224 | -50.25351 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb2632df-fe06-3a14-af7d-c19710465a09 | -2.96392 | -51.02074 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83048d1d-d3aa-3370-a245-e6bc46d14101 | -3.29758 | -50.3589 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11473ecf-2eb0-3dae-866b-48c6821793ef | -2.75059 | -52.11568 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a48edba8-72cb-3b25-b501-75daced40262 | -2.59615 | -54.00437 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74762f33-e20c-3726-a682-436b9a252c1f | -3.81162 | -51.27098 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08afea2d-fae7-3753-b742-151950618dea | -3.11924 | -48.66837 | 2024-11-21 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e21a2923-accb-303a-af59-e2397d1ee4a4 | -3.38436 | -53.2713 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7fdc42e-33ee-3703-85c7-0c1047a31201 | -2.74433 | -51.82627 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28c38f9a-6467-30ed-ba3b-641cbbf1a4cd | -5.35981 | -46.86831 | 2024-11-21 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d336d5fb-1dd9-3ed2-9ea2-3b7bed173ba7 | -2.6182 | -53.97234 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15f05415-4038-321b-8b6b-b29fe5abfcca | -5.94984 | -44.23876 | 2024-11-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17e503a7-fa62-3cc6-9edf-15eea63b0b26 | -3.26686 | -50.62875 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12c40149-eea8-3126-b176-2aaf7d67e6b7 | -3.21099 | -54.88268 | 2024-11-21 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7851b1fa-a927-3b23-93e0-21a9562eb834 | -3.81595 | -51.35735 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7e7a564-d18b-3b00-8d05-78210cda178e | -3.82796 | -52.25481 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7132761a-7e30-3896-a3fd-451b11603e48 | -3.29998 | -50.22292 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc0f8e8a-5129-3ce5-95c7-4c322b81a6d2 | -5.61067 | -46.28894 | 2024-11-21 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ff5e7e9-16f1-350b-a942-23250ce83357 | -5.45601 | -46.48409 | 2024-11-21 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18a014dc-53e2-39ad-9595-ab18c4c0fa42 | -3.07445 | -50.96235 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ed918e4-f4fa-38aa-98dc-1b26ab3f6c0d | -3.08926 | -49.47316 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c673a9b0-9d65-38f5-87c9-dd9fa1ff4543 | -4.12818 | -49.438 | 2024-11-21 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f31f6a1d-ab2b-3386-aaaf-02a628c59ff0 | -4.61203 | -48.47887 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8822e817-786f-3eac-a8c0-466fbb9a5792 | -5.55223 | -46.3926 | 2024-11-21 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a539fc1-8a94-3145-99dd-b36b98caea85 | -2.74471 | -54.00992 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5003e87-ad7a-3612-8ac0-b8bb20714b92 | -2.92605 | -53.07252 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 905f6059-8366-34f6-8f24-be230e37649c | -3.66839 | -54.65572 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95d0449c-66e1-3bf3-bdaa-370c21a51877 | -3.42567 | -53.28835 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bb8cf4a-cbaf-3726-9369-e4da38068e6a | -3.05475 | -54.4118 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14936dd7-4a42-3a36-bf0c-3a79fd65f494 | -2.58558 | -51.71716 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abfdd797-7587-3a85-8cdc-263aa30d69c0 | -4.01309 | -51.02296 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f28ed668-42cb-3d5d-9d2d-8e9cf5c3bfb5 | -3.83232 | -50.28848 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 582a63fb-9d2b-3e4c-9a0f-9053c1a81b27 | -2.83924 | -54.01434 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 258bccbb-fd37-35e8-b5fa-fafcc5c73f07 | -3.78635 | -49.3693 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e113c1a-5338-3b8e-8664-6456ab8f3064 | -3.42532 | -54.60721 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33c58292-b507-38b5-bb9c-bf48f8d7dfa4 | -2.58163 | -51.72025 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9102c86e-9cb5-3f33-9a90-71ff7eb09aec | -4.60074 | -47.03393 | 2024-11-21 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 758b6445-ca3f-3de8-a1a8-20d7bcbdde53 | -2.59066 | -54.03909 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95e73883-2478-3d89-8fb4-16e5bb7a1496 | -2.92222 | -53.07541 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a76d578b-16ab-3acc-b3e2-744233771989 | -4.24382 | -46.11096 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 52ad6dcb-47fb-364a-92e9-ca272e8d5f18 | -4.24939 | -46.10646 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b027b95-4131-3902-bf35-bd108aa90d3e | -3.3964 | -50.25383 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| da043e37-ee6e-39f1-990d-67f093ad4da1 | -12.65237 | -48.82463 | 2024-11-21 04:57:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a02e258-d173-3cbb-ac79-68951292017c | -9.99642 | -55.65686 | 2024-11-21 04:57:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b535f3a-7767-3d83-96d4-b70c890ed6f3 | -11.22456 | -45.57463 | 2024-11-21 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04a497ee-b493-3a60-a07c-28f59fb43c0f | -11.2241 | -45.57823 | 2024-11-21 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ae58457-86e0-3b20-875e-0e46a0936111 | -11.45925 | -48.01313 | 2024-11-21 04:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfb66ce6-792f-3aa4-b4ff-32920461bcff | -10.73321 | -49.5284 | 2024-11-21 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 102054ed-87e9-330e-a1e2-9917f4086ca7 | -11.45992 | -48.00819 | 2024-11-21 04:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d20e5b0d-ef94-367f-af4d-fcd2c90f5d44 | -10.73217 | -49.53608 | 2024-11-21 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 49071abc-607a-3767-80e8-b7ac4e901e5c | -11.84779 | -52.33946 | 2024-11-21 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ff2445a-b2de-3d4d-9fce-78bb4be18053 | -12.64949 | -48.82708 | 2024-11-21 04:57:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1caab52c-0880-3e70-aa6b-adaf14337c1b | -10.11823 | -65.0314 | 2024-11-21 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| af845db5-4754-32ac-8204-8b7046f53031 | -9.9931 | -55.65632 | 2024-11-21 04:57:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57df2e0b-c4c5-36c2-834d-bc5b7ab4a53e | -11.51725 | -48.13386 | 2024-11-21 04:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f7de040-1e6b-31b6-9a68-dc384439b4f1 | -10.72851 | -49.53163 | 2024-11-21 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f42aa891-10d8-324f-b784-017f0a8e7e02 | -10.12057 | -65.02879 | 2024-11-21 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ed10cb50-7ddf-32a7-8777-bcdf81240abf | -10.73269 | -49.53225 | 2024-11-21 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e58bffc8-248e-3ef6-811d-e8a34da95b90 | -9.99697 | -55.65334 | 2024-11-21 04:57:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a7f2e0a-945b-3df6-b07e-f4856f633d71 | -12.65458 | -48.82312 | 2024-11-21 04:57:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57926659-529f-37e9-a7fc-a6b2dec57e30 | -10.11896 | -65.02762 | 2024-11-21 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 46213f1e-cf40-3d51-99d8-fbb8f927f76a | -12.64849 | -48.81939 | 2024-11-21 04:57:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c52d4f81-7a66-3b93-aea5-2a1597523873 | -10.08363 | -55.87729 | 2024-11-21 04:57:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7355ac15-e3d3-326d-ad03-2ae541b05219 | -10.73739 | -49.529 | 2024-11-21 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cc1978d6-b3b2-3f4d-84cf-8a2a665433ef | -10.61422 | -52.28705 | 2024-11-21 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3527257-f8e7-3014-be5c-9906d07e492a | -11.46206 | -48.01095 | 2024-11-21 04:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b7aad55-7abe-31c3-8c0a-28dd19c73495 | -10.11986 | -65.03259 | 2024-11-21 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 85d3ce8a-601a-36b5-88fa-7cf3aaf8767a | -10.73164 | -49.53994 | 2024-11-21 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 72c43a53-6229-3d78-b918-e519207b6801 | -11.8442 | -52.33893 | 2024-11-21 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc4d4751-2d7c-375d-9e0d-d35ccbd0089e | -12.65067 | -48.81786 | 2024-11-21 04:57:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cce5de5-1fb1-3f30-96b8-c4245c94ed10 | -9.99366 | -55.65281 | 2024-11-21 04:57:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 304ebb69-a42c-3176-91b6-1db55070484c | -12.65008 | -48.82248 | 2024-11-21 04:57:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b79dae0a-ef1c-3124-9502-775110fba225 | -20.11173 | -57.13813 | 2024-11-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8c0a949d-abba-3bc0-b72f-912b140b80c3 | -2.7675 | -52.1251 | 2024-11-21 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 67f8c336-5301-3c75-8bb4-8b0e0e917699 | -3.295 | -53.8597 | 2024-11-21 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 3ca20f18-579e-3ab3-9acc-38c8eb46d6d6 | -2.7676 | -52.1045 | 2024-11-21 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| bfcabcc1-f954-3a98-9621-7d4dfe601193 | -3.2767 | -53.84 | 2024-11-21 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 341f5f13-79cc-3c59-85c2-9b0bd04e349d | -3.2768 | -53.8199 | 2024-11-21 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 0d6165d5-d0ba-3a1c-9f20-cc0038114d70 | -2.0259 | -54.5289 | 2024-11-21 05:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e5aba918-0804-37bf-9f37-aca3b7b99e42 | -3.2951 | -53.8395 | 2024-11-21 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 3a7d28e8-be41-3888-be50-1befa5625943 | -4.2575 | -46.1188 | 2024-11-21 05:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| c554c3c4-569f-3e5f-acbf-231bb1fa676f | -2.0259 | -54.5289 | 2024-11-21 05:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 5e653113-611e-3f91-92af-b557bc5652f8 | -3.2768 | -53.8199 | 2024-11-21 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 4e069772-06f9-35a6-b539-4b09c377275f | -4.58 | -48.0132 | 2024-11-21 05:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 3f15c462-cda5-3df3-8d2b-297570edfaae | -3.2951 | -53.8395 | 2024-11-21 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 5b38bc33-f7e4-34ba-8de1-8a6838d2f096 | -4.2388 | -46.1197 | 2024-11-21 05:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| b5f3a743-362c-3b77-9cc2-74400f4e194d | -4.2575 | -46.1188 | 2024-11-21 05:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8aadde18-9ee4-3b53-8614-af515e377943 | -3.295 | -53.8597 | 2024-11-21 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| bea9646e-962b-3902-82c4-dda566810d17 | -3.2767 | -53.84 | 2024-11-21 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| f2311864-48a9-3d2f-b805-05ad06b37336 | -0.79896 | -51.77996 | 2024-11-21 05:18:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.8 |
| c72a9eda-3dfc-30c8-99b0-001e0acc992a | -1.59439 | -47.4854 | 2024-11-21 05:18:00 | AQUA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |


[Clique aqui para ver as próximas entradas](README77.md)
