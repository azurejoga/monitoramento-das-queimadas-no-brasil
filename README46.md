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
| 59a56525-7694-362f-b671-aec53970a7c3 | -2.62211 | -52.44556 | 2024-10-26 04:17:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb287f82-7b58-3a59-adb5-3f0caa99b87b | -2.62161 | -52.44863 | 2024-10-26 04:17:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8205a51-340c-39c5-a42d-9aac061b5642 | -2.6211 | -52.45172 | 2024-10-26 04:17:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a04bdab8-43e9-35e5-af92-0e163c056eed | -3.51198 | -53.14359 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0dabec1-3bce-38d3-9e2c-773eadbf244c | -3.50964 | -53.14329 | 2024-10-26 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa131848-6194-33a6-91ac-65285c5521d2 | -3.28517 | -53.68254 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17b5ddb2-419d-3f82-8ebd-944fe57449ee | -3.27959 | -53.68151 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bb4df2f-6e72-324b-a524-2bc9a89b330d | -3.99111 | -53.80329 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1320982-937b-3584-94d2-c31a4b6c93c1 | -3.99048 | -53.80701 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2448b2a3-52e6-3a37-b633-5a32bf15a3d3 | -3.98552 | -53.8024 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a070057f-8ac2-3192-97cc-b7188ea15769 | -3.84172 | -52.39762 | 2024-10-26 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d52deac8-d003-3199-a02c-5bb6c771aaf1 | -3.84124 | -52.40049 | 2024-10-26 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57ae539d-d8bf-3b02-b35d-728f1335f7cd | -3.84077 | -52.40335 | 2024-10-26 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ff98cc2c-3e3d-32e0-bee4-65c6e60dd821 | -3.83611 | -52.3999 | 2024-10-26 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 422982d7-5277-3226-bf1c-cde7d33bf48b | -3.74229 | -53.41014 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a470805c-61c2-3427-ac83-843f369d1ad5 | -2.19091 | -53.72889 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be85d991-8465-365a-b877-d46b2fdac8c0 | -1.34914 | -54.61134 | 2024-10-26 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 992d3128-0385-3e4a-9021-bab74f1b802f | -1.3487 | -54.61345 | 2024-10-26 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22127d88-e573-3c28-a358-b08eb1ca9ac3 | -1.34305 | -54.61014 | 2024-10-26 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa3593ce-5075-3261-aad0-dd67c7f6ff79 | -1.34262 | -54.61226 | 2024-10-26 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aac0d07c-2d29-3e57-a744-317db6413f97 | -1.34233 | -54.61467 | 2024-10-26 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 036a5212-ea04-3c3a-8a3a-2aae9f7cc909 | -1.18662 | -53.66513 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4e744060-8173-3400-ab76-66e177b55175 | -1.18539 | -53.67286 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1099adf5-70cb-392f-8236-868beb377736 | -1.18475 | -53.67693 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa8ec085-4a68-33e3-9d4d-a8ba727004e0 | -1.18467 | -53.67501 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcb77151-2034-3b8d-aa5e-95c99fcb0e53 | -1.18079 | -53.66448 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb88ab7b-853a-3717-b920-626a86db8234 | -1.18016 | -53.6685 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58e55e65-dc2c-3c51-a869-be5f932c1f0d | -1.18013 | -53.66661 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9bc99fa-e0dd-3408-af2f-dcea73f87ede | -1.17951 | -53.67254 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3e286de-58df-3aa4-a924-1dc04fae9671 | -1.17946 | -53.67065 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b983bda-baa8-34c4-ab57-5be0eaaf5c65 | -1.07613 | -53.65165 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ac3db6a-3bdf-3a9f-9672-0999ff9a5fe0 | -1.07576 | -53.6526 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aca9b1bc-fc54-3705-a098-3c8071be72ac | -1.06965 | -53.65492 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b98bf08-f733-32b6-879f-a9e95c6b4ddf | -1.06931 | -53.65582 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aca7eb5b-e956-34cf-a20d-18a4c5247684 | -1.06905 | -53.65855 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c8c11b12-64f2-390e-a3a1-4dbfe2309051 | -1.06873 | -53.65947 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7178f13d-0a2a-3061-9001-48e21665c409 | -1.06843 | -53.6623 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36c3441d-b597-3f8e-a318-1cab5e56a93b | -1.06812 | -53.66332 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7af724ce-38e3-3350-bd3d-d684dc685bc2 | -1.06773 | -53.66645 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f901e5fc-d504-3f4e-8b5d-6f02820d01d8 | -1.06745 | -53.66755 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf718c2a-56f9-3bf4-9e59-15d76276d6cc | -1.06703 | -53.67069 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29ee5a85-1061-3dbd-b080-fa3a689e3344 | -1.06167 | -53.66658 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0e1711e-8746-3d66-9286-2029c0949e2b | -1.03885 | -53.5144 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9613a0bd-ad0b-3577-afb1-914069cdb133 | -1.03819 | -53.51844 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0081ff41-6b84-3c90-8d58-85488b49fb22 | -0.87522 | -53.68481 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfbd1841-34a4-378a-97cb-5ff7db816a85 | -0.87473 | -53.68567 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8763a092-11e9-3590-b578-3df692860981 | -0.87453 | -53.68924 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c042fd69-7ebd-3737-9f52-11253ee6fc2b | -0.87402 | -53.69004 | 2024-10-26 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a707f6f0-0821-3d9a-9848-04c0ab94cfc4 | -3.14965 | -54.34906 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5376cd6-7e35-341c-bebf-c69b64022a0d | -3.14209 | -54.28734 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec995da2-9d54-3b32-a989-b4cb6da9726d | -3.13699 | -54.28202 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9a59315-11eb-3186-bb4e-9de170bc98be | -3.13629 | -54.28613 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0742e27f-a3db-37dc-b0e9-892720902420 | -3.13352 | -54.27226 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3467e9be-3ba9-3666-b4fd-92155392d159 | -3.13286 | -54.27626 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b073309-6d68-3344-8e8a-1848152a9988 | -3.13256 | -54.27287 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e46d62a-0ff9-3c4f-b4de-1101b04a35e7 | -3.13188 | -54.27687 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c172f7d4-d48a-3e12-976f-ecda197796c1 | -3.12705 | -54.27515 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aaa26262-f88d-32e3-97ae-b04d0d10b4ae | -3.12676 | -54.27175 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0c88c81-ccf1-3923-9ab9-b74ae4d3799f | -3.12606 | -54.2758 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1e1c5e0-358e-382f-bae4-3c42989dc8ea | -3.12124 | -53.71105 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b33edf1-7410-3599-8578-a589349053e4 | -3.11996 | -53.71859 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbdd23bb-954d-390e-9f6f-afe9cc2a0d63 | -3.11031 | -53.72628 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ea0e7a5-b6e0-30fd-a52f-74e38c266b8b | -3.10983 | -54.99196 | 2024-10-26 04:17:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d10f84c-3dfb-3cdc-9d6d-789ff8d0bf07 | -3.10928 | -54.99302 | 2024-10-26 04:17:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9caf9048-e9de-317b-ac11-a488ffc1b5b8 | -3.10741 | -53.72429 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3229846-dfa7-3f4b-a0f9-6ffd7db357f7 | -3.10677 | -53.72805 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99b5e3a2-8f23-3d3f-bbb9-9f9f3eb6ff23 | -3.10613 | -53.73182 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95d16345-dd79-3fca-96b3-b4c83a20edff | -3.10548 | -53.7356 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 028af19d-07fa-3680-b715-3f12a7d7e48e | -3.10531 | -53.72153 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22e7ed1d-e021-3b2f-826a-b8073e09bdda | -3.10469 | -53.72531 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cd7f054-a5e4-3c90-b6de-11cd0da63644 | -3.10407 | -53.72907 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eaf94c9-1a83-3213-a8c7-0c8cb6d3e116 | -3.10346 | -53.73285 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f348aa4e-998c-32ed-8a21-d11433698325 | -3.10284 | -53.73663 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6c15d71-b502-35e4-92a7-dad8b78348fb | -3.10244 | -53.71957 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acbdc0e6-308a-378a-ace9-3427dcdfb10e | -3.10179 | -53.72333 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b2b4e31-7bb2-3650-8eec-4e706ebfbb2d | -3.10115 | -53.72709 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76726325-edc5-3f15-8c15-8b581b1bdc26 | -3.1005 | -53.73087 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7483838-64f4-3c1e-9b98-9b2d9a7cbfad | -3.09985 | -53.73463 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cd17698-16dd-3565-b1ec-ce935cdbdf05 | -3.09968 | -53.72057 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62ada73c-b10b-3630-973d-fea68230e64c | -3.09907 | -53.72433 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70e94081-76b4-3dfd-862f-b0b3fef44321 | -3.09845 | -53.7281 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51f60151-241a-3935-9024-c7c19c7d1736 | -3.09682 | -53.71859 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27886272-e293-3bb4-a7a4-ffac9104775a | -3.09617 | -53.72237 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ac96d49-23dd-38bf-b196-367675bd98e2 | -3.09406 | -53.71959 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fe82ac3-9665-3e58-baee-2961f6857ed1 | -3.08311 | -53.83225 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4202c253-9246-375e-9b3b-cc0d69bceff6 | -3.07677 | -53.83524 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a27d4491-d3c9-3bcc-95e7-c0ee57826dac | -3.01188 | -54.49499 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a12b309-c298-3a72-8d32-aebc90ab7f71 | -2.98181 | -54.63621 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6677f42f-0f09-3a20-bea8-f561f546fec3 | -2.97578 | -54.63549 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 790dd472-9b93-382b-bb91-c985a244eac6 | -2.80533 | -54.10445 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba49654d-5bb6-3776-98a0-07c7b55e71e2 | -2.80399 | -54.00485 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69d6bee6-f8b1-3773-90bd-eb6abdca5d00 | -2.79954 | -54.10347 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b670624-dcf7-358f-b1db-74db24e0b9c6 | -2.79887 | -54.10753 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a6b0688-4caa-3752-998e-c6a1baa6cbdd | -2.79823 | -54.00387 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f40a75c6-e41c-3cf9-90f1-2af3156992e3 | -2.79239 | -54.11065 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 631ce90b-d14e-3d4e-8be8-bc98b7004e26 | -2.77816 | -54.7253 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 338f29c1-9a6f-3464-bcaf-6719179d6b92 | -2.77673 | -54.73379 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 81c98452-d520-3ff6-9fac-0d77a3860e62 | -2.77212 | -54.72431 | 2024-10-26 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcd8be6a-290a-337d-9581-5ab2cc9faf4b | -3.66268 | -53.84645 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2400cab9-8f45-3bcc-a096-325908edc9df | -3.65695 | -53.84616 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |


[Clique aqui para ver as próximas entradas](README47.md)
