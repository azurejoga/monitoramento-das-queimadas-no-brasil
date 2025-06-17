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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 255712a9-d81d-3650-9005-9e21628b4c96 | -6.21716 | -43.33521 | 2025-06-17 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc11e1aa-6744-33fd-ac3a-2bad8ef7589b | -7.52885 | -43.79837 | 2025-06-17 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66a83551-bec9-3158-ba19-d7f44146967f | -9.66953 | -48.76722 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2abde053-1f97-3250-a090-006562275c84 | -6.15101 | -48.06363 | 2025-06-17 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90d93954-2806-3ca9-8bb1-618487b7aaaf | -7.72467 | -55.1419 | 2025-06-17 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b86249b-4a5b-3276-a4ab-89e2d3d0ade9 | -9.39729 | -48.43294 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ae868f5-5f73-3d8f-8b6a-ceb549b99cec | -9.40226 | -48.42297 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 477bfa5a-0b68-35eb-b951-dc2d7cd9c76b | -7.27879 | -50.00978 | 2025-06-17 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4ae3dc0-cd00-309f-965c-80800298fb6e | -9.88107 | -47.81006 | 2025-06-17 04:34:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4faf33f8-ab37-3a0c-bcff-626cb733d217 | -9.40394 | -48.434 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1aaf58b3-c1b2-3a55-aeab-3bcc6feed528 | -3.76834 | -41.60151 | 2025-06-17 04:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ab1a9d35-924e-3545-86c0-3292e03545b2 | -4.81409 | -46.82202 | 2025-06-17 04:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6806807-4303-3e71-a260-6786445adcec | -6.16153 | -48.06171 | 2025-06-17 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0988b402-151a-36ab-9b99-80348b825114 | -7.18665 | -43.60313 | 2025-06-17 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d11f6e2-1683-3f28-a63a-1aeb64e894bf | -7.4485 | -44.89281 | 2025-06-17 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b378eb09-1457-3bb5-8376-f658ddb9e206 | -6.67404 | -43.21521 | 2025-06-17 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 92a6ac85-3336-3079-8340-55d0991e36aa | -6.15156 | -48.06015 | 2025-06-17 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce06a70d-978f-3036-8e92-648e872ec415 | -7.96815 | -45.93894 | 2025-06-17 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dc988ec-bbe5-37ef-88e3-edd2ebafc243 | -7.20768 | -43.21886 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f6f6781a-ba05-31ad-9a51-f3be8537783a | -7.45338 | -44.88501 | 2025-06-17 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a232ad4-2899-3e54-9155-8b56a5bfe8b3 | -9.14631 | -48.97396 | 2025-06-17 04:34:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3238fe5d-f5d0-3641-a914-b6dd7a2d6565 | -6.49979 | -47.0266 | 2025-06-17 04:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe9e46e4-a5b4-34f7-a970-e640aed05c06 | -8.0678 | -43.10989 | 2025-06-17 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b1d8afc3-989f-38ed-9d7f-571fcbf771f6 | -9.88777 | -47.81107 | 2025-06-17 04:34:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3ccc125-a28d-3cb4-a23d-272b8e91cb99 | -8.74364 | -48.03222 | 2025-06-17 04:34:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 455d4e42-6d03-36dd-a369-5ec5718a6334 | -4.8102 | -46.82499 | 2025-06-17 04:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca6ae182-0c88-3629-bc5b-dd52b0911812 | -7.10795 | -47.84874 | 2025-06-17 04:34:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6ca123b-958f-3041-ad57-5990ef1e22db | -6.84235 | -47.84271 | 2025-06-17 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dfbe7c9-49f7-307a-b042-cab031571a47 | -9.41057 | -48.41354 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8043eab3-7618-327c-a97f-a78ffb2fab49 | -9.41002 | -48.41704 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff8d3973-db13-3fa7-9b1e-3fb8b44f45c2 | -8.96245 | -47.97324 | 2025-06-17 04:34:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61373b09-7473-34de-a6cc-ec1e53323c87 | -7.1911 | -43.60075 | 2025-06-17 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 465b77dc-0615-3df2-86b8-b40c6de2904d | -8.87949 | -48.52261 | 2025-06-17 04:34:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14e7e8e4-bc30-3d7d-aa8a-d00d4c5af914 | -5.68157 | -46.47848 | 2025-06-17 04:34:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3f64668-7465-3976-943c-3b5e6407ef3c | -7.2794 | -50.00605 | 2025-06-17 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65b012a4-fd74-35f6-acee-9f73f910d3ae | -7.26817 | -44.6284 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7e9dfc6-b954-3c05-b946-d89f3dca0dd3 | -7.22423 | -44.75098 | 2025-06-17 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4321f25-74ff-3bd5-973b-1a059c157717 | -7.20445 | -43.21302 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a23e95c9-68c0-39ae-bffa-4f54fef8a441 | -7.5486 | -45.64311 | 2025-06-17 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22cbb268-a529-3d87-9a49-9fce2eb992ce | -8.60019 | -48.05973 | 2025-06-17 04:34:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52e2ee94-550a-3b7b-a042-262b09e35782 | -7.22058 | -44.75039 | 2025-06-17 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8c6d727-442a-35d2-ad44-615aba945c16 | -6.15875 | -48.05771 | 2025-06-17 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d03030aa-458c-35fb-904f-4b674823229d | -9.61287 | -49.01672 | 2025-06-17 04:34:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3cc4ed55-99e7-3155-862d-8a3ed997d903 | -6.83809 | -42.80565 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab2f6336-5df9-3b8b-b52f-f199e15d96b7 | -9.41334 | -48.41757 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d438355f-6371-3095-b1c6-570b5e2ff988 | -4.25114 | -47.58249 | 2025-06-17 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1384d2f-5dc0-340d-9f7b-d6ff8ac564c6 | -6.15543 | -48.05719 | 2025-06-17 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58f91791-de06-38ab-abae-52aa0712d5c4 | -4.81354 | -46.82551 | 2025-06-17 04:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0cee05e-6c9f-3156-94a5-00f2c741f4aa | -2.45031 | -47.50144 | 2025-06-17 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 074953e3-d6a1-3c8c-bd86-430709f7aa8b | -7.96466 | -45.93839 | 2025-06-17 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87560283-1cbb-3ba1-9d99-6753866621c9 | -6.86894 | -44.83604 | 2025-06-17 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1dbd0911-b427-3935-99cb-5f1dec01c1b1 | -7.00284 | -44.08028 | 2025-06-17 04:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13ec9103-3dac-39a9-8c35-af7c1d37dc42 | -7.98011 | -55.29531 | 2025-06-17 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b597860-d96c-30ad-aad7-dd3815cf742e | -2.97477 | -48.86699 | 2025-06-17 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 215f1e0d-0925-328b-976a-b5edb5ffd792 | -9.41776 | -48.41114 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8f144d3-6333-3cbf-8105-0ee80609b964 | -4.54803 | -48.0163 | 2025-06-17 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3086bdf-0c4b-3086-9a25-7c0af21dbf0a | -8.61188 | -45.0204 | 2025-06-17 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ce58c92-5a31-38dd-85b3-f33aa9edec0a | -7.26625 | -44.64144 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cc932fb2-e3d3-32fd-9207-83249ea08197 | -7.72551 | -55.13719 | 2025-06-17 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8eb8499-0b53-3951-b184-d3969c41b628 | -4.13366 | -43.06514 | 2025-06-17 04:34:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7876eafe-cc88-39e9-8604-0d74e4088234 | -9.40669 | -48.41651 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae4fc574-2367-3ec1-9b2a-fbe332615aa6 | -7.72104 | -55.1391 | 2025-06-17 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bd7e03a5-d60f-3c7c-97e3-d7f02ea31190 | -8.61732 | -45.03443 | 2025-06-17 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4003636c-8b2c-386d-8cdd-8067f53cd5cd | -7.23608 | -43.08256 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e3d01302-110e-3f69-8432-25e507eaf415 | -9.39506 | -48.42541 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67fea1e1-6d07-3d70-a113-d7dd079e03ad | -7.44788 | -44.89699 | 2025-06-17 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 808bc878-8005-3e08-8d8f-a1e4487760cb | -7.26 | -44.61544 | 2025-06-17 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6f903c6-80c1-3fb5-b584-a6609f5f8671 | -7.98391 | -55.30083 | 2025-06-17 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d577c15d-ca11-3948-b7f9-ccaf8e2e1b1a | -7.98473 | -55.29611 | 2025-06-17 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c5a74c6-b040-33ef-b02f-c2a05a3c1cd8 | -7.97454 | -45.94391 | 2025-06-17 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dcbd423-2dce-3908-b20a-51e3ca214718 | -8.61253 | -45.01601 | 2025-06-17 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31b73515-687c-30cf-a1d3-d8130d2c5a14 | -5.14636 | -48.44765 | 2025-06-17 04:34:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f31182f-bc9b-3765-bfcd-00aac55b984e | -3.10887 | -47.48811 | 2025-06-17 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6044469-4bbe-33c6-8062-9a63e37a2d99 | -7.45815 | -45.50056 | 2025-06-17 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad3a46c0-f4b8-310d-9264-af8db5888162 | -9.88442 | -47.81057 | 2025-06-17 04:34:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ffe17ae-a62d-32bb-9124-74ca264905e3 | -5.62361 | -43.99819 | 2025-06-17 04:34:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c037704-7a2f-3fd8-a3dc-c6c28546d0a7 | -4.24727 | -47.58543 | 2025-06-17 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f06a66b6-35a3-3804-b057-edbaf939fdd1 | -6.15211 | -48.05667 | 2025-06-17 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49525f06-15a9-3042-9103-57814dfe7a82 | -8.39315 | -47.46188 | 2025-06-17 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48b590e0-a063-35f9-bac2-99b5dbea6d1e | -9.66843 | -48.77421 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e56c3a6-826c-34f2-82bd-71eb851c0c11 | -7.41446 | -49.36813 | 2025-06-17 04:34:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d781d96c-934a-3b84-be38-a94163cce694 | -6.29422 | -44.23126 | 2025-06-17 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bafec27b-0722-3025-9ced-7f8e697eaadd | -8.62063 | -49.16732 | 2025-06-17 04:34:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dae05e92-0e1b-37f3-97d2-d34f2c3081ef | -8.61492 | -45.02526 | 2025-06-17 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d17e8e5-b9e0-3266-a807-d095326e552f | -7.25119 | -43.09208 | 2025-06-17 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a64e2a4a-5128-378d-9fae-f50c631e78ae | -8.07136 | -43.11411 | 2025-06-17 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 484b25c3-5f13-35a5-be3c-b1172e8052f1 | -8.95912 | -47.97271 | 2025-06-17 04:34:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4ce7a19-ea55-35c0-8537-6fa2eeca56ba | -6.30025 | -47.00613 | 2025-06-17 04:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9009567f-8096-3956-9412-1b5423b4c08c | -6.68245 | -43.04838 | 2025-06-17 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 633674f4-d9b0-30f5-8a53-5cd36de2fe9b | -2.44753 | -47.49745 | 2025-06-17 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2826f84f-08e2-31cc-b81a-11642341b7a6 | -8.9106 | -49.83713 | 2025-06-17 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 680dd4f1-cc17-30d7-a019-850d9c3ec700 | -8.70297 | -46.96987 | 2025-06-17 04:34:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 619384ae-62a7-3b65-bd9a-9dcd941b0e86 | -9.39839 | -48.42595 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77bb1099-d082-305a-90c2-94df19f7d04a | -7.54567 | -45.63866 | 2025-06-17 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d7511d4-f198-3fb5-9933-8c962e79afd1 | -4.37711 | -48.06817 | 2025-06-17 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b57c8ca2-52d9-3293-8388-8bf88ee4cf1c | -7.18201 | -43.60742 | 2025-06-17 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c48a0a4a-acd5-3b03-8f15-86c40661bf04 | -9.40614 | -48.42001 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ae988f2-9a80-3bb5-bd9f-a56e0f9a872f | -4.38045 | -48.0687 | 2025-06-17 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68dba72e-bb7d-31b8-b750-22e9fab2c540 | -7.18258 | -43.60445 | 2025-06-17 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b7c3fbbf-5323-300d-ac2d-ab34c55cedcf | -9.39229 | -48.42138 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README13.md)
