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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b50ceb2-4618-389d-b803-4c41463afb2c | -10.90822 | -46.34437 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e6abbbd7-4ec0-3411-aeef-f1b04229deb8 | -10.9077 | -46.3485 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59432d1d-a7f3-3dcb-bdc8-40ae3d52cebd | -10.90719 | -46.35268 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 820ef45f-064b-38be-b4e9-2701a084b536 | -10.90247 | -46.34333 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1893eb32-35b0-35f5-8dbf-0e0a1c4783f6 | -10.7774 | -46.53783 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc37f433-f884-32b7-9f82-a7b06c90d319 | -10.77684 | -46.54233 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 104bfb55-2c7a-3b78-bdc4-d4aa0df9daa2 | -10.77166 | -46.53744 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0869378-3423-3955-a4e8-31e01a28d9cc | -10.49963 | -46.30502 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b47426f-b2f8-3ed2-bcfc-c3a9a4ee92d0 | -10.49917 | -46.30894 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 023f4c4f-e33e-3f97-b9d9-5ddc81a7e675 | -10.49841 | -46.30738 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a258ddc5-29c1-3edf-aacd-bedf15286cfe | -10.49314 | -46.30275 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b204ed3-f306-3ec3-bbd1-9be9602157a4 | -10.93051 | -47.29397 | 2024-10-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87d5205e-92dd-324f-8e2e-898d894da9a4 | -10.92859 | -47.29367 | 2024-10-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9041a0b8-efaa-31f7-b792-2a32dbfa55a0 | -11.86606 | -47.12473 | 2024-10-01 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 295ac938-5612-34c6-bea8-60ec89391ee4 | -11.8656 | -47.12845 | 2024-10-01 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6eade070-8c94-35fa-83bb-000c09d60044 | -11.76885 | -47.60259 | 2024-10-01 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff3194c8-8136-3dd2-ac26-0fbc7fa8d69d | -11.44394 | -46.94995 | 2024-10-01 05:06:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec799964-77e3-3346-a6a8-7d9165a33fa9 | -11.44346 | -46.95383 | 2024-10-01 05:06:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c2cc0ac-d870-3d4e-9ad7-ffd2732e7da9 | -11.43777 | -46.95391 | 2024-10-01 05:06:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c26728a-dced-3278-b2a8-424c2f426c1b | -11.4373 | -46.95779 | 2024-10-01 05:06:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55e61fa7-7c45-3fa7-861e-ebbdd579a233 | -11.31163 | -46.85005 | 2024-10-01 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bc9e8cb-5fe0-3007-9fa9-408ac55e337b | -11.30957 | -46.84976 | 2024-10-01 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 209ffdbf-9cdc-3bf1-a598-826588293374 | -11.30603 | -46.84915 | 2024-10-01 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8223906f-95de-3ea3-b5df-326377af69df | -11.01009 | -46.48809 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60b35aaa-6ca7-3e9b-86f2-70086527f1a6 | -11.0097 | -46.49142 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fa72232-fcf0-3463-8bd2-9481e40f41da | -11.00916 | -46.48187 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a3205bd-8630-3039-ae53-d1f40bc116f5 | -11.00875 | -46.48512 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0b067d31-7f0a-32ab-b179-3deeb401815d | -11.00833 | -46.48842 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| da034eb3-dd97-31b9-baf2-997a0aea2351 | -11.0079 | -46.49185 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b0448cd1-7791-39a0-a196-ffb5d925a882 | -11.00393 | -46.47702 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9bf78f9e-f26c-3cdd-8705-2e934c656dd2 | -11.00353 | -46.48026 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a2de6cb2-14a4-3037-b8c9-b40987b0f5cf | -11.00312 | -46.48348 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d29ff713-f28f-377f-9b0a-9b6a68167617 | -11.00271 | -46.48676 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 75ae1852-d67e-3105-853c-16c49d5771ed | -11.00226 | -46.49041 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 06cce36d-75cd-39b0-ab87-32bddf9bfe30 | -11.00177 | -46.4943 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3b2e6ee5-0003-3ff2-9b22-80fd052aa1f9 | -11.00128 | -46.49823 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4a24a3b5-35ab-32db-819d-d956b02f81d8 | -10.99862 | -46.47286 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4e50fe67-a78e-3388-af37-ef3f4971b40e | -10.99822 | -46.47605 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b36486cb-301f-31ac-bc01-8a03d18c6d9b | -10.99782 | -46.47924 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f1c9485d-24e5-3aa0-bb3f-c19ce50106ee | -10.99741 | -46.48254 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 407556eb-0e59-3e8e-a3e1-752ff7f1d5e7 | -10.99724 | -46.53064 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4cdbe69d-129a-3c0e-b264-a892f7fa7dd6 | -10.99674 | -46.53463 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f951a30d-c1bf-33f7-9e45-52621b750e2d | -10.99605 | -46.49346 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9407396f-801f-38aa-8d75-608fb162ccd0 | -10.99556 | -46.49741 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8eb66ece-14df-3594-af3f-e5f7d6f1381a | -10.99507 | -46.50137 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 426d7c8f-a2ad-3fa6-9d2b-4b16476cd713 | -10.99408 | -46.50935 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| aaed1168-7945-36af-b3e7-921e26dfea2b | -10.99357 | -46.51341 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60c83d2b-dbd1-3b47-9622-ead3ac079980 | -10.99306 | -46.51755 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3f0263b-93cb-3c15-89d0-c241bf91d5ca | -10.99204 | -46.52575 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 845eb2bf-4fa1-3af2-a31d-6c00c8ffae00 | -10.99154 | -46.5298 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 838e0d7a-2e34-39c9-a476-92f72a4a2ed6 | -10.99104 | -46.53373 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8cdd2e30-b8be-3a9c-81ce-a47667a9d567 | -10.99056 | -46.53765 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 81616001-cb41-38d5-a981-cc454a581431 | -10.98486 | -46.53675 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49ffcc83-1462-3fa7-890f-a64d6c7d6766 | -13.53906 | -47.58154 | 2024-10-01 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b841b90-438e-3159-b093-efcacb994586 | -13.53442 | -47.57348 | 2024-10-01 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0040b3c5-483c-3507-9943-066f7a9510b1 | -13.534 | -47.57701 | 2024-10-01 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1d1aee9-e46b-389a-9419-092dd0565570 | -13.13202 | -46.77277 | 2024-10-01 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6aa29c7-c0ba-3f4e-979a-44e3db38d7b9 | -13.12691 | -46.77292 | 2024-10-01 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fd0003e-1011-3b8b-b060-5df74a5fa53f | -13.12644 | -46.77706 | 2024-10-01 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76f1930b-e59d-34df-a734-c69a06eefcb1 | -13.12598 | -46.78112 | 2024-10-01 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac72b67c-618e-3821-8970-b80aa17a483a | -13.12574 | -46.77622 | 2024-10-01 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce58955d-5438-3870-b634-5fc9452ec329 | -13.12526 | -46.78028 | 2024-10-01 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e3763c2-1e03-3dd9-8032-1e72e250cbd6 | -13.12112 | -46.77223 | 2024-10-01 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 571ff99b-1eb2-3c72-b783-f1581aa146de | -13.12044 | -46.77144 | 2024-10-01 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2678b7d-2222-34c7-86fb-bf3f02aa46c8 | -12.47709 | -47.49775 | 2024-10-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a9cde40-a76f-3b2d-8f5e-721c9de7fbcc | -14.78191 | -48.07584 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8be0e47-101a-3544-a2ee-eca9f14bcbb0 | -14.77856 | -48.07239 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9eae3fa-44a0-333f-8990-59fc44db47c3 | -14.77818 | -48.07573 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 809d90d5-88ab-353b-97ed-ac60fe0e3430 | -14.77782 | -48.07896 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 100786c8-0ff8-3ee9-b0e8-5189d7e3fff7 | -14.77749 | -48.08196 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39fbd114-554f-3e2c-aa90-141aebc761ef | -14.77691 | -48.07154 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc53d898-e24a-3e47-8557-cad8458f0cd0 | -14.77652 | -48.07488 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3eb6fee5-48df-370d-a76e-a4e344aa3e68 | -14.77577 | -48.08116 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a7ba2c64-86b5-3621-86cc-03a84b166a98 | -14.77319 | -48.07113 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ffb2c50-0d27-34ae-9b47-fc4b271d2878 | -14.77282 | -48.07442 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0dd6643-5c3a-3244-9acf-bb27cc91e689 | -14.77246 | -48.07764 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c998b9b1-5288-3065-ab71-984761e33f3b | -14.77116 | -48.07357 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b56c66e-da0d-3e5b-9903-256ce3c1c0e7 | -14.77078 | -48.07678 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 202e1309-e310-3d5f-be7e-32444bd8d11e | -14.7697 | -48.08601 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3aecb1e7-620e-32e5-86ae-4d73fb7f558a | -14.76639 | -48.0827 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d90e46f2-be02-37ff-a3e8-69fffae6b6f3 | -14.76605 | -48.0858 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 422c16db-276e-3980-8d66-6c2ac0663b08 | -14.76467 | -48.08194 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4b6b3be-bc45-3e1b-900f-b046c6884d17 | -14.7643 | -48.08507 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f18dab73-aca6-35e5-9829-7da041f599f4 | -14.75893 | -48.08394 | 2024-10-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 181068c7-0a36-3f30-bfd4-c40681b019aa | -13.74691 | -48.15423 | 2024-10-01 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bc02f28-bb58-3093-ac5f-317fc7ff17b8 | -13.7465 | -48.15763 | 2024-10-01 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f07e3cb0-df6a-3186-a731-3d9587a7c423 | -13.7417 | -48.1525 | 2024-10-01 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37ecc6b0-b839-37a3-86dc-73afd707ffdb | -15.33001 | -47.54609 | 2024-10-01 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bd4858f-da04-38c9-a7a5-779fc879bec1 | -15.32961 | -47.54971 | 2024-10-01 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c02715fa-f528-3da0-b750-258c3a24d2b3 | -15.32753 | -47.56836 | 2024-10-01 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c5c5652-3752-3834-b07a-91dabe84a474 | -15.28428 | -47.49147 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9044b2c3-f186-3013-93e3-c9eaad71b6f5 | -15.28378 | -47.49608 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b4efd84-055a-343d-bba7-4fb1f61c257b | -15.28336 | -47.50006 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e74c35d5-9a4a-36a2-ac07-c71d17b2e404 | -15.28293 | -47.50399 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 91757334-b6ba-3d4c-a4a1-b57aafaf70b9 | -15.28249 | -47.50816 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e65b1073-9963-3134-95b9-9de3f70389dd | -15.28153 | -47.49241 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7732d141-f86b-321e-9b47-ff214d29426d | -15.28105 | -47.49656 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 416de084-a200-3549-9218-affcba4e42cb | -15.28059 | -47.50057 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d351c5ac-5b10-33f5-8019-f77cfbcaf680 | -15.28011 | -47.50472 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8cd74fd5-cbf4-371c-8c2c-067cad5e8a9c | -9.21 | -48.65932 | 2024-10-01 05:06:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README106.md)
