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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bee77fdd-8b7a-314c-a584-b5c611f5d24b | -11.6489 | -44.0854 | 2025-10-19 02:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| e7434ee8-1812-3538-a95c-0cbc32bedc6c | -5.647 | -44.8192 | 2025-10-19 02:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| d039c909-609e-3a04-9109-1a4d47f7baff | -10.5522 | -43.3761 | 2025-10-19 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| c7d5d365-fd6e-3746-9c54-ef211e7a2927 | -2.7026 | -49.5422 | 2025-10-19 02:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| bb359ae3-1f46-3f1e-b877-94bbd79cab98 | -2.6841 | -49.5427 | 2025-10-19 02:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 1b901b34-40f8-307f-a56a-8b15aeabe533 | -5.6472 | -44.7964 | 2025-10-19 02:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 9f13afa6-63aa-3d90-9918-d4e655a3cd6b | -12.4493 | -45.4262 | 2025-10-19 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 622c7cd9-7c0a-3e9a-a752-b3f6dbb25b06 | -11.6489 | -44.0854 | 2025-10-19 02:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 39485eec-cb00-3ce9-bc15-074a2c4fe69d | -2.6841 | -49.5427 | 2025-10-19 02:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 88e148f3-f6d8-3e39-8242-7efbea46f9eb | -12.4686 | -45.4232 | 2025-10-19 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 7f4d663d-1ebc-3b7a-ae29-a6068522522b | -5.1017 | -47.79 | 2025-10-19 02:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 28ecd33f-508d-35e8-9118-d1c404fe1eb9 | -12.1485 | -45.08 | 2025-10-19 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 31051916-eccf-3c36-b1b4-ab36e94b07e8 | -8.6032 | -40.1834 | 2025-10-19 02:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 107.0 |
| cc23ab0e-8c65-3ed4-a337-6395dd079c3a | -12.6447 | -50.7644 | 2025-10-19 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 116.0 |
| fc12b503-c85f-3382-a9b9-2ddb9e688702 | -8.6219 | -40.2058 | 2025-10-19 02:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 60.1 |
| d39353d5-ec69-3451-8c97-9cc886cf8916 | -11.6113 | -44.0443 | 2025-10-19 02:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| c7f7c2c1-6d59-3d45-a3d6-18b8b25af451 | -10.8891 | -46.0814 | 2025-10-19 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 7bc807e4-7ccf-3e43-b8ae-8d0d0c3eaf47 | -5.647 | -44.8192 | 2025-10-19 02:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| e4defd0c-38f8-3635-b131-d3b4bdedec8e | -12.645 | -50.7429 | 2025-10-19 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 1d4d2685-94d0-367d-bf17-ec28470ff16c | -16.1528 | -41.1524 | 2025-10-19 02:10:00 | GOES-19 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 43.9 |
| 33517706-8789-39e7-9cac-46305c7c37c4 | -8.6029 | -40.2083 | 2025-10-19 02:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 57.5 |
| 0e026c01-c96b-3f56-a242-ec9ffde992a0 | -12.699 | -48.6299 | 2025-10-19 02:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| d23c6fe7-c3d4-3562-a6df-049cdc86167a | -12.1489 | -45.0568 | 2025-10-19 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| c24304b7-c15a-35df-8ffd-b7e788e870ed | -11.6109 | -44.0678 | 2025-10-19 02:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| c908cf33-401c-3bf0-8aa8-7ae3378daa7d | -2.9127 | -52.735 | 2025-10-19 02:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 7f367124-3c9d-331c-98d2-97d0879a58c1 | -2.7026 | -49.5422 | 2025-10-19 02:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 50fcaab0-ff0f-3fe6-a152-488b21ccc235 | -2.9128 | -52.7146 | 2025-10-19 02:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| f6ba0d87-3f63-36ce-9a79-f719018a0445 | -7.6238 | -60.9212 | 2025-10-19 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1fe21733-3730-3f4f-beae-47dc72d345e2 | -13.5405 | -43.0077 | 2025-10-19 02:10:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 873373d3-6b96-3781-9f74-f37615564b61 | -12.6638 | -50.762 | 2025-10-19 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c36a2416-c7dc-3362-bfc0-b292b0f7696c | -8.6223 | -40.1809 | 2025-10-19 02:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 108.7 |
| 62231a04-b0a5-3754-bedb-cfca4656ef4e | -11.6301 | -44.0649 | 2025-10-19 02:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 5851f1b7-9ccf-323f-bbfa-cd8a24641903 | -10.8891 | -46.0814 | 2025-10-19 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 8c60a4e8-d82e-34a0-a760-cece031f3819 | -14.457 | -51.4935 | 2025-10-19 02:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ba2466b2-c98b-3427-a41d-d79fe24c0168 | -11.6113 | -44.0443 | 2025-10-19 02:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 0e1eb94a-f3a2-3416-b8f0-0d18d917e698 | -8.6219 | -40.2058 | 2025-10-19 02:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 1c2757a7-35ef-3f4c-bd10-0d2201d2f24a | -2.9127 | -52.735 | 2025-10-19 02:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4bb433ea-8214-3437-bee1-64c413bf140b | -2.6841 | -49.5427 | 2025-10-19 02:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 0c73b8fe-1a66-374b-893a-09099c3f5eb1 | -12.699 | -48.6299 | 2025-10-19 02:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 33e27027-39aa-3c5f-9431-7a0c263bf699 | -5.1017 | -47.79 | 2025-10-19 02:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 281dcfe3-52db-3f22-bc33-13ded60acebf | -2.9128 | -52.7146 | 2025-10-19 02:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 710c803a-1145-382b-a9dc-16e44a083a40 | -8.6029 | -40.2083 | 2025-10-19 02:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 73.8 |
| d3b389f8-9b91-3114-9d81-34c827320527 | -8.6223 | -40.1809 | 2025-10-19 02:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 3de7dcf1-c2df-3bc6-8351-5682a3464d0c | -8.6032 | -40.1834 | 2025-10-19 02:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 123.7 |
| a5388eae-eabc-36b5-a202-81ff660018d7 | -14.4377 | -51.4961 | 2025-10-19 02:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 21129ce3-e436-33a5-8cc2-21105efc54ed | -11.6109 | -44.0678 | 2025-10-19 02:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7fdfbafc-42ea-3898-9d8a-7c56fc1af33c | -2.7026 | -49.5422 | 2025-10-19 02:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| d2bf4ccb-509f-385f-a2ec-023919ab8193 | -10.8891 | -46.0814 | 2025-10-19 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| adc6f2eb-511e-323a-8a61-dfacaaf6f0f7 | -14.0166 | -46.1848 | 2025-10-19 02:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| a4a5a554-5ebf-344a-bc33-00d055574e89 | -11.6109 | -44.0678 | 2025-10-19 02:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 03deb2d9-937c-3242-b96b-12c29fca6381 | -9.2399 | -46.0541 | 2025-10-19 02:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 3cbf44e2-7bd5-3c6f-bf7a-dd3142b315b6 | -8.6032 | -40.1834 | 2025-10-19 02:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 114.0 |
| 9349d99d-4f8f-397a-ac9c-2988f47fa741 | -14.0365 | -46.1585 | 2025-10-19 02:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 243.8 |
| 21a11aaa-b3f2-33c3-bca5-e70e4c086ac9 | -13.5405 | -43.0077 | 2025-10-19 02:30:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 54.4 |
| a6770555-b012-33e1-8b25-0d7eb5195721 | -12.1489 | -45.0568 | 2025-10-19 02:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 68a50d14-ed57-35b4-bbea-293aeb88ce7c | -8.6029 | -40.2083 | 2025-10-19 02:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 91.5 |
| dbc2b48b-6bad-3f8e-89c6-200bda6816a2 | -14.017 | -46.1618 | 2025-10-19 02:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| e07331a4-71ad-3fdf-8b78-69aac56ad8d6 | -2.9127 | -52.735 | 2025-10-19 02:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 4c5f7b40-0045-354e-8ba3-0edc03f1110b | -2.9128 | -52.7146 | 2025-10-19 02:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ca6472ca-1349-3465-8a4b-ac57394602e7 | -8.6223 | -40.1809 | 2025-10-19 02:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 123.1 |
| 1f830d5e-e68d-3aab-a850-65daea30841f | -8.6219 | -40.2058 | 2025-10-19 02:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 98.6 |
| ced47cec-cb01-332f-ab76-fc108c849ab2 | -14.0555 | -46.1782 | 2025-10-19 02:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 5eae7d48-27c9-31df-8f35-a99e13ed0f18 | -14.036 | -46.1815 | 2025-10-19 02:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 256.3 |
| 3a5a8434-7299-3ba1-a077-687311a31851 | -14.296 | -51.8781 | 2025-10-19 02:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 3681b576-07f4-38be-9bc6-53e1e872b29f | -14.2963 | -51.8568 | 2025-10-19 02:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| ae59d90c-9e47-310a-8225-8c7425d3af6e | -2.9128 | -52.7146 | 2025-10-19 02:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 6676ba88-a009-31d2-9dbd-6bfd63ff2c8a | -11.6109 | -44.0678 | 2025-10-19 02:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ba13d04d-2a2a-37f0-acb0-20dbaa1e9b63 | -9.2399 | -46.0541 | 2025-10-19 02:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 5fbdce14-0e59-3ccc-94f9-2819bde42ce9 | -12.1489 | -45.0568 | 2025-10-19 02:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5cc1ea84-b8ed-3db4-bcc3-f28427a5e259 | -8.6032 | -40.1834 | 2025-10-19 02:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 129.8 |
| 36c362c6-73b1-3ef5-8d9c-32e50f5a5137 | -16.7435 | -42.7761 | 2025-10-19 02:40:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 39cad3f4-4106-37f9-88b3-32c792412e5c | -2.6841 | -49.5427 | 2025-10-19 02:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 4c23af94-331c-39dc-b68f-351a6b819f58 | -8.6219 | -40.2058 | 2025-10-19 02:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 90cf5f68-6421-3a28-829d-fb5d42d50261 | -8.6223 | -40.1809 | 2025-10-19 02:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 101.6 |
| ca81f00f-508d-3aa3-9cb8-21862b083d19 | -16.7635 | -42.7714 | 2025-10-19 02:40:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 229.7 |
| 73c109be-e5fc-3bb9-8384-08db24e92ae0 | -13.9976 | -46.165 | 2025-10-19 02:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| e09c7fbf-da21-3b73-9737-342d9ba1ae87 | -8.6029 | -40.2083 | 2025-10-19 02:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 92.0 |
| aa5d9559-9269-3008-8e20-e3e8c130080b | -9.221 | -46.0561 | 2025-10-19 02:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 09858387-15b1-3d4a-80dd-9bb1053eb659 | -14.017 | -46.1618 | 2025-10-19 02:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 507fd1bf-3c6c-3b0b-9f28-601f4dda77c2 | -10.8891 | -46.0814 | 2025-10-19 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| fa93ff4d-1cda-3377-8d1e-627dbbac95ec | -16.7628 | -42.7961 | 2025-10-19 02:40:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 6017bb8d-bce7-3fdb-96d3-a38d00915f7e | -2.7026 | -49.5422 | 2025-10-19 02:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 47bd20e7-c649-3bb8-bd99-f37096ff5019 | -2.9127 | -52.735 | 2025-10-19 02:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| c3a4798e-5389-3dc9-bc77-46df880de140 | -16.7834 | -42.7668 | 2025-10-19 02:40:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 54a46043-b009-3028-a06b-8a6a2015eacf | -12.9917 | -47.2767 | 2025-10-19 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c5ca7389-a927-3338-95ea-05e729c25c4d | -16.7834 | -42.7668 | 2025-10-19 02:50:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 8464212b-6bac-3467-b55a-2472ff6d35e0 | -14.0555 | -46.1782 | 2025-10-19 02:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 53f7999c-6ecc-3182-aea7-7aea0d1cdfe9 | -16.7641 | -42.7467 | 2025-10-19 02:50:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 8f1b6fb2-c5eb-3040-b021-3f744f425870 | -8.6223 | -40.1809 | 2025-10-19 02:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 120.4 |
| fe0903e1-5bd0-38b3-ae0f-82dc928b2794 | -16.7628 | -42.7961 | 2025-10-19 02:50:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 11844b7c-4249-342c-8a2c-ac441a1b5ed0 | -10.8891 | -46.0814 | 2025-10-19 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 1cb293f2-c438-3e64-a06b-71ced537cf6c | -11.6109 | -44.0678 | 2025-10-19 02:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 452bab58-b9ce-39b3-a64d-01d09f99f1fb | -16.7841 | -42.7421 | 2025-10-19 02:50:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 98.5 |
| fc702835-5a2c-37c2-a0d9-3e676df3141f | -2.6841 | -49.5427 | 2025-10-19 02:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 03bd2975-9cc7-3ec6-8ed5-4c4f54803ed0 | -2.9127 | -52.735 | 2025-10-19 02:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 7b2e507b-5af6-32e0-9f37-8dfc9094c35d | -8.6219 | -40.2058 | 2025-10-19 02:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 84.6 |
| d7dc11fd-4d4d-3469-8390-43ababb0fdc8 | -2.7026 | -49.5422 | 2025-10-19 02:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 9c4dd9c9-b656-3ab4-a6e0-d854eb13b5ab | -8.6029 | -40.2083 | 2025-10-19 02:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 1074001b-73ad-38c2-896e-d8e55ed6a5f8 | -2.9128 | -52.7146 | 2025-10-19 02:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c973fb5f-f932-39e5-be9d-0c7f9fb3d0ce | -16.7635 | -42.7714 | 2025-10-19 02:50:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 374.4 |


[Clique aqui para ver as próximas entradas](README7.md)
