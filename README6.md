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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93e13de5-f82a-3344-9972-21841f8cddf2 | -11.5072 | -46.7446 | 2025-10-04 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 200.5 |
| 7c6bcf52-7aab-3036-be14-620dd5b5c592 | -4.4446 | -43.2164 | 2025-10-04 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| c79f2b9c-5ab9-37e3-a50e-50585df319f4 | -11.9339 | -46.3699 | 2025-10-04 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| d2da6c14-0d2f-3572-8f70-9eb502c8f5ee | -13.3225 | -48.1216 | 2025-10-04 01:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 12622a20-3c2f-3e95-bf0e-40db0cf12720 | -12.0502 | -45.2103 | 2025-10-04 01:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| bcf4a394-a5a8-30eb-8224-75e9bc406b8b | -11.9143 | -46.3953 | 2025-10-04 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c6a7f430-6e33-323a-a805-2d8f8d651d7e | -11.9151 | -46.3499 | 2025-10-04 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e121ec7e-4ab4-387a-a01f-0bc2495aecb2 | -10.3154 | -50.3421 | 2025-10-04 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9487c280-ecce-3743-876c-3efe4dcc91b8 | -3.8572 | -41.5719 | 2025-10-04 01:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 5a42cf97-1f4d-32cc-af98-daf5c7f2be39 | -5.3849 | -47.2271 | 2025-10-04 01:40:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 41939f94-8074-3649-a97e-04a23c2ed87b | -16.0212 | -50.9425 | 2025-10-04 01:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| cd196bb0-3fd5-3e8c-a25b-6676ab6f5c8f | -4.4443 | -43.263 | 2025-10-04 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 37a9ac74-4951-3db9-b90a-4546e5f9545e | -4.4845 | -42.8631 | 2025-10-04 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| d562425f-e339-3908-9448-67ad0604fdba | -12.0314 | -45.1901 | 2025-10-04 01:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e796c46f-29b7-33ae-99c3-f75155d7db50 | -11.5069 | -46.7671 | 2025-10-04 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 71f53955-5be0-3872-844b-f48135037996 | -11.4877 | -46.7696 | 2025-10-04 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| ede8339f-c432-3ee8-991f-fe8d8cc5c22e | -5.3851 | -47.2052 | 2025-10-04 01:40:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 345d49f2-000a-33fc-af6b-e75c9b86aad7 | -8.6322 | -54.9949 | 2025-10-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e68318f3-6bfc-309e-843a-3871f47f1eed | -4.954 | -45.0694 | 2025-10-04 01:40:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 177.2 |
| d3a1c6a3-8fc2-334b-aa4f-066315057ce6 | -4.6133 | -43.1594 | 2025-10-04 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 165.0 |
| e59d5f43-f716-3fe5-8a7a-18a9b6f2fc2c | -4.6135 | -43.1361 | 2025-10-04 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 2bc6d1c7-caaa-300a-8ba5-573be4d7214f | -11.5264 | -46.742 | 2025-10-04 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 152ac2bc-d18b-3567-90f0-9b7eac6cc07c | -4.9726 | -45.0683 | 2025-10-04 01:40:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 4cc9d4e9-70fb-38f8-8c82-a92f42d1ede0 | -5.1965 | -45.0768 | 2025-10-04 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 93aa1924-2f4f-33ca-a4dd-189977fd9dc7 | -13.3426 | -48.0742 | 2025-10-04 01:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| c1a9d24a-3a54-3881-93f1-8eb374e06572 | -5.1967 | -45.0541 | 2025-10-04 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 71932695-a853-388b-b4a0-90e21034ac44 | -9.3464 | -54.5201 | 2025-10-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| e6a1dc1e-a462-3f2f-b29a-a8cb5a4c9dbb | -4.6135 | -43.1361 | 2025-10-04 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| f2c02f4b-9d12-307c-99d3-33cf0ad5cc5e | -8.6322 | -54.9949 | 2025-10-04 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 1898771e-e9ed-3cd6-971e-5b2a49c0ea03 | -11.9151 | -46.3499 | 2025-10-04 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 550b3f27-22ff-35ac-92d5-e8191f20142d | -4.954 | -45.0694 | 2025-10-04 01:50:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 2b5acdcb-4357-33cc-b25f-31955b69cf1f | -11.9147 | -46.3726 | 2025-10-04 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 0c0357b5-3c1f-3fe8-b51a-975661e3547f | -5.1967 | -45.0541 | 2025-10-04 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 5a91da5d-6e14-33ec-9811-54443a46e323 | -9.3464 | -54.5201 | 2025-10-04 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 1f37126d-8a78-3bf5-93fe-b959d4d01c33 | -6.8774 | -47.2334 | 2025-10-04 01:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 3e064c1e-d059-3d78-b6e2-976734c4dd87 | -13.3225 | -48.1216 | 2025-10-04 01:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 2374ffe9-527b-357e-9339-68ccec6d5e99 | -20.4082 | -44.134 | 2025-10-04 01:50:00 | GOES-19 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.3 |
| 16147f40-cb4a-3f20-92e3-22f259cf2246 | -4.9726 | -45.0683 | 2025-10-04 01:50:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| d96a9f7d-f8d3-3a92-802e-26ffd5f4ba6e | -10.3154 | -50.3421 | 2025-10-04 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| cbdd9d98-4d0f-3272-a54f-4e254a8b77e3 | -16.0212 | -50.9425 | 2025-10-04 01:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 5daf45dd-31ce-3e13-8c1c-82db752e596c | -4.6133 | -43.1594 | 2025-10-04 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 162.7 |
| bab4dac7-57b8-3696-af50-aeaf1632a5db | -5.1965 | -45.0768 | 2025-10-04 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 27828021-0b45-3151-878a-8ce49af5db4a | -4.4443 | -43.263 | 2025-10-04 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 4192dcd3-ff42-3dda-80dc-0a60d77f5b03 | -20.4288 | -44.1284 | 2025-10-04 01:50:00 | GOES-19 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| eaefefb5-ab64-3937-bbcd-0a07025ca626 | -10.3346 | -50.3188 | 2025-10-04 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f5fc34a8-66b5-34e0-8389-3a9d4a1ac31b | -11.9339 | -46.3699 | 2025-10-04 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 3112fc00-b2f5-3661-8a48-724b8ba3046b | -9.3276 | -54.5215 | 2025-10-04 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| a5ae6caa-e472-38b9-9eef-1e5c32e974a4 | -5.3851 | -47.2052 | 2025-10-04 01:50:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 2efc06c9-7d52-39c1-8ee4-9b4cc0603f1e | -4.4632 | -43.2386 | 2025-10-04 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 40f6f62b-840e-3bb3-91b5-a2fbe07fb0f2 | -4.4445 | -43.2397 | 2025-10-04 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 353.3 |
| 61e07db7-84b5-3663-b701-4674e25897eb | -4.4446 | -43.2164 | 2025-10-04 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 10d9b185-7a6a-3559-a4ba-9565d221ae1b | -4.4845 | -42.8631 | 2025-10-04 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 077689c3-96e6-3782-8eae-282179739a47 | -4.4258 | -43.2408 | 2025-10-04 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 9b318629-5d18-3da7-ba8d-d67922519261 | -2.9013 | -50.7351 | 2025-10-04 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 961e7746-f7a5-39f3-a1ad-b3beead97846 | -4.4445 | -43.2397 | 2025-10-04 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 409.3 |
| c04e29bd-4347-3323-8407-9880786b366b | -15.0872 | -49.8865 | 2025-10-04 02:00:00 | GOES-19 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 05974d54-0b25-3e69-8d02-77d2d14e80d7 | -9.3464 | -54.5201 | 2025-10-04 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 30e0b101-2122-3587-9aeb-1666e4a5520d | -4.4258 | -43.2408 | 2025-10-04 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 70cbf68d-185b-36a1-93c3-44b8ac7a530c | -6.8774 | -47.2334 | 2025-10-04 02:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4b118d1e-7067-37a2-aacb-16168555d68c | -12.0314 | -45.1901 | 2025-10-04 02:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 292.5 |
| 7873f85c-b2b6-3b7f-961c-8d2e05cfb30a | -3.8572 | -41.5719 | 2025-10-04 02:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 51.7 |
| e83e3183-7910-3b04-8ce0-536f00173ef2 | -11.9147 | -46.3726 | 2025-10-04 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 161.7 |
| b5230156-4c56-3bd9-99dc-a25f0755a3c3 | -12.0502 | -45.2103 | 2025-10-04 02:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 367.1 |
| 9cfce365-23ac-3a12-83e6-8b169141d64a | -16.0212 | -50.9425 | 2025-10-04 02:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 6dd74d25-dbdf-3168-ba46-ab21e4e25078 | -9.9172 | -50.5094 | 2025-10-04 02:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f11696db-c0e0-3335-8665-bb654fb8831e | -10.3346 | -50.3188 | 2025-10-04 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 117ac750-e695-32a7-9345-cd7d0bb93f35 | -4.4446 | -43.2164 | 2025-10-04 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4667a3d3-0deb-38e1-a56e-55482f1399a7 | -9.3276 | -54.5215 | 2025-10-04 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 2d42cce8-a848-3e16-86bc-725b5c3492f7 | -5.1965 | -45.0768 | 2025-10-04 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 3f25420a-9070-3665-a811-47ccb18c776c | -11.9143 | -46.3953 | 2025-10-04 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 34bd7506-f62a-38d0-882e-a50f2f144785 | -4.6133 | -43.1594 | 2025-10-04 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 92b45ce7-ba38-3a5b-9ffc-f4c21ddb7a61 | -4.9726 | -45.0683 | 2025-10-04 02:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 4e6fd552-4884-347c-bc63-6ebe19783563 | -11.9151 | -46.3499 | 2025-10-04 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1778b553-9a1f-343a-b3bf-06fc479c0180 | -3.8384 | -41.5729 | 2025-10-04 02:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 53.7 |
| e5ec3e59-9bed-3117-8f89-4dbf08e36dde | -11.9339 | -46.3699 | 2025-10-04 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 90c27a09-c982-3eac-8c9c-a95670724d12 | -5.1967 | -45.0541 | 2025-10-04 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 38a5e4a0-f118-3216-821c-438087aaca5b | -12.031 | -45.2132 | 2025-10-04 02:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 218.2 |
| ec64603b-f9ee-3e38-961e-9e0747915bf0 | -4.6135 | -43.1361 | 2025-10-04 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 9128bf62-0c18-34f4-a3b4-e8b20af4eae4 | -12.0507 | -45.1872 | 2025-10-04 02:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 483.4 |
| 0b0a6954-57e4-3bb6-a1d7-4cabdc129278 | -4.4443 | -43.263 | 2025-10-04 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 67552638-e070-3f4a-9740-5858b956ace8 | -15.0868 | -49.9085 | 2025-10-04 02:00:00 | GOES-19 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 149.7 |
| a2411524-a527-315c-bb6f-679f89473e6c | -4.954 | -45.0694 | 2025-10-04 02:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 47226d95-666b-3c59-be2b-a49021f03b43 | -17.0903 | -46.2347 | 2025-10-04 02:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 5640d678-5dae-3c80-8b98-04ada487773b | -8.6322 | -54.9949 | 2025-10-04 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| c318264c-d747-3482-8754-854b1e33a439 | -13.3229 | -48.0993 | 2025-10-04 02:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 32074c53-85bb-3312-881a-8b9f1338cdde | -11.7924 | -46.8184 | 2025-10-04 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 728013d7-fffc-3d25-aa44-8d9acbac1300 | -15.6019 | -52.4888 | 2025-10-04 02:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| b04c477a-6046-3c74-96e9-9657360b638e | -4.4443 | -43.263 | 2025-10-04 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 303b6862-de67-3144-a775-c3e4fd18de17 | -4.4445 | -43.2397 | 2025-10-04 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 381.4 |
| 4df71882-0279-33d4-8a21-86b7f43c1ef2 | -12.031 | -45.2132 | 2025-10-04 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| e95db925-bc41-3094-aeb7-560994b65005 | -9.3572 | -45.7698 | 2025-10-04 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 5347b43b-6dad-3821-a2a1-14b7edcc4207 | -9.3569 | -45.7925 | 2025-10-04 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 7ef308ac-69dc-33b5-80d6-7ecae8901763 | -11.9147 | -46.3726 | 2025-10-04 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 269.1 |
| 4228ca67-ee34-3dd2-b30e-18bebed33b22 | -15.0374 | -49.4549 | 2025-10-04 02:10:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 5ef006a4-e014-3690-8e6f-c0310dc30c00 | -9.3464 | -54.5201 | 2025-10-04 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 4072df14-d0ac-3b46-a4ac-aea9ac7a81fe | -11.9339 | -46.3699 | 2025-10-04 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| bf310f62-c120-3c88-b981-b314e01eaa01 | -4.6135 | -43.1361 | 2025-10-04 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 474a126f-7605-304d-96f7-9bc1ccae0c53 | -4.6133 | -43.1594 | 2025-10-04 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 84835f78-6dab-3649-9e40-b37b12f2e4a5 | -9.9172 | -50.5094 | 2025-10-04 02:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| dba7791e-6a2b-34d5-8e5c-9d18ce5df6a1 | -12.0314 | -45.1901 | 2025-10-04 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |


[Clique aqui para ver as próximas entradas](README7.md)
