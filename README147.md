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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abf1f491-3973-331d-a288-e39994d0ff86 | -10.3195 | -47.42856 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6a23380a-51f5-306a-9b39-71d168cd2880 | -10.31442 | -47.44116 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 187a48e6-1582-34c3-80f3-140b7c2cfca9 | -10.31321 | -47.43351 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 19214c98-009e-39f4-83b2-915cb6296405 | -10.28687 | -46.58721 | 2024-10-25 16:50:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| caeb79e6-9011-3561-9a09-35ec927b71ed | -10.27365 | -46.75443 | 2024-10-25 16:50:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 19cfdf03-1c24-39fd-93f9-f74046a42f81 | -10.27007 | -46.75477 | 2024-10-25 16:50:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0c42c636-2e49-3285-ac06-123cdb490122 | -10.14092 | -46.60705 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| fdba8817-21b0-3b06-bb2f-670601504dd4 | -10.79535 | -46.50263 | 2024-10-25 16:50:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 4fad281c-82ad-3d2b-8f20-02b93b5841f8 | -10.78601 | -46.51279 | 2024-10-25 16:50:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e338205a-abc5-3849-9672-26c3e836cbfd | -10.78534 | -46.50865 | 2024-10-25 16:50:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 723c34c7-26f1-31c8-9a97-af81e8661dc3 | -10.67661 | -47.42501 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 155ccfdc-3637-36ec-bc0f-bf5f701cdf36 | -10.65813 | -47.50614 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8442dd4f-2c2a-357a-923e-bcf70d143656 | -12.32229 | -46.45489 | 2024-10-25 16:50:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b6571d8e-2e26-37e6-9ae1-5bfae59a0fd2 | -12.31878 | -46.45551 | 2024-10-25 16:50:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6f33d84e-9355-35be-9a51-9922505c106e | -12.20429 | -46.9859 | 2024-10-25 16:50:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 91d7dc10-9066-35f9-b075-a3d2fa3688cb | -12.1966 | -47.13633 | 2024-10-25 16:50:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0a07ced0-2ddf-3a23-8cf5-4c4ab0b040d6 | -12.19599 | -47.13253 | 2024-10-25 16:50:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 10510b92-f224-30d2-8fda-18e9ac8aa9e4 | -12.16865 | -46.9844 | 2024-10-25 16:50:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e3e4df5-1a38-3117-8364-40abc5efe098 | -12.0423 | -46.63184 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3a53b647-62f8-38e8-8c24-370f6697965c | -11.96223 | -47.60572 | 2024-10-25 16:50:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb5acf0b-aeab-39e7-8fe9-f25960e13aaa | -11.94863 | -46.79276 | 2024-10-25 16:50:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 11368aba-8e3a-350b-8eb4-309c01b878db | -11.92801 | -46.64212 | 2024-10-25 16:50:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 547a3392-dcb0-3be9-bc6d-906115f2014c | -11.90304 | -46.77612 | 2024-10-25 16:50:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 2ec68745-b7f2-3de4-86b9-052a1ed477d9 | -11.87997 | -46.78823 | 2024-10-25 16:50:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f34aa086-9d49-30a8-a6fd-1fa907669b9e | -11.87931 | -46.78424 | 2024-10-25 16:50:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8a36a198-9f3a-3ae0-8e4b-6664d26bd64d | -11.87813 | -47.71799 | 2024-10-25 16:50:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d8355e78-36e0-3041-8889-12f3a4e0d777 | -11.87476 | -47.71856 | 2024-10-25 16:50:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 674fd403-a11a-32ab-a41e-f5b9f8a0afaf | -11.87418 | -47.7149 | 2024-10-25 16:50:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| fdbdcc4d-4c03-39de-91f4-48e8b43e7014 | -11.64866 | -47.35495 | 2024-10-25 16:50:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6efcf648-dd0a-3ceb-87f9-367b760802e8 | -11.6484 | -46.83565 | 2024-10-25 16:50:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dfd08749-ec51-3a23-b763-176f311a3bb7 | -11.59688 | -46.7703 | 2024-10-25 16:50:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a15b56fb-5a29-3eb7-889f-e8960dfc6c35 | -11.58868 | -47.15854 | 2024-10-25 16:50:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 32686e85-3949-3e97-bab5-4a84702ef80f | -11.56602 | -47.74339 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c104241a-37ba-3e2d-95a6-96912f639e88 | -11.56544 | -47.73972 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7cd85e90-7fee-3d21-bfd9-138a3a298059 | -11.49324 | -47.24096 | 2024-10-25 16:50:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1cb6c6ce-3fc6-35e8-b534-bac6608e6748 | -11.49263 | -47.23717 | 2024-10-25 16:50:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86177cfe-3f83-3899-b213-2ee5f0988f1d | -11.45581 | -46.90248 | 2024-10-25 16:50:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| feea616e-ab9f-3768-914b-316c02ee9723 | -11.43482 | -47.68915 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2aa0f2a3-5f99-3483-938b-9130391953da | -11.42864 | -47.69405 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20cd4f57-4a73-3db6-a02d-a557c0dc4e7e | -11.42688 | -47.68296 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 15b69cee-930b-3241-af94-17e247214663 | -11.38752 | -47.71951 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 819f7197-798b-39e5-b21a-4e44329876da | -11.38414 | -47.7201 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 66c32cdb-24ad-33a7-9841-47f608a1e918 | -11.37959 | -47.71335 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 08a5bc74-0f3d-33c0-9867-f8edf296ce6c | -11.36658 | -46.9577 | 2024-10-25 16:50:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 621191f1-c799-3b62-b0b2-8a9c30f30b5b | -11.35805 | -47.22746 | 2024-10-25 16:50:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d65abba-ee1d-35a4-b6f1-ff817d48f9c2 | -11.21335 | -47.50857 | 2024-10-25 16:50:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3a23850d-519b-3974-b088-018cd7ebccd9 | -11.20994 | -47.50912 | 2024-10-25 16:50:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6bf0b22c-4782-3ac3-b1b9-04c7c9a7824a | -11.1981 | -47.56846 | 2024-10-25 16:50:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ecd867ff-bdf4-3ac9-8742-e9d459b81001 | -11.03843 | -47.57876 | 2024-10-25 16:50:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b86e8860-e0c6-32f3-b274-ea2a5dec6a8c | -11.03783 | -47.57503 | 2024-10-25 16:50:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79f3e459-fc8f-3c7b-bb49-151c09337cbb | -11.03038 | -47.30878 | 2024-10-25 16:50:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 178bd60f-9b9d-3e14-ab4f-3e4f9dc219c5 | -11.02694 | -47.30934 | 2024-10-25 16:50:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 441f4753-3da4-30c4-86e2-2081c272ff11 | -11.00795 | -47.60673 | 2024-10-25 16:50:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7d33102a-3252-30a9-abca-b4e5f5c74783 | -10.99613 | -47.60108 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c9ce89f2-76cd-3b9b-9ff6-87b3831cf133 | -10.99272 | -47.60165 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b5eef461-669d-3cc8-a1b2-5ab680c4b080 | -10.98671 | -47.25704 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 75f615d9-4bbf-3d22-b298-9b0ac2abebde | -10.90511 | -47.46985 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| aac71dde-43d9-3024-9441-76d0b68b93ac | -10.85968 | -47.42681 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 13f35a27-eb1a-3df8-9b48-dbc764dc0e7d | -13.41408 | -46.69348 | 2024-10-25 16:50:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 184d26a0-41d9-39ea-a85c-cbd0dd493691 | -12.53152 | -46.82045 | 2024-10-25 16:50:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| fd5610c0-775b-3c56-9d94-62c5a27db9d7 | -12.53089 | -46.81659 | 2024-10-25 16:50:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3a3ec1cb-ec80-3720-98b3-852762a90e0c | -12.5287 | -46.8249 | 2024-10-25 16:50:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5631b3e2-122e-3081-81ca-062ec4c777f7 | -12.52807 | -46.82104 | 2024-10-25 16:50:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04161da3-cb05-3b31-8e6e-b441c3c17b56 | -12.51706 | -46.81889 | 2024-10-25 16:50:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8a41b3e3-631d-3bfe-b61d-697473a83296 | -12.47937 | -46.43711 | 2024-10-25 16:50:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f0b5758-ee47-3e81-9d81-7f6696bfed22 | -12.41418 | -46.43979 | 2024-10-25 16:50:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 55b726e6-40f1-3ec8-bb2f-a8cdb23940c8 | -12.41067 | -46.44042 | 2024-10-25 16:50:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7422f81b-6914-38e7-a56e-d56dcee4759b | -12.39711 | -47.90836 | 2024-10-25 16:50:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36434291-bf19-3c41-bbd4-d760d7d49d65 | -13.38398 | -61.95532 | 2024-10-25 16:50:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8d78f5c9-d528-3233-a560-231b6ca02673 | -12.54085 | -63.05807 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ac1d2a87-36bf-37c6-8634-5130ee3ddda2 | -12.54011 | -63.05096 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 41c251fe-b4e1-3d4b-8cb7-46d13cbcd2d7 | -12.53685 | -63.05763 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0d4b4723-5b22-3ef1-8a3f-f048026636db | -12.53606 | -63.05054 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2a48d581-35ba-3e1f-b0c2-54f9ff8f7540 | -12.5337 | -63.05876 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 960a52ae-5d9f-378c-844f-bbad777b5a1a | -12.5297 | -63.05829 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.0 |
| b3f62197-490b-3fb6-a894-255fb96ec2c8 | -12.52656 | -63.05945 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1af42581-8f95-3e86-b1b9-1f182f9dc2f2 | -12.52255 | -63.05895 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 11fdaab7-7aa5-3702-9448-d731d05464e4 | -12.51941 | -63.06014 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a40c866f-efb2-3594-b1b4-e9d10f9325f4 | -12.51113 | -63.1914 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 26.7 |
| af4b5712-8021-339c-9600-3df24ee19e5e | -12.5079 | -63.19055 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 33.5 |
| a78f96bb-38df-31ac-a645-c1bb07013335 | -12.484 | -63.17091 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 9eb56fce-ef45-3026-8baa-676ad8005ed0 | -12.47605 | -63.16438 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| f7d3b9aa-e41e-3c68-8ab8-423e544f7b9e | -12.46886 | -63.16504 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 4f6b2eb3-d1eb-32ef-91b1-ebd13ed3176c | -12.4681 | -63.15783 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| a6ce6804-9ad2-3863-9808-52e1cdb3b3a7 | -12.46618 | -63.16821 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 3ae1fd6d-4c19-3858-bceb-48ce4c4a5249 | -12.46537 | -63.16099 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.7 |
| dc5cd43f-1a4a-317a-8af4-e8607b843b4c | -12.46243 | -63.17292 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| abb57643-31ec-3d48-bf78-0a6932f24fee | -12.46167 | -63.1657 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| fdcffdc7-0c5d-3e9b-95b5-f4f7551e8a2a | -12.4598 | -63.17605 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| b74bdbc7-574e-3bea-836f-bd5932cb1716 | -12.45899 | -63.16883 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 8ff239d0-51d0-31d0-8f4d-1e6664cab2de | -12.45261 | -63.1767 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 2e1cf69b-3955-3da8-a121-85b6fcd2e6b6 | -17.18605 | -57.28547 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 3bc51596-8c35-3389-9f15-f2088d42c96d | -17.18153 | -57.29281 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| c7d5cf45-3113-39cd-be8b-d6469e4c604e | -17.10636 | -57.47412 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| d1da2cf8-1d7e-301e-b637-18c2345ae14d | -17.1014 | -57.47816 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 92a719ab-6bd9-3718-a6d1-4c3f9fe41435 | -17.0818 | -57.40009 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| 7ae437ac-b5e7-38a8-8c95-cf90de66d91a | -17.07686 | -57.40409 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 9cbc8f17-c2ce-328f-8049-b2cfa6929716 | -17.07648 | -57.40067 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| b0ce3c14-6ec1-3536-bd42-7ff35233d875 | -17.06394 | -57.4333 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 7915f6a3-e8b9-3653-b5e8-a30a1b2b3875 | -17.05822 | -57.47935 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |


[Clique aqui para ver as próximas entradas](README148.md)
