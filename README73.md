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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33e13dd0-3fc4-3b14-ad64-0eba74087627 | -3.84229 | -52.36523 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a50ef475-ac0b-3abd-aac2-fffbd2527b66 | -3.71902 | -53.6937 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 835b540f-38e5-3a38-a331-ca16eec9fcc1 | -6.22379 | -53.89698 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79417444-7a98-36ec-8089-297b54fdb1d0 | -6.22299 | -53.89798 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc77e60a-cc2c-3775-99e2-78a0351d9bff | -2.22057 | -53.67394 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45b9f00f-fdbc-3bc4-bf94-a08e1db33eb6 | -2.21996 | -53.67784 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff27e263-79b2-3a7c-b797-534492a9857b | -2.21828 | -53.66555 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 868f4291-9db4-3345-aeb2-790273f0e629 | -2.21767 | -53.66949 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37ad0e26-1fd0-3207-9520-4c3075638717 | -2.21705 | -53.6734 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 768b8488-562c-375a-8b2f-49fc58e333b8 | -2.21477 | -53.66499 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31b58ee5-e3b2-3ea8-bea5-b4baa70637e2 | -2.21415 | -53.66894 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c258246d-85b8-38cd-9721-314e306351f3 | -2.14502 | -53.65018 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffdf80e9-a85e-37be-8df1-a04ef5ccf505 | -1.72265 | -53.75981 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f7158b47-4970-391e-a09d-934f46d09f57 | -1.72206 | -53.76364 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2bc8b2b-29c7-34ed-b316-35f42f6e0302 | -1.71916 | -53.75927 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8567b315-b569-3230-b75e-c40222141359 | -1.71857 | -53.7631 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac467d3c-636e-39d1-82fe-761042f80bd3 | -1.71568 | -53.75874 | 2024-09-28 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbb22896-0c6a-313c-a322-b6c35a55dd29 | -1.57929 | -54.77045 | 2024-09-28 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c003ccf9-d516-3f03-a50a-81b3053a5dc8 | -1.57873 | -54.77402 | 2024-09-28 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b0a0734-ea77-34dc-9642-0459a77369f9 | -1.57592 | -54.76993 | 2024-09-28 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17a8d639-4823-36ad-8216-93449be4c080 | -1.57537 | -54.77349 | 2024-09-28 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad5901c4-3865-3ba5-bc7c-37ad26f22a3b | -1.5004 | -54.37865 | 2024-09-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dc067db-e054-3c5e-bb7b-9ac567cdf83d | -1.497 | -54.37816 | 2024-09-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3da5ce77-45ba-335e-9e1a-fe5b8fd5d9b8 | -1.49019 | -54.37718 | 2024-09-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae294fd8-4914-3caf-bfc1-134e8e0d4dda | -1.48907 | -54.38441 | 2024-09-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39867db0-a663-3244-a71b-7dd492128a59 | -1.43832 | -54.48169 | 2024-09-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2842c591-d65c-3589-b900-fad330f4a1e5 | -1.43553 | -54.4774 | 2024-09-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16643388-42d9-3f2e-b8a0-99577ec081b7 | -1.19062 | -54.20826 | 2024-09-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4987e4d4-d6f9-3af0-9f3f-ebba848dfcb9 | -1.19005 | -54.21193 | 2024-09-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 412a8699-35f9-3e95-b796-be58addddfb9 | -1.09241 | -54.16314 | 2024-09-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2f4d4277-fd17-380d-bc65-4c24021403d7 | -1.04767 | -53.35127 | 2024-09-28 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eefa86ca-8293-36e8-8e74-000736351ad0 | -1.04705 | -53.35523 | 2024-09-28 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c1485e7-cc81-3b7c-9079-629b9b8e4eeb | -1.04644 | -53.35917 | 2024-09-28 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ff9971d-ccdc-3737-aef4-512768cb2e1a | -3.14133 | -53.6853 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 729ecbf5-d121-3cb3-986b-fbc09849def3 | -3.14071 | -53.68934 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b37c5d52-5d9d-33b7-bf8f-263249a4b0f6 | -3.1384 | -53.6807 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1a3808f7-c892-3f9b-8798-f3892ebe45ca | -3.13778 | -53.68474 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9f86ea81-aa8e-3509-b17d-4a97e324aa39 | -3.13716 | -53.68879 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 15c17d81-09ec-3ecb-99e8-4445ebf2b6a3 | -3.13546 | -53.67613 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4f141d04-17bc-365b-8bd6-6a666482dc68 | -3.13485 | -53.68016 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7df70ddd-a389-39ff-bc7a-91d19fa183c4 | -3.13423 | -53.6842 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 47043159-d13e-390d-bfe0-fbbd08a102e2 | -3.13361 | -53.68824 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ac4c43fa-777f-398e-9a1a-eddc9b342f7f | -3.13191 | -53.6756 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aa895a0e-b675-30ee-b6cf-be0b588c9d29 | -3.1313 | -53.67963 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e429336d-f9ed-3397-8808-594d58490211 | -3.12799 | -53.74871 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fb23519b-89f9-316d-a7f4-2d7aee2ecef8 | -3.12738 | -53.75269 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| edcf9223-4066-3b3a-9fb3-6241cf495ccc | -3.12677 | -53.75666 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| eb8d1b09-affe-314f-bfa4-b8782f3d85a2 | -3.12445 | -53.74817 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9625c14c-95d4-3954-8575-330a51fc9a62 | -3.12384 | -53.75215 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cd8139d6-d8aa-3b6e-8b24-ef1e753da25e | -3.12323 | -53.75613 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| aaf03e05-b2f8-382a-b7f3-b5d8ff4465eb | -3.12262 | -53.7601 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2e810b69-2553-3b16-9e1e-618a8ba6a7d5 | -3.12091 | -53.74763 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce9616b9-f4fb-32d8-8461-b5985fd171b7 | -3.1203 | -53.75161 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5f1f4448-4ea3-3538-9700-7956a26fda65 | -3.11969 | -53.75558 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8f3c0dee-48b5-3315-a31f-3a4cffbaefb1 | -3.11909 | -53.75956 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c468210e-f8b0-300d-96fa-18223e3a01c1 | -3.11677 | -53.75107 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9b330106-d1d5-31c7-bc96-962c7a28bb8d | -3.11616 | -53.75505 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b7fe951a-0055-35bf-a7fd-cd383102e9f9 | -3.11323 | -53.75053 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bbdcf1d-b9a2-3c83-9ca3-118d1cd1bee9 | -2.98112 | -54.6352 | 2024-09-28 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d28a6e7b-f379-39fe-9bbc-1afe78c6e1b6 | -2.95293 | -53.71132 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b9da142-ff63-34cb-9dc5-8d2b2a51c8d9 | -2.9494 | -53.71077 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fe07ccc-19cf-3169-a162-136f9fc3a9da | -2.93709 | -53.69667 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a17eb59c-0562-3c9a-aa60-1e964555606d | -2.93355 | -53.69614 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e33d30b-81c9-31b6-a951-2664a9a6b8b6 | -2.93293 | -53.70012 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cccf4c2-8167-3eee-b224-b5c80a38f67c | -2.85432 | -54.86584 | 2024-09-28 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1105987-eaf0-3a53-a017-601af34e316f | -2.77406 | -54.72725 | 2024-09-28 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7af5ae0d-84ea-3c9c-bf90-03f469996156 | -3.65883 | -54.19806 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38bb8f70-722a-3b43-8009-c5e7bdda2364 | -3.64316 | -54.04494 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2f824c3-506f-3e0d-a9f2-3371a2b0d164 | -3.64026 | -54.04042 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3629bdf4-1ef3-3344-b478-a968563989b9 | -3.63965 | -54.04437 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7879e9d-81b6-3281-a391-415ce46cb328 | -3.45447 | -54.09294 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 063fa567-8f79-3265-aac0-825cb741e14b | -3.45387 | -54.09679 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| bf227787-f545-3d46-a917-deb57194fbd0 | -3.45328 | -54.10063 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c03b56c4-705d-3888-9ae3-6e1c594e7c88 | -3.45157 | -54.08858 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d22df214-8d58-3595-a8d6-3b9d7c1aa5e4 | -3.45097 | -54.09243 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e8179141-ccb0-3bb7-a549-0b4b6e1864bb | -3.45037 | -54.09628 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8fd9f2bd-52c0-3e82-a2bc-f52dbad60e54 | -3.44978 | -54.10012 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37844941-8be0-3782-8f02-5c6f89a39294 | -3.44807 | -54.08807 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f50facc0-8fee-3160-90e5-6bb9f505a17e | -3.44747 | -54.09193 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 954b12e1-8f4f-3a38-82bb-3134a9bac778 | -3.44687 | -54.09578 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 87826fea-0703-32d5-8dba-06d763d467bc | -3.44457 | -54.08754 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dcef05d-e45b-39d9-a72c-b9c8f2fc6137 | -3.44398 | -54.09141 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6874ed9a-f8f0-3d3e-9a53-4d3821dad9e3 | -3.35809 | -53.78119 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4fc42e7-b415-37a2-8222-7c564ae98903 | -3.35455 | -53.78066 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 680eb971-6b93-338f-9c23-6108212d208d | -3.35101 | -53.78011 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8ffb1fb-f509-365d-9800-0a18746c9c84 | -3.34686 | -53.78349 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a82fb9ad-ffff-3d80-ae37-3c9ed46c96f6 | -3.54478 | -54.72764 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c87ee821-b9df-3417-b24d-831a43cbb2d1 | -3.54421 | -54.73132 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab8ba69c-a907-3f9f-bec3-c37de58fd85e | -3.31037 | -54.92764 | 2024-09-28 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eadf5c92-693f-358a-9c55-495a7bbd17df | -4.52101 | -54.84691 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab313574-14a5-3b0e-b2d4-74c2f35cd6d8 | -4.51758 | -54.84639 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4145dcfa-7d53-32dd-97de-08063d9eff9f | -4.4975 | -54.95346 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e87f8617-5d13-3f93-b971-1a24df173968 | -4.49692 | -54.95717 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91b49c54-4841-37db-bffd-fc0f7b7f163c | -4.49635 | -54.9609 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5204ba12-b9fb-3566-b406-8e85fd34ce85 | -4.49465 | -54.94927 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 677ea7b1-16b6-3a00-86b6-dd45ba45058d | -4.49409 | -54.95293 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16c0e445-3cba-3b52-8d95-ee536c8eb371 | -4.49352 | -54.95662 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b23bb4f9-cfec-396a-bbae-b48ba7132923 | -4.49294 | -54.96035 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ca1239e-187b-3a0a-b667-ea94ee76f884 | -4.49237 | -54.96406 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6420ed7d-2129-32ff-9d5c-66229c09dce2 | -4.49125 | -54.94872 | 2024-09-28 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README74.md)
