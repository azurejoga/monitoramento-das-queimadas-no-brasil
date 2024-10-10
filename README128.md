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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7755bad7-84e4-3e4e-b1f6-01034bdaf04a | -8.61864 | -54.60208 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af60f3ea-e4e8-336e-a673-77638f8bf61a | -8.61816 | -54.60575 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c85b288-777a-3564-9bb1-a26dcc7d9bc6 | -8.61768 | -54.60938 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f0b4312-ff7a-3bad-9b56-fd46a285d893 | -8.61458 | -54.59032 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09b34752-ee58-33f3-8c2f-0e0f55dc69e6 | -8.61411 | -54.59393 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3c2e393-f8ad-3adf-b021-0734dc86fc7b | -8.61363 | -54.59758 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5cddcb1-ba57-3d90-b79f-8ca4c8a09057 | -8.61315 | -54.60128 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80aea827-2735-3e11-9831-c57376755c4c | -8.61267 | -54.60497 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8caef78e-b4f4-37d5-865b-8a11b5bc6e56 | -8.61219 | -54.60864 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1f31884-25f1-3491-811b-2258c53dd5f1 | -8.60909 | -54.5895 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eca3470c-22d6-322c-a146-c65bf3bb6521 | -8.60815 | -54.59673 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b40fa7a-d3b4-3c30-bcf1-af5a0faaf4f5 | -8.60767 | -54.60042 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0f5e389-7ed2-364f-aa66-fdc1f1e9de44 | -3.56396 | -54.34335 | 2024-10-10 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2fa7143-df2a-3f15-b869-327c1bfbd7e9 | -3.56352 | -54.34641 | 2024-10-10 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f239fb06-e3b7-3419-996c-366aaff2eed8 | -3.56306 | -54.34966 | 2024-10-10 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96899303-e6b6-306d-8502-4cd70dd6c98e | -3.56241 | -54.34508 | 2024-10-10 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32311fe9-772c-332b-bf4a-7ae88a717aa5 | -3.56194 | -54.34826 | 2024-10-10 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ae04bd8-7342-3305-ac6c-2eac2ad35b3c | -3.26393 | -54.18335 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1944972-28ff-367a-ba1b-3e8a7be89531 | -3.26344 | -54.18662 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dc15ab9-bad5-3337-8cd4-ae64d052bb86 | -3.26193 | -54.19663 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 898d81bd-22e1-3c02-8d0f-91523d8d84bb | -3.25869 | -54.1827 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47842ad5-b9e4-3155-adc7-0565a1ad1e3f | -3.25819 | -54.18606 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6b4d957-3104-3bdb-8c76-6b75e3a3341c | -3.25769 | -54.18938 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 982acc7c-4185-3f40-a8ee-9bb48da6afe5 | -3.2572 | -54.19264 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d4113fab-0573-375f-9899-438d0d5c6aea | -3.25671 | -54.19588 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be2fa652-d2db-3838-9ce2-6075a99ab2d6 | -3.25345 | -54.18207 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| adb88ba8-7c37-35dc-925e-942f9fef7b8f | -3.25294 | -54.18547 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db5612e1-6cdd-3efa-8f9a-ac2c7f907130 | -3.25245 | -54.18875 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f8a01254-0895-3e58-912e-5a8d1ad5ad44 | -3.06701 | -54.77338 | 2024-10-10 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83ec24c1-44fb-3d2a-9512-83fbed8dc3ae | -3.06656 | -54.77631 | 2024-10-10 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc0a7b70-6a11-3fa0-afb0-63aba9f7ff48 | -2.89328 | -54.25639 | 2024-10-10 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d6ed8b3-5710-31db-b437-89b93708dcec | -2.89284 | -54.25932 | 2024-10-10 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46a9c556-27b0-3ae8-b1a9-19931caa3e5e | -2.82127 | -54.01801 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4aee7e34-7eb2-3c94-9461-a0f0fa76a0e5 | -2.81602 | -54.01724 | 2024-10-10 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 599bce8e-8133-39cb-94f7-38a405c45da4 | -2.81485 | -54.36031 | 2024-10-10 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7bab507-5668-3fc5-ae3e-72375733a4bb | -2.8144 | -54.36345 | 2024-10-10 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 640bd5d0-56ca-3272-8bf1-4c0f1a781366 | -2.80279 | -54.58529 | 2024-10-10 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e68f153c-8053-33b0-b357-a66db6c6da0b | -3.13317 | -53.73539 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebb7f0c1-52c4-34dd-94cc-0f517f280829 | -3.13265 | -53.73878 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f434e7f5-de37-3aef-a819-90e4490e9b98 | -3.13054 | -53.73736 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46fe6b26-cfb5-3636-bb22-fc976f3d2b5e | -3.13005 | -53.74076 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c835552-f9ad-3a41-b84e-a6c9a0d5a385 | -3.1278 | -53.73459 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e30b8e5-6f2f-37a8-bac9-ff01987757fc | -3.12728 | -53.73798 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e68d5504-82c6-3c77-b727-620b044005cb | -3.12517 | -53.73654 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d753a387-61ef-3b4e-92c3-50fbba1b0c5b | -3.12468 | -53.73993 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18a249fa-7a71-3cfe-b95f-8579cf0240f1 | -3.12243 | -53.73378 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eaed3eb8-79f7-346a-a0fa-ddfe35aabd2c | -3.1214 | -53.74055 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fee9ac76-d80c-331b-9a4c-00090b1285ee | -3.02193 | -53.85828 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb0c552b-f414-32b9-a452-59b29a5db5b7 | -3.02142 | -53.86184 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee87e01f-f5a1-3248-960e-940670172e8b | -2.97921 | -53.71718 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5189c475-0278-3c51-9221-dae86420df98 | -2.97869 | -53.72068 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30fa39c3-1cc6-3fed-a64d-ac776fe5b2df | -2.97818 | -53.72406 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1fa346d-d6ad-3b50-9c08-95466fe96ab5 | -2.97383 | -53.71644 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb42dd41-6e1a-3f74-919a-a681fc2bdefb | -2.97332 | -53.71986 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07b4b5a0-f67f-3905-8f71-03725459e409 | -2.94852 | -53.7021 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43b96c37-1005-3739-8a21-783f66cc434f | -2.94802 | -53.70551 | 2024-10-10 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e25afa5-684b-3553-92da-9c51b339ea0e | -3.71068 | -53.9263 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1f9d74ba-a556-3733-8e18-5334f2ed1200 | -3.70529 | -53.9258 | 2024-10-10 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7158efa4-7d77-3490-8703-92db7cce345d | -6.17108 | -55.48436 | 2024-10-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfa8c5b6-cb61-34aa-a315-804cccf33965 | -6.17067 | -55.48728 | 2024-10-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f386a05-8d05-31b3-9342-990ceeb14aa7 | -6.16733 | -55.47493 | 2024-10-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27e059d4-9fc4-3dc2-bf1e-affefc6be388 | -6.16693 | -55.47778 | 2024-10-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b5efb3f-ef73-3c23-ac66-bc56ee7530c5 | -6.16194 | -55.47702 | 2024-10-10 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffaaae01-6dc7-39d0-be44-c371bbb43c61 | -7.9733 | -54.83503 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28d5ca6c-527f-3459-9329-a8c7ecd209fc | -7.96409 | -54.78171 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f719e85-9d02-3be3-abc4-28da5c222b89 | -7.95965 | -54.77396 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f10a3da1-f466-3906-a659-dcf0f705529d | -7.95919 | -54.77743 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4958dbb-3744-3850-820a-1f7002616274 | -7.95872 | -54.78091 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af1dc004-cefb-323b-9a50-bce638eb6122 | -7.95826 | -54.78439 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d889d499-f910-3664-88b7-1dd13bb30908 | -7.95427 | -54.77324 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 204b3867-bfd2-3e8d-96e4-8485d743791c | -7.95381 | -54.77668 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5987457c-7057-39ac-8e5d-b1951522ab3f | -7.9489 | -54.77242 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 697ee3f8-b732-36d4-9baf-eeae2835364a | -7.82588 | -54.72673 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f99744b5-ce80-368f-8227-8016192c0124 | -7.80911 | -54.70907 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa669e1c-d4c3-3764-984c-2145b0f1ad0a | -7.80856 | -54.71304 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c25a496-dc95-343c-ad51-2307a17d08cd | -7.72515 | -54.80359 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9f57870-20b2-32ca-9913-571ab5a115bb | -7.68953 | -54.83744 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7796af7b-29e0-3cbc-96db-2915a2d80270 | -7.68819 | -54.83615 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fe09282-a409-3347-a17d-e9dc52b9be8f | -7.68516 | -54.82978 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 922e8b6e-da2b-3170-8d32-2a45a185eb1a | -7.68469 | -54.8332 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8935c15c-8913-3c9e-a88a-217d383c2249 | -7.68421 | -54.8366 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa52e286-a514-3244-b9b5-68a94e58c1e8 | -7.68331 | -54.83189 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68a54928-8d4b-3f56-a5c3-9dbc9c42626c | -7.68287 | -54.83528 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4f06470-a00f-35a9-86c7-17ae3fe1cfd6 | -7.67936 | -54.83236 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d2c43a1-7e11-3568-83a1-02ff69e2356e | -7.6789 | -54.83572 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9576658a-c80b-3348-8876-b5932c9d36b4 | -7.67799 | -54.83104 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae05aea6-b817-3d66-aaf2-a72aad536592 | -7.67755 | -54.8344 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 952cbaa6-a418-3f95-bbe2-4270402ddc55 | -7.62777 | -54.97161 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87e22e44-07ec-3c80-98c8-c36931956f94 | -7.5586 | -55.36172 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1132a3a4-71fb-3fc2-9505-f15b0c451c0a | -7.55389 | -55.35788 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4cd534d-158d-3f25-88e2-8b5edd0ca521 | -7.17018 | -55.54652 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f3eebd7-0fd8-3c47-841e-ba0ecc5b4f3f | -7.16979 | -55.54945 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1869e129-38a7-38ed-bbbf-40797b36781c | -7.16939 | -55.55237 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da60b811-86bf-3cca-89b8-ef0d709e8e89 | -7.16518 | -55.54893 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 265ac611-a00b-34c1-bcf1-bf267ebe26df | -7.16475 | -55.54864 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fffd392-3c14-3428-a8ed-41e4d41b6c5d | -6.87821 | -55.11679 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c764a56-eb0c-3503-a8d2-6129ca9d991a | -6.85535 | -55.75257 | 2024-10-10 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fafc2a5a-8788-332e-a103-a408d1149c43 | -6.6504 | -54.94543 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d45a63d7-fd2d-30bd-b2b8-63634fe20f5e | -6.64518 | -54.94468 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ae3c5d6-21c1-3ac1-a6fc-b9b9fece61a6 | -6.64475 | -54.94778 | 2024-10-10 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README129.md)
