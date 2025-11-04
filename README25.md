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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72a6e259-26c6-344b-94bf-206b5aa4cca4 | -1.76861 | -53.55529 | 2025-11-04 05:20:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d45484b-c74b-32c3-9d17-fad651db03cc | 1.12784 | -51.18096 | 2025-11-04 05:20:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce9c73a4-7efe-3e64-b850-8c16801c2632 | 4.23248 | -59.93864 | 2025-11-04 05:20:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb6e4ec1-591e-3618-aacd-692acedf0932 | -2.37575 | -47.72185 | 2025-11-04 05:20:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 038bec94-9d24-383b-aa71-94cfa67aeaab | 0.83518 | -59.3218 | 2025-11-04 05:20:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a172fc93-251d-3f31-a0b5-41dc747bdd08 | -1.22543 | -49.15491 | 2025-11-04 05:20:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 20d4407d-d8b4-3ea9-8ea6-5698efcec176 | -1.97489 | -52.10759 | 2025-11-04 05:20:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24fd6e9d-08ef-30d2-bbad-5b7d0efcfea6 | 0.84287 | -59.32767 | 2025-11-04 05:20:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce38cd9c-3936-327a-82fd-c2aa3ae3ac45 | 2.47642 | -60.20428 | 2025-11-04 05:20:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d85cad72-a41b-3e3e-b0f1-15f791d40424 | -1.96947 | -52.11185 | 2025-11-04 05:20:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c1e013f5-fc96-3380-8a8a-4c71f22c536e | 0.97128 | -51.21283 | 2025-11-04 05:20:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b1fd8b26-897f-35f0-b1f0-0f1a821b22e2 | -2.375 | -47.72687 | 2025-11-04 05:20:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fecf3db5-6862-3fd9-b05b-6acf65f19be3 | -2.37649 | -47.71688 | 2025-11-04 05:20:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8980cea7-f680-39a1-a4cf-e77def754027 | -2.3087 | -48.60002 | 2025-11-04 05:20:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf11b48a-520c-310c-844b-0cb3a340c238 | 0.47167 | -50.87932 | 2025-11-04 05:20:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cdcb9d5-8738-32ff-8685-b56671f8fc48 | -1.38937 | -55.19448 | 2025-11-04 05:20:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 990b61a8-fcb7-3b05-ba81-f131473574a1 | -1.58991 | -53.22856 | 2025-11-04 05:20:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68864d88-3c18-33e9-abe9-134a819f3a7d | 0.83902 | -59.32473 | 2025-11-04 05:20:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d31b3733-cbdb-38b9-914d-6fcaf37e4a44 | -2.3153 | -48.59665 | 2025-11-04 05:20:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2cda4862-5515-37f4-935a-2e00b9c54ccf | -1.19671 | -53.38617 | 2025-11-04 05:20:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a737df3-59ad-3832-bbf1-5a8bcf085991 | -1.76031 | -53.55162 | 2025-11-04 05:20:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89692d61-9fc4-3cda-9f86-9a0afd66dcfe | -2.32125 | -48.59771 | 2025-11-04 05:20:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 819abe07-2693-382a-89e3-9247b9b72b4a | -1.97258 | -52.1062 | 2025-11-04 05:20:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ac384abf-f8a1-3e08-b16d-e732a113b68c | -1.9702 | -52.10688 | 2025-11-04 05:20:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5bcd39a3-3e3a-308b-bc1c-1ce9cc58f023 | -1.1473 | -53.56708 | 2025-11-04 05:20:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e68cbf7-2b9f-3f89-b4b2-b5652a42c297 | 4.0744 | -59.93593 | 2025-11-04 05:20:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e7d9aac-365b-331e-afd5-fab7c5ff3831 | 0.84341 | -59.33112 | 2025-11-04 05:20:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eaf4e4ff-6551-3516-8ca6-43604713612e | 0.83572 | -59.32524 | 2025-11-04 05:20:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5ad961a-8ee0-3365-9de1-5610bbe74017 | -1.58773 | -53.23022 | 2025-11-04 05:20:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc7321a4-0e28-3c38-8fcb-aacf2246b5bd | 2.60154 | -60.12936 | 2025-11-04 05:20:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbcf4716-b5f6-3a15-8c66-cdf632dcb7e4 | -1.96789 | -52.10547 | 2025-11-04 05:20:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2361b54-9938-3d14-8071-7825ca019874 | 0.97603 | -51.21204 | 2025-11-04 05:20:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4fc33477-e653-38db-a984-ed5257a96e30 | -2.32189 | -48.59334 | 2025-11-04 05:20:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f9bcc156-6eba-3eb6-9ebb-4682091d9f55 | -2.32786 | -48.59432 | 2025-11-04 05:20:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c612e1e-a44b-328e-a035-6094e556b320 | -1.7692 | -53.55136 | 2025-11-04 05:20:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a632cbd-9730-32c0-8440-1f53768eb091 | -1.43384 | -55.2578 | 2025-11-04 05:20:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05f48746-8035-3fb2-b12a-20e73788393b | 0.83626 | -59.32869 | 2025-11-04 05:20:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a22785d4-790a-3f97-8cfc-ae573cb7d930 | 0.05655 | -51.11224 | 2025-11-04 05:20:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7619b2c3-0cfe-358e-a9c0-449123fa9dbd | -1.41576 | -52.66766 | 2025-11-04 05:20:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17e0d3c1-c0c0-32a8-a299-7e6d0a171a27 | 1.12865 | -51.18011 | 2025-11-04 05:20:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 954aaee5-881d-33a7-844f-50f8ec39db3c | 0.97208 | -51.21794 | 2025-11-04 05:20:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5d4e7722-5f31-3f26-994f-6729b7fd3c7b | -2.31785 | -48.57932 | 2025-11-04 05:20:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 290d7edd-ab37-36ba-b2b9-b841fd9fb7eb | 1.19891 | -60.59024 | 2025-11-04 05:20:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa63bea6-bf7c-3755-8aee-0ac7da50d112 | -1.14671 | -53.57093 | 2025-11-04 05:20:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abf2b5f7-55f7-3e8c-9dba-bfb2b5742476 | 3.35559 | -61.11086 | 2025-11-04 05:20:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0c90aa9-87de-31c4-8c21-c3b95571f7d8 | -1.76497 | -53.55071 | 2025-11-04 05:20:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9110f58-6e0d-3d5b-92e1-f3c838dde0f8 | -2.31722 | -48.58364 | 2025-11-04 05:20:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8834ba2e-f8df-3c64-9280-d6beb36411ed | -1.9718 | -52.11119 | 2025-11-04 05:20:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ca6cf418-9d16-3b27-9463-e3fa97cfa80e | -1.96713 | -52.11041 | 2025-11-04 05:20:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b686c26-428e-31aa-9064-1431215c5a69 | 0.84395 | -59.33456 | 2025-11-04 05:20:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52c02399-e009-383e-b1ae-3e66b6a23514 | 3.35498 | -61.10683 | 2025-11-04 05:20:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd2ab0f8-2339-3a89-b5b7-547a7c888b4c | 1.19948 | -60.59393 | 2025-11-04 05:20:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72c00b94-9aba-3ae6-854c-edcb6cb4527e | -1.22603 | -49.15104 | 2025-11-04 05:20:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 50c36c6e-ce10-3dd3-ba8a-92345dfc0e31 | -1.76074 | -53.55006 | 2025-11-04 05:20:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99039642-85c7-38ea-9cc0-b4862f2e6575 | -1.76093 | -53.54767 | 2025-11-04 05:20:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc5d5764-6373-388f-9d7e-11791a390674 | 0.83956 | -59.32818 | 2025-11-04 05:20:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7f4d2a6-02e5-35f3-9c7f-e28f56829660 | -1.22037 | -49.15012 | 2025-11-04 05:20:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2d2824ef-6526-3ba2-aea6-9e7653331e07 | -2.83772 | -49.41032 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b82e2969-840f-35da-b9dc-68e9e79c6589 | -3.49598 | -50.45777 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8123b605-449b-39e2-a04b-5c25ca33eeed | -3.48942 | -50.31552 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 863fd92d-1baa-318d-b035-c381d8b87e3f | -11.95887 | -64.89332 | 2025-11-04 05:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b57e5b2-7b25-390c-9f56-a519d8ec2ff1 | -3.29199 | -50.19941 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6c8ec26-020e-33ba-9c7f-90da2c6d4177 | -3.91581 | -47.69715 | 2025-11-04 05:22:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ba30345c-9028-39a4-ab28-4c3b11d5a4f8 | -3.38943 | -54.27203 | 2025-11-04 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 329febb9-9b32-306c-9c53-2b68f2cba173 | -3.57537 | -50.64655 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8eac0a5-2eb6-3ee5-a76e-8411a68af948 | -3.43383 | -50.2387 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81126998-7564-380c-8a54-1de8ae47c5cf | -2.24798 | -51.916 | 2025-11-04 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3467c7b-b269-3424-97da-23b528f1999d | -15.13713 | -58.18736 | 2025-11-04 05:22:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| abacd3c2-3f15-3777-98a1-9d8c610906b3 | -3.44155 | -51.47353 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce545072-4993-3b61-bf7a-6a4f5f6c50c5 | -2.4121 | -57.91921 | 2025-11-04 05:22:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9df764fb-63a2-3dec-abe0-6779c19d3f53 | -2.90452 | -51.46267 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99aff2df-5d34-35e3-bbfc-ccf44ff5cd08 | -3.52685 | -55.43299 | 2025-11-04 05:22:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a2e0c18-66cc-3b54-8fbd-664a5622bc05 | -3.38888 | -54.27578 | 2025-11-04 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b45011e-0a3b-3b6b-afcf-eaf13007c1f4 | -3.44824 | -50.21586 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbc0fb34-f006-31c2-bd00-5b6000cea678 | -3.44309 | -50.2428 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 84f2943f-6534-30f9-93d0-a1dc7c0eb460 | -3.228 | -49.49475 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e778cd6-2312-3630-bd78-9d94555532af | -1.8313 | -55.34707 | 2025-11-04 05:22:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33bd1dd7-5db8-384c-a9a7-8119c732581a | -3.01723 | -51.39656 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8320392a-c6a3-3bd0-95f1-37c4028851a9 | -3.31811 | -53.84665 | 2025-11-04 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d7c526b-2b85-3497-a24c-8226a0392bd2 | -3.00692 | -49.47836 | 2025-11-04 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b686d9c-967c-3010-9154-a91e946470ff | -3.50265 | -50.47065 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e2a1ac3-3023-35bb-9e73-0cca8a1366d9 | -2.66641 | -54.76587 | 2025-11-04 05:22:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea84a9c6-714c-36ad-8414-aa720dfecba2 | -3.49941 | -50.47156 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a6665b7-a35c-3ee7-8cd3-68fa9a6c2fa7 | -11.84311 | -65.02 | 2025-11-04 05:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e89f72fa-44f8-3604-b25e-ffbfa4a718ce | -3.92227 | -47.69811 | 2025-11-04 05:22:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7a55dbf7-9e1a-3f6c-be72-9d138edeb521 | -3.45326 | -54.68428 | 2025-11-04 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79e00fba-12e6-3c70-9b76-a5da365bf49b | -2.84349 | -49.83172 | 2025-11-04 05:22:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3fadacc-7f47-3c43-b64b-9e66fa96b5a3 | -3.46181 | -52.87207 | 2025-11-04 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a89170a-938f-397a-b238-454876b9ff5d | -3.24626 | -50.80205 | 2025-11-04 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f24a3806-6d71-3163-b840-e81033646c7d | -3.06853 | -47.77316 | 2025-11-04 05:22:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 52ba1052-03db-3fe1-a696-a5accc470a59 | -3.24129 | -50.7958 | 2025-11-04 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf468275-379a-3cf5-8dba-c882bc8e1f32 | -3.11109 | -51.21081 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab80f68d-1553-3887-9df9-e0588fec0d0f | -3.44029 | -50.23241 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31145611-c5ca-3d1c-8238-f35122137ead | -3.49501 | -50.46429 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c92c427a-50a3-3160-ab3c-2f14bfb77c12 | -2.66533 | -51.61994 | 2025-11-04 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de9f4be1-d407-38cd-b2f3-18c121b092a0 | -3.44347 | -53.2576 | 2025-11-04 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbbeb1be-11bb-3169-971b-718c18071e8b | -3.57004 | -50.64582 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba7b9b20-0d8f-3b15-ac3e-be57bfda9d49 | -3.44699 | -51.47141 | 2025-11-04 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0f739b6b-e332-3a9d-aafe-00cf18e9ef93 | -3.44679 | -50.21823 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24a88114-f2c3-356d-b2c6-d1fa00adf471 | -2.84296 | -49.83542 | 2025-11-04 05:22:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README26.md)
