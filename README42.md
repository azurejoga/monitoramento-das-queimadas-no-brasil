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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47cc3dec-8472-3cc1-a099-4f8ee946e38d | -3.08669 | -54.66344 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d08bf331-3387-3063-af0d-9157b9e18afb | -3.03815 | -54.39973 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 384f0d22-ff8c-33f5-88a7-6c0f9516e0e4 | -2.61468 | -54.33046 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fe7b4b2-a299-3777-b1be-7932d38b54c1 | -2.19531 | -53.6654 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30e53c7f-aaae-3986-99ad-08223c001539 | -3.69222 | -50.11947 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fce86f65-9931-3514-a932-cc88e56e2956 | -3.74751 | -54.71998 | 2024-11-18 05:29:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05a1b6dc-fc4d-34a0-8b17-6a379a327ee3 | -2.59083 | -51.71975 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f4cfe49-e378-3055-a3f0-8480581a1bef | -3.18552 | -53.25234 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d9dbf940-ddfc-3316-8850-c5090352f94a | -2.34059 | -54.59103 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8162588f-8b08-312e-bdc2-2d45b41be7c4 | -1.62126 | -55.14646 | 2024-11-18 05:29:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48eedd5f-578b-321b-be5c-83ead373855a | -3.52962 | -50.25169 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35b4ee13-2a00-315a-8e64-1ba82c6d8925 | -12.55472 | -57.81961 | 2024-11-18 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65b12a35-7ed8-3445-95ac-e311d8d642d9 | -2.61468 | -54.32747 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 069f7734-d383-37db-8eed-811690676b0a | -1.79992 | -54.03115 | 2024-11-18 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ffccd2a2-70a4-3697-86ec-13ae1ef22ba8 | -3.40782 | -53.30099 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2c3d310b-58c1-32b9-afb3-d4e3c26eef97 | -2.58017 | -51.7172 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fa647856-a01a-3d7c-81b8-15bb742bb00c | -3.58011 | -50.25129 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 544f5339-b21e-34a4-96c5-c0dff61455d5 | -4.26792 | -50.67345 | 2024-11-18 05:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04fd08f5-976e-3bed-ae71-8d34f219e37c | -3.57398 | -50.25056 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a7211deb-979a-3ed4-adf4-131b7e597fde | -3.32606 | -50.49562 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24657e56-2c27-30a1-9373-1987b29b25c5 | -4.10096 | -51.05822 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b9fad7c-ead0-3ffb-a833-8576707f1ad3 | -3.66408 | -50.44419 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 52f0203e-f200-3cdb-b561-e4ef8db7bb71 | -3.55424 | -54.57405 | 2024-11-18 05:29:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7c25ac3-3499-35a9-b1c9-3f7f065b0b97 | -2.60717 | -54.25788 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69ef3fac-6a85-38c2-95c0-8415105ced84 | -3.69362 | -50.10971 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9ebe501-2531-3c93-b716-c554f0753ff0 | -3.47781 | -49.9742 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fdee225-0eb4-3f9d-9d69-da1349d26577 | -14.28406 | -57.63657 | 2024-11-18 05:29:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cd8ba2ab-74d5-3421-8f27-435e7d9a8d2e | -3.74063 | -52.03759 | 2024-11-18 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28f60388-449c-3eb7-a7cf-82db731ca1fe | -3.18227 | -53.24024 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 77c593d9-74aa-3782-a4c1-edbb635307bb | -12.57356 | -57.77464 | 2024-11-18 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76f2b0d4-e687-3b4f-b017-f3f5ac5dc6c1 | -2.85072 | -54.00889 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9cb2d10e-c4e9-3fd3-b936-a9d9e130dbeb | -3.39726 | -53.26991 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4486e7f-4ed2-3866-83e1-efde57e8b66c | -2.57966 | -51.7207 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5d6656c9-a4b3-31e8-b79d-a2b7e04840bb | -3.25085 | -51.51925 | 2024-11-18 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88e7c8d7-145e-3ee9-b57d-5c86453009ab | -3.06105 | -54.40317 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 44514f42-2906-326e-9e32-8ff580d0e325 | -4.3721 | -50.51643 | 2024-11-18 05:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12b1eb13-dfea-3f91-8ea0-a9e6e31ed2a3 | -3.58326 | -53.71908 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4cfb18b-e16f-31e2-866d-22d1a63a31f1 | -2.42447 | -54.62397 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b79224cc-30bc-3cdc-9b24-06f82859d704 | -3.33202 | -50.4967 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1a2b2f11-59ae-300e-b750-acd05a0b9bf5 | -2.61176 | -54.25859 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ab42b71-859c-3547-9d8d-f31f14a7d4cc | -3.08739 | -54.65893 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6a6cb24-0565-32bb-8c94-c20b39abe77c | -3.7738 | -50.16179 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d67b308-3eef-3182-bd98-32119dec1a7c | -3.24525 | -51.51842 | 2024-11-18 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4f47fe0-f5a5-306e-9d31-68f29eeefc6d | -2.61997 | -54.32652 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 855f6e2e-e966-30f6-8bee-96477d065e09 | -2.65835 | -51.71825 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94e97920-5a18-3e51-b0bf-547e9300b5fd | -2.23371 | -53.73632 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b40076f5-903e-3d29-a26a-edf637a063b9 | -1.69309 | -54.12397 | 2024-11-18 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46e8445f-c46c-3093-a374-0ff1894b1623 | -3.52418 | -50.24633 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f836e47b-9999-3f05-9134-4d064affe6f8 | -3.03845 | -54.40158 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d65f5278-251a-39f6-8fef-ffc6f2431da8 | -3.47628 | -49.97032 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44291de3-95b6-31a3-bc93-b6dccc6318c7 | -2.19451 | -53.67046 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d981262c-e1b4-3e84-9cc4-8cbb32e9932b | -3.14536 | -52.97934 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b19ba06a-7d47-38d4-b3f3-f70e175eb5f7 | -3.06034 | -54.40799 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d65fff17-f7f0-3123-adeb-217d80192635 | -3.56785 | -50.24978 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b15a1705-b750-3430-a6d9-530795ea8fcb | -1.62614 | -55.14315 | 2024-11-18 05:29:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 636e53d9-a385-30a9-99da-d1da7b1f1d6a | -3.32669 | -50.4913 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b6ef19c1-3b3c-3c72-abf1-0e9e43fde79e | -11.65645 | -57.35225 | 2024-11-18 05:29:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 033c866f-0f7d-37cb-b845-31936b02907e | -3.34501 | -53.3134 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d092c190-9951-31ca-ab2c-74137f30c451 | -3.52352 | -50.2508 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85d70e25-6217-3194-84da-e126faa650a1 | -3.34399 | -50.49859 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 259571f1-5d22-39b2-b1ef-c0b8cbea2111 | -3.99335 | -49.39963 | 2024-11-18 05:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 782ee50a-a47d-3920-8032-95f87e560ca6 | -13.01669 | -56.46191 | 2024-11-18 05:29:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db808ec3-01a0-3fa6-a297-e52a9294623e | -3.56654 | -50.25885 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9c900b9e-35c4-3dc2-be86-3e60c7eed5bd | -3.39226 | -53.26927 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87dbb701-2745-3519-bcf3-5b5b2236d54e | -3.5611 | -50.25331 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47eff98b-4a78-3827-86b4-60283b322b17 | -2.65888 | -51.71474 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d1f2456-6f78-3068-bd77-48bed1854ebb | -2.58512 | -51.72156 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e397edb8-385c-3097-9fa8-c5d1063894dc | -3.26268 | -51.61763 | 2024-11-18 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07360b61-f47c-3137-8579-7c84b49bee0b | -3.06972 | -53.27342 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e033016-c061-3c27-9392-f053aecc1c85 | -3.18814 | -53.23511 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 31d3cb0f-abb8-382f-b8b9-a5367bc2a43a | -3.58578 | -53.72202 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df895897-1b15-38ef-a18a-65a7a19d1d2f | -1.62552 | -55.14708 | 2024-11-18 05:29:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aaf3185c-5bfd-3c3e-a9c5-881f9cdabef0 | -3.66471 | -50.43979 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| fbab67bb-7fb0-3072-933e-c5a3ce9c2130 | -12.57094 | -57.73038 | 2024-11-18 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8d9aa41-052e-3239-89c9-0b686102e49f | -4.37815 | -50.51749 | 2024-11-18 05:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c382396-2bb0-3664-b302-3704111862c1 | -1.51227 | -55.81179 | 2024-11-18 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69a5d88c-2c85-3d19-90fd-2287cfa095e1 | -3.06237 | -47.99696 | 2024-11-18 05:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a987c96-320a-3bb6-96d0-86fdf956b09e | -3.06886 | -53.27912 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 14cb5e45-9e14-3a7e-9b34-50b7cef20ad5 | -14.28784 | -57.64146 | 2024-11-18 05:29:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b26cfa58-994c-35d9-955e-266df18248bb | -12.55003 | -57.82282 | 2024-11-18 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4fad7548-28b5-3e67-af88-a1819582795b | -2.5799 | -51.7181 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f71e09b3-623b-34d6-a0df-e2b21abad857 | -14.65134 | -59.62121 | 2024-11-18 05:29:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7497b833-845c-3991-866e-e47394cca844 | -2.42894 | -54.62465 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6070525b-dd14-3343-8b88-ae41fb9ac979 | -3.56625 | -50.257 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e20d63f-b2a1-340e-9583-e69434b17d3b | -3.05719 | -54.39766 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2b7d352-5457-3e9e-969a-6f6b30729e03 | -12.87824 | -56.76493 | 2024-11-18 05:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6260ab6-7666-399c-96bb-49b9d41b3e18 | -3.05963 | -54.41276 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba2e1095-8586-3567-9b44-df412ba29c82 | -3.06563 | -54.40385 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cec598b7-f9cc-352c-afa9-cc23887933c3 | -3.0519 | -54.40176 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9e4fb55a-468c-3cb5-93f6-3a6b008c69a6 | -3.06391 | -53.27839 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0fede155-04df-3eeb-8b45-bfad7f2adbfc | -13.01733 | -56.4571 | 2024-11-18 05:29:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 014a27df-b35d-3b93-be76-f8ec78e3aa70 | -4.10847 | -51.04752 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f5b68a8-0a86-3465-85a6-cabe998b6728 | -2.58536 | -51.71893 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7bd91697-7630-3b04-a8f9-ade68d2e21c2 | -2.57914 | -51.7242 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c2bd088-e275-3282-939e-8b74efc24b1f | -3.18726 | -53.24085 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ffdd18a-930a-35c6-9585-4ec861e199f9 | -3.74589 | -54.72215 | 2024-11-18 05:29:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d6bfd1c-ff3b-3a99-a843-efe13097e504 | -4.27421 | -50.88281 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b21c5585-fd21-3ba7-a831-eb72319804d5 | -3.5622 | -50.24254 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fd420d2-8e83-30f7-8fe3-b3cc95bebf83 | -13.0213 | -56.46258 | 2024-11-18 05:29:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e2236b0-b2a7-3402-9d8a-3cdff86eb065 | -2.63073 | -54.28229 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README43.md)
