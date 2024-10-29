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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c67eff5-9379-3ab5-b17f-b5d621c7aee4 | -2.16242 | -54.63809 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea8dd919-3eaf-3be5-984b-03a79c2f7a0c | -2.15632 | -54.63361 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37565f6c-087c-32d4-8232-8839f94f4287 | -2.15578 | -54.63706 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac18701a-ea88-3737-be61-2425aba4f79e | -2.1259 | -54.80531 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02bdc4b6-629f-37f9-9a9a-eda0995e7112 | -2.12536 | -54.80875 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72bbe13e-d70a-33de-9ff1-dd6fec1f7431 | -2.12258 | -54.80479 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ac981fe-47f1-3e66-84b5-6b08a6033914 | -2.11981 | -54.80083 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0f7ac2a-2911-3520-9fd2-a017a6ba564c | -4.51998 | -55.45958 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49c0cdd4-579e-3843-be9f-d5883ba9f27d | -4.50972 | -54.96257 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b677211e-2e54-3965-88a6-176e167f4b0c | -4.5064 | -54.96206 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2496eb86-c33a-38c9-ab58-564b29e6c09e | -4.49693 | -54.85434 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 891deaa2-4eb3-3efc-9318-fe62674184c5 | -4.48743 | -55.08301 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5effb3c-617b-36a8-8a79-1d13db245673 | -4.42 | -55.42995 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aca14c7f-0048-38e0-961d-a6bba4e12421 | -4.35871 | -54.93563 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfbd0696-d74b-329b-a0d7-e244b77fdcd9 | -4.34961 | -55.03688 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19bd2720-cf9f-34a6-82a0-2a36ac09b7d9 | -4.34492 | -55.13165 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5df3dbe-8e98-36f2-b48a-864f4e250309 | -4.34214 | -55.12767 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35ea28ca-3544-3999-9a08-90dab9673d2c | -4.3416 | -55.13113 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1da21b99-3591-3654-b43f-99f26670e876 | -4.29513 | -55.12387 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa9c64b9-a951-3c29-8c8f-36537b0b4cc8 | -4.29181 | -55.12336 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3e5cb69-ea10-35c4-91c5-d1b3107ad151 | -4.25983 | -55.15374 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 589a1662-7545-302e-b68a-64b4e62c0551 | -4.2321 | -54.88064 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39007a11-a9bc-357c-9617-42b406979237 | -4.22878 | -54.88012 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0f35d02-e9fe-349f-b4be-c97db5e8647c | -4.22507 | -55.31472 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a55afaf-5d6b-399c-9910-0ef53abc6225 | -4.22175 | -55.3142 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 917076ba-3351-3ca0-b206-cba8a569da77 | -4.18492 | -54.90163 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6d7fc75-4623-3270-bbd2-b915cd5ddad4 | -4.13557 | -55.04252 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c55c3d4b-2a75-3946-8b87-4e4bc315245c | -4.13226 | -55.042 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1cbd658-1f46-36ca-9949-6fbb79cb36a5 | -4.10136 | -55.06549 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36983ca6-063d-3e3b-9ce3-f638b1fbc1f2 | -4.01738 | -54.82552 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bac04af9-ccf6-38dd-8402-2ee91a366063 | -4.0146 | -54.82156 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a5f21c0-36b8-3e4c-9a5b-8c4215e8d256 | -4.01406 | -54.825 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b19fb00c-24be-3d63-b8ba-e351590b8bb2 | -4.01074 | -54.82449 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e555e627-7bbb-3806-904d-a82396fa9ecb | -3.96369 | -55.38313 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06ad49bc-ab1e-3808-91b9-1e7463a227fc | -3.95673 | -54.75938 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c350001-ac0d-3a46-9d71-8b6f2dd082de | -3.92384 | -55.3769 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbffac7f-319f-3dae-894b-aae2bd2ab6c3 | -3.92276 | -55.38379 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2a79df9-70d3-3794-afe1-5429ce150661 | -3.91944 | -55.38327 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74a8f2e1-b4d6-3166-bb09-ea49b16f4c45 | -3.91612 | -55.38276 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4346d8b7-5ea7-33db-bc36-8ab7c4764364 | -3.8755 | -55.36224 | 2024-10-29 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49f1f3c7-20c7-38c2-bd1f-55366e18eb2a | -3.85464 | -54.76489 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0b48984-b7f3-3e50-b55f-ffeb29bc5d84 | -3.85131 | -54.76438 | 2024-10-29 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d89872d1-0015-3c42-acd2-f1ac0e17831a | -3.70509 | -54.4251 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab5aefeb-d6b5-370d-914d-2632dc0fd8b1 | -3.70454 | -54.42859 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2200025-630e-3310-831c-9b2764de0912 | -3.70176 | -54.42457 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 716058bc-aed3-39df-9e3f-f5597738d15d | -3.66094 | -54.5108 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79f09a4b-b77c-392d-a0b6-b31414cb6d0b | -3.6604 | -54.51427 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3b37091-13f7-3f27-84de-abe3e6d83eac | -3.63816 | -54.67769 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca3c16a4-2c60-304d-a79a-d4c409e90278 | -3.63762 | -54.68116 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d77b722-c155-3fdb-9eb6-718d206cafd3 | -4.11504 | -54.28852 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c5e24c2-ca5c-3b43-a8c7-6b81d6f1a9c3 | -4.11449 | -54.29202 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef07b3d5-4a42-3f7e-957b-3839c020451e | -4.11224 | -54.28452 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb485080-8a44-3ec8-957d-78a4445ecbc3 | -4.1117 | -54.28801 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44597ad8-05b7-3612-a57c-cb710997fe76 | -4.11115 | -54.29149 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a756d52-aa95-355e-9aeb-64be4c183920 | -4.10836 | -54.28748 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7254c0ff-6c12-3e32-aa30-118763ae0a23 | -4.1046 | -53.94722 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0747d235-fd46-3f95-a370-74e23fa9b267 | -4.10179 | -53.94315 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f4d4dae-6a23-364d-b36f-df23036b6144 | -4.10123 | -53.94672 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1f10119-409b-31db-9321-5ac50ac58848 | -4.09842 | -53.94265 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4cb1521-65cb-343b-9bef-bcea19af44ed | -4.09786 | -53.94622 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a18907e4-562f-3142-ba79-1d074ff2275d | -4.09673 | -53.93139 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3592b824-dcfc-3b24-b2dd-8bc78e6de6ba | -4.09561 | -53.93856 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1246eacf-1d71-3bd9-8783-652714130f78 | -4.09281 | -53.93446 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89ae6530-f444-30f8-9a7a-dbfca26df940 | -4.09277 | -53.89056 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0ad8074-ef3e-3978-ae10-0816fc7c85ce | -4.09225 | -53.93802 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d51a691-2515-32d6-92bf-3f2dbc42d840 | -4.08939 | -53.89007 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 829df68c-c962-33aa-bc91-adee16b89729 | -4.0716 | -54.28162 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f3173d7-17d9-392e-a7cc-bdd989a1b589 | -4.06846 | -54.11205 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ee5aa31-6b79-3415-a608-3545d3d19081 | -4.05541 | -54.28284 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dd8faad-3626-336b-a56b-a4c67c998c90 | -4.05206 | -54.28233 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3dae13e-509d-3053-9c07-d072ea7d4885 | -4.04834 | -54.10899 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f623b10d-1b39-3c37-b670-a919dd3b9acd | -4.04779 | -54.11252 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7f41e8e-761d-3e8a-91cb-3ecf9ae368ad | -3.99422 | -54.1259 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69ba37bb-d62d-35e2-ad6e-af868872bdde | -3.98696 | -54.12841 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99bb9be1-5a68-347d-ad39-1d977780c784 | -3.98642 | -54.13194 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e3da50a-7d34-3124-8d06-03d952806d02 | -3.9859 | -54.1249 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3c6de34-b807-3a08-b025-61de3a3e6ab8 | -3.98587 | -54.13547 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d80273c-00f3-39a2-86d0-93e55437e05c | -3.98535 | -54.12842 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6f1d82d-fb8b-3b9b-b499-b90936c8fb4e | -3.98479 | -54.13195 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35314ae8-9c65-3329-a189-9a9f2d1ade07 | -3.98256 | -54.12434 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e197e144-77cd-30d0-b916-bd04626b6826 | -3.97587 | -54.12324 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 369556b6-a44b-37c4-a8fc-3d57f1feb51f | -3.92544 | -54.50949 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3107f8ce-d575-3360-af36-051c05abebfc | -3.8833 | -54.14479 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46db3ee9-160a-31cc-b91d-be26ec7da75f | -3.85707 | -54.07963 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 608099d0-5e4a-3b62-b7d9-e2c66d4a9d65 | -3.81506 | -54.47813 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f58d6f32-0fe0-3bcf-a56d-d33e2fd5bcf8 | -3.81452 | -54.48161 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbe33b9f-3bff-35fa-8ce1-75b0ba1863f1 | -3.81173 | -54.47762 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6fcb3ec9-a525-3379-ae3e-3c4f16ee9e86 | -3.72125 | -54.46721 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b0c2a8e-1ae4-3812-b984-2b180e4784e8 | -3.70305 | -54.06643 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed2fcd28-82ce-322f-91d5-c1ee924adb08 | -3.69354 | -54.25906 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f880367f-c65c-3c15-b8e2-abece7ccd7fc | -3.69299 | -54.26255 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e72850fa-4710-3934-86ba-83c58be3c4c6 | -3.69074 | -54.25507 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a4cce1d-a9d6-37e2-b5ee-83580cb2619f | -3.68339 | -54.2145 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d47d8cde-5b9c-3209-8239-76c3af218eec | -3.67424 | -54.31687 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1a95f3a-c009-359c-b181-295652bb0af2 | -3.67036 | -54.31984 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b1e56ae-4b81-3684-933c-b44918421b3f | -3.66948 | -54.21593 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89d9eee0-0b81-3546-8cfe-3161d4256eb8 | -3.66812 | -54.31233 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 279413e7-7fbc-3117-880f-1a977b942108 | -3.66478 | -54.31182 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48c204a1-b983-3914-acde-89f34fb12814 | -3.65701 | -54.31777 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e802a18b-f073-385e-bbcf-f934217a7383 | -3.65607 | -54.36758 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README88.md)
