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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c82447a-98c2-3f0e-8645-aa1b43acd1c6 | -13.2934 | -47.6129 | 2025-10-04 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 52f5fee6-5a99-3855-b046-30c37aa20b4d | -14.8271 | -54.7719 | 2025-10-04 14:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 46e57887-a737-324b-b77d-887b4b7a486c | -8.9948 | -47.4845 | 2025-10-04 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3f95abe2-f94d-33dc-9779-f06eb4df922c | -12.3853 | -50.2595 | 2025-10-04 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 779.1 |
| 1c32de65-1965-36f1-84cc-fa9a3850e66b | -12.0887 | -45.2045 | 2025-10-04 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 225ef269-c329-312b-ba14-86c85854c738 | -6.6602 | -42.8153 | 2025-10-04 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 130.2 |
| 39fc0a20-361a-3bb3-9abe-2dc0d78be5a3 | -7.7938 | -42.5607 | 2025-10-04 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 150.6 |
| 5fedff86-4017-327d-81d8-842ab894f170 | -13.114 | -47.9518 | 2025-10-04 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| c1e85893-f584-3ab2-8c98-7e05aa7cc736 | -13.0959 | -47.8876 | 2025-10-04 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 6bc8b429-f18b-334b-a993-f0d32c5143a7 | -7.7684 | -46.2479 | 2025-10-04 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 34e8eb5d-4bb0-350c-b25e-cd025f0ad92d | -13.9387 | -48.1629 | 2025-10-04 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 87b6ae35-4cec-3518-8990-12fdda7d7e1a | -15.2835 | -52.9146 | 2025-10-04 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| efa50e8c-1286-336e-8c13-5797e5c6e054 | -13.4732 | -47.2714 | 2025-10-04 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 0bf857f4-7951-3000-84e8-000979d69a3b | -6.7167 | -42.8101 | 2025-10-04 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 192442b7-8300-3397-b4ae-a6da71e76418 | -8.1702 | -44.1377 | 2025-10-04 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 717ddb92-cf68-38f9-bf55-c768136d414a | -14.9548 | -46.8473 | 2025-10-04 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 33c93d57-ab55-373d-b715-954c938f7381 | -10.202 | -50.3536 | 2025-10-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 484aaac1-cc82-375b-93b4-7108552d7df8 | -12.4105 | -51.0917 | 2025-10-04 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 8c90d600-5466-39c9-afc1-fef4a7ff6e50 | -14.251 | -46.0991 | 2025-10-04 14:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 19454fe8-93b3-33fc-8c24-de9ccc28916a | -10.1456 | -50.3379 | 2025-10-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 50616a41-4baf-3707-9dc7-ece8bad8e1fd | -6.3673 | -43.8916 | 2025-10-04 14:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 293baa3d-33e2-3a88-8fc9-60cdb8aaa258 | -11.4486 | -43.504 | 2025-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.2 |
| dd620895-0a19-39cb-b2b1-2da7c6c95309 | -13.1585 | -50.9359 | 2025-10-04 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 0a445793-c6be-3170-ba0c-1bb26cedbd63 | -5.4742 | -43.1711 | 2025-10-04 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 513e9139-afa4-3087-b2cc-df1f486df5e5 | -7.7938 | -42.5607 | 2025-10-04 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 169.1 |
| e27df8f5-ece6-3d45-aa00-93e504d7c018 | -10.6339 | -49.1687 | 2025-10-04 14:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 194e54fb-44a8-3e83-8657-8c8dcc45ac22 | -8.8529 | -46.7897 | 2025-10-04 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| f0deb03c-f86a-3788-aa78-8cb04624a7de | -12.3853 | -50.2595 | 2025-10-04 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 211.2 |
| 8eb3b4a3-bfd8-3006-833b-8aca93b453e9 | -6.4366 | -44.4618 | 2025-10-04 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| fe869117-53de-3a90-a877-a94869f6bc80 | -7.0604 | -45.7946 | 2025-10-04 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 431.4 |
| 19254579-3707-3f67-8929-1f75b496b08b | -13.5119 | -47.2655 | 2025-10-04 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 3a30cbae-db2c-3583-a5b7-39c9efd412de | -8.8526 | -46.812 | 2025-10-04 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| b7eae776-ba21-3a4d-8f46-a0c41648e56a | -5.6843 | -42.7328 | 2025-10-04 14:30:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 144d0178-ac2d-3d0f-bd23-647ebc57cdd1 | -6.3673 | -43.8916 | 2025-10-04 14:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 37c9369c-3677-3fe3-b76e-6b4ea32640e5 | -8.6322 | -54.9949 | 2025-10-04 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| cd86bcde-1028-3034-ac4f-2971f72d2d46 | -11.9138 | -49.9289 | 2025-10-04 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| bda6326f-a73c-37f9-b444-792a2db261b9 | -14.8461 | -54.7903 | 2025-10-04 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| bc142f02-30fa-3fee-82fb-9c346ce99889 | -13.2934 | -47.6129 | 2025-10-04 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 0c33630d-d1a7-31d1-a4f5-123f3afafe33 | -11.2024 | -54.8567 | 2025-10-04 14:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d2e1eb7d-de34-3318-9577-0053125632f3 | -9.4229 | -47.9028 | 2025-10-04 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| a2494198-f3b5-307e-8352-97f4be9d7106 | -11.7924 | -46.8184 | 2025-10-04 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 29addf02-8531-341d-a3fd-6adfaa858702 | -5.7882 | -45.7809 | 2025-10-04 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 250c503f-dd8b-3922-8e40-d77a6e8c3195 | -6.0618 | -42.5133 | 2025-10-04 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 157.4 |
| a1a4fb93-5c9c-3581-a593-10e71af01aef | -8.8534 | -46.7451 | 2025-10-04 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| cfb27272-3a32-335e-8507-857b01e7ad5b | -5.4554 | -43.1725 | 2025-10-04 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 7b82eec2-d2ea-3ac9-80ee-4d9571c6deae | -10.5838 | -48.696 | 2025-10-04 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b426c316-e6bd-3979-b926-100554f278f6 | -11.9135 | -49.9505 | 2025-10-04 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| b14f9b26-47f9-3976-8a17-a3d08fe73d59 | -9.3196 | -45.7515 | 2025-10-04 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 649ec50a-67a9-306f-a49a-72450beafb92 | -8.1891 | -44.1357 | 2025-10-04 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| f6faba77-eabd-3f7c-aaf9-b9260ea6dfef | -15.5408 | -46.8344 | 2025-10-04 14:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 125.9 |
| c4777071-d102-3748-86c7-7e8cb80f9689 | -14.9881 | -49.9892 | 2025-10-04 14:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 0e8d5c39-7aee-34a8-93f4-f081791b7e74 | -6.1542 | -44.5989 | 2025-10-04 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| f2952223-f69e-38fd-81cc-390e93f12fa8 | -5.8258 | -45.7559 | 2025-10-04 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 7ab9f3ad-8c46-3c9d-936d-cbdf1839835d | -5.8256 | -45.7783 | 2025-10-04 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 16a8d42c-ca1d-353e-94ec-c9bf0ecc727c | -11.4298 | -43.4833 | 2025-10-04 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| eaff7296-05a7-3b45-b5c7-2967461d50b4 | -11.6314 | -45.0646 | 2025-10-04 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 7cf60dac-7a8c-3e26-94fd-dad6d229484f | -13.1959 | -50.9954 | 2025-10-04 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 205.5 |
| abcf4669-1dc9-35ec-b05d-79f40da95292 | -11.449 | -43.4803 | 2025-10-04 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.9 |
| b816728b-85df-33b5-9acb-9dab3039bfba | -13.6909 | -51.2315 | 2025-10-04 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 252.3 |
| 1a9b92cc-d9cd-37c4-816b-2567d15a3455 | -14.3899 | -45.9601 | 2025-10-04 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 29bda7a7-d7c2-391d-ab34-60c0e5d208ac | -14.9352 | -46.8507 | 2025-10-04 14:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4b33df30-6cc4-3018-aeb3-918de0c0d191 | -12.4105 | -51.0917 | 2025-10-04 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 39981111-4167-3440-b44f-4015b4f9eb8b | -7.4281 | -46.4793 | 2025-10-04 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 21f23def-79dc-309a-9f5b-4a65fd425f1e | -12.0887 | -45.2045 | 2025-10-04 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 350768dd-2e25-36b2-8159-329a32fbbfa3 | -3.7481 | -41.048 | 2025-10-04 14:30:00 | GOES-19 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 120.4 |
| b41a2c52-4efa-3e2a-bd15-a1db4beee592 | -6.0616 | -42.537 | 2025-10-04 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 32e88bab-ff53-3a51-9dbe-3bb01403f66e | -10.297 | -50.3013 | 2025-10-04 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| e5be1e57-4dce-3e01-a2be-cf433d2e2f1e | -12.8265 | -46.8509 | 2025-10-04 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 9120bda4-a234-38db-993e-959df99c29df | -6.7167 | -42.8101 | 2025-10-04 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| 200026e7-8245-3498-85b1-d3cd87da08ae | -14.7521 | -54.6357 | 2025-10-04 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6896cab4-c28c-3930-bfeb-30a690b88458 | -14.3904 | -45.9369 | 2025-10-04 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 0b312c46-f40d-3e4e-a993-8d3a54a5b84c | -6.2408 | -45.3424 | 2025-10-04 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| f35e5a71-507a-3350-8f5e-71e14b6b76f0 | -12.0891 | -45.1814 | 2025-10-04 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 157.2 |
| efb26ca2-7c2d-3674-b761-bd9c82849494 | -7.8593 | -48.2037 | 2025-10-04 14:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 2ef221b7-d917-3915-bb06-2c907ee383eb | -11.4486 | -43.504 | 2025-10-04 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 291.8 |
| 1d5b02cd-7322-3c4d-862c-251bad0bf6b3 | -7.7684 | -46.2479 | 2025-10-04 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 155e4bf3-59bb-3144-be2d-9e64a1eb9c06 | -14.8271 | -54.7719 | 2025-10-04 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| dc215d5b-8bed-3df8-bfda-8560c6c55744 | -8.1705 | -47.2112 | 2025-10-04 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e3cf2250-31a8-3a87-b1f0-c8e21193dd79 | -13.3229 | -48.0993 | 2025-10-04 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 6ee258b3-b7d1-301f-b00d-d19b7b319705 | -7.0369 | -42.78 | 2025-10-04 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 290.1 |
| 3b8e3f76-3638-3460-a2ea-d71c4535107b | -7.7489 | -46.3168 | 2025-10-04 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 4b8fe37e-8a9d-3c59-9245-175591a4e2c8 | -5.8739 | -42.5289 | 2025-10-04 14:30:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 3b0a0a48-32db-3384-9c26-90ee03aa670f | -11.8352 | -50.0891 | 2025-10-04 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 790525fc-c2f9-34c4-8736-6f346d0c8b9e | -13.7476 | -48.0583 | 2025-10-04 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 2ae3734a-3946-3b9c-8d68-d15b92851e46 | -5.818 | -42.4861 | 2025-10-04 14:30:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| a4d9b7d1-2177-3802-a39d-9c1d3c22bccf | -11.9011 | -44.9786 | 2025-10-04 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 1615d625-d567-3c77-91aa-de57ddca4c63 | -3.7669 | -41.047 | 2025-10-04 14:30:00 | GOES-19 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 108.1 |
| c0df3edf-bad9-31db-aa2b-52ca43e9b14a | -5.8927 | -42.5273 | 2025-10-04 14:30:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 512cdefa-c6c9-35b3-957d-e0e9f760cc88 | -13.1582 | -50.9574 | 2025-10-04 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 14a36b85-4913-34dd-98f5-d2aa45a45df0 | -10.2973 | -50.2799 | 2025-10-04 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7bbc97d0-d233-3359-83c0-8921e743f881 | -6.2596 | -45.341 | 2025-10-04 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 1e5e9fb3-dcfd-3e49-bb38-0921f017c469 | -8.6136 | -54.9961 | 2025-10-04 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 7bacebda-cb26-33b2-ba87-a68ba1b958b7 | -13.0959 | -47.8876 | 2025-10-04 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 8e5ffd97-ce2e-376c-b7e4-60f1547c11e4 | -5.8634 | -45.7308 | 2025-10-04 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 63adb40a-6877-375a-8d25-553ba7facddd | -15.3179 | -46.3011 | 2025-10-04 14:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 875b6659-6927-3bcd-824e-573a696856b3 | -7.6458 | -45.4716 | 2025-10-04 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 63f80cc5-f5da-34be-8520-bd52d7845a2e | -5.6655 | -42.7342 | 2025-10-04 14:30:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| 4ffd74dc-5c4d-3fd8-a69a-42195049bd84 | -13.3127 | -47.61 | 2025-10-04 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 1abccac1-189f-3a8e-aec2-4768f5550f07 | -7.7941 | -42.5369 | 2025-10-04 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| 227d5056-94d1-305b-b85e-7c21337c25bf | -9.6293 | -54.3158 | 2025-10-04 14:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |


[Clique aqui para ver as próximas entradas](README157.md)
