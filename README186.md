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

## Dados Diários - Página 186

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4aa783bc-e969-38c9-b39f-2fb578f18376 | -10.86594 | -63.91343 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 334a2b38-2852-3fd6-959f-d827c92b17e3 | -10.86422 | -63.92305 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8261d7ff-4e77-3a9a-8631-6689797a8a66 | -10.86208 | -63.90841 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| abe6e087-8954-3a2c-8a7d-c90ccbd5b2bd | -10.86126 | -63.913 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d303d340-01be-3c4c-8dcb-2ef8184ad679 | -10.86082 | -63.88893 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f28121da-b49c-33a4-814c-2c7c0b096e7c | -10.86041 | -63.91771 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c6ed59a6-94a8-3495-87ae-306edc39ce66 | -10.85956 | -63.92245 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d86b67b4-a77e-3f30-8f9b-211ab9fd90fd | -10.83976 | -64.1776 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96f4c62c-4ae0-3020-bad8-072b8a0f0afa | -10.83833 | -64.17578 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47b61d68-45b4-31b6-bb19-fe4b94609785 | -10.83587 | -64.17242 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 445dd3dd-5f75-3ce3-af30-f53771e09017 | -10.835 | -64.17709 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94d01317-0c0f-3c96-afa1-7e2828da7dec | -10.83358 | -64.17525 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce138ecd-84af-3fbc-b5c1-a5f2253ab160 | -12.13638 | -63.35981 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eeb89639-b777-39df-b575-600e29aff2b2 | -12.13562 | -63.36408 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 026036ee-2a3b-3450-acce-e448d319c267 | -12.13205 | -63.35899 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 463ca4d5-a043-330e-8dfb-1a6b3307d8bc | -12.13128 | -63.36325 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 989304d4-735c-341f-ac65-26ad2e221f41 | -12.12694 | -63.36242 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4743b446-c39b-3462-83d5-e124a0a325f1 | -11.89191 | -63.28651 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4669387a-ed36-33bb-9e83-35057a16a256 | -11.88759 | -63.28566 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c7d36d67-5c2a-3172-b3b9-bbbb22bf44af | -11.88273 | -63.28215 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0494805d-4068-3f97-b9ba-f2f20a6dcc0f | -11.8784 | -63.28133 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d8dbf69-68e6-33f4-93c3-ccf56751520f | -11.87302 | -63.29169 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 172153df-cd37-38d4-be3d-03fc7c7edf09 | -11.87182 | -63.29327 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f97d0346-b691-3414-8d6d-3d2dc2126754 | -11.86869 | -63.29087 | 2024-10-09 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 157820bc-46b8-343f-9ef0-8f9f2673652a | -11.00624 | -63.89396 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ef48630-0aa4-3ba8-b5d9-49e06eb5eb52 | -11.00538 | -63.89645 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf0704df-601a-3578-8351-7b02ca514416 | -10.9943 | -63.90503 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7340a90e-b2df-36f6-9fc9-fd1dbffb929d | -10.97737 | -63.94963 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3267841b-65aa-3a24-876a-fe911bc17079 | -10.97654 | -63.95424 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ff705e3-fe4b-300f-bcf0-c2dd556bbcc4 | -10.97571 | -63.95889 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ae69164d-e9f2-3d33-bc83-a730da7065a9 | -10.97486 | -63.96369 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17c0076a-f6a4-304e-b834-99b0675f503d | -10.97397 | -63.96865 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fcfcba4-b5c6-3e4f-8d6c-dfd87fc5e103 | -10.97308 | -63.97364 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef541e59-551e-35c2-8613-bf158edfd15b | -10.9727 | -63.94915 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb2866b6-ac3d-3926-928d-aaece0105f32 | -10.97135 | -63.98333 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a6496ba-e6ea-3912-be13-aca3b40446ce | -10.97052 | -63.98801 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3af9dfa5-4851-3b5c-af0b-56111ee0d605 | -10.95876 | -63.60122 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 399a50e4-7bb2-3511-8254-a3b3e833c341 | -10.92654 | -63.8629 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85c8ffdb-5161-3e53-a135-24116df7f183 | -10.92572 | -63.8674 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f539334-3ab3-30f5-8ed4-3a7fa2711e12 | -10.92482 | -63.87231 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa585f1c-4b06-3f0d-860c-3bcfb8bd9aa7 | -10.92209 | -63.86132 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 652f02ce-9e82-34a8-a0c6-64c4efed4e8c | -10.92121 | -63.86615 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb3e40cd-986c-31a4-adca-9dc8e15ae6ba | -10.92025 | -63.87135 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de531868-a7e1-3b63-a32c-badf7ee011e7 | -10.91836 | -63.85582 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0be0658-d4e5-33fe-b968-f669647678e8 | -10.91758 | -63.86009 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0781ad2-29a1-3777-baf0-deb51851bc6f | -10.91487 | -63.87486 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dfa606f-8b47-3acf-b59f-52e2c7bc96c8 | -10.9138 | -63.85754 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71c2af89-7a53-3da4-b3b5-a66ed198caba | -10.91376 | -63.85508 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b972054f-e1b3-31ae-b4ac-b818bde2f3cb | -10.91169 | -64.15495 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 257396f5-9d32-3bb4-8a0c-e416c746a106 | -10.91079 | -64.1599 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1eb61878-3acd-3410-a0a1-8ec2a04ab14f | -10.90784 | -64.14955 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6be7deac-4ef8-38f1-aba3-51d2d48b10ae | -10.9071 | -64.15362 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9a0108d-51b7-3be3-bd71-3f5d1d2c1027 | -10.90686 | -63.89703 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73ea10fc-e4fe-3ee4-bfe5-a5b7a4715f95 | -10.90622 | -64.15845 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5535d55-052a-3683-838e-54516c9ede58 | -10.90609 | -63.90139 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82380d4f-db49-3889-9fe0-c5f5e99f5ab6 | -10.90577 | -63.89857 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9c624bf-1b8d-342c-9132-68c1d9a53fd8 | -10.90495 | -63.90302 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63268f27-ae84-33a0-b6d9-77296eac0c98 | -10.9024 | -64.15285 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a619223d-5568-3cf5-8100-897b651b260f | -10.90155 | -63.90017 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cd1a203-1ed8-315f-bea0-fd3a53037924 | -10.90074 | -63.90477 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1e01039-a7cf-3e16-8fc1-cb97d1126e66 | -10.90043 | -63.90173 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cece7b7-1ca2-365a-869d-9fe31a72f528 | -10.89955 | -63.90652 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b46a4ed-74ce-3e74-b472-6efdb99aecbb | -10.89763 | -64.15254 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1f5dcb3a-56dc-3dcd-9094-746c8e146914 | -10.89674 | -64.15742 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec957a01-716a-349d-a9b3-5e9d9a315e89 | -10.89583 | -64.16242 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9ca5c31-b173-39db-8d2b-5aa386e9f750 | -10.89439 | -63.91382 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2aa0403-0145-3f33-b584-88a4609e556f | -10.89313 | -63.91555 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35738447-1549-360a-b12f-3be6e9543c23 | -12.11529 | -63.84694 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de8125a5-fa15-3080-b800-0eacda94d526 | -11.74717 | -63.81432 | 2024-10-09 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f30425d5-95d3-3b3f-a1eb-6c54304c41d5 | -11.74473 | -63.82787 | 2024-10-09 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60bfe879-2068-3277-91d8-8fa8b6f27837 | -11.74242 | -64.07733 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1b72235-cfdb-3311-8483-d9e7345f136e | -11.74028 | -63.82667 | 2024-10-09 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac0abd86-d2a2-33ed-95e4-7d103ac69e03 | -11.72577 | -64.14419 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f33c7876-1998-3e94-9c70-f20b247393d1 | -11.72519 | -64.17424 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1a5ee8e-4293-3d27-a922-fe9c863d40be | -11.72118 | -64.14323 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 725e4e55-59b9-3b35-8a48-54572440eb10 | -11.72065 | -64.14009 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 631634d4-e55f-3923-ab77-ff565c3a5823 | -11.71657 | -64.14239 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f77eaac-1f11-38b6-b9af-fa672bcb7eaa | -11.70551 | -64.04545 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b766f9d-af13-32bc-b696-d15414351ca5 | -11.70184 | -64.03957 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c635ad6-e5a4-3706-80b8-7d8690278c4a | -11.70095 | -64.04453 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fc004dc-2b93-3e4b-b8d7-f8792aa4ee84 | -11.69259 | -64.01237 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4eb82734-0a4a-329c-998c-79501fa877cf | -11.6908 | -64.02222 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5ccdaff2-c73d-3d75-a95c-532155ba925d | -11.69003 | -64.02642 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 16da4220-c4d1-3840-ad73-68b856434853 | -11.68804 | -64.01139 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1baf5b78-386f-313a-bd49-ba7a4e054598 | -11.68713 | -64.01643 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b305f997-79be-3290-a7ef-601feba862fb | -11.68444 | -64.00526 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8e346c7-1056-3c6c-a6bd-4fefcbc120fd | -11.6838 | -64.03466 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 48ffba69-1c88-3889-b251-290734d2c5cf | -11.68349 | -64.01044 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 475109e9-11f4-3d58-9611-1f4482231e48 | -11.68171 | -64.02023 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17d5d7ca-28e6-31a0-9920-b229fd891341 | -11.68018 | -64.02859 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c6b54370-730a-3007-a747-d43a2f131e5a | -11.67995 | -64.00397 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96620133-f716-344d-bde1-be09a4fba9a0 | -11.67926 | -64.0336 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8386f471-643c-357b-8463-b740ff6828d9 | -11.67896 | -64.00938 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b640fe54-e2a5-3392-bb3a-1b3be286e70c | -11.67831 | -64.0388 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6b738515-1fc3-3e28-b110-16d723c8f6ed | -11.67718 | -64.0191 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8bd24cbf-cbd7-3c59-9d48-19f8b29b0cfe | -11.67639 | -64.02344 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 923e18f9-4af5-39b7-b1e8-caf3473495e7 | -11.67561 | -64.02768 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a695b43-1832-39da-a5c6-0048360bdbe2 | -11.67472 | -64.03257 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| edf19db9-cf74-3bd0-826f-ac764a4b590c | -11.67201 | -64.04741 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be865175-3f70-374c-9e22-8fe85f700ffa | -11.67185 | -64.02238 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README187.md)
