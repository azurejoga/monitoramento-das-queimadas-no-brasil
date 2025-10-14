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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 890c52be-cadf-3b66-ae30-586fcdada564 | 1.13635 | -50.72694 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| febf53f8-2e19-3bc9-a94f-829a76112d0c | 1.10947 | -50.98525 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c02d4c41-4252-3c9d-a0b0-f94e2161c0ed | 1.10118 | -50.99111 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f82c1fa-962e-387f-9d0d-5a729f2412a0 | 1.1326 | -50.73193 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 987895ee-b00e-3897-9af9-461db1037e68 | 1.127 | -50.95058 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b30e2c0-cec5-3bdf-9feb-007950aa41a4 | 1.10188 | -50.99556 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0d853e39-23b0-33cb-80ec-ca58dbca8e71 | 1.8785 | -55.69782 | 2025-10-14 04:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a662ef13-32a1-3419-a82b-84fbcc66cad0 | 1.87927 | -55.70279 | 2025-10-14 04:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08e2490f-f85e-31d2-9c06-f496ba394aeb | 1.11327 | -50.98012 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b94b98a4-eba0-396b-aac4-81c33790efe5 | 1.14076 | -50.72625 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2eceb9a6-2362-3f2b-b37a-019b44b38aa8 | 1.45587 | -50.84734 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b3969da-b136-3fb7-9aa1-3d6004051989 | 1.13008 | -50.94105 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43b8e4cf-a77a-3957-b55f-65c5c0c01034 | 1.46125 | -50.88301 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 552cbf23-b420-30d7-baa2-48f5f9e48872 | 1.10637 | -50.99486 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ed30b488-404d-3e99-be34-ec7b4ec970ca | 1.46506 | -50.87783 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e4e1983-fdc4-37b2-8975-b88ba46fd648 | 1.47267 | -50.8675 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9cf8983d-9df6-3c00-a668-41193775553e | 2.18197 | -50.93891 | 2025-10-14 04:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9619c411-8f7e-390d-b5f7-4bd2736d8fd2 | 1.1263 | -50.94616 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc93cd27-79a0-3039-a05e-733ebbf24a5f | 1.88395 | -55.69186 | 2025-10-14 04:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b825d5fa-b19f-3f5e-afe6-a7967fb1eac9 | 1.13273 | -50.94279 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e52371f5-527f-3209-abb2-e574606cfceb | 1.10706 | -50.99931 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d8676c2-e64c-3eb1-ad6a-8235788f5121 | -3.14035 | -49.03503 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f60a276a-7549-3dec-9eab-127f5a635456 | -7.40106 | -39.78782 | 2025-10-14 04:23:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 9a43baf1-d6f1-3c3b-a307-c5f9dbb199dc | -3.47616 | -43.2962 | 2025-10-14 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89a527fd-f3cc-30ad-bad2-669dd05d7868 | -5.48569 | -44.99788 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37674750-e3db-3ec0-94e2-924266af7ec1 | -4.01542 | -47.34963 | 2025-10-14 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ba630cd-5cd7-3f9f-98e0-9d02e4b9dd21 | -4.67227 | -43.14345 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 83bbdc92-5886-3f87-bc8e-6f8e6beb7680 | -7.08998 | -41.9669 | 2025-10-14 04:23:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 621afc87-89f1-3f3b-9f40-cd716ae40226 | -3.12226 | -49.1004 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8cccb40-3139-3c75-9a27-97e74dbd8618 | -6.15842 | -41.72326 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3abb8a31-4d6e-3651-978e-2cf8d3700809 | -4.93312 | -45.74856 | 2025-10-14 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af1ee667-bfc4-3c45-9daa-93546850823c | -6.33873 | -41.60967 | 2025-10-14 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ea0286cd-87c1-32ab-a3c6-36a0a4ecc386 | -4.66294 | -43.13408 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| cc6efafe-f201-3c26-8ec4-5eea8a703ab6 | -5.61991 | -42.68904 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d8da7ffa-265e-3d30-b5f8-f6f3aa54845d | -2.44608 | -47.16396 | 2025-10-14 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c3b9999-94fc-3fe2-8c68-7c0e1b7739b9 | -6.52143 | -44.55705 | 2025-10-14 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61c84947-c9ac-3aa8-8fee-8219231a0a5e | -6.22364 | -47.03511 | 2025-10-14 04:23:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36b84fd8-50a9-32a4-b767-3afbc6ff846f | -3.40844 | -51.66877 | 2025-10-14 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a599ed01-e2db-34cc-a080-d736c744ad4c | -5.53548 | -46.2789 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ef8028e-2206-3b9a-aa92-6adaa6f06e10 | -2.29937 | -47.40294 | 2025-10-14 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45aeb19e-d1ff-3a4c-bf07-b4d32040ebf0 | -3.15475 | -42.89106 | 2025-10-14 04:23:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b45160e0-a99f-3dd9-ae72-4f4cdb9e77a8 | -4.66472 | -43.12237 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7ea431aa-8f57-359f-b6c3-07218b933110 | -5.26648 | -41.01033 | 2025-10-14 04:23:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b3f4717-2235-3c6b-8ab5-e0631e360585 | -3.09317 | -50.37511 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ab926a1-47ac-3591-a184-bf7714711e7f | -3.51702 | -52.89706 | 2025-10-14 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8902299-ca65-3630-9d2b-a938fc6ee9f0 | -5.38593 | -43.22765 | 2025-10-14 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9ac6639-bd32-369b-9c4f-1c99705c1a45 | -5.79399 | -43.89074 | 2025-10-14 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41f031cd-08a4-3d97-91bd-759952b282e3 | -2.30434 | -48.57189 | 2025-10-14 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f705b29-e28e-3869-b55a-1045830196e5 | -5.635 | -42.6871 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 93bf1bdb-1733-36b5-b105-01992bbd7b88 | -5.53993 | -44.91293 | 2025-10-14 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 309aa9b3-907f-3992-9562-2f78eb67c78d | -4.66003 | -43.12965 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c32b8589-ec5d-37aa-829b-c6163d872826 | -5.87691 | -42.87327 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6f70d548-e3c8-3350-aa11-fb4b9ea681a2 | -4.23336 | -48.69061 | 2025-10-14 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 22256393-4f90-3aba-a4c1-0a9170f4f239 | -6.44793 | -41.839 | 2025-10-14 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| aec40248-77dd-3c3d-8243-9907dd1e4c2f | -5.56738 | -42.98759 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be739c6d-97f0-31d1-97dc-e9830f652fd1 | -5.7387 | -47.47431 | 2025-10-14 04:23:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69489234-2c66-3517-b8fe-b4045c6d7eac | -6.57633 | -39.2466 | 2025-10-14 04:23:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| de6780d8-81a9-3d7a-93c0-aeffd4904d2f | -4.84767 | -45.21181 | 2025-10-14 04:23:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17ae4e84-ff3b-31e9-ba26-e9f7055b5580 | -6.33417 | -44.02102 | 2025-10-14 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4221943-7079-38f2-9ef9-55532fdf6182 | -3.13199 | -50.21317 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 42e8cba0-4eb9-356e-b676-0aea3c5e622f | -5.84711 | -42.32769 | 2025-10-14 04:23:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 83815704-a69b-3726-b0a4-e70cc0a18dab | -6.45749 | -44.58071 | 2025-10-14 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| adfea4e4-f4bc-3dde-ab42-1181ab717a30 | -6.48863 | -44.10853 | 2025-10-14 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0708eb37-c34c-39d7-9bbf-393c874c34b7 | -4.25249 | -48.55056 | 2025-10-14 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab986c79-f114-3793-8ca7-1bc0085b6c90 | -4.61848 | -45.78339 | 2025-10-14 04:23:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63c482fa-690b-337b-8a05-ebc6ac1df62b | -3.29321 | -43.50411 | 2025-10-14 04:23:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 831bd12f-3ef1-3f60-a3cf-068f7e9ed404 | -6.2986 | -42.98774 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0f0db49-2943-34b1-bda0-ead2943eb291 | -6.53582 | -43.55856 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2604ee74-f105-30fe-b524-942bc1de498c | -5.89683 | -42.83846 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 247562b1-4c8a-3da5-963c-41b24ef963b3 | -6.1607 | -41.72132 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 434ded89-9294-38de-abd7-671f1986aed9 | -5.88051 | -42.87378 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f6d103b3-5549-33ca-8d94-8cc6b7a53e3e | -4.7233 | -45.37635 | 2025-10-14 04:23:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b82f4af-cea3-3dfd-8238-f3944c1f5ef9 | -5.96887 | -42.2527 | 2025-10-14 04:23:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5391c2cc-30fa-38c5-9c2e-defa5a3806c4 | -5.48892 | -45.4121 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17d47850-227a-3407-819a-a4761a4bc41d | -5.84779 | -46.45258 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22ba8566-cb84-3d3f-9c6d-0540908c9e4e | -5.49224 | -45.41261 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e98b7ce1-6042-327f-b755-2bccc0feb335 | -5.03499 | -47.18163 | 2025-10-14 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b721b0fe-e1f6-3b49-981c-f1361bbec507 | -5.721 | -45.27426 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3aff510b-9012-3659-b66e-53bc95aeef1e | -6.3031 | -43.14186 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eddf40e-87db-306b-ad76-f12912c10de6 | -6.44554 | -41.82892 | 2025-10-14 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 72fbdbd2-fac7-3a4f-a308-872dadf30e54 | -3.62775 | -41.63301 | 2025-10-14 04:23:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 663bace6-5424-35a8-9804-54b290486b6a | -6.53978 | -43.56147 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 192d25a8-0d24-3535-af3f-d000cf0dcebb | -5.42601 | -41.33338 | 2025-10-14 04:23:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6c7cf0ee-93eb-3085-905b-9e1435b7e2bb | -6.43387 | -36.89224 | 2025-10-14 04:23:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c0a18c69-71eb-36cd-bc36-ae4f0f08c1e6 | -7.08058 | -41.95116 | 2025-10-14 04:23:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 32c7fd8d-faaa-3acc-a75e-6b72c684dfc0 | -5.72101 | -44.53848 | 2025-10-14 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66e441cb-f364-3dbf-89da-615c62268a55 | -2.87671 | -50.73665 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9d6ae32-5ef0-3c5b-93d9-8ee574e0d321 | -4.66413 | -43.12628 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 34cd5b26-4564-3e77-9bd3-5ded09029747 | -4.40318 | -47.5992 | 2025-10-14 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22b07e23-76a6-30ad-ae39-c67d67dd42c6 | -6.39297 | -41.48706 | 2025-10-14 04:23:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a2f565cf-7e6e-3887-a1bd-c80e0ba1ef9a | -5.30913 | -42.90678 | 2025-10-14 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 778e34e3-d233-3bca-890c-98a19bfda324 | -3.39045 | -50.13287 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24da02b4-92af-382c-ba61-51dbc778ca55 | -6.96927 | -41.68055 | 2025-10-14 04:23:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9fa3aa8d-4134-33b2-b17a-1784de2cd327 | -4.85361 | -43.20655 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c932bbe6-917d-3997-b05f-4a0c1dd5bf92 | -6.11339 | -46.34175 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed29abdc-9e9b-3ad8-a335-5418e0d79f3d | -5.90403 | -46.37628 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f47fc6ee-72d5-3631-9600-27f6be3f048c | -3.43145 | -50.24755 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b22ab6c-bbc1-39a1-ba2a-31f5ac7cf537 | -3.09821 | -51.29975 | 2025-10-14 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc0a459d-e660-30ac-b2c5-2cdf64773036 | -6.2937 | -42.99566 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 765f8901-728d-3f0b-a406-b750da25cf08 | -5.63493 | -50.03201 | 2025-10-14 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README24.md)
