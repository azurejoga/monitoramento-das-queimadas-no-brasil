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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bde97d5-b03b-390b-ae21-4a45c691c356 | -12.61606 | -53.12097 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 23f625f3-3ce2-3256-8613-e37f547e526e | -12.61577 | -53.11056 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6efd8978-7599-3c4c-858e-12e71e7bc766 | -12.61547 | -53.12403 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 0c2a1ed6-c997-342c-8580-1b4d2bad0852 | -12.61519 | -53.11366 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 591bfbbe-b55d-3c19-98a6-3bb842d75dbb | -12.61487 | -53.12709 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2863996-7805-37d4-bdf5-1e26883ad244 | -12.61461 | -53.11673 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 9832322c-acbc-3f54-88be-2c6bbd6625a9 | -12.61427 | -53.13013 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 262484ad-fb08-3999-827b-cff67af99a44 | -12.61403 | -53.11981 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 47905d35-9972-3d24-8ce9-e65a35a0f80e | -12.61346 | -53.12289 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 562afb0a-0cfa-3d9f-90e1-4c8a5514aa04 | -12.61342 | -53.15135 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db98db94-5931-3fdb-8bb6-667cb003a737 | -12.61288 | -53.12597 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 95d4923e-d4d4-32dd-a6f0-f77e5241f4f4 | -12.6123 | -53.12905 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0fd924c3-080c-3a57-b8d0-8ac7f7f06b59 | -12.61173 | -53.13207 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3482f47c-3b45-3aa3-8b85-7c7eb889f761 | -12.60952 | -53.11569 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| fd61a490-2caa-3f88-af74-f9823190fca3 | -12.60893 | -53.11879 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3d0585a7-d809-320d-896c-6361404ae11b | -12.60835 | -53.12187 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ae87bad7-c4a2-3a17-b805-b22b9d774ebf | -12.6083 | -53.15036 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d4e78d2-650c-3ce7-bff6-636587d20be6 | -12.60778 | -53.12494 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 71b87d5d-7d67-318d-a4c2-7f71b4846651 | -12.6072 | -53.12801 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 78d9f44a-6a97-3b41-b786-19785c7b1a44 | -12.60662 | -53.13106 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 475daa9d-d862-3d5f-b9be-7aa678a17e51 | -12.60605 | -53.13411 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5f9097d9-ca90-3cae-9e60-a7eda99cf743 | -12.60384 | -53.11774 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7a851ca3-64d9-3bb2-8c1e-e8ad3298fe28 | -12.60325 | -53.12085 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 939bc01c-2f28-3dd6-8f81-6aebc53f2208 | -12.60267 | -53.12392 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| a24f4300-1c66-3494-98da-4eb24f4ef803 | -12.60209 | -53.12699 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f7127ae7-cddd-3b51-a6ce-7d66420aaf52 | -12.60151 | -53.13006 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e50a2648-848c-3a48-9255-3c5dc401a5f3 | -12.60094 | -53.13313 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 58dda2ad-bc16-3879-9a3b-fafd8f5850ba | -12.59814 | -53.11983 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e3a1b8e5-beac-3e63-a865-f482041f8402 | -12.59756 | -53.12292 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5fb8fc12-f8c9-349f-89e9-f83b19bd955d | -12.59698 | -53.12601 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f9c6242d-57f5-32da-b4fc-3bf78ca6dec6 | -12.5964 | -53.12908 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2506fbcf-f5fb-3183-b043-76489a8d97b0 | -12.59582 | -53.13214 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 729bdefd-ed42-365a-b1a2-e8902b906b61 | -12.59245 | -53.12194 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 01c78c8d-d0d1-3a9e-a2a2-335c083627d2 | -12.59128 | -53.12809 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db2c07f5-5426-3d47-9668-43e2cd479cf8 | -12.58617 | -53.1271 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c97ce06c-de90-30f0-ad33-4c8e5910de0f | -12.57596 | -53.12505 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71601452-bb65-3a69-b376-55503ba2b9ff | -12.57538 | -53.12812 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 447837d6-3d11-3129-915b-0d04106f439d | -12.50626 | -53.21078 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cca34a84-c86e-3a90-8393-0e7b7fd9dd95 | -12.5055 | -53.21059 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 128a62d0-4197-302e-aa7a-2814283a00d1 | -12.50111 | -53.20975 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0484e52-329c-3529-9694-db7ed69d18b2 | -12.50036 | -53.20955 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b91fc598-3ce6-3c59-abc0-a2d05e434507 | -12.49977 | -53.21268 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 75d72d7c-dbb2-3db4-8327-eab1214cf2b3 | -12.49597 | -53.20873 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6df73d9d-b93c-3ef6-bd9a-49f14fc23861 | -12.49522 | -53.2085 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 928644ae-a654-39db-a293-67566f17ecbb | -12.49158 | -53.14284 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89f7cdf5-7f6e-3133-be7f-6174ca8e8daf | -12.49101 | -53.14584 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8376244-136d-3313-80ac-71da3eb62c04 | -12.48646 | -53.14182 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3402435a-8d20-33a8-b516-a7646488b77d | -12.48247 | -53.13478 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60e77d26-eb58-3118-a6dc-2a17fa9a14ca | -12.4818 | -53.16647 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c593a32c-0776-37d6-bc0e-a93f4a7ad4df | -12.48003 | -53.17587 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5dcaede-a5a8-3962-93e0-c9dc62a6fb80 | -12.47668 | -53.16542 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2e41795-7a6f-3593-afb2-c4bcc0fe74cb | -12.47609 | -53.16855 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc0580a0-9c72-3e91-8ea4-b0cbf65fca95 | -12.47549 | -53.17168 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36ffb522-a369-3d17-807c-5a6952c8c601 | -12.47037 | -53.17064 | 2024-10-05 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb518e06-dc8e-3d19-bfd0-5eecd79e3086 | -12.4636 | -54.18165 | 2024-10-05 04:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77599c35-5c3e-3b11-81b3-bbc2809a5eef | -12.37878 | -47.67868 | 2024-10-05 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50480ab4-5ad7-3135-b3b8-79af1c759e62 | -12.37524 | -50.97772 | 2024-10-05 04:14:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb61d943-ab8c-38ba-8aee-2a31c122fcd2 | -12.37318 | -50.97477 | 2024-10-05 04:14:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 72d71b05-a18f-39a6-af8a-89aab5b6c064 | -12.37238 | -50.97924 | 2024-10-05 04:14:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2d1593a3-9e74-37c7-8ed5-a611ae7ffaf9 | -12.37159 | -50.98371 | 2024-10-05 04:14:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dc4c0fdf-b1a1-3b57-ab3c-7752b282d180 | -12.37079 | -50.97688 | 2024-10-05 04:14:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3d308730-6235-3c74-9831-3e972ba04eac | -12.36996 | -50.98134 | 2024-10-05 04:14:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dec0d0e1-eb53-3657-9662-7ea9213f09ba | -12.36714 | -50.98286 | 2024-10-05 04:14:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b272ad3a-3b36-352b-8e23-3d0a9843eacc | -12.35022 | -46.46265 | 2024-10-05 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 59c4b71a-ae4d-3512-afec-c5fffddcd507 | -12.21919 | -50.52312 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8a5c395-ee3e-3b1e-a6a5-4db26213fc62 | -12.21486 | -50.5223 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c05f0752-46fd-35d1-82cb-3dec80c5db2c | -12.14339 | -50.44838 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a90be841-0ce3-3df6-a66e-26d0fa550e83 | -12.04467 | -47.37907 | 2024-10-05 04:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ca3daf0e-5a63-3a48-b4ad-587fc5669a46 | -11.93228 | -50.11475 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e427313-1bc5-344f-a970-6509344776cb | -11.93014 | -50.12673 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4f5102e-f427-3709-8f17-f4a35d9f9581 | -11.92942 | -50.13073 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f17d556-b702-37c9-a240-68626a815c3f | -11.92871 | -50.13473 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1227bc88-0468-3e45-87e2-e8e4f984f7ba | -11.92804 | -50.11396 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cfcf5954-02db-3062-8f2d-b0ec12e44dcd | -11.92799 | -50.13874 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64bea9c7-f53c-39f9-8a39-7ca14eedccbf | -11.91608 | -56.93878 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 28401461-78db-30e7-8e98-c5eb3ea37cb5 | -11.91491 | -56.94444 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61eaeffe-f8f7-3ba8-ba00-d727914ce1b6 | -11.90839 | -56.94297 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27b90ded-5003-3d4f-865c-bd98f2460e61 | -11.90724 | -56.94852 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 959d09e7-b19f-3b1f-b8c7-1ed3fbf8b0fc | -11.90185 | -56.94156 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f080bdb8-361e-322a-9bf0-e1614d9753b1 | -11.89903 | -50.12924 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 913adf39-7de7-3cc6-a620-c9257d0e2352 | -11.89646 | -56.9346 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5fbf88e6-296a-3c6d-9cb1-63ffa57761e5 | -11.89532 | -56.94011 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9511b06c-563c-3977-a612-263c57e27ee5 | -11.89418 | -56.94563 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3201e70c-bf2e-326a-b321-ef1698fef2e9 | -11.89303 | -56.95119 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 532c2c7b-7d44-351e-bd8d-1e6fcbe4f73a | -11.89079 | -56.93832 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 346d40a2-7b1a-3e0d-9f8a-55008acfc0b3 | -11.88968 | -56.94388 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ea55494-f8c4-3a87-a4dd-5abfea76e786 | -11.88877 | -56.93879 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c4058d0-7701-38a2-a991-10f4e371831e | -11.88268 | -50.14693 | 2024-10-05 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3681cd9-212b-3449-8f8f-9f334c3de913 | -11.88204 | -56.94793 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0fad656-5bf6-3bd2-8345-5dc5f01db5c2 | -11.88089 | -56.95366 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6ce2fb43-c710-3786-8e52-bc1585fce05b | -11.87994 | -56.94836 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ea4de51-f97f-3068-85b6-afb23deca476 | -11.87874 | -56.95413 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37370841-7a47-33b2-8578-b67392e19b84 | -11.81791 | -56.60211 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| daa57ca7-a8f1-35ec-9c58-df3e9acb4d3e | -11.81741 | -56.60237 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b6166c9-58cd-3405-b71a-407c08fc4fa4 | -11.81681 | -56.60758 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e65853cc-f9b9-335b-bc4c-fb0dab9f7f56 | -11.81627 | -56.60784 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e2126db-68a5-37f8-a6d8-0582dbddfdf7 | -11.81038 | -56.60624 | 2024-10-05 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a44797b1-e205-30a2-aeea-38df5363ef81 | -11.72705 | -46.90991 | 2024-10-05 04:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb3f6f8c-7285-32aa-8dcd-14adb41c03b6 | -11.72071 | -47.10153 | 2024-10-05 04:14:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24ae14e0-2b8f-398c-acdd-bff9f122c74c | -11.66852 | -47.67839 | 2024-10-05 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |


[Clique aqui para ver as próximas entradas](README73.md)
