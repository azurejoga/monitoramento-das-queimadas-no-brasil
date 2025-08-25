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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a5aa64f-f814-3b47-845a-840d9015ad9e | -5.0994 | -43.1977 | 2025-08-25 04:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| eda09f81-87a7-30cf-bd79-0755e60e4b42 | -8.8919 | -62.4487 | 2025-08-25 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 127036f7-4fff-32aa-a9f3-c7ffef60cd02 | -8.8734 | -62.4495 | 2025-08-25 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 149.9 |
| dc7a85c2-f3a2-3459-abc6-7571bce74639 | -8.8918 | -62.4677 | 2025-08-25 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 86e74651-7fb4-3bc4-98b3-f0bb69bb5619 | -8.8548 | -62.4503 | 2025-08-25 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8db727e0-68dd-37ae-8944-2b710a0951f4 | -8.0496 | -49.6753 | 2025-08-25 04:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| fec835bd-c6fe-3162-9857-e35709a22e57 | -6.8229 | -58.956 | 2025-08-25 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| c7731f4d-a535-39dd-979e-43022fe9abbf | -9.0061 | -65.3813 | 2025-08-25 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 743b4b5e-2a92-35b9-986f-e58759e00407 | -9.1722 | -59.4629 | 2025-08-25 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| fcdbc6e0-8e4a-3ee7-8191-e504c105b4f0 | -9.0601 | -65.7157 | 2025-08-25 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| b6e022e5-7bd5-3e8e-8aa9-dd653b32739c | -9.0972 | -65.7145 | 2025-08-25 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 5f7ec7bb-09fc-31f5-87d4-81ae17c09bc5 | -9.0415 | -65.7349 | 2025-08-25 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 1bd8f974-7e43-3a8c-8dc9-692b9c735705 | -5.0992 | -43.2211 | 2025-08-25 04:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 0d2fd239-aac9-38ec-b34a-36a3602a8415 | -7.9078 | -63.0542 | 2025-08-25 04:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 30e6275d-4e8e-3d21-8f74-b8a4fca5a216 | -6.8413 | -58.9552 | 2025-08-25 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| ea2b1b57-4f34-36ad-8a09-2f5d3cae811f | -9.0787 | -65.7151 | 2025-08-25 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| a267f4d2-168d-3f94-b682-9589650ea7bc | -6.2643 | -60.0167 | 2025-08-25 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 259d6e90-d56d-3ca8-9138-57003fa8618b | -7.9078 | -63.0542 | 2025-08-25 04:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 819e16d0-b753-3d14-9e87-ed4a8c6ba883 | -8.0683 | -49.6738 | 2025-08-25 04:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e0a05989-2a26-3eda-9ee0-3065696d6cb1 | -6.8413 | -58.9552 | 2025-08-25 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 5b1daa06-564f-3e98-9506-24479498d799 | -9.0061 | -65.3813 | 2025-08-25 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| aa1674d1-d1cb-3403-a7e8-bf29ecf3c496 | -14.1076 | -53.9847 | 2025-08-25 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 930e902d-2f9b-3b34-a8f8-3b095888b795 | -9.0601 | -65.7157 | 2025-08-25 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 1de39cc5-38fd-3e6a-9be3-b2c696bc0e78 | -9.06 | -65.7344 | 2025-08-25 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 53d5d5bd-a0b5-3e34-a02c-f4dff6ff460f | -8.0496 | -49.6753 | 2025-08-25 04:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d4df01d4-2823-32c5-a00f-499bf325a655 | -9.0416 | -65.7163 | 2025-08-25 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 0675404e-446e-3e83-9936-2168b25fa086 | -8.8919 | -62.4487 | 2025-08-25 04:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 7bfafec4-8145-371f-827e-e289e2e26227 | -5.0994 | -43.1977 | 2025-08-25 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 8bd78f84-5cd8-329a-abcf-da9f905b2b40 | -9.1812 | -60.7939 | 2025-08-25 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 7c1fc878-512f-3e64-acbb-0c9aebdea591 | -8.9875 | -65.4006 | 2025-08-25 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| a0e90704-4e1c-3330-ac99-08da6e8f4c72 | -5.1181 | -43.1964 | 2025-08-25 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| b9814dce-a234-3bec-8f2c-62943cf64266 | -8.0493 | -49.6967 | 2025-08-25 04:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| d65e2c02-e47e-3134-9aff-c8a216ae1b15 | -6.2459 | -60.0174 | 2025-08-25 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 6e233837-4312-3467-836a-a66c8d24cd8e | -6.8229 | -58.956 | 2025-08-25 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| c6c596e3-8ab0-30d2-adc5-3ba1b4c4a25f | -9.0972 | -65.7145 | 2025-08-25 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 19c32407-c52b-3c7a-aec2-36e0191e59dd | -8.9689 | -65.4198 | 2025-08-25 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| dfe5a124-df38-3494-9d20-7fd4447ef29c | -8.8734 | -62.4495 | 2025-08-25 04:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 676103a8-2aff-300f-a778-01fcd8688247 | -11.4595 | -55.4633 | 2025-08-25 04:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f70144d1-2761-3d00-b5b6-4dbc41f7562d | -6.2644 | -59.9976 | 2025-08-25 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 64c9052d-01f4-39ac-b80e-4050b7edfd6e | -8.0681 | -49.6951 | 2025-08-25 04:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 9f7a91e4-ba52-3ead-8c7c-cc99ce9f2b96 | -7.9077 | -63.073 | 2025-08-25 04:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 9b6e203c-1ffc-3e44-b3e7-7ffab293d04e | -8.9874 | -65.4192 | 2025-08-25 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 1ce03691-7431-3440-a613-33f7d0bef5cf | -8.8733 | -62.4685 | 2025-08-25 04:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 8117f9ea-45c4-3bd9-9300-d1c3b9a0583f | -6.246 | -59.9982 | 2025-08-25 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| ee31b7e9-5e3a-36b2-b430-e5a0532a0275 | -8.2129 | -61.3739 | 2025-08-25 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 778cc594-4143-30b7-82c2-1e0568e2c99a | -9.0415 | -65.7349 | 2025-08-25 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 901deabc-3a40-3272-9349-ca00f5e6171c | -9.006 | -65.4 | 2025-08-25 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 0e2ac9bd-f3e3-3bcf-93a0-d0fcb1d920d4 | -7.9078 | -63.0542 | 2025-08-25 04:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 78ff0442-eee0-360c-81cb-5522bdc90c7f | -8.8733 | -62.4685 | 2025-08-25 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 83.2 |
| cedb9fa8-d37b-37ab-ad05-7883c39eb2cb | -8.9874 | -65.4192 | 2025-08-25 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 62256d54-2b48-3b2d-8c14-e52d8ae20c3b | -8.8919 | -62.4487 | 2025-08-25 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 87fe5761-23ee-389e-a8b9-410143509945 | -8.0493 | -49.6967 | 2025-08-25 04:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 59c793a9-348d-38c2-895e-084b353e9cb3 | -8.8734 | -62.4495 | 2025-08-25 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 189.2 |
| 34f0437b-17a7-3d43-8fc5-52dc33ad6a40 | -9.0416 | -65.7163 | 2025-08-25 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| db216154-bf2a-3b32-b0bb-c90dfb1f7311 | -8.9689 | -65.4198 | 2025-08-25 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| c935a29e-8b01-3c2e-a04b-84d3f0fe9161 | -9.0787 | -65.7151 | 2025-08-25 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| b23b27a8-e140-30c3-b760-2715f2a032b4 | -7.9077 | -63.073 | 2025-08-25 04:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 3848cb15-a867-30f3-bd07-35e463591f4a | -6.8413 | -58.9552 | 2025-08-25 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a71f4a66-b33e-38df-adee-fad10f0cac85 | -5.1181 | -43.1964 | 2025-08-25 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 68be495a-0b1f-3316-b71e-bbb47267a312 | -8.0496 | -49.6753 | 2025-08-25 04:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 6386966f-9374-3ac7-82bb-ba0070929deb | -8.2128 | -61.393 | 2025-08-25 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 0b42133c-bfa8-3990-a713-f3bb68adcc7a | -8.2129 | -61.3739 | 2025-08-25 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| d8f6864d-e0b8-34af-af1e-0e9960535b5d | -9.006 | -65.4 | 2025-08-25 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 6488c710-b3fa-32b6-9aae-f9c52a3912da | -9.0972 | -65.7145 | 2025-08-25 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 75980705-6fc2-3923-9f14-740d8fd1ffd2 | -9.06 | -65.7344 | 2025-08-25 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| aabd6283-e758-3bc4-8c83-ee4264d8cad4 | -9.1722 | -59.4629 | 2025-08-25 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 27e01716-1fad-397d-9299-e149d01d1594 | -8.9875 | -65.4006 | 2025-08-25 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| f42de33f-6dc1-3365-bc67-badede0adc2f | -9.0601 | -65.7157 | 2025-08-25 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 8054c553-3963-3d91-9722-04b077edfc34 | -9.0415 | -65.7349 | 2025-08-25 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| ce3550a0-4d72-37be-8f38-2907d677f082 | -8.0683 | -49.6738 | 2025-08-25 04:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| f3a9655c-0afa-32bf-939f-4c886b4e4b94 | -5.0994 | -43.1977 | 2025-08-25 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a2b8dca7-d88e-3241-a01a-969de8d0f7f3 | -9.0061 | -65.3813 | 2025-08-25 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 13608f6b-ead1-3536-bc64-c12b10456a71 | -6.8229 | -58.956 | 2025-08-25 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 78799cd9-8808-3754-88e4-e647ab7af1e6 | -6.36311 | -44.47496 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37beb117-854c-38bc-8e88-5045a33df950 | -8.1656 | -45.06267 | 2025-08-25 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9abdd29d-98b0-341f-ae9a-e9ede6c3a6db | -6.13921 | -44.39498 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 557ae059-c053-3cf6-9e1a-d9f3f1251e35 | -4.96427 | -55.82304 | 2025-08-25 04:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a36f0449-473f-3564-9958-5afd6bdc9428 | -7.66334 | -42.67435 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0e68adca-4ae4-30bf-a9a9-547e3f12f617 | -7.90111 | -42.54241 | 2025-08-25 04:40:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fb704c4d-e6e4-3ff4-95a7-9cf51a8deb65 | -5.30278 | -45.2637 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71b23f2d-3509-35cd-80f9-c530ac12b809 | -6.03677 | -43.99438 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4badaae-913c-35b9-bb63-d7ee18a098c1 | -2.29615 | -47.98549 | 2025-08-25 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c316aa39-b007-39fe-8059-cd7efaba70cc | -3.36867 | -47.22321 | 2025-08-25 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04719e88-2a40-37b8-b12c-cff5ee0ee4e1 | -5.69592 | -45.51992 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2774f95-e8f4-3233-bc9b-bf71acbce1a8 | -6.9083 | -44.4292 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d379c9e-f37f-3cc0-999c-7ecc4f073ecf | -5.79459 | -45.39833 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9eb0fa22-2ae9-3ece-91da-7e3d63f43c99 | -6.88773 | -45.66063 | 2025-08-25 04:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 699e85a8-f109-3d8f-af53-a8be079bf9ef | -3.59671 | -47.52478 | 2025-08-25 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf39fa55-0643-3694-b42a-44a12ac8d767 | -7.32862 | -43.41793 | 2025-08-25 04:40:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13be66f4-d83b-336b-a7a8-806f08b26f50 | -7.47361 | -45.02 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9008acf9-74fb-3665-a9a3-a1ee1704e9f2 | -0.57547 | -50.43459 | 2025-08-25 04:40:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f696e81-418b-3d4f-a4d2-550dc2460735 | -2.26598 | -47.85606 | 2025-08-25 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5937abc0-7104-3bd8-8f0a-53d601fae0a4 | -6.6816 | -44.42223 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db8516dc-cdb8-3f1e-8c42-95d9ae502ff5 | -6.43712 | -44.56162 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e80f44ba-4ebe-3b67-8e72-6b4466f09ebe | -4.3108 | -48.10028 | 2025-08-25 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebe940c5-df46-395f-9ce2-78d679f0c4da | -7.09529 | -44.62901 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2535b9de-957e-3bea-bfb4-2c7d0abc14e6 | -6.45326 | -44.61617 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6a37a114-fbe9-3b0a-8189-05b600bb023e | -6.91851 | -44.41628 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca759dba-0b45-3bf8-9baf-80b97813d39e | -7.09317 | -44.63233 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72117ffb-79a1-3293-9c98-8ffc3d44db6d | -3.93617 | -55.75757 | 2025-08-25 04:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README37.md)
