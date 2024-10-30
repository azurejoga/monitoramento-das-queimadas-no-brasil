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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10b963a2-7f81-3ed7-87d2-5de97cb1fb8e | -3.10912 | -51.102 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b670b72-dbbf-3cd5-a13a-6525f0f71872 | -3.10855 | -51.10579 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dcb959cb-cd7d-3298-ab50-d011e8da4098 | -3.10553 | -51.09754 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87aa0fd1-85f6-3c6a-9ab6-1ae98f9b4e26 | -3.10496 | -51.10133 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 517ef6be-7440-344f-8466-4246101027b7 | -3.10439 | -51.1051 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bd22db47-3b7b-36e7-8673-2f8d77eb4c9a | -3.58912 | -51.47715 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ab5e113-ac5d-3795-9df0-665fb827545e | -3.58751 | -51.4319 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e534dd2e-a41c-3552-9e79-5dcd5b5da28f | -3.44966 | -52.00578 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8242050a-f33b-323d-bd50-96af862d09ac | -3.37625 | -51.07727 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97d1fd1b-d8dd-3835-b0fc-44bac0de051e | -3.2889 | -50.94287 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 298b8e29-0bba-3085-866c-97d1e0315574 | -3.2643 | -51.01883 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a01d53ea-c866-387b-8023-dad494c07ff3 | -3.26009 | -51.01822 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 454bdf3a-e32c-3ac9-bd3c-83bb6bba5e5d | -3.20367 | -51.02167 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d06d46a3-a2e3-39eb-83fa-9307b0e4ba1e | -3.20184 | -51.37159 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 121acb51-6c63-3e00-9c5e-07e507bffbe5 | -3.20127 | -51.37527 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a07cf87-030d-35b7-ad46-74ae2244e41a | -3.18719 | -51.2176 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dff83d96-1ad9-3559-bf9b-76793764f65d | -3.18305 | -51.21697 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdf725b8-2910-3073-9efc-0b309a7fd8a3 | -3.18241 | -51.36129 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d725c1d9-60cb-3a98-8f0a-4db982a7910e | -3.39593 | -50.80695 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5277cb71-8ecd-38c0-88c0-6fe426713113 | -3.39104 | -50.8103 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 949b8cb0-e334-346f-aa74-be422e6a8acd | -3.24955 | -50.6386 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1504d751-52be-39ad-9d87-d834a67010a7 | -3.2489 | -50.64273 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a6f7c6a-c2c8-3ccc-b4be-e42860a67265 | -3.2469 | -50.64171 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b180dff8-4aac-372c-af35-f515c1d10cdf | -3.17678 | -50.59421 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| eeae6fa3-eb54-3907-81c6-53421ac1bfb6 | -3.17185 | -50.59767 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3950fb7c-148a-3bcc-864d-95d2aed67a81 | -3.16752 | -50.59701 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87727b01-bbf1-3708-8468-3858b578fa69 | -3.16381 | -50.59225 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1c9f6727-6c0c-3ee5-9361-adacc3d17964 | -3.1632 | -50.59635 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b5c5283-b5a9-31b9-805e-0079c001c028 | -3.15949 | -50.5916 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c236d234-29fd-376c-9f5c-9f401248a494 | -3.15892 | -50.62511 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| beaf41d6-460a-3c3f-8e7b-d2461463d485 | -3.15831 | -50.62919 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a3fbf9cf-a3d9-3133-a33a-ad55528613f8 | -3.15771 | -50.63324 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 391a1bc9-27a2-3149-828b-902dd6580104 | -3.15023 | -50.59441 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44beab83-86a5-3ba6-a510-a086b06768d8 | -2.48126 | -50.48537 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0b587ef-9886-397b-81e0-de07bc211bc5 | -3.07491 | -51.3561 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d114f36e-f78a-3a0e-b462-087155afe8b7 | -3.03612 | -51.44701 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32c667b1-72ea-3b78-bb54-c80544738f71 | -3.03207 | -51.44624 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99536265-7499-32cc-93a1-90f2568f63fc | -3.02925 | -51.79091 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 219a01a1-3d3b-3973-9973-b5ea4318189c | -3.02579 | -51.7869 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bf99a3e-c42b-38e1-af05-68d7803f535d | -3.02527 | -51.79029 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f91947c2-398c-3621-814a-4365ca69873b | -3.02181 | -51.78628 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9399d7c-e714-326d-a002-5092bdb95d72 | -2.93215 | -51.58454 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abd87a3f-66f3-3b24-8bc6-13b618a05907 | -2.92812 | -51.58393 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc2e2236-412e-35bc-9312-8ed90ab56b69 | -2.89803 | -51.48142 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7861af7f-139e-31ee-9c71-69d6dda95bef | -2.8975 | -51.485 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4a1cf7b-4f07-374a-b261-29642b1a9aa8 | -2.89705 | -51.4847 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fd9884ee-bc0a-3544-a667-e52e6628987c | -2.88433 | -51.65624 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2010f5a6-ae34-309e-bba1-a5f2e0cf642f | -2.88381 | -51.65973 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9de75c90-ecb1-36c3-a8ac-f5c30043a2b7 | -2.88033 | -51.65559 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22c1a364-6053-36f1-bf5b-51efb0d4c3ba | -2.87787 | -51.31176 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6602defa-5564-3b9b-9455-97a02b636ea5 | -2.87377 | -51.31114 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ad10f10-7d56-3e64-bd11-aefdadd29be2 | -2.87322 | -51.31479 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19315f77-2321-32ad-836d-301f85cae46c | -2.84319 | -51.80355 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eb55642-9c79-3aba-82d2-785f37bacac5 | -2.84166 | -51.80559 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9b4275b-67dc-3332-899e-8b71982b6b03 | -2.84091 | -51.81069 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bec7664-88b3-367f-9aed-33c3eee98ced | -2.83843 | -51.80805 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eef0b46d-6f75-3dd4-af65-fe2a0c2ae1a3 | -2.83447 | -51.80744 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfd8736b-3b3a-37b1-922e-0d799d0d72b9 | -2.81182 | -51.95309 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5265f6ff-8bae-3b7f-8e07-b72a22d04756 | -2.80396 | -51.95189 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c11596e3-3cae-3646-ad8b-153165d06dd2 | -2.80319 | -51.95688 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7d7c908-587d-32b0-9360-1123a50d9bbe | -2.80197 | -51.80767 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48245993-4a7c-3a2b-b399-34d02530b716 | -2.80003 | -51.9513 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a768b109-1705-320e-a766-e61bc57b6592 | -2.78355 | -51.95393 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 936476d2-fbd8-387e-b64d-d1f75d6970f4 | -2.78278 | -51.9589 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0d19b5a-d033-376b-ae56-d08c7c92f85b | -2.73897 | -51.72558 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddbdc1b2-b2ec-3e3a-9f4b-a0741e0d2597 | -2.73843 | -51.72902 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 111c6248-646b-344c-a10b-0b23d1d48335 | -2.73499 | -51.72498 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7edbfb5b-ae15-3a82-965d-1aac9de55dc6 | -2.73445 | -51.72842 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98cfde13-1db9-3d22-a133-81e96c0cb19b | -2.72571 | -51.70589 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 236979c0-ce67-33b3-a134-3f5ac57e6b11 | -2.65028 | -51.75514 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0e4871b-9407-3093-9132-4f8e94d56828 | -2.64961 | -51.75128 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90763afe-6b88-3df4-8444-af2f79f9a375 | -2.64884 | -51.75638 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8b3444c-8c57-3e26-a87a-772f671823fe | -2.64711 | -51.74944 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9e6ce3c-dfda-372f-9f51-839391244f40 | -2.64631 | -51.75455 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c223db8-9bd0-399f-82a8-ada93f06dc5e | -2.64628 | -51.7464 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e75b607-4397-3b9f-88a4-2612b210e0e1 | -2.64564 | -51.75067 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cb78b68-b95a-3e80-86f3-0e1b94a2125a | -2.64515 | -51.73607 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a3329ab-8778-3954-8c81-5956a44a06fd | -2.64487 | -51.75578 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80393242-c8fb-379d-b8e9-aa55162333a1 | -2.64395 | -51.74373 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdf3dc17-06b6-3a77-9afc-9593656e80b1 | -2.64384 | -51.73555 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc96c826-a18d-3510-b9a3-55bc9c16356c | -2.64314 | -51.74885 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfeb9491-fb6a-3b10-a39d-3ef39669dfa5 | -2.64234 | -51.75396 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbda94aa-d3b7-3347-b125-551a2f8594bf | -2.6423 | -51.74581 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 463c8e96-29c4-34a3-961c-72cf2186a5e9 | -2.64166 | -51.75008 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be5a0023-48e6-3561-8d73-b6f93118fdb6 | -2.64118 | -51.73546 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80bf1e61-2647-3ece-aabe-b3eebad85f84 | -2.63998 | -51.74314 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a358f86a-9453-3f9a-8323-93f65dcd010f | -2.63917 | -51.74826 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b015301a-1565-338d-9dfb-502433918453 | -2.63774 | -51.73145 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c65c8e47-dc7c-3de7-81cc-027a29346ca4 | -2.6372 | -51.73486 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f30fd0c3-66af-3cf4-a3c6-1bcb516b6a19 | -2.58409 | -51.92042 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98f7f3af-5e29-3d31-b259-a40114082903 | -2.47947 | -50.46836 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 363eb7d5-40c1-38f3-bde9-db8ce567db12 | -2.20264 | -50.97055 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74a40c9c-dba4-372c-9421-19a89ddd4a79 | -3.90752 | -52.26447 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85243207-8a3a-35b1-adc2-e2d3443f7085 | -3.89219 | -51.91853 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b8bde1d4-023a-33da-b602-6fe663070634 | -3.89167 | -51.92194 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 84d2146e-b095-386f-8cba-1185446f798e | -3.88819 | -51.91793 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 37083b73-4dd4-33a0-8354-4e289be032d5 | -3.88767 | -51.92132 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cac98792-3776-33dc-ae83-e0c27258bcc0 | -3.88091 | -51.02971 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51aa5296-890a-3558-ab11-5d3b7889356f | -3.85967 | -51.69733 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7af7cb7-fb91-3bc1-a659-f33c231410dc | -3.85914 | -51.70093 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README89.md)
