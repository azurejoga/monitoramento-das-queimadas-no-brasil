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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09394c78-e6ac-3edc-978d-91221fe6dd6e | -1.75151 | -54.52158 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 060c3c0b-8624-3691-9e4e-9e88e6d54a65 | -2.2901 | -49.06321 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0a67efd-76dc-37e3-9d41-07430bf29b99 | -2.1771 | -53.6359 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 876b6765-96da-3702-9777-bd23063f444f | -1.29719 | -51.7349 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8e4c5b6e-aef7-355c-8ef5-61403ad18aeb | -2.14754 | -50.88425 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b944fe3f-1e10-3ade-b90e-2759a71ed5e6 | -2.9643 | -53.92212 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b7153ea-970e-36f4-8451-4fc337350402 | -4.02855 | -49.92067 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79fee5c0-9ce1-3647-aa78-f700cf3d6db9 | -2.80845 | -54.01896 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc29945b-9c6f-3888-b01a-d1c39e2aabd8 | -3.24697 | -54.2201 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 810c9934-a9f6-3a60-afaf-f4ee0720f106 | -2.85203 | -53.96545 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f92d9c67-91fc-3ef1-a5da-f4e069fe976d | -2.69585 | -51.36147 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b8e797d-1fd5-36ca-84c9-1f1b1b94161d | -3.47196 | -50.00699 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af3a5ad2-3c05-3722-9f5b-e926b0ccb652 | -3.38507 | -49.17338 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cc69bbd-e013-31a7-94f3-23d5ad88f8eb | -4.53021 | -46.42661 | 2024-11-24 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53979b95-dd27-3350-bc4e-59758ebae3fe | -3.24803 | -54.23558 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8db302c5-bd58-3577-99e8-a45dac92ca8e | -2.17537 | -50.90288 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2d90c7d-995f-3d67-90ae-e361bfc7186f | -3.28741 | -53.85594 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b16ab574-f0f4-3f00-9410-f7e7fcacb9c8 | -1.77406 | -53.63043 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ae980a2-1fbc-3d46-9127-19e5efe73d02 | -2.45205 | -50.36722 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 989e3ddc-d29f-36f1-8484-f62d3f84d7e4 | -11.31014 | -54.02454 | 2024-11-24 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 293ca08f-9fd2-3cf7-8151-e584203d492c | -1.60328 | -47.1418 | 2024-11-24 04:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bbfa26c-93ca-377b-97ec-bd1fb9fed774 | -3.26479 | -53.26926 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d8e1678-f149-3371-a850-4b219aef0413 | -3.83754 | -46.01884 | 2024-11-24 04:53:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e97e61e-f751-3cae-b57b-898ca105fe83 | -1.52866 | -51.56001 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33258e1d-9044-304f-a217-4b5fbc197e5a | -3.35375 | -50.13854 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1aa69532-e753-3380-9a16-f6afffec8388 | -2.8657 | -53.96756 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a49da916-dc1c-3213-a9b3-f66b9cfc3116 | -1.61778 | -53.31281 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b82753a-2dd6-36d5-b96a-1e2856332147 | -1.2375 | -51.79241 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0edf105-1ec4-354b-b09c-4705e2a0d8a8 | -3.90892 | -50.59101 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd688372-cbb7-3908-8798-fea0ce355a6f | -1.05714 | -51.81303 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e195b6e0-3cd2-3271-8f54-840295166bd1 | -3.37141 | -53.32629 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c4906bc-c9ef-322b-aa37-5e07a9bbe131 | -4.06893 | -50.00533 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5727055e-a9c5-3330-b5d8-fb6b4e0cc314 | -2.0531 | -52.08147 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 15007792-48aa-3bbe-acd8-0839d99bca26 | 0.63058 | -50.57423 | 2024-11-24 04:53:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7787714-7f60-358f-9357-5c2b7e867707 | -3.25147 | -54.2361 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a16ac88-89ca-3e89-8cfe-2f4e92336c2d | -2.62234 | -54.93235 | 2024-11-24 04:53:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 379987ac-86ea-36e2-9ae9-88a8cfd21406 | -2.0135 | -51.17751 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc63708b-2f43-3b1b-b2df-fe82e2d00289 | -5.35961 | -45.03538 | 2024-11-24 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffc9b7ec-2a15-324b-b604-0055ec9d4821 | -4.02685 | -46.67437 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7659ef4e-c3eb-342c-9167-93a1a94174ce | -2.94715 | -51.42908 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 734cb579-97d5-3f8b-8805-a8f2f69f8be8 | -3.50653 | -53.80391 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9ca0e11-26d7-3893-b567-14a8e91bfcbd | -1.18735 | -53.70202 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6bde33dc-8db1-331a-a9c5-4b23bc62af69 | -1.42149 | -52.81306 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8022cb93-b4b3-3ac9-866d-bc550b7d1ec3 | -3.0226 | -51.35908 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4c36024-e400-3b71-a2a2-8538e8152e95 | -2.30422 | -53.87755 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b42b0a22-7f05-3280-af9c-584f64bab0b8 | -2.28282 | -50.57962 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f86d88d-7ecb-37b4-a628-63d634f3c617 | -4.38257 | -55.08117 | 2024-11-24 04:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86858bde-f233-3c98-8903-7e860204be25 | -4.24118 | -48.63603 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 021d2494-ed41-3a30-8c91-460fc773dd70 | -3.44291 | -50.44678 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9942e1bc-abd6-34c3-8fa6-6fed27953af3 | -1.73552 | -52.04571 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6aa50963-d40f-3113-8976-98cfbb2b7456 | -1.6444 | -53.87555 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ab3a772-2b66-33f3-a451-0b73dbbf7dfb | -2.29366 | -49.06376 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f714577f-901b-3fa6-b114-29cce2ec322e | -3.00113 | -51.38774 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1be97a18-bdc8-3338-a457-47314ae84732 | -3.25146 | -53.27089 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5675eb60-84fa-3887-bc66-3da30c5b50fa | -3.04991 | -53.4248 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4bcc822-f752-314a-86f5-e82612557138 | -2.21936 | -50.68629 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de8172ba-98a5-341d-8dde-cf6332cd763b | -3.29817 | -53.85387 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af169c26-83c8-31a4-ae41-e5652357808a | -2.51288 | -54.11198 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 00ea84b4-ec75-3736-a46b-39e1fc7a1c28 | -2.29132 | -49.05517 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78458ecd-8231-3e7c-897b-b88e1aa0ebba | -2.18555 | -50.96888 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f00bdf5-0a82-3fd2-9896-b61bc560b6ef | -2.26853 | -48.7088 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77f2df2f-fcaf-3828-ae94-3e0a29746669 | -2.19839 | -49.00031 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9a760b2-4217-33ea-b5bb-15e524b642ee | -2.56302 | -54.06212 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2346315a-71c1-37ac-a822-cffbbf41ca77 | -3.38885 | -50.32221 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a9e55c77-f1e1-3fdb-a914-f81692ce2047 | -2.22042 | -49.86712 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b089663d-60ad-3986-a34a-3b669c3b7879 | -2.87871 | -53.99607 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 350fec58-616d-35ad-a43a-bfdfc43c9aef | -1.6263 | -52.43801 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6d8638d-3508-3053-8a58-14876385c197 | -3.54571 | -50.19019 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8085df4-9dd1-360d-a342-f40a879e1868 | -1.19346 | -51.76734 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b95dbbf0-03fc-3086-805a-65c4e8f42326 | -3.83209 | -49.94688 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daa3e283-5a1a-3398-8a6e-797d703207c8 | -1.06992 | -53.35752 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51f58677-6e45-32c3-abaa-bb665efeb436 | -2.69191 | -51.71398 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d92471ba-fd7b-3882-b608-5587fab3f3ac | -3.30553 | -50.36185 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cb734cc-6a94-3a44-ab27-fdb24770489d | -2.61961 | -54.25933 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9bebdb97-65dc-3a6d-9807-65c3f0661108 | -0.03076 | -49.64273 | 2024-11-24 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf6352b4-a0c2-3ad9-abb6-0942cbe3dae9 | 0.40025 | -51.71536 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae3ce0ad-b71e-394d-9d9c-fbd6b12821e6 | -4.05916 | -53.65179 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba356c68-bd64-3592-a65e-7b3cacb2ca55 | -0.96654 | -51.71814 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6377500a-8d41-3743-a997-821a00ba8195 | -2.27217 | -50.34715 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c086db3-e5b4-324f-a2a0-f893aba9e484 | -1.19084 | -53.67969 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0744fadf-31be-3efc-a2bd-6326ef58fee2 | -2.99662 | -53.74013 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a8e3a9b-e2f3-3006-8f50-d82be8a48ed6 | -0.90929 | -52.58603 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c73ce656-4044-3e7a-80d8-32c84b2486a1 | -3.42266 | -53.2836 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a26b36e7-76cd-376a-ae79-6336ce4796bb | -1.77689 | -53.63462 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e96fe8e-f7be-3ca5-9287-b56f54b59d72 | -5.06576 | -43.69746 | 2024-11-24 04:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f91cc72-4cb4-3c95-a364-493990283841 | -4.73961 | -48.12555 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e71fb61e-94e3-3d6a-b632-f0be6d485e1b | -2.26335 | -54.83832 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edf8c97d-b7f9-382e-99d9-7385cb326801 | -2.57479 | -53.96451 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 464a0fa9-7be9-32ac-8883-ee0552435c5c | -5.43441 | -45.34007 | 2024-11-24 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc67e988-5751-3020-863b-046cd73ed0c7 | -3.1816 | -54.32539 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12319580-2f40-36df-a6fe-f99582ba3fcd | -0.89506 | -51.7212 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20935bcd-537e-34c6-9b9b-2f8f2f10c021 | -1.61194 | -52.59562 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 635c8302-b507-38d9-82ab-9c21f25f0543 | -3.17157 | -49.07624 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2db21a3-c803-3649-8f70-af65be1b4d83 | -2.1737 | -50.53753 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fc2b311-52bf-315c-bded-82076629689d | -3.01576 | -54.03961 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35efe2dd-ff66-3495-88d8-8a05d119dbe7 | -1.08235 | -53.36685 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bef19b95-3722-3701-8392-1fe3672143be | -1.12079 | -53.38765 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b282f3a2-3ecc-3364-80b0-6f411ac54dee | -0.88075 | -52.76847 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4e28456-be1c-34ce-9037-9e1a95c9d3d9 | -3.31657 | -50.12904 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e7a9db6-1df0-3bec-83e3-b3d3bb4c5c67 | -1.28291 | -52.26394 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README44.md)
