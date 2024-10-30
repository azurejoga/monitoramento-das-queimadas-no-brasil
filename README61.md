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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39da7342-2c34-3939-ae73-6f73c165788d | -3.86801 | -49.99153 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e218d8b-72e1-39de-9983-f5246e821cec | -3.86468 | -49.99102 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e31a4e4-8b87-3388-a443-461d2cfb488b | -3.81132 | -49.92184 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52355f49-a21d-3c1d-b251-4035a1d1543c | -3.79729 | -49.85931 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58f8c8ea-8489-37c7-9fc4-07504f0040bb | -3.79342 | -49.86227 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4ec958d-9f4b-36cc-904a-5806ceebf09a | -3.77881 | -49.97705 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 708b9af8-2ff0-3b99-8466-ded3590bd7d5 | -3.77827 | -49.98051 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4cc2bdd-5c13-3efe-b133-e88efd3fe9f4 | -3.77607 | -50.16772 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd2a6f38-52fa-391a-8b0a-4981f6b368cc | -3.77549 | -49.97653 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cad28859-fca0-3ea5-b0f8-4d7ba6f0487f | -3.76668 | -49.98933 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5c95bde6-a328-37df-a14a-c5f0250b9365 | -3.7639 | -49.98536 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbfa10b4-bdc7-3eb2-a6af-9b2e88543fff | -3.76083 | -50.39224 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78231b9f-8484-31a4-a5f9-ce2dd30d21e1 | -3.74146 | -50.06327 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 701d42ac-a15b-33d3-af9e-b267960cf85c | -3.73814 | -50.06274 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0091746e-64c9-3538-879d-2f3854b91707 | -3.72826 | -49.80612 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68d4c366-613a-3b3f-9f12-fdf175de5bcd | -3.67212 | -50.11986 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc3dd525-a3d1-32d1-8134-6005fb549a38 | -3.66935 | -50.11589 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9dd17d4-c67a-3cf2-8ab4-f6ac84d29f4f | -3.6688 | -50.11934 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a8e5446-4dd2-36b5-b768-781ce276f9f2 | -3.66826 | -50.12279 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58156271-4f33-383d-a15c-d018a592eea7 | -3.66603 | -50.11537 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2a74ceb-84d9-3ba7-bc45-3ec6995fe8e4 | -3.66548 | -50.11882 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 891178f2-ee10-3f8c-a617-6bf0f9b3e057 | -3.65619 | -50.15628 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a066bef4-5386-30a0-abfd-1ecf99ebc4de | -3.65565 | -50.15973 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddbd57df-56e6-31bc-ba65-c3225ca78b7e | -3.65511 | -50.16318 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37e3987b-7451-348f-9dcd-fe8a96fbf6f9 | -3.65456 | -50.16663 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2c4036e-9c21-37c1-9dae-a027960848a1 | -3.65287 | -50.15575 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 187fe799-9369-3232-b1c1-32006ae14de8 | -3.65179 | -50.16266 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dbf4542-199b-37b4-ab71-cf6c5254ae30 | -3.65134 | -50.44168 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4954f623-4b13-3969-83d8-9b00a9adf99b | -3.65124 | -50.16611 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 186d6d7e-ab85-3fa3-9296-19025083161c | -3.64802 | -50.44116 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e766709e-e36d-3d61-b418-1b7bc6c291b9 | -3.63024 | -50.16991 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a1d8706-7c62-3973-a5d6-fa174763df66 | -3.62747 | -50.16594 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 458b8b08-2a8a-389b-b952-3b4a98ee84a8 | -3.62692 | -50.16939 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2039d33a-f22c-3057-a2bd-4133dd654f4f | -3.62198 | -50.17923 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dad699ff-a000-3201-af91-47e1192595bc | -3.57957 | -50.42707 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59e1f835-08e4-3a4b-9588-89bb58ec6224 | -3.57625 | -50.42656 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5a6dc9f-7282-38fe-950b-99c26541062b | -4.12861 | -50.67927 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb893356-368c-3d46-ae0c-f6e17bef66e5 | -4.08175 | -50.52335 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d40772bb-462a-3ea8-9012-70d79b307df1 | -4.0812 | -50.5268 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e9e60c4-7be7-35b0-a056-68263095bcaf | -4.07843 | -50.52283 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47669fc4-7092-30ce-8313-012b62e6a6ec | -4.07788 | -50.52628 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b67384d9-875c-3309-8a4c-27e162dc822f | -4.07734 | -50.52973 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68d46e73-0d4f-3ccb-8142-a9229d51898d | -4.07511 | -50.52231 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 521f6403-46e6-36b2-a1f4-e85d71fbadbd | -4.04329 | -50.55641 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44bbf031-6930-3db4-a0f6-ab5b69676471 | -4.04275 | -50.55986 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1cd785b-4dde-3e16-a736-3deada159397 | -4.04052 | -50.55244 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb9219a8-6ebc-3d52-9940-2ab7e79441c1 | -4.03997 | -50.55589 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 581ccee6-de7d-3886-bbb8-e3fd5c6abed9 | -4.13913 | -49.42248 | 2024-10-30 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2f879551-31bb-3bfe-b908-dc9cc07ada60 | -4.11676 | -49.26718 | 2024-10-30 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c194ee91-7a6a-32ad-b473-c68121367ffd | -4.09477 | -49.99106 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0791083-5cca-317d-9c2a-3f6097627a8e | -4.07767 | -50.01324 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4fcd8a0-9578-3c4d-97ee-de8e3fb82161 | -4.07712 | -50.0167 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecc8a51a-ff45-307e-8d28-79af8670b4de | -4.07488 | -50.00926 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| de6fc9db-46fc-356e-8465-3641ce0b025e | -4.07434 | -50.01273 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| a4dfea73-2e81-3c90-adb0-113c9f2e6c9b | -4.0738 | -50.01619 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c04eef3f-0d6e-35bf-940a-cd9dcf2b98f7 | -4.07326 | -50.01965 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 24a83bc3-aafc-3b12-807c-8089112d79c5 | -4.07156 | -50.00874 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| ec27f172-5c5e-3831-97d6-b2f4608d00a8 | -4.07102 | -50.01221 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 68186226-b9dc-339a-81c1-23de0ea50d0d | -4.07048 | -50.01567 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d3a045b4-7813-3647-9937-2e168ad1d58a | -4.07 | -50.04042 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 90185c9d-487b-3f4a-a771-86930f0777d7 | -4.06993 | -50.01913 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ed0778e8-9fc7-38f9-84f5-02d291ae9ffb | -4.06769 | -50.01169 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66034bf7-4767-3c96-8a5a-1366f04284c7 | -4.06715 | -50.01515 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 003fc38a-17e1-3d5e-907d-8dc37befbe93 | -4.06668 | -50.0399 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a82ea368-4c56-3fac-92c7-67d5c8281725 | -4.06661 | -50.01862 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c3088ce-afce-359c-a2f9-9606bd82b24e | -4.06383 | -50.01463 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33aa354a-58f4-3c40-9dd0-6a52c8ee38fe | -4.06328 | -50.0181 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ebc229d-e9d0-316b-b09b-bdebe5588c3b | -4.06274 | -50.02156 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5224911c-d392-3b20-bc38-0bfb1b7348a4 | -3.99059 | -49.98553 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 458ed3ff-fa91-3b85-89a8-8efb3ead9752 | -3.93751 | -49.8959 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7504e326-0290-373c-b41f-9904ef488fc0 | -3.93712 | -49.74642 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 819d7876-e3c2-3d0b-bb3c-a8930c4b08ea | -3.93658 | -49.7499 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 767c38c1-0947-31c4-a2b7-7720ea265b86 | -3.93418 | -49.89538 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d6fedba-da52-35c7-a5d4-8f4bc37158a3 | -3.93379 | -49.7459 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 747a370b-21f6-33fc-9aa0-7390c39bca40 | -3.93325 | -49.74938 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f8236b2-47c7-3b65-8d9c-293357563217 | -3.93086 | -49.89486 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67845b8a-1847-3b1e-9580-c405ef4dcfc8 | -3.92753 | -49.89434 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 558ec1c1-63d8-3b01-9607-0d2abb92de0b | -3.9247 | -49.86903 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f97bfff7-3588-3c81-8471-73adc9f650d2 | -3.92415 | -49.87251 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bae56726-d938-3fef-8a5e-f0b4f318f08e | -3.92137 | -49.86852 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01096cb9-54ac-3df5-8167-071198dafc1c | -3.87548 | -49.90046 | 2024-10-30 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82c8b09b-c158-3ff0-b073-d91926dfe3ad | -5.00599 | -49.85518 | 2024-10-30 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8f4f9b5-956d-3d4f-9436-dea5cf8fd1b2 | -4.97461 | -49.77141 | 2024-10-30 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02c58fa5-a7f3-3c18-a01b-16eebfe6e440 | -4.95918 | -49.65022 | 2024-10-30 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dd5ef51-84e1-3cda-bf8c-51b3faa5cd1a | -4.85781 | -50.77676 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 419ff5f6-f83e-3d28-921d-5c021482f5ac | -4.84949 | -50.76484 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fa0cdbd-6f0e-3469-ad17-93529f4423fb | -4.84617 | -50.76431 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5dc9b22-45a7-3c4f-9286-ad69de75dd6b | -4.72186 | -50.37262 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f069b987-4c12-38aa-899f-c028468b3286 | -4.71149 | -50.73614 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f84f423d-1304-3840-a757-63d952e6889c | -4.70531 | -49.50236 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9f4b3f0-5f52-3371-963c-a6f0faaca269 | -4.63138 | -50.45055 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d874e7eb-234d-3bd0-965f-0d67adf595c7 | -4.60594 | -50.6554 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 526a2967-b4c1-3781-a1cc-fc4b77f27d51 | -4.60404 | -50.55953 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 419c0ff6-2490-3527-8a58-294dc7a12637 | -4.60349 | -50.56298 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caf2b708-2e8d-3aea-bbc5-1e53cd7f5903 | -4.56636 | -50.412 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b030e087-95b3-3343-a454-77e013600d3e | -4.56582 | -50.41545 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58587c96-f6a4-36d2-8db9-a02826e15a8c | -4.56304 | -50.41148 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5121c52-21ec-39d9-933b-af19fdaace55 | -4.5625 | -50.41494 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10594801-337c-38b4-92bf-d0a1009af0f8 | -4.55779 | -50.50975 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 020c7b64-11d6-3eeb-a598-d6419d83e28b | -4.55447 | -50.50923 | 2024-10-30 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README62.md)
