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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55659866-bdcd-3fe3-b142-6512300c7dc9 | -3.90372 | -50.01928 | 2025-07-18 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7da25459-367f-33b9-9576-46393af24331 | -7.39558 | -43.79683 | 2025-07-18 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e623074a-f86e-36af-8010-3e3988e45d24 | -5.65276 | -43.71062 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9a618c67-48cc-3e17-b688-68b16f45e599 | -3.11814 | -47.00837 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1658bff2-8a9a-3eef-a66a-c544c1de8d7e | -7.35021 | -44.19133 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4aea178a-fd2f-3607-938f-6075b2925b0a | -7.19359 | -43.09919 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 387f7a07-4a03-3ec1-814f-eaf8dabf41f4 | -5.78368 | -45.07596 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47035ed6-44a3-3b9f-8639-9e3b62ac122c | -5.84106 | -46.21596 | 2025-07-18 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 163a69fe-6f72-3e88-955f-2088f79cae29 | -5.20045 | -45.48201 | 2025-07-18 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 04848b61-2e8e-36e1-a403-3bf089c2b6db | -7.34205 | -44.19806 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc7579c0-d575-3cda-8967-43472af87137 | -5.85311 | -44.97404 | 2025-07-18 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd50c86d-894d-303c-8b1f-1e5577885fad | -4.10584 | -48.20735 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4b9c484-f82d-30f8-bf8d-c558195f4dc1 | -5.66207 | -43.7201 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1926cd6e-df4f-3e09-a1c3-08129ab8bbec | -5.97289 | -43.77282 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2f7e836-347f-3b38-b4b5-c34b33d140ae | -6.99903 | -45.61458 | 2025-07-18 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fac6e11-cf06-3ada-9e3c-d6b9c68d73b3 | -4.21665 | -48.60887 | 2025-07-18 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cffb526-f0c6-3b26-a030-4bdf3ccad490 | -7.39619 | -43.79278 | 2025-07-18 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42ce1c1d-5905-322c-9a0c-d7a6f4710341 | -8.10143 | -43.15244 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 57bca131-fd36-3137-89e7-fd1570db8c2a | -6.40206 | -46.5451 | 2025-07-18 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7714f91d-59f8-33f8-9985-00e2d0a1c22c | -8.02541 | -43.67064 | 2025-07-18 04:25:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0f4ae1c-1ea5-381e-b826-bc4c27afc715 | -7.23583 | -42.93396 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a2223406-1177-3345-8aab-a57512db9ec5 | -7.00099 | -43.74842 | 2025-07-18 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48d47a82-4569-31b0-860b-38e21a0a5432 | -7.30991 | -44.38601 | 2025-07-18 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 344c8fde-77d4-3455-b560-b76f5523a80a | -3.04663 | -49.42831 | 2025-07-18 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa44d1fb-f1d1-3c1e-8409-c34572be03fa | -6.46015 | -45.07766 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c4d2aa-52aa-3805-aec9-55eb9d6367e7 | -4.95763 | -47.70435 | 2025-07-18 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbb946ea-8b05-37e6-ba48-3e5a604579e9 | -4.14926 | -48.21725 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 674b3b2f-1215-3f99-87d7-0f6cc5ae5bae | -2.927 | -48.23657 | 2025-07-18 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa20e224-309d-3ab2-87aa-6694eaa0093e | -3.93561 | -50.44604 | 2025-07-18 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7248685d-6a38-3c10-8348-1ccaa3627b78 | -4.96171 | -43.23048 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 104d18a3-8772-3f36-9158-ade73469de44 | -3.38955 | -47.47807 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e8c895f4-3a9e-3a6f-8dbe-bc4bb982787e | -6.26904 | -44.06206 | 2025-07-18 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33da99cf-0ac0-3114-a528-b3c1082c19e6 | -6.61637 | -47.19373 | 2025-07-18 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb8091c1-9a9a-3aa5-b931-14d9d722222a | -3.84769 | -47.75272 | 2025-07-18 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6b4cef5-2da9-3d78-964a-b9eb067a408c | -6.85732 | -42.05161 | 2025-07-18 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9af358df-3a36-367a-b8ae-f90ba856c740 | -5.97819 | -43.76154 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb1b749e-67db-3508-b356-95f832ff4802 | -3.61351 | -43.54287 | 2025-07-18 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9bbfc14-7b7f-3003-9d45-3f09aa870b0f | -7.19457 | -44.07696 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42205862-a3ec-3c45-8d98-a4dbbb367c6e | -4.80053 | -43.22031 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ab2fe39-41c2-3c55-a901-752bdf4e5e18 | -3.73087 | -53.99019 | 2025-07-18 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17bbd7e8-9648-3de9-99dc-316279cfd11f | -6.47202 | -45.17086 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f9c0796-753d-3f7c-848d-f494976f9481 | -4.31124 | -48.10631 | 2025-07-18 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4c38bbc7-ce6f-3ab1-9ec3-4acb7709739c | -5.65858 | -43.71955 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| adc486aa-04c5-3e0f-aa50-db6e040a22af | -5.65217 | -43.71454 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 250c9ec0-0a56-33b4-9350-3de72e99f10a | -6.47678 | -43.5066 | 2025-07-18 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5665a943-a3ab-32d1-a5eb-514a4a19800a | -6.49558 | -43.4714 | 2025-07-18 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aac9706d-28e1-3242-89b5-44a4c8967544 | -3.39682 | -47.4979 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6af60a3e-c56a-3f22-9521-1fdbfb811a5c | -2.44329 | -47.3317 | 2025-07-18 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 997ba6aa-147a-3d3f-a922-6688b4d8142a | -4.96526 | -43.23105 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0af11816-1546-326b-910d-6e7fb31d469f | -3.21636 | -48.97128 | 2025-07-18 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d4f08b1-d6ea-3672-ad45-0feeedbbf590 | -6.93694 | -43.81381 | 2025-07-18 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec4e978d-c10d-386e-a86b-45921aab022c | -6.81729 | -44.76451 | 2025-07-18 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 262b520d-ae21-327d-b771-966dacaeba5a | -3.39294 | -47.4786 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| aacbd30d-0cfb-3a68-aa23-b721f3e0e8a8 | -5.64926 | -43.71007 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e917ae37-8399-3537-8bac-054768c3ec56 | -6.71226 | -44.32563 | 2025-07-18 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01c65b9b-dec0-3c5b-a6a8-edb3f82e05ae | -3.11423 | -47.0114 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 045c4dc1-3c77-3fdd-8e51-52c7f9e3e731 | -4.77694 | -45.34066 | 2025-07-18 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9db3f712-0a2a-341d-a911-c964dbf5db7d | -6.72837 | -44.33586 | 2025-07-18 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a24f6c6f-155e-394f-be46-36d42e69a2ab | -4.80369 | -43.22036 | 2025-07-18 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fad223c0-2592-326e-a5fe-33b5f251be5e | -3.50628 | -43.34722 | 2025-07-18 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5f053bd-fd62-35fb-8ba5-b210fff1ab00 | -7.45253 | -44.6925 | 2025-07-18 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6c88261-e6a3-3a87-a4a3-0f6b28bbf62b | -5.73308 | -43.9442 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ba060c9-1f9d-38b5-8feb-ca1fc8a0b48a | -3.12368 | -47.00913 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bb5c1198-526e-30d5-9660-5b05c92bd7b0 | -6.50078 | -43.46901 | 2025-07-18 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a26e953d-e33b-30a4-878b-07156d6d5f59 | -7.06022 | -44.05719 | 2025-07-18 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5434a329-3373-3866-8c7e-1d80a4400d85 | -5.44238 | -46.28734 | 2025-07-18 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0217178a-28af-3fb5-b966-5fc9b9685257 | -2.63636 | -47.30576 | 2025-07-18 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 936c1d28-b4cc-3d24-9a00-190c70b82f13 | -6.16054 | -45.09735 | 2025-07-18 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70086dc4-da1b-3c48-b039-d946c191a09b | -7.25129 | -44.51658 | 2025-07-18 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea14cac0-b615-3731-8018-d6a3beab816f | -6.49143 | -44.46571 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6276e26d-c568-304f-996b-2bffe1b11f37 | -5.19936 | -45.48895 | 2025-07-18 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 101f6de6-4f46-39ce-8ea7-0ee7d4411d07 | -6.98088 | -43.73866 | 2025-07-18 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82822c78-0439-3cdb-a720-a07de057f693 | -3.98377 | -48.4051 | 2025-07-18 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c0f77d5-d919-3601-a1e1-642de035f824 | -4.54336 | -45.15853 | 2025-07-18 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d0a8635-ae4e-34ea-bddf-126f9d841213 | -5.48703 | -43.07861 | 2025-07-18 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| feff8026-e1de-369c-b276-02e98e7016f4 | -6.91184 | -44.83466 | 2025-07-18 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d31963e0-402e-3d9e-af48-f863d2855678 | -7.00749 | -43.75352 | 2025-07-18 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff5b76fb-784e-393d-80e5-e52f4bcb2841 | -3.80711 | -43.2239 | 2025-07-18 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ad9ddca4-3b9e-3572-a379-837b74aac137 | -6.72894 | -44.33206 | 2025-07-18 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 325df209-b814-3820-b8dc-759c55904fec | -7.61039 | -46.32162 | 2025-07-18 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8e6ba9a-de2f-3e47-8508-ef4f00dc8802 | -3.46576 | -47.68218 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be962933-d7d0-3b5e-802b-20e7fbe540bc | -6.77353 | -45.51117 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18512c3f-a38d-3ed3-84ef-bf0c45911e97 | -3.40031 | -47.47601 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 27311a10-8ac1-3865-83d6-ec9febb0082e | -6.72549 | -44.33154 | 2025-07-18 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 010ff7dc-c7d8-3f1b-b8c2-b08b54422dd6 | -6.77299 | -45.51468 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7db586ff-a3f0-32b0-a257-4c874b6846c3 | -2.58884 | -51.92299 | 2025-07-18 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8c3b5ff-a152-3eb9-8a4c-07a3b54715b1 | -8.09772 | -43.15188 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8bdb78e0-2b10-371a-8901-850c22e3d39e | -5.75392 | -43.40008 | 2025-07-18 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 84fb0658-680b-3766-b84a-911e46151da3 | -6.43612 | -47.88219 | 2025-07-18 04:25:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00e8cf26-143e-3c06-b1b7-769dc7f67dd8 | -7.28912 | -44.02591 | 2025-07-18 04:25:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17faf90b-4070-3691-9786-c8d70a90a888 | -6.292 | -43.43003 | 2025-07-18 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 296009d0-fca1-3853-9b34-7da2ecd0c019 | -6.88146 | -42.75663 | 2025-07-18 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ccfacbc0-4888-3b31-8fad-c009be5ee385 | -7.18815 | -44.07196 | 2025-07-18 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b335c3e-bec4-3ffa-86db-580074354f5f | -4.95706 | -47.70799 | 2025-07-18 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 422d4a44-d83b-3e07-bd96-b256fc86bdfe | -5.48174 | -42.14428 | 2025-07-18 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 72ba36db-35dc-3861-bfe0-34106230b89f | -7.20304 | -43.0114 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| acd3e025-8fce-3058-ade9-5325fa2559da | -4.84046 | -44.32051 | 2025-07-18 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4a0b0e21-e128-3474-8c28-4571de28a7fb | -5.73117 | -44.50735 | 2025-07-18 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 394d3bc7-55f2-3ba0-8e8b-73a5e4e806a1 | -6.49485 | -44.46625 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d809570c-b121-341f-a234-b26eb3f5b4f9 | -7.06463 | -42.9839 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README13.md)
