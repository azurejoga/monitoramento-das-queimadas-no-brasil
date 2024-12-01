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
| b3be8ae3-81eb-35a8-8d0d-b0749f5777d7 | 0.99751 | -50.27153 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84a3437f-2749-39fe-8cf8-0d8be82a478f | 1.14656 | -55.99007 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 40e68750-64e8-3bb9-b328-bcfed4039b7e | -1.32149 | -51.74163 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae08251f-751b-34f6-86df-01b4d9ed0b24 | -0.90038 | -52.63752 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2987751-9d9d-3899-9c3b-cd698e3f978f | 3.63721 | -60.11922 | 2024-12-01 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4ee4fc3-c1ec-3c94-9c68-2302f38c47eb | -1.24409 | -51.79643 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 33513415-92e7-3e4d-b38c-e8e432f9f9d5 | 1.14764 | -55.99694 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 46f54a9d-3456-3eae-b126-038d80f69dc1 | -1.25531 | -51.78564 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d5977b6-866c-3263-a32c-f7dcbd5fd245 | -1.18371 | -52.12705 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5abaad69-de1c-3303-8932-7f2016b14664 | -1.09506 | -53.65014 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 22e4e589-7f11-3ce5-8c96-8718ea2fffa9 | -1.27319 | -47.86904 | 2024-12-01 05:05:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35d980c3-9a06-3c48-9047-16252a0e365b | 0.95637 | -50.22486 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 717e1c53-cc09-3a5f-b9bf-6287e7cd569a | -1.27964 | -51.73021 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93e37d98-096b-308b-b6cb-b1bbe33fd85d | -1.11112 | -53.5929 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42399742-68b2-3e5e-b05e-55c784822285 | 1.1504 | -55.99299 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| aaef091c-772d-3fe8-9a90-2b1abebe72e3 | 1.17604 | -56.00358 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75ebe0ed-34b9-36f6-b718-649b6482df84 | -1.14285 | -51.67557 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09c26ef3-de3a-3795-bf96-133c70bcf0dd | -1.07188 | -53.63842 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5c2d561-a714-390c-9cd3-aaee1e8feb50 | -1.00739 | -51.72182 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 198763e4-8be1-3488-a6f5-a890b7b276d3 | -1.09408 | -53.39851 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a3ff166-84ba-308e-88f8-969a7c8c63c0 | -1.32073 | -51.74646 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d19222ab-8cd3-3ece-ba96-1a62de3b760c | 1.25346 | -50.68031 | 2024-12-01 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7687802-2935-3376-9f04-aeba83bfff52 | -1.26819 | -51.75317 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef6abe85-edaf-38ea-857e-aad7fc94cab4 | -1.09662 | -53.38256 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18ee76a4-319e-387b-988e-8f8abf59fdfd | -1.27641 | -51.82806 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6fbb29b0-0167-3c21-a1b8-65730238ca5a | -0.77432 | -52.39135 | 2024-12-01 05:05:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbe1a740-10e1-3269-889a-e76f081f3c21 | -0.98187 | -51.70807 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16631f49-f165-39c1-ab0b-a5ad8f6a58d5 | -1.18409 | -52.12486 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70573283-cb10-3bf2-aaf5-bba0b6f49e5b | -1.26432 | -51.75257 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 81e7301f-af5f-33aa-af5e-b72f461a081f | -1.05365 | -53.2173 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 481dbb33-a8c8-3cb2-b266-535651df9e0a | -1.18538 | -51.76785 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95d16c6d-f67c-3ac7-98f8-a3e935ee3a80 | -1.3246 | -51.74706 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c3d1a8f-decc-3eab-8901-8806c7ee8c48 | -1.40889 | -46.59755 | 2024-12-01 05:05:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0290061a-b989-3ced-9e05-69552f3588d3 | -1.31657 | -51.67123 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8f88300-c415-3172-83c5-da82b45eb2fd | -1.07536 | -53.639 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1548624-f118-331f-a64e-8fd71cc5e69a | -1.51296 | -45.90664 | 2024-12-01 05:05:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16f9052b-5ac9-3c62-b710-0196cdeaa269 | 1.15094 | -55.99643 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1588d0b3-0dbb-318d-9348-2db24f21f69b | -2.28921 | -45.60985 | 2024-12-01 05:05:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| fdf477fa-394f-31c0-9162-1f4a4feb0070 | -1.70215 | -46.14857 | 2024-12-01 05:05:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2bcdc9a-932a-3ba4-8594-4feb56404969 | 1.14213 | -51.14681 | 2024-12-01 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e385c948-13ac-34de-847f-1b383802dd50 | -1.51812 | -45.91154 | 2024-12-01 05:05:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cba56ad-42de-324f-be0f-31125d0d51d2 | -1.06843 | -51.79699 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ec4612d-a5f0-370d-842f-bb13fa584be0 | -1.06331 | -53.63749 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9223965-5c63-3978-aee7-025c0aa30e93 | -1.00664 | -51.72659 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2accfa56-2657-364f-8259-5e34df55fdaa | -1.31268 | -51.67064 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0143c675-c9a9-3fc1-a08f-48737f22ec32 | -1.19921 | -51.7552 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 60beaa1b-bb5f-3057-b80e-0af804d5f903 | -1.15635 | -51.69924 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cd62af78-1cb2-3796-b21d-828292702f5f | -1.29488 | -51.37553 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4c4caf4-cb53-3d61-9be5-e039c29fcdd3 | -1.31762 | -51.74102 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2c9f356-51f5-3c96-8efe-e542a0914aad | -1.09566 | -53.64631 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7cb307e6-15ec-36e0-ada9-9fb55c83a879 | 1.15628 | -55.98553 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ddd70a67-d703-3a8e-b6c0-e02a2dc88950 | -1.15527 | -51.69731 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03f00393-d186-33e8-8423-5a9c859c3e71 | 0.94093 | -50.73344 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f65f6454-6ae4-3a53-ae84-4ba35945f351 | 1.15574 | -55.98209 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 719b4feb-56ea-3df0-a4be-2d76d341404a | -1.15174 | -51.7035 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89fd0086-0ec5-33a1-869d-addc6f8a3c67 | -1.04185 | -51.73907 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a19e96d-a3c5-3bf3-ae45-591925c2be2a | 1.49386 | -55.94988 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e05b8dd-c237-3c36-a4e7-18f4c438bd0c | -1.03799 | -51.73847 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7f905710-8c51-3872-93ee-2952622fdc81 | -1.15108 | -53.54369 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c569d8f0-69e6-37b7-9dc0-1b3df64cd858 | -1.12754 | -53.09535 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c871a58-72a5-39a7-9732-90ee9c9f7d79 | -0.01043 | -51.16977 | 2024-12-01 05:05:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 31bc7748-ccc2-3ba7-94c9-d786810aa280 | 1.15736 | -55.9924 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 57aea608-a76d-3582-ab70-8361cfe366e1 | -1.08294 | -53.63621 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea340284-337f-3bd9-a2e7-d563f1775bf0 | -1.20071 | -51.74558 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec634365-fc20-3be1-b60d-c5dc31190bcf | -0.96762 | -51.64658 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d133501-2836-3423-952e-2a3f307ac0c8 | 1.5293 | -55.7016 | 2024-12-01 05:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0a05a4e-7bf8-3047-85b4-62c4156d134f | -1.00353 | -51.72122 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da72ebe0-9e84-3648-bade-98df9e62ac2c | -1.36512 | -51.85406 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5404de3-c041-3228-a8f0-def742f90b74 | -1.32385 | -51.75188 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79bf4d61-18d3-3c69-85e1-fa8cebf9a09f | 3.61186 | -60.11973 | 2024-12-01 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 712dc8cf-7ee4-3a07-968a-a35aee6b032b | 0.97872 | -50.25934 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a31b2b39-c5af-3bc1-a126-ab17774e2930 | -1.19931 | -51.77983 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69ddabc3-8ed4-31d7-a950-027a7bce979a | -1.26657 | -51.63354 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd496212-de23-3b82-8e31-5b75d579a11d | -1.03074 | -53.54916 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c8e9ce4-8120-3685-9d17-04a413ee02cb | 1.19001 | -55.94156 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abe7acdc-78ff-3838-b055-8c47d364ca28 | 0.93458 | -50.74505 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67f7bcc5-1f62-3227-ac91-0846f693c583 | 0.97899 | -50.12555 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0901a9f-a999-3431-86b1-ae2385a906f3 | -1.05048 | -51.76 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 99c881d8-264d-3bc4-94c9-6fe59b40e24a | -1.36054 | -51.85823 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5a92b1d-37e2-35c7-bd05-da9d9b5dc6de | -2.11991 | -46.55872 | 2024-12-01 05:05:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6de93e28-a025-35d7-b57d-c7856c0fbdc8 | 1.15371 | -55.99248 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a69072d0-ce8c-3c8d-99b5-9b413ff46958 | -1.18748 | -52.12763 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75111220-520a-35ec-84fd-180087cbfa4e | -1.09623 | -53.36224 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ed247be-cf5b-301f-b508-8179ce594f2f | -1.07736 | -53.22862 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f45cacf4-f759-3382-b749-051ce05e7ba7 | -1.29201 | -51.72716 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aea906c9-5fcd-3aa7-9e46-b3ed8c8942af | 1.15797 | -55.9747 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0846b29-0c1e-3ab5-aa9c-f8d13519ced3 | 0.93857 | -50.74441 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97dc5343-068d-3bc3-8e60-79d450395f18 | -1.1438 | -51.67743 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a65af997-17c0-3549-b1e7-efc20ef15370 | 2.11419 | -55.87789 | 2024-12-01 05:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e7f3d9e3-b92c-31ec-9749-d55682357f31 | -1.28306 | -51.65611 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcc402ed-4f10-39e9-bb2a-c984da80c025 | -1.06963 | -53.23155 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47be75be-e50e-3f19-9c55-633219af4b81 | -1.0572 | -53.21786 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2becb06e-37bf-364e-bcec-739fb318021b | -1.09888 | -53.3911 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fc644db5-7da8-33cc-918f-5687882fdcdc | -2.1002 | -47.62992 | 2024-12-01 05:05:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98b46eed-dd96-3542-90ec-e874321f515d | -1.07356 | -53.3913 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51c9ff46-b3cd-31d8-961c-9c7f66033f5c | -1.09217 | -53.64578 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58373fce-ddd9-3917-86cf-3e455a4cf30a | -1.07308 | -53.63066 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 139871e7-8e03-39d1-ac8e-fbbd0c9d9c13 | -1.32748 | -51.67792 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9551ffaa-1b9c-357e-ae35-2e750ac5b445 | -1.03675 | -51.73611 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d8aeea6-c4f8-33ed-b68d-aaf493fa3451 | -1.09056 | -53.39799 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README73.md)
