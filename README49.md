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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65c20800-14ff-3efb-967a-2fa0b83750e6 | -10.22747 | -52.73837 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b0f5c6d-fa26-3a21-afea-eb245a00bd08 | -10.22692 | -52.74189 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74e89526-63bd-364b-bf5f-e33d3f5f0b79 | -10.22578 | -52.72729 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e77f57c-49eb-3671-ae72-48f46d96eb0c | -10.2236 | -52.74136 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59a0e784-149e-3dd4-add5-ecae5eadf00f | -10.223 | -52.72324 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 878f12fe-cde9-36c1-97b3-759fd29e3084 | -10.22246 | -52.72676 | 2024-09-29 04:49:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 718ed77a-5234-3afd-accd-989653831238 | -10.05088 | -53.47661 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e58f6d35-a822-3ec8-b509-f76924e59869 | -10.05033 | -53.4801 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7809eb6f-3a96-3eb1-8167-b93d51700168 | -10.04867 | -53.4691 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9d9da32-b0e6-3ba4-be40-d07cffe27912 | -10.04812 | -53.4726 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a41e2444-b00e-3f9f-ae04-d7c7ff26a12f | -10.04757 | -53.47608 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c82bcc4-1a76-39b1-946d-5f7cd7280f1c | -10.04756 | -53.45462 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d1ee435-85c1-3d6c-ac7c-184ee1f9c1d4 | -10.04592 | -53.48655 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31ff1897-a72c-30da-867c-24661fd821c1 | -10.04537 | -53.49003 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3a6ad11-0e4d-3bd6-8139-8705fcb214c6 | -10.0321 | -53.42358 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92eac571-9859-32f2-9f25-d5d157480402 | -10.02824 | -53.42654 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e3945ac-5cfb-3bb0-a2eb-e940b2927341 | -10.02607 | -53.48336 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e907160-47ff-3a34-9506-1e07ff8e3a3c | -10.02493 | -53.42601 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 756ca7b1-479f-3158-b15f-f1d9f786e3bc | -10.02332 | -53.47934 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 172bc40e-4619-3a15-bb6e-e0fc0af6c8b4 | -10.02277 | -53.48283 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3830feb-e902-339a-8523-4f1c51ea6e22 | -10.02162 | -53.42548 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcb1625f-17f6-381d-b3b6-5d88fcfd389e | -10.02107 | -53.42897 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8745dbd-ed81-3128-b946-c9693884f28c | -11.08319 | -52.49443 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec035d0c-8dce-35a1-aba8-00d850313d36 | -11.08263 | -52.498 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 424a5f85-8310-3c40-bc6f-ec5ae215ddf1 | -11.08209 | -52.50157 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e47b013-8fd9-31a0-b52e-38c294e1a9e4 | -11.08154 | -52.50514 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72a69f0e-f7c5-3eea-97fe-c8af213354d1 | -11.08039 | -52.49033 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d558ce5-9049-3554-8e0f-ef6030d7662a | -11.07984 | -52.49391 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 471b83e7-5531-3380-98bc-aa749f61884d | -11.07925 | -52.47548 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2315f677-012b-3960-a69a-dd7583854e5f | -11.0787 | -52.47907 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6261679b-ca6d-3a19-81d6-d1c348e89288 | -11.07819 | -52.50462 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c99e2399-1ed3-377e-b231-b9a5ded7f24a | -11.07815 | -52.48265 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18c948ac-6e21-3f18-aae0-bda137954e1a | -11.07764 | -52.5082 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf73d214-65bc-3dc6-a32a-6329c8eabe55 | -11.0776 | -52.48623 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbd5328d-69b8-3fd2-b1d6-8f20ae23b5cd | -11.07705 | -52.48981 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f2de768-5f58-381c-a0e3-0d0131d03ff7 | -11.07646 | -52.47138 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22968eb9-6781-3899-8f84-340453a67328 | -11.07591 | -52.47496 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27645346-b5f8-3ed0-b26c-21a2b573a1a0 | -11.07536 | -52.47855 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 505b8b70-6932-3365-a8b7-3690e20eb8cb | -11.07485 | -52.5041 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d60a7990-d41e-3903-9975-65d044279fa8 | -11.07481 | -52.48213 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d0d19340-f676-3b17-99b0-86db76bb1203 | -11.0743 | -52.50768 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7577321f-89c6-3c7c-8af9-20511c4106af | -11.07425 | -52.48571 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ad809109-1fce-379c-9b0f-4b8f5142a1eb | -11.07371 | -52.48929 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 48fa2385-ca02-3619-ac2f-5d04c58be6fa | -11.07316 | -52.49286 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12514f04-3355-3b2a-90f0-2996b669c004 | -11.07311 | -52.47086 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 845d7da2-a349-3854-a5f5-e33d3db5ffb1 | -11.07256 | -52.47445 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6974975f-83e1-3312-b8af-30d007806eda | -11.07151 | -52.50358 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 381bf65c-eb49-363e-866a-40cc0b61887a | -11.07146 | -52.48161 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2dc4cd2d-894b-3084-83d4-66cf2e094c34 | -11.07096 | -52.50716 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 68ab1ba2-63be-3d8f-a97f-884d11a4adfe | -11.07091 | -52.48519 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 61448c52-e85b-32a2-9c68-3b4b54fc444b | -11.07036 | -52.48877 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 25f8a267-f9a5-3ee4-8cdf-280e5252af1d | -11.06981 | -52.49234 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71151812-24cb-346e-b035-98277e306be4 | -11.06977 | -52.47034 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c87b90ae-2252-33ff-adfe-09c5023deb97 | -11.06927 | -52.49591 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85dcf516-8f8f-331c-86a8-ff954830571d | -11.06922 | -52.47393 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b583eb39-19ba-3ac9-803a-58ee074bfa09 | -11.06867 | -52.47751 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 6a50fc79-d594-3e50-801a-d65edf574012 | -11.06817 | -52.50305 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f79f621-4a44-3abd-95ee-c2e2bef77dae | -11.06812 | -52.48109 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| a5db533a-0185-33f6-a7d2-d9337510c06b | -11.06762 | -52.50663 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7f4c9cb4-8e5f-3fd9-a69a-645ba5c664eb | -11.06757 | -52.48466 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 411d2eed-6163-387a-86f6-5d96aa49f5b2 | -11.06702 | -52.48824 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 759c01f3-2a48-316e-9dcb-11ae51e0a3fa | -11.06647 | -52.49181 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1eaf46b-2a09-33b5-8702-96bb0b728d03 | -11.06642 | -52.46983 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4aea7d1-e552-3a6b-b9d7-8fadf34c33f6 | -11.06592 | -52.49538 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2928995c-b0a8-30e1-bd84-f5028369d79c | -11.06587 | -52.47341 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 443a6bd0-591c-3e19-aac1-db2857d0ae6b | -11.06538 | -52.49895 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f0cd91e-226b-3bb7-bbdc-14a53b8c9800 | -11.06532 | -52.47699 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 315b1a66-b976-3071-9204-81257fcc6542 | -11.06483 | -52.50253 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8daf1050-6e81-3eb5-86e9-658c6a4f81b7 | -11.06477 | -52.48057 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 15d645d9-808f-3dbb-bdec-394daf276bb4 | -11.06428 | -52.5061 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 93409674-93e7-39fd-ac70-dd9660a82e98 | -11.06368 | -52.48772 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 7095e242-aa57-34c1-b054-1256a2699783 | -11.06313 | -52.49128 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 612dd080-0233-3bce-b28f-5b23dda2ecf0 | -11.06308 | -52.46931 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2080b2a9-3ebf-3af7-8345-1b2991b2df00 | -11.06258 | -52.49485 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45b5515a-6635-3e69-8842-dd0b97ffad82 | -11.06253 | -52.47289 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce3e83b7-9ef1-32ba-a168-44b0ae8f4592 | -11.06203 | -52.49842 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6a6fbf0-a4d4-3c95-8d1b-e6fe42982dbb | -11.06198 | -52.47647 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3f42a38-afd2-3015-8d1e-eeeaa8a607eb | -11.06148 | -52.502 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 671134cb-27c3-3c42-af46-11d24e0b4e15 | -11.06143 | -52.48005 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 551d2c2d-c4ec-39e6-b0bd-d29d20c16d51 | -11.06088 | -52.48362 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 010ff4d9-d95b-3a7c-aba8-125150a47d06 | -11.06033 | -52.48719 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adea6f2a-398e-3d60-9746-27e1545b70a4 | -11.05979 | -52.49076 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34c8ef80-6b82-3d67-a010-60c4779885a6 | -11.05924 | -52.49432 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df2ac8d2-8b8f-38ca-ba84-ba1c4adede40 | -11.05918 | -52.47237 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee0956f1-c0e6-324a-a945-1c3422b67586 | -11.05864 | -52.47594 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3894a291-6b54-3189-8f65-34d5f902f929 | -11.05809 | -52.47952 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fae17e7-6e39-37d6-8f06-a716566ec258 | -11.05754 | -52.48309 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9549de54-82c2-3479-ad90-d14a95424059 | -11.05699 | -52.48667 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4838a442-e17d-3739-956f-68278e7492af | -11.05644 | -52.49024 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3feb0221-62dc-3cbd-96c7-47ec4aa0735d | -11.05474 | -52.47899 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bd0a46b-8204-3581-b3a9-b7b278c27db0 | -11.0542 | -52.48257 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 517f6a1f-572f-3ec3-bca5-cf5026d950c1 | -11.05365 | -52.48614 | 2024-09-29 04:49:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8048d4f1-1525-3e1f-900b-aa69726d061e | -11.22569 | -53.86727 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb4dc368-dbca-3617-90c8-d65afc6a38f3 | -11.22404 | -53.85621 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d5e4669-e96c-3a1b-83f2-796cf6f61663 | -11.22348 | -53.85971 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8df05394-fa37-379d-bcef-c61cee4fa0f4 | -11.22293 | -53.86322 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83bd596c-5d9b-34a2-be00-995bd147da1d | -11.22238 | -53.86673 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cadeef55-5971-3f93-93a7-18096b7761a7 | -11.22128 | -53.85217 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfa29c7f-434a-3ce2-9da5-99729d39e8d5 | -11.22073 | -53.85567 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11f2909d-7164-3942-8c4c-30e8a1fb545a | -11.22017 | -53.85917 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README50.md)
