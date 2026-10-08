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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3e41435-b9b1-3e3a-925b-781dd90a8460 | -8.53317 | -66.98 | 2026-10-08 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 300d9a62-e9d0-3a3e-aae9-aad28e5c4f0a | -8.53448 | -66.97404 | 2026-10-08 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 2b770acc-2c61-35ad-ada1-899d6f10d2aa | -9.05002 | -65.91936 | 2026-10-08 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 1868e60f-b46f-3fef-8ff8-772f48081ae0 | -4.3471 | -43.8021 | 2026-10-08 01:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 33261bce-cec8-350d-a20d-047066866618 | -3.5861 | -54.6741 | 2026-10-08 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 832c9a1c-d0db-3230-83e8-0add5428bd18 | -3.1298 | -53.7834 | 2026-10-08 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 93f9cf14-5151-34ce-a21a-d798a94e7432 | -9.4749 | -64.3713 | 2026-10-08 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f4375f18-54fd-3190-8936-e9c5bb37e60d | -2.5903 | -56.1642 | 2026-10-08 01:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| f0577afe-4576-35bd-89b0-f60e8bbe0388 | -3.586 | -54.6941 | 2026-10-08 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 842e8151-d005-3222-9b3f-867e14bd41db | -2.3849 | -57.885 | 2026-10-08 01:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d1c41643-5128-35a1-9be2-43d622e51dcf | -3.1601 | -50.6021 | 2026-10-08 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| ac75e3c1-5fa5-3c43-a72e-0d38e28ce678 | -6.2527 | -52.8675 | 2026-10-08 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| c96fc199-f8ce-37d6-bc56-24676c06ecb7 | -2.9449 | -54.1099 | 2026-10-08 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 4625a4fe-759e-362f-a6ff-c79ad4680453 | -3.478 | -59.597 | 2026-10-08 01:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 0fe0094f-6053-3ef7-ac17-652b1ceb9464 | -8.0895 | -55.311 | 2026-10-08 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0ff7fb8f-4fdb-3bee-8bc1-e1db83e5f422 | -2.3848 | -57.9044 | 2026-10-08 01:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 7ef83c00-f48f-3c46-abca-2f829c76ff5c | -3.0373 | -53.9469 | 2026-10-08 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 88809654-cbc7-3912-98f9-881563f0fffc | -2.4988 | -56.1462 | 2026-10-08 01:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 615f7642-bc5c-37d5-b860-c13ae7157ecf | -3.1284 | -54.1857 | 2026-10-08 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| e18b7585-1526-312c-bcf1-7f64bab0763c | -3.5515 | -59.4807 | 2026-10-08 01:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 44af451c-8a4a-337a-b20e-8c65891b7158 | -3.1697 | -58.6437 | 2026-10-08 01:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| cbe70439-30d9-3c4b-949e-dc54e44a8cb8 | -6.2529 | -52.847 | 2026-10-08 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 96c276ec-954f-37e0-a9b2-9dfe19968ce2 | -3.0374 | -53.9268 | 2026-10-08 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 15477085-e38b-30e9-890d-4ea6d765a4d2 | -2.4805 | -56.1269 | 2026-10-08 01:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 661d2714-12c2-3d3e-a0a8-d09203adf44e | -3.6045 | -54.6736 | 2026-10-08 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 1dd37843-6c93-370b-8a55-08f0dcf160b1 | -9.4936 | -64.3518 | 2026-10-08 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 99279f29-7e52-3260-b8d3-b657aafca4e2 | -16.8642 | -40.5709 | 2026-10-08 01:40:00 | GOES-19 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| 23d25d19-de43-30af-9e65-2fcc1cf79d23 | -3.8383 | -55.9774 | 2026-10-08 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 8bc821dd-2a9c-36bc-96de-b4ab2515d403 | -10.4151 | -47.2623 | 2026-10-08 01:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 7dbacdb8-1835-32bf-b67f-0aa55aa39822 | -3.1972 | -50.5592 | 2026-10-08 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| b314939c-be9b-3f36-bfb7-00e772c8e373 | -17.1213 | -41.3421 | 2026-10-08 01:40:00 | GOES-19 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| 25214e88-6336-3235-9ec1-8cc0a6b8ad86 | -5.7376 | -45.1533 | 2026-10-08 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 423bb931-8a23-3bab-afe2-7f29279d596f | -10.434 | -47.2601 | 2026-10-08 01:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 3e0c20ec-824d-34ff-8c5d-d3b0f38a7ed6 | -2.4987 | -56.1659 | 2026-10-08 01:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 79b47c79-705a-364d-a25c-c2485ba27588 | -5.6931 | -53.5073 | 2026-10-08 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 7b9ea3c0-d540-3dea-8bda-4a410f28d3a5 | -2.798 | -54.0933 | 2026-10-08 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c688082c-0ccf-3853-874f-38baeaf2dd51 | -2.9447 | -54.1702 | 2026-10-08 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 97b25e3b-6bbe-3954-8a2b-4af1f1a3afa7 | -3.1101 | -54.1661 | 2026-10-08 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 04b61f0f-72e2-3f64-8053-5549accbeb63 | -8.7225 | -45.204 | 2026-10-08 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| bbe86226-71c8-35b5-a79d-6c88dce13bf0 | -3.5698 | -59.4803 | 2026-10-08 01:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 601a174b-f6bf-30fa-b546-c93a00020376 | -3.11 | -54.1862 | 2026-10-08 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| b9da4964-cbf5-375c-a54f-d2f05d272cad | -6.8764 | -43.685 | 2026-10-08 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| eafe0e9a-3f8b-3d93-8e88-ff0402fd8c45 | -2.7612 | -54.1142 | 2026-10-08 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| c947e09f-f29d-3ef9-8deb-5b5281ed98d7 | -10.4147 | -47.2846 | 2026-10-08 01:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 14bc9b9d-c50e-3cbb-aa15-99c045b977b6 | -3.2499 | -46.9589 | 2026-10-08 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 10241182-e7bc-36ed-92b1-e1d671374bf5 | -3.1115 | -53.7637 | 2026-10-08 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e0358e2c-1b19-3f0f-917f-45860f4e35b0 | -2.9449 | -54.13 | 2026-10-08 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| bce838f4-0855-3fc4-be67-908f31976a01 | -3.1114 | -53.7839 | 2026-10-08 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 26d5d69c-c514-3fd2-9a2b-99164de42a21 | -3.1879 | -58.6433 | 2026-10-08 01:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| ad544f04-8846-38c5-acc7-ee737521d322 | -2.4032 | -57.8848 | 2026-10-08 01:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 651bc24d-7a05-32a7-9729-daa7a786057d | -3.0913 | -54.287 | 2026-10-08 01:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 67df75b0-f168-3e79-9921-ef05dacd4b13 | -9.475 | -64.3525 | 2026-10-08 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 88.3 |
| e796326a-76b6-3f53-9c68-b978c2437ff4 | -8.7228 | -45.1812 | 2026-10-08 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 232.0 |
| d6af29a7-1d0d-3edb-8b21-77f80ae3f86d | -4.4507 | -47.9112 | 2026-10-08 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 88f5866d-0609-334b-87b0-19523e4b26f0 | -10.4337 | -47.2824 | 2026-10-08 01:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a8ad66be-a158-37bf-9c83-995d58b34856 | -3.478 | -59.5779 | 2026-10-08 01:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fa24dd1e-c7ee-3841-b486-abe0560e05ef | -6.2342 | -52.8685 | 2026-10-08 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 219e8f60-eb92-3583-99e9-2a4e467290d9 | -8.7231 | -45.1583 | 2026-10-08 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 244.6 |
| 5f5550f0-3324-3490-b599-e2e9d4816136 | -3.5493 | -54.6752 | 2026-10-08 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| e0e26e4b-e81b-3da7-b7a0-333015bb5e26 | -4.2954 | -49.0807 | 2026-10-08 01:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 4527f490-12b6-3119-ad82-f9e9cb65fef1 | -2.4805 | -56.1072 | 2026-10-08 01:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e1fcd51a-c927-3cb8-b059-8c2a4ffa67f5 | -2.7797 | -54.0736 | 2026-10-08 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| a397c0dc-234e-301c-a320-98677e392e32 | -5.7117 | -53.4862 | 2026-10-08 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 167.8 |
| 0e41a189-3bfa-3839-ad37-efff60c744c1 | -3.2157 | -50.5586 | 2026-10-08 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 656ba6de-6d17-3724-8564-153f2e4780e3 | -8.7039 | -45.1832 | 2026-10-08 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| d96242bd-20e7-3eba-8f45-f8d387fb0eaf | -4.1551 | -54.9165 | 2026-10-08 01:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 727aea9d-b30a-392f-b5e4-0ed22cc72815 | -2.4988 | -56.1266 | 2026-10-08 01:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 0bda6c6b-0e40-377c-bd60-4bc1678ff20a | -3.0914 | -54.2669 | 2026-10-08 01:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 9313f5c9-0bc1-336c-bbf7-fda2f16a0a6c | -8.7417 | -45.1791 | 2026-10-08 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 31e488d1-1692-355e-b283-943daf756597 | 1.6937 | -55.6263 | 2026-10-08 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e20da9c3-7419-3290-b51e-834e89124462 | -2.572 | -56.1646 | 2026-10-08 01:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| d549f493-cd6c-3f51-bfaf-10621a50f7ea | -2.572 | -56.1842 | 2026-10-08 01:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| c7091a0e-daba-3e44-bdd0-adfd7c862530 | -4.4506 | -47.9329 | 2026-10-08 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| a9394ff1-54b7-3427-8d39-0effd648e2cf | -3.8627 | -50.4106 | 2026-10-08 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 6c96e731-dea9-3cd0-9d66-ea0a6677d7e8 | -3.5677 | -54.6746 | 2026-10-08 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| e497b439-1b8b-3772-b58f-44e91a150bda | -11.3937 | -46.6922 | 2026-10-08 01:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b66d889d-17ba-3d02-a5fe-d3ac64730c94 | -2.7796 | -54.0937 | 2026-10-08 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 615949c8-c9d6-3287-805c-7531bb3fda1d | -3.1285 | -54.1657 | 2026-10-08 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 3b8166a1-e35f-3ef2-9b16-5ee74745be9f | -2.517 | -56.1656 | 2026-10-08 01:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f7f4ae25-6ccd-3a07-90a4-7f35bf0a2fa9 | -2.9448 | -54.1501 | 2026-10-08 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 6165d43a-576c-3973-9748-f6f374cde2ba | -3.073 | -54.2874 | 2026-10-08 01:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| abe20fb1-254a-3f8a-a260-989c6b19fba8 | -3.1097 | -54.2865 | 2026-10-08 01:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| d4a85922-ef08-3aa4-af20-08cb83e1a7e5 | -9.0592 | -65.9209 | 2026-10-08 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 75c37b8c-7424-377b-8386-3d516b7456c6 | -7.0065 | -59.1223 | 2026-10-08 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| b6e55979-cbed-33bc-9a4e-d82c7393a986 | -2.7613 | -54.0941 | 2026-10-08 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| dc2b357b-7e9e-3eb7-acec-ab1cde5967c1 | -2.8575 | -59.1107 | 2026-10-08 01:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 4ba66438-4daf-37a6-bf33-082c90ea97b5 | -6.2343 | -52.848 | 2026-10-08 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 24693f1c-080a-3367-8295-d558c7754796 | -5.7116 | -53.5065 | 2026-10-08 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 86f08981-423d-33cc-9600-44645bdd6db8 | -8.742 | -45.1563 | 2026-10-08 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 215.0 |
| e83cc930-2809-38ad-8914-48c76700ebf7 | -3.0558 | -53.9263 | 2026-10-08 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 206d2fae-c5fd-3621-97ca-fabb93dad6d0 | -2.7981 | -54.0732 | 2026-10-08 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| f30b9127-1d7e-3ff3-82f2-dbe93fe84e1c | -2.4031 | -57.9041 | 2026-10-08 01:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 841b33d3-4d31-36a5-ab6f-3b5440fe6322 | -3.5862 | -54.6541 | 2026-10-08 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 1402922c-ee81-3658-bf73-e6510ec37253 | -2.9265 | -54.1305 | 2026-10-08 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| bead81f8-bbaa-3bed-8297-fcc603771d7d | -5.6932 | -53.487 | 2026-10-08 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 177.5 |
| 3188edd1-0f86-3ed3-b0e1-e4960af17b58 | -2.9449 | -54.1099 | 2026-10-08 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 93e86d21-f611-3173-90a5-c07c2b7c7050 | -9.0592 | -65.9209 | 2026-10-08 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c260bc16-6abf-3902-b2c6-afe9221c48ff | -10.4147 | -47.2846 | 2026-10-08 01:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| b52a2766-df4f-370a-9be4-581c319be5f9 | -5.9587 | -55.3448 | 2026-10-08 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 72a582f0-8584-3d9a-9dd9-193b3b3003b8 | -3.1298 | -53.7834 | 2026-10-08 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |


[Clique aqui para ver as próximas entradas](README48.md)
