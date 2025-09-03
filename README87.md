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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b10c21e-f3a5-3457-8647-eae1f4a220eb | -11.79866 | -51.49436 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db128a7e-b266-3e8b-806c-5a27a7d9c6de | -14.40303 | -51.66601 | 2025-09-03 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fab6bb71-187e-339d-b961-fbb7bbe98ed3 | -11.66804 | -57.35748 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2281599b-3f0f-3e66-897b-353437f52f74 | -13.49931 | -47.02514 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3251bbed-cf42-346d-bf2b-2d467bc0c50e | -11.03037 | -45.06147 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 270d396d-ac47-3482-81fe-9b663632d481 | -14.3483 | -52.80149 | 2025-09-03 05:14:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b5d34c9-aad9-3662-8959-ff195ad4fe0e | -14.63665 | -48.94146 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d94e4367-cac0-3bc2-976f-b47e6fbadfcb | -10.47168 | -53.63111 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cc3d4a7-b229-3442-8346-935368a35854 | -11.6746 | -52.17781 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7b79387-891e-38d3-ac53-5754b3617848 | -8.09404 | -47.59469 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae780d89-b8dc-32cf-91f3-0d6440e62095 | -10.88569 | -55.74386 | 2025-09-03 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1294ea33-349c-3b02-8497-f8c12175f5ba | -10.45744 | -53.61863 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e87a2d4-f414-30c5-b58e-07e7d4b03975 | -14.55115 | -51.94361 | 2025-09-03 05:14:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 099029f7-ad5f-3e62-a425-567f6c45bde8 | -12.94071 | -56.96687 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8656d94-3670-3c15-8121-245b196407a3 | -9.63506 | -46.12234 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da8138ff-fbbe-3331-b5bf-9268b73d3438 | -13.08756 | -57.12378 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 721cae7c-38e2-3fcd-9eae-f8bc88cedcb8 | -8.30581 | -55.09573 | 2025-09-03 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec229090-8333-3802-8e6a-5d9dea8471e1 | -14.30116 | -53.09961 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 823cd209-3614-3fc7-8bba-580bd498ac0f | -11.59237 | -52.12449 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 29da86c6-9613-3665-9bba-7e4e59ecebd7 | -8.05863 | -52.36708 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e48eb305-3840-394e-940c-2b806b5f4bb8 | -13.087 | -57.12752 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95848d55-e2a3-3d80-bab0-ebe59d625358 | -13.29104 | -46.83385 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cd42454-f6c7-3378-ac30-cabc18d38e28 | -14.982 | -50.21036 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59ac3351-a197-300f-9579-1b8c02ae35fc | -15.02515 | -50.06916 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbf25e3f-e527-345c-bc32-b3c694176f10 | -10.49192 | -53.6512 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fc36541-2aa1-33e9-b98b-0e0ad977bc9a | -14.78568 | -48.15062 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 229a2aa2-7de2-3219-b30b-a82e6110f854 | -10.5435 | -50.41922 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb1105ab-284d-3329-a052-b6cb8d4475c3 | -7.71349 | -50.29498 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d6cf95d7-bfef-3f1c-ab3a-e7c2dbcfb716 | -7.76813 | -61.19743 | 2025-09-03 05:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59add1a1-2220-3945-985f-79fa0018dcce | -11.66915 | -57.35024 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 178b8a65-473e-3901-b500-049fd9c0f4cc | -14.78696 | -48.15242 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 876b67bb-679b-34a6-bf75-1f16e019b2d7 | -12.63054 | -56.98911 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa55a8aa-e315-3211-b1f7-fa8b98169fe0 | -10.91132 | -50.82705 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c55f8bf-fad3-36ef-ac24-1ec46355d0e5 | -15.01529 | -50.06095 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d86e358e-fcbb-36ae-ae49-70b1df32d070 | -11.58854 | -52.11958 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 66debe03-f057-3de7-9835-c9382602038b | -12.99431 | -48.11903 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4f64612-be5a-392d-9e68-2f8691c7196c | -13.01498 | -48.09645 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bfadcda-4257-3e0a-ae8d-8e3ec28331e7 | -12.97765 | -48.10845 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ae2569b-f5ec-3545-8fe5-bf5a83946ad4 | -11.60799 | -52.10894 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da67596a-278b-3ec0-9d34-8def8aac4bad | -12.17297 | -60.74109 | 2025-09-03 05:14:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a8f6cdf-7771-3d92-aab3-0072d9b11c6f | -12.9356 | -57.00074 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e13f0d20-7119-37c3-9547-0d7bd1885e50 | -13.10184 | -57.14513 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 146d8fe1-7d15-314f-9502-b6665cfbd550 | -6.79902 | -59.87576 | 2025-09-03 05:14:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba6b8b0d-a361-3d06-a693-7f50033bfc1e | -11.85787 | -51.46052 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 374a0208-fc6d-3144-b61a-70eb6de683fd | -8.0627 | -52.35213 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9110631e-ef3d-30e6-8501-580d9c8cca0f | -7.70655 | -50.27208 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d6191bad-704b-3ca0-a7f3-9eaca704cbc3 | -11.59472 | -52.10719 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f7522f0a-a41b-3eb4-a911-b4a4fc4b0047 | -12.91782 | -56.93228 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7068fb70-ef5e-3992-bb8d-6215c079106c | -7.3496 | -57.62637 | 2025-09-03 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03ec19de-8389-3c45-9a69-25b9fa5dc82b | -12.4882 | -53.83453 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52d9ee04-cb30-33f1-8847-577a9af9e014 | -10.09381 | -54.76341 | 2025-09-03 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 219236ac-e1c5-37f5-9603-e2640f0310e7 | -13.00806 | -48.10417 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d37d9bf-c7d2-3bdb-80a1-d1976611d7a7 | -12.93499 | -56.95827 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 93a3f133-c4e6-3371-9a23-897056aebd73 | -12.90954 | -48.09797 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 940e139d-3f6a-3c2b-954f-1aba931aa85a | -14.98163 | -50.21355 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c49e7296-ec82-3215-aa91-3e64de8b6838 | -13.71349 | -51.94554 | 2025-09-03 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b648ae87-d88e-3cf9-8fd5-462865c61890 | -10.08741 | -54.76377 | 2025-09-03 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d229fef4-5fb2-3e92-8f0d-ff5d6d110d20 | -10.25266 | -61.76593 | 2025-09-03 05:14:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c3b84b5-5cfe-3f94-86c8-637664c3f93e | -14.78559 | -48.1653 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39743c60-c884-313d-9472-79927581dca2 | -12.94016 | -56.99377 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 729d9409-2323-3d0f-b93f-8a5fdf1e5507 | -8.36014 | -48.304 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f742fb6c-4c14-3b9f-a8de-d5cd53e3f369 | -9.75687 | -46.91185 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c03cdc9b-a33c-373e-8a9f-33d1927d8ba8 | -11.84506 | -51.41341 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8254d4ad-9a43-3d89-9586-8ea51fc95f20 | -8.5399 | -51.31025 | 2025-09-03 05:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f6d6e53-07f7-3b4c-8d52-6313cb79b777 | -12.9413 | -56.98624 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c79b1c9d-ef61-3a36-9878-4decb264e3b3 | -13.29701 | -46.83847 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bf5930f-2972-35d2-bafd-f337c7107637 | -12.88189 | -48.02929 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76aaa6aa-7efb-37b6-9310-4baebb2dfa4e | -6.78678 | -56.30102 | 2025-09-03 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2a01c1f-b3d5-32b1-841c-fb118330ea53 | -14.60863 | -48.02234 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be51b415-1cd7-3d59-b47b-7057859badf0 | -7.04938 | -57.81016 | 2025-09-03 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 31cc33c1-89a3-338b-ab34-c79b749f7efc | -9.63915 | -47.85553 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d1a16717-7b5c-399d-8aea-03d78abe669d | -9.76176 | -46.91752 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8bbdaa2-a399-3b14-b0c9-a83abbe4b3dd | -14.57341 | -48.06586 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f27d7e2-271b-3f7c-991b-58e5bc401f52 | -13.45634 | -46.93533 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a5a41dd-4920-3eec-8360-878a15781b8a | -14.59365 | -54.58582 | 2025-09-03 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 438b1fa1-91e8-3036-9e05-15899f469699 | -12.90773 | -48.09304 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c7d9703-e636-3684-9f70-1f6863dd9b57 | -8.4318 | -45.08716 | 2025-09-03 05:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 710ee3da-ae95-3c5c-ac32-3dbb5a5d3175 | -11.94851 | -50.59947 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcd62a3e-ca43-3c77-8e96-a3cdb48cc085 | -9.77488 | -49.97806 | 2025-09-03 05:14:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 174aeabe-75ea-3a67-8808-6f5e652d5a24 | -14.97285 | -50.20792 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c9f2a2c-923d-3495-908f-c3c5754ab3e7 | -11.63347 | -52.05479 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 935c9144-8077-36b0-a8ea-670356266e6a | -13.09552 | -57.11735 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d532fd83-be59-39a1-8a6d-9bc478fc6075 | -12.44166 | -48.70902 | 2025-09-03 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fdd81ed9-227a-3fed-95f5-378ac66c8a91 | -11.66075 | -57.36002 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cd9d783-57bd-3b41-b86f-66330dde3611 | -14.9903 | -50.06388 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63221f12-b7fa-3122-ab91-9e4c6b9eea28 | -14.56793 | -49.14452 | 2025-09-03 05:14:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7719e05-d9a3-3a05-96c9-754216df0cdc | -12.88907 | -48.04668 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30bfe9bc-bdda-3134-b6e1-43cc97e90b98 | -11.22141 | -55.06528 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 477eb203-0b47-36e5-b7b1-993b6f212bdb | -10.48548 | -53.64 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1cc0bd4-5521-30aa-833c-d4d044658e2d | -12.6408 | -56.9907 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cd2a154-0a79-3770-8100-c96151c8408c | -11.64174 | -52.06036 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7e73b0e-0ba0-3c5a-bf22-1d874e2c2c18 | -12.49407 | -47.48125 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cfac78e-1694-3c1e-8402-f1f962ab2f01 | -6.5825 | -58.59203 | 2025-09-03 05:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69c65741-55e6-34ab-a31d-3274d50ff32c | -9.62933 | -47.07875 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3f66bbe-e6aa-3e99-a66f-e8717e97a0de | -12.61118 | -57.00143 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7280c202-8cf9-3a9c-84c0-b4cbb8cc6aae | -9.72922 | -49.00593 | 2025-09-03 05:14:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dab18d17-3bd6-3753-8e4b-40e11abd819a | -7.70329 | -50.2991 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d981aaf-950d-3a62-b2bc-adb6b75d8062 | -11.12275 | -45.11304 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69931a07-f8b3-3490-bc45-1e7c689d8f85 | -11.58795 | -52.1239 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1e0f47b4-a472-3351-9ce7-27c9d371d349 | -12.90071 | -56.95277 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README88.md)
