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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbbd04bd-6a15-3dd0-b33a-44ce2d6fca6f | -21.58953 | -47.85196 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| bc2436ca-c0dd-3236-8080-56a966fbc788 | -21.58931 | -47.83223 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85d8ca17-98a0-3d54-876d-812bb12d57d5 | -21.5889 | -47.85577 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 5b517907-57d9-339f-8e30-0571042c9a32 | -21.58868 | -47.83606 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7a1b739-e09e-3cf2-b4b0-521f0fda4b15 | -21.58827 | -47.85959 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 116.7 |
| daec0aa0-c33e-3616-b608-b2ba12a5024a | -21.58805 | -47.83989 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e674bb14-d02b-3c7d-91c2-749f8b75b2c8 | -21.58765 | -47.8634 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6af259bf-0bad-3fc7-9799-f053a81e16df | -21.58743 | -47.8437 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1dd37785-56a0-3acd-a762-977f6adb41cc | -21.58702 | -47.86721 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36ab3869-be9c-39f7-8af4-f9a342a6b1ff | -21.5868 | -47.84751 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 495faf04-c9e7-3663-a103-f81bd08677f5 | -21.58618 | -47.85132 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a89fb3b0-1c5e-332c-aef4-518641df5b03 | -21.58596 | -47.83157 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca2ee762-0bab-38ff-8162-356104cb18d3 | -21.58555 | -47.85514 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 57.3 |
| a2bbef04-84c0-3932-9a73-f8153002926f | -21.58533 | -47.83541 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b70d305-7d16-330b-949c-4b6b6463da51 | -21.58492 | -47.85895 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e411c4cf-aff0-35f7-a909-2cc130fdbf69 | -21.5847 | -47.83924 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| feed7102-26de-3e71-81ee-8c82025a3df8 | -21.5843 | -47.86277 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5af1c0e7-1a44-3b20-a5ad-86ab80303e57 | -21.58408 | -47.84305 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7fb89ad-7c39-3609-aace-47013c419d82 | -21.58367 | -47.86658 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 690139b5-a023-3ad1-b047-5e197ea49a64 | -21.58345 | -47.84686 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6b046a88-33a2-35c3-8b08-89fdd019acc5 | -21.58304 | -47.87039 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8575f4cf-4938-3f8d-b3a9-f69b93fb74a1 | -21.58282 | -47.85067 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 48d4d898-e826-325a-9f8c-0b1864c37341 | -21.58261 | -47.83092 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58168f99-cb83-30bf-8507-f2853a7ac33c | -21.58241 | -47.8742 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c2792d8-6bd7-31aa-9a3c-7dd32eafd208 | -21.5822 | -47.8545 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 867d91ae-68e5-3aae-9c7b-7848c70a0b5f | -21.58198 | -47.83477 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e77ad2a7-0e1d-392c-9490-fd9d1388b79e | -21.58157 | -47.85831 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 57.3 |
| ea309ae2-d8f1-3c30-a917-ff7071ab4adc | -21.58135 | -47.8386 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58119909-5fb5-3b1c-ae2f-6bf40a7cb74b | -21.58094 | -47.86213 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c9eb2fc5-8858-3c0c-9b94-651bb08664a0 | -21.58073 | -47.8424 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d370d558-571d-3f2f-9a90-0349a45cb4eb | -21.58031 | -47.86594 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c39b0a18-3da6-3128-97a4-d1970c64c59b | -21.57969 | -47.86975 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 478a4191-bf3b-35c9-b7e6-965de1602071 | -21.57947 | -47.85003 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73b1feb1-d30a-3f5b-9d87-8cab6c1bd3e9 | -21.57926 | -47.83028 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68a60235-8378-323a-86dc-ca38674ca629 | -21.57906 | -47.87357 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 685249a6-fa79-32fd-811f-d95abaf9d9a2 | -21.57885 | -47.85384 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e0aa549-6208-3047-a1aa-d23a8b179ca7 | -21.57863 | -47.83412 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b598c84-83ca-32b2-94b8-f6e91deb3ed4 | -21.57822 | -47.85766 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be8b397a-f6b8-355a-a831-16432bdacaf3 | -21.578 | -47.83795 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac04e09f-0106-3e68-b4f8-3144a1197b95 | -21.57633 | -47.86911 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d509a1e1-aaba-3da5-81dc-07bf2ad39718 | -21.57612 | -47.84937 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0dec334-2b12-32f3-a659-ee176c6c61a9 | -21.57591 | -47.82964 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e60a86d5-de98-31ed-b882-ac015f5b8456 | -21.57549 | -47.85318 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a7ada5c-7478-3d26-926b-1607eb731aba | -21.57528 | -47.83348 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50da8280-ca3c-384f-b242-d3065fc3abc8 | -21.57487 | -47.857 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afed22cf-0492-3acc-a59a-a7d33a359685 | -21.57465 | -47.83731 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b162dee-b4ac-31e5-8368-f6c45113df2f | -21.57424 | -47.86081 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f346ff1-076f-3f38-9fe4-fa652b9dfa46 | -21.57277 | -47.8487 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96ebbf19-7946-35d9-9cfa-c80a49b95097 | -21.57256 | -47.829 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 375bb0d8-8bff-3dc0-abfe-daa18a079671 | -21.57193 | -47.83284 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 324af03b-9b22-38f5-9c6e-40f956261d39 | -21.5713 | -47.83668 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23a6e12a-0ad6-3bc0-b517-a6224be69a67 | -21.56921 | -47.82837 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b55979b-0e9f-3d69-a691-2a99a81c2fae | -21.569 | -47.80866 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65bd19a6-2704-3fda-9de1-eea799ee00ab | -21.56876 | -47.78913 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00b93bb8-6399-3ef2-b4f8-c15e06caef83 | -21.56858 | -47.8322 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4daefa1c-23f5-3e00-a62f-acd60aa8bd28 | -21.56838 | -47.81246 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b2c354e-e741-3acd-ac21-bfa0fe8e55a3 | -21.56814 | -47.79292 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06ac627e-ed9a-3646-8f88-75b7fd303baf | -21.56795 | -47.83603 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2333dec8-dbee-3819-9ad5-fd5a08261c2d | -21.56775 | -47.81627 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 423adfc9-d57c-3b47-bf53-6ba29d573637 | -21.56752 | -47.7967 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7911cc56-2fe9-3ae5-9b2a-ffaccb437030 | -21.56712 | -47.82008 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20fbb3c2-d389-3e6a-9673-4d30d0991f65 | -21.5669 | -47.80047 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69bff5d9-90af-3ac2-aacd-1f3b64cfd281 | -21.56649 | -47.8239 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64db4780-1735-3896-bd9e-389db7949c34 | -21.56627 | -47.80425 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99493066-6a41-3494-9d4d-5ac27d88022e | -21.56586 | -47.82772 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abb81c89-567f-3487-9209-0a6590eb6d41 | -21.56565 | -47.80804 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19769aba-dd09-33ac-88f4-5ddc30b28799 | -21.56523 | -47.83155 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a08859be-d0c9-372c-a51f-99f1905687e5 | -21.56502 | -47.81183 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29c80da1-26a4-31a0-a1f2-5ae4613a4bf0 | -21.56479 | -47.79229 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 731c64df-050e-3ef8-a83b-3096cc440591 | -21.5646 | -47.83538 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 097ca761-cafc-3baa-afa4-214eeb498c4a | -21.5644 | -47.81564 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b84654f0-2123-3124-871b-59c8bcd2ab47 | -21.56416 | -47.79609 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5ec2591-dd34-3c87-aaa7-96720a6d9254 | -21.56377 | -47.81945 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 836c4858-d742-3bfd-8e53-863e190ff913 | -21.56314 | -47.82326 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9caefab-41a2-35ff-8d2a-f31456f52f3d | -21.56251 | -47.82708 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4281f5c7-3b13-367f-a340-6fbe10703834 | -21.5623 | -47.80742 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2eb1b8c8-9fc4-382f-8168-e009a093bceb | -21.56188 | -47.83091 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf5829da-b318-34f6-ae7d-93d7e6a02354 | -21.56167 | -47.81121 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fa9c2e6-d847-3b76-8e5d-502e16970d56 | -21.56125 | -47.83474 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 446fe756-2743-3d86-8e47-a7e079f5ad2b | -21.56105 | -47.81501 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec8b2007-575a-3836-afde-30bf006c25b3 | -21.56042 | -47.81881 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0232479-c281-32b9-9a16-e8731e3c7e46 | -21.55979 | -47.82262 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a13bca7a-147e-374b-88b1-1203c3dfb8a0 | -21.55916 | -47.82645 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0265eb9-3b1c-3e97-9676-a29a7fb24ac2 | -21.55895 | -47.8068 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb09d609-04da-34de-95d9-0abfb81e406d | -21.55872 | -47.7872 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 210ac9db-5b3e-35f2-b2ec-954d64b4cdb5 | -21.55853 | -47.83027 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b45f3361-fcab-3deb-be5e-23bd82005cbf | -21.5581 | -47.791 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f40194ed-00cf-3c08-98f6-2a6361747f30 | -21.5579 | -47.8341 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c1e74e3-cf08-3992-934f-378b2895fc3d | -21.50845 | -48.06958 | 2024-10-01 04:17:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6d30e7d-7182-34b0-9964-530e8b05869e | -21.1643 | -48.15364 | 2024-10-01 04:17:00 | NOAA-20 | BARRINHA | SÃO PAULO | Brasil | 3505609 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e95ade7-61fd-3e29-87c7-c3447610534d | -21.56332 | -47.78027 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70186360-d573-3f02-bce8-a328e04d71ab | -21.56269 | -47.78405 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6bdeeff-f465-370a-8acc-751eb63c7b87 | -21.85325 | -47.1673 | 2024-10-01 04:17:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 041c8284-d117-36ec-9ad8-27ac19ea706d | -21.85265 | -47.17102 | 2024-10-01 04:17:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e82463f5-a5c9-3835-91d2-2925091bd863 | -21.84933 | -47.17042 | 2024-10-01 04:17:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd328278-8b36-3e3d-bc1d-1d92d1f90b84 | -21.58675 | -47.78472 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9237f931-f821-3090-aa62-8a64ee82615c | -21.58567 | -47.74923 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a43fbd2-7706-3f38-8075-b5187d864d6e | -21.58233 | -47.74859 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22014f88-beb8-3ce6-b41a-2af0e71c953d | -21.5817 | -47.7524 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cbef2073-cab0-359a-a68a-e4c5b70035ce | -22.18304 | -47.5279 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |


[Clique aqui para ver as próximas entradas](README94.md)
