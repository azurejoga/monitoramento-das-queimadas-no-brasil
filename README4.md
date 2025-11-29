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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b4bb14e-78c5-34a9-bac0-3eb5e1cacb69 | -3.843 | -44.1213 | 2025-11-29 00:24:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 747935dc-c206-36db-aa47-e8a995cf8443 | -2.6375 | -48.545101 | 2025-11-29 00:24:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c21d4a78-b389-391a-a825-acc6a6fb56f1 | -6.7804 | -41.712502 | 2025-11-29 00:24:00 | METOP-C | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b6b7b1de-4a40-33ff-9a9c-dfafd99bcaad | -20.9783 | -48.616901 | 2025-11-29 00:24:00 | METOP-C | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f0e9e5ca-ca1c-3c72-a679-fdf3edadf3f4 | -8.1678 | -43.188702 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| de929834-c73e-3dd2-9169-040b8e574b3d | -9.9203 | -47.412498 | 2025-11-29 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e5c6a47-4730-3cee-ad7c-3f4fba409343 | -2.6003 | -47.339298 | 2025-11-29 00:24:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8adcfbff-0147-31e5-919b-d17fb2bc197f | -2.9124 | -45.502102 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a073f628-c7c0-3382-8ffd-7f07344e5a21 | -19.7187 | -49.52845 | 2025-11-29 00:28:00 | TERRA_M-M | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| e4a4aaf3-05bb-30c8-817b-ea1660e2f4b0 | -22.44506 | -47.0145 | 2025-11-29 00:28:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 35123e35-fd6c-3e67-b8e9-932548e2ec85 | -21.12558 | -48.41697 | 2025-11-29 00:28:00 | TERRA_M-M | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3aeceaa9-14a9-3596-9536-698d462f451e | -20.74958 | -47.20098 | 2025-11-29 00:28:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e8370e05-4022-3a31-8461-3099db91604b | -21.54337 | -48.03448 | 2025-11-29 00:28:00 | TERRA_M-M | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 62606ba2-4d96-3677-92fa-044d68785b1d | -20.2176 | -47.54346 | 2025-11-29 00:28:00 | TERRA_M-M | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 23.8 |
| db9b62f4-d91e-35a0-bb35-fd59e12041f2 | -20.20874 | -47.54485 | 2025-11-29 00:28:00 | TERRA_M-M | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 7ed98c42-b2f9-33db-87e5-cef69cc81ff7 | -20.97948 | -48.63238 | 2025-11-29 00:28:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 781c83ca-adcd-3c3f-a971-51b9fbca69d9 | -20.1945 | -52.3806 | 2025-11-29 00:28:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 54.1 |
| db3f47dd-cd6a-3b7d-a9dd-ca8001f42a49 | -21.11656 | -48.41833 | 2025-11-29 00:28:00 | TERRA_M-M | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fc0cca09-047f-37b8-af68-6d29a7b0a34d | -20.98712 | -48.62544 | 2025-11-29 00:28:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| bd3bb08c-79b4-38cb-8813-8f6d18ed1f9a | -19.72572 | -49.53165 | 2025-11-29 00:28:00 | TERRA_M-M | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| da27c3c3-c0d0-3468-a831-0a3df0fe559b | -20.45048 | -47.50401 | 2025-11-29 00:28:00 | TERRA_M-M | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0df40d2a-9071-34d5-adb1-4bea5eb89158 | -20.45177 | -47.51341 | 2025-11-29 00:28:00 | TERRA_M-M | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 192a42cd-648e-3830-8e0c-05a0b82dcd31 | -20.92387 | -46.79753 | 2025-11-29 00:28:00 | TERRA_M-M | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 61d6adbb-252b-30f7-ac9c-3795a5ee6e67 | -20.18156 | -52.36644 | 2025-11-29 00:28:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 00bb95a4-0683-3600-996f-1f32b1b50ae0 | -20.19276 | -52.36497 | 2025-11-29 00:28:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 758a077f-4e7a-3917-8b57-c292c462c1fc | -20.44162 | -47.50542 | 2025-11-29 00:28:00 | TERRA_M-M | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 87057b6f-94f7-3f8a-951b-884187e8ba5a | -22.08691 | -46.82476 | 2025-11-29 00:28:00 | TERRA_M-M | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 618967a5-9953-3c58-a589-9dbce1df14f3 | -20.18501 | -52.39772 | 2025-11-29 00:28:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 6cc8f915-820b-3e60-bc82-303d43fb617f | -25.34939 | -51.15055 | 2025-11-29 00:28:00 | TERRA_M-M | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| eeec6b17-939e-3f58-a090-01e58fb1bd7a | -20.97818 | -48.62249 | 2025-11-29 00:28:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| a8ac8336-927a-3dfb-9594-4685248c40df | -20.44292 | -47.51482 | 2025-11-29 00:28:00 | TERRA_M-M | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2b44a515-4540-3665-b67f-925e0dff04c6 | -20.18329 | -52.38213 | 2025-11-29 00:28:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 273.5 |
| dde1a19f-34ca-374d-b972-75275eabfbc0 | -22.09724 | -47.09549 | 2025-11-29 00:28:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 138d4052-0787-3e2f-9533-a2238f7601b0 | -19.72003 | -49.53873 | 2025-11-29 00:28:00 | TERRA_M-M | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| d7cd97a3-6f8a-3a0c-b2ca-989678151500 | -20.92521 | -46.80701 | 2025-11-29 00:28:00 | TERRA_M-M | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c2c1994c-6ce9-35a8-8200-ee296114e11b | -20.75089 | -47.2104 | 2025-11-29 00:28:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 35.9 |
| ec793e4a-8f10-35c1-8066-bdb7d621f9fa | -20.21631 | -47.53406 | 2025-11-29 00:28:00 | TERRA_M-M | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 8dd783f1-1900-39ec-9edd-fe392d9258dd | -20.98841 | -48.63541 | 2025-11-29 00:28:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| 823c9b31-1984-3185-b814-c2772dca9be1 | -22.95346 | -49.0632 | 2025-11-29 00:28:00 | TERRA_M-M | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 9db3c233-f457-3e2d-9d06-39cdf301969b | -20.41144 | -47.22208 | 2025-11-29 00:28:00 | TERRA_M-M | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7fbc62e4-7cd1-35f3-8940-bb51f96a6742 | -20.17206 | -52.38349 | 2025-11-29 00:28:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 563e8486-f8bc-39a5-8aa9-d278a81d13bb | -20.21502 | -47.52468 | 2025-11-29 00:28:00 | TERRA_M-M | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 89286389-39d7-3f7a-a53f-13d1f35adc4a | -20.20745 | -47.53547 | 2025-11-29 00:28:00 | TERRA_M-M | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf7c9377-eb4a-31d0-bcbc-130cdf22286d | -20.1818 | -52.3533 | 2025-11-29 00:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 2c65be2f-4aa4-33b2-9cd5-fe7a11354219 | -3.0883 | -45.7687 | 2025-11-29 00:30:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 430dab31-b79b-33ea-94df-b2c2e4aa6299 | -17.6155 | -46.6607 | 2025-11-29 00:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 54a6dec7-fb01-3707-aaf0-a413ded69224 | -20.201 | -52.3937 | 2025-11-29 00:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5ae7ec1b-387e-3c85-9c1d-d514855b2a42 | -20.99 | -48.6293 | 2025-11-29 00:30:00 | GOES-19 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.0 |
| dcc3e64f-f8ea-329a-98c8-201054f97c14 | -3.0882 | -45.791 | 2025-11-29 00:30:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ff965fb9-ee13-3705-82d8-b84e1c577c8f | -20.1813 | -52.3754 | 2025-11-29 00:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 296.3 |
| bc614016-3aa9-3498-8674-c49bd91f0370 | -2.3645 | -45.7031 | 2025-11-29 00:30:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ffa88ce1-3193-3f85-94b8-4de349de5771 | -20.2256 | -47.5285 | 2025-11-29 00:30:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 138.8 |
| ee55852a-8094-3641-8ce1-45793c42b4da | -2.3459 | -45.7036 | 2025-11-29 00:30:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 77bf9b69-7797-3810-8632-91dae25f732e | -2.6507 | -48.5414 | 2025-11-29 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 6d709e4a-ddd4-37b6-8586-233f05fcccb3 | -20.1807 | -52.3975 | 2025-11-29 00:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 126.5 |
| d0a1a92e-2886-3b3a-9619-15face94f19f | -2.9792 | -45.2567 | 2025-11-29 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.6 |
| cba0c12e-5832-3e10-a560-ffb8e4f81177 | -8.1633 | -43.2055 | 2025-11-29 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 92ff82a8-c4e6-3007-b015-143844247f53 | -2.6322 | -48.5634 | 2025-11-29 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0ba9df1f-d2f8-3b4b-a94f-63afe19b4d12 | -2.9626 | -49.1736 | 2025-11-29 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a59de6c9-21e8-3377-aa3d-81517e65ea8a | -3.1068 | -45.7903 | 2025-11-29 00:30:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 8915e268-19d8-32cf-bc22-e97fe65ba662 | -20.4503 | -47.4995 | 2025-11-29 00:30:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8773b98b-87d3-35a2-a5a8-c3fa762806bb | -1.4923 | -45.7903 | 2025-11-29 00:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 1bb7a39e-2262-388d-85f7-2bc66a27ec5f | -4.1161 | -44.9129 | 2025-11-29 00:30:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 068a8ac8-6ea1-3efa-b7c7-b3ec17abd0c2 | -2.9606 | -45.2574 | 2025-11-29 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d6d2748e-54c2-381a-a690-ab98d0a161dd | -8.1822 | -43.2034 | 2025-11-29 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 0ad1178c-5748-3951-af41-d4b1ebb4b1ef | -2.9793 | -45.2341 | 2025-11-29 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 8c95f81b-2752-32ab-b3b6-e51412ed2618 | -2.7845 | -47.4343 | 2025-11-29 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 0a16a84c-b1b8-3e2f-80f7-bf67cfb6063a | -2.6322 | -48.542 | 2025-11-29 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 7373f6cd-d8f3-376c-b33d-b3fd69251ac7 | -2.9116 | -53.0606 | 2025-11-29 00:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 611eba2d-771f-3ea7-b8de-3f96b2cf4040 | -20.2016 | -52.3717 | 2025-11-29 00:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 126.6 |
| e800c44b-5f70-3507-892d-6f01b2d60cd9 | -3.1069 | -45.768 | 2025-11-29 00:30:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| cb97d506-72bb-3308-9dd3-255269d945b1 | -16.67326 | -46.65434 | 2025-11-29 00:30:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f64527bc-bfef-30e9-b069-d95a314fd786 | -17.61441 | -46.65916 | 2025-11-29 00:30:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 22e1599c-c09d-30a4-ad3c-d3ab59183e23 | -17.60538 | -46.66062 | 2025-11-29 00:30:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9b47f9bf-8ca0-37df-aeda-410c1bb2c1c0 | -17.12992 | -48.72353 | 2025-11-29 00:30:00 | TERRA_M-M | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ff7406e5-ca94-3046-b909-aa665b61ef95 | -17.00703 | -49.17518 | 2025-11-29 00:30:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3b42e8d9-dcdc-3872-9d2e-fc7c46fa5602 | -17.85917 | -49.22284 | 2025-11-29 00:30:00 | TERRA_M-M | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8cc43ad9-eb85-3456-85e6-70e2b070027c | -18.2001 | -49.72969 | 2025-11-29 00:30:00 | TERRA_M-M | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d3680662-ac56-3813-a5b1-d8c8b94804b5 | -17.61581 | -46.6688 | 2025-11-29 00:30:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 34.9 |
| b1dcc61c-e226-374e-9fca-6c05e7674dc5 | -18.5914 | -48.10402 | 2025-11-29 00:30:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2c093b3d-1b25-3102-bae7-7108d42dc798 | -8.16945 | -43.22258 | 2025-11-29 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 84e34efb-4138-37b4-b54c-2212d41f9e8f | -8.02426 | -43.1434 | 2025-11-29 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| b292a855-ff6a-330c-b819-7108138996cf | -8.03409 | -43.11964 | 2025-11-29 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 538.8 |
| 5edb6eac-df75-3ca7-b5d9-5c2e9c5805a3 | -6.23967 | -40.30346 | 2025-11-29 00:32:00 | TERRA_M-M | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 27.1 |
| de40dc08-7710-3bbd-be82-19af38cbe710 | -9.92779 | -47.4159 | 2025-11-29 00:32:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6058b1aa-ce1d-3e4f-bfc4-bda93ef0a012 | -8.16614 | -43.20149 | 2025-11-29 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| 7b7f823c-015d-3c3a-94c3-bfc0c5665c06 | -9.9184 | -47.41736 | 2025-11-29 00:32:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ffe0777-f56a-35c9-888b-0df07b46dcca | -8.02863 | -43.14838 | 2025-11-29 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| 3ecc11e6-dfcd-3a99-bb3a-67394601b353 | -8.0474 | -43.11749 | 2025-11-29 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 204fc631-3aff-3f28-a2f3-2ba28a1f8e59 | -7.46192 | -44.75135 | 2025-11-29 00:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fcd71625-2b70-3f9d-9829-fc760af4db99 | -9.37013 | -48.41632 | 2025-11-29 00:32:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8feaf4de-5e6b-34bb-ac3e-52d21c0c7495 | -8.02533 | -43.12672 | 2025-11-29 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 185.2 |
| ae6b2376-567e-36a1-af7e-c2e62075e06b | -8.03754 | -43.14126 | 2025-11-29 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1034.6 |
| d8a25d1e-51ef-308e-b0e0-80c4faab7d72 | -7.46673 | -39.9734 | 2025-11-29 00:32:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 37.2 |
| 1858576d-d5e7-3927-b228-96d557a0b2b9 | -6.60227 | -43.68965 | 2025-11-29 00:32:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| eb73c549-bc4d-3450-84dc-889f9068d4a0 | -8.0508 | -43.13904 | 2025-11-29 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 167.8 |
| 7a0f6a20-e712-3868-b9ec-75667b8d4d6a | -7.45009 | -44.75293 | 2025-11-29 00:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| a2172d1b-9c25-3956-b22f-3805f07c6665 | -11.95576 | -48.71989 | 2025-11-29 00:32:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 266b9631-dc0b-3bed-82d3-aa55baa00dd2 | -9.87591 | -47.45498 | 2025-11-29 00:32:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e208e669-0ae5-3ade-9ad7-dad0d7d803da | -4.04963 | -49.49803 | 2025-11-29 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README5.md)
