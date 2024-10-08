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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d90d82d-bef0-3ba5-a9a7-72419ef9ab85 | -7.30148 | -42.24059 | 2024-10-08 03:40:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f9f69e0-e940-3921-a20c-5e00287bc965 | -7.11436 | -42.64509 | 2024-10-08 03:40:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3c59471a-54d2-3d2c-9a74-9f39708b2f90 | -6.83563 | -42.80707 | 2024-10-08 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 2f6ae88d-a2b7-3eb6-9ea2-83477c196154 | -7.65351 | -42.49223 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 89bbaa73-c4b4-3f84-95ce-3a90af19cb04 | -7.65098 | -42.5067 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e8790884-e5e6-3df7-90a1-99f2b53d76b2 | -7.64843 | -42.52131 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f71edc42-5959-3860-b74f-5e194dbc8dbe | -7.64209 | -42.53032 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c1e69d3a-1fdb-37b7-b893-7ba2c103e8ce | -7.63388 | -42.4152 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2c90cec1-08ec-3420-b2d7-f7aa785f87d5 | -7.62467 | -42.41383 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f9a610c2-ee16-327f-9e65-934376d89862 | -7.6177 | -42.42994 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7f8936df-a9cf-3e0c-ad93-a75b7a5f7682 | -7.61756 | -42.42717 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 63cd4084-956b-37cc-8157-ac2baa8b8736 | -7.61672 | -42.43187 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 638a921e-10b0-3ee3-bc3e-43ec9bfc126f | -7.30822 | -42.25616 | 2024-10-08 03:40:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 844db9be-d022-3a61-91a2-f820a5088413 | -6.83174 | -42.8012 | 2024-10-08 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| efdcef65-5bac-3bf3-9860-ee30cb8532c9 | -6.54278 | -42.70844 | 2024-10-08 03:40:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6dd2a831-af85-3761-a356-eed6ca00d0ba | -7.78031 | -43.08766 | 2024-10-08 03:40:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0b5da575-63ec-3982-aa2d-adb0f77a7e87 | -7.73331 | -43.04656 | 2024-10-08 03:40:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9b274cfb-a1ff-3f74-ae2e-71fb667d7a19 | -7.66188 | -42.49873 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4768e9d0-d739-3f9a-a749-bf5e90229ef8 | -7.6539 | -42.51722 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a4d1779e-95c3-34c9-a8a7-4ac80134889a | -7.65305 | -42.52209 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 30ae4799-95e1-3753-a991-adb0b4b1e99f | -7.63929 | -42.4114 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4cfa57f7-66c1-3609-805b-20e144b44712 | -7.62928 | -42.41449 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8fc92bb3-c5b3-3a8f-a38d-7e3e8e748347 | -7.6247 | -42.4166 | 2024-10-08 03:40:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 657e6595-a7fc-3f3e-aed6-6e2c1396a895 | -7.3007 | -42.24515 | 2024-10-08 03:40:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d7fc88f9-d0eb-3f82-a472-001caef7bca1 | -8.00506 | -44.37963 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c74dc9f-376c-3f9f-a087-56d67124a486 | -8.00449 | -44.38284 | 2024-10-08 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb1faf8b-8280-3b95-982e-3e742e5423a4 | -4.65317 | -44.37604 | 2024-10-08 03:40:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8053d33-0bf7-3307-b911-69435a773c3e | -6.51096 | -44.00757 | 2024-10-08 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66c359b7-19ef-36ee-8df6-7f2524a81c73 | -5.99081 | -44.44421 | 2024-10-08 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13ff5de0-9636-34bf-8d64-c0e7f8b367b2 | -5.98943 | -44.44253 | 2024-10-08 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a0ffbc1-e0b5-3fda-80e1-561e08b5c0cd | -5.98605 | -44.43964 | 2024-10-08 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba8e372d-3c12-3eb8-b77d-350ca2ef9ce2 | -5.98543 | -44.4431 | 2024-10-08 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfc59f2b-2cf2-38bc-bc05-bd391b783f70 | -5.98404 | -44.44146 | 2024-10-08 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68fb5392-2feb-3d2d-9998-85ccd996af3f | -5.85166 | -44.87916 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13dc9da1-20b8-326c-999b-d1e65d93bd56 | -5.84679 | -44.87412 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8598cace-05f1-3979-907b-fb73a9efb4bb | -5.81683 | -44.12641 | 2024-10-08 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 642ef416-7c7d-3a55-a449-0191451670ed | -5.81627 | -44.1297 | 2024-10-08 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f2fdfe2f-c72d-3570-905c-f9dbb947c9dd | -5.8157 | -44.13303 | 2024-10-08 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4843c3d9-45d4-303a-8b43-21dcac467bc0 | -5.81513 | -44.13641 | 2024-10-08 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f9821bd-e101-3d1b-aba7-738cd010aab7 | -5.81509 | -44.12611 | 2024-10-08 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5a4018ee-202a-3224-93d4-6350b58c6cf4 | -5.8145 | -44.12938 | 2024-10-08 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fca4d334-ee4a-3ced-a5a6-795f104e01a4 | -5.81391 | -44.13272 | 2024-10-08 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a79d6dea-16db-3996-984d-8ed3f9b94f16 | -5.81151 | -44.12554 | 2024-10-08 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1cdd5092-17cf-30cd-b5ff-6bad05c49718 | -5.81095 | -44.12881 | 2024-10-08 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9bce0aac-aa27-36fe-9f00-c8a970f9b3b7 | -5.80917 | -44.12856 | 2024-10-08 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1d5aff4d-932c-37c1-9af7-5420e2a7ab8a | -5.58047 | -44.88072 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9fcc5357-9205-3cda-8514-12482f3de3de | -5.5798 | -44.88462 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88f5f259-8828-3dfc-87a3-41f286422982 | -5.5784 | -44.88065 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9d3d11a3-1fe6-3817-a24b-406c141259b1 | -5.5777 | -44.88453 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b1f149cc-b283-3e5c-a21d-b314b0aee1fc | -5.57552 | -44.87588 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4b011153-2f06-3fd1-a74a-e230cdaade2d | -8.28214 | -44.09564 | 2024-10-08 03:40:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ffdce64-798d-3e7c-a3a6-4966cb4f7a21 | -5.57487 | -44.8797 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3adfd9fa-d9e8-3de2-b77c-373eeabf0338 | -5.5742 | -44.88357 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6c7a760-87d8-30eb-aa58-bfee00d63b87 | -5.57347 | -44.87588 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b3d22172-208c-3bdf-b383-aebe9a0c4e78 | -5.57279 | -44.87967 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2485713b-ad55-30a8-b37c-a44a8f3e9dd6 | -5.5721 | -44.88353 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6381e4b9-f848-3587-bef0-c19159590661 | -5.57141 | -44.88736 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| de397e4a-68ab-34f9-b91a-92a29e272d0c | -5.56989 | -44.87503 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 13cea695-86c7-36e9-954f-2975a2691ccf | -5.56924 | -44.87884 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ba2b1327-e54c-3a89-b185-cc52393ee7ad | -5.56858 | -44.88268 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| adbfc40f-0492-339d-af7f-99c15c8fc650 | -5.56792 | -44.88651 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e1168b07-b3a0-37c0-ad03-96f0d5f1b3ed | -5.56782 | -44.87516 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1835d66b-a631-3305-a864-feaa7d9d55d7 | -5.56714 | -44.87896 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e53e3825-49a8-32d7-9272-bdfac08317f1 | -5.56645 | -44.88276 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 36afc402-0733-3da4-a9ed-a5af52bccfb7 | -5.56577 | -44.88655 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 07399960-9b0d-32ef-afaf-372a36b14162 | -5.56292 | -44.88196 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7dde8319-267c-3cb9-8bc8-dff82c456ee6 | -5.56228 | -44.88569 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a97723eb-6767-3e92-a0ac-9ec35853f5e5 | -5.47994 | -44.25387 | 2024-10-08 03:40:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b85609e-0053-31f0-b475-d6eada6fe08f | -5.47933 | -44.25733 | 2024-10-08 03:40:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 605278ac-68f0-3282-854a-6349c2941271 | -5.47871 | -44.26084 | 2024-10-08 03:40:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ba3eb90-8b57-3a68-a672-a4a8d4ef7cfb | -5.47752 | -44.25426 | 2024-10-08 03:40:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 55aeefce-291a-3f4e-a0f3-e7a30dbde69f | -5.47692 | -44.25777 | 2024-10-08 03:40:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4d9345af-49c1-38bb-8ed6-fd5f7e86778a | -5.47633 | -44.2613 | 2024-10-08 03:40:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2f7f0a12-41d8-3515-8727-43c13f92ff77 | -5.47456 | -44.25291 | 2024-10-08 03:40:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ed2462e-212c-35ea-8c7f-d4f4552c5dcb | -5.47395 | -44.25637 | 2024-10-08 03:40:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| deddce02-2303-3edb-9c05-f70f5f0e0cf2 | -5.47332 | -44.25988 | 2024-10-08 03:40:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e88354f3-bc58-376e-a352-1ea413b68433 | -5.47271 | -44.26336 | 2024-10-08 03:40:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2557d7b9-ad1e-31ca-b642-ec3a7265c6e2 | -5.47094 | -44.26031 | 2024-10-08 03:40:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a29492b-f50d-3902-b5c2-937e0786698a | -5.17005 | -44.66474 | 2024-10-08 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b826068c-c734-34f7-8cdf-486dfecdcfc8 | -7.2756 | -44.97087 | 2024-10-08 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69424ac6-4019-34a5-8f19-d51bf32af0da | -7.27534 | -44.97011 | 2024-10-08 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba592476-1d58-3484-b6e8-cb22e3f48d1d | -7.27486 | -44.97489 | 2024-10-08 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 309aced9-2214-30f5-a27f-6291951163a7 | -7.27464 | -44.97411 | 2024-10-08 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e510f93-fae1-3f49-ab2c-87800c7b644d | -7.26986 | -44.96914 | 2024-10-08 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd6c1892-280f-380e-a292-374267076d13 | -7.26915 | -44.97317 | 2024-10-08 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ffd5e2b-a788-3dbe-9502-7ef963e350e0 | -7.26436 | -44.96825 | 2024-10-08 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 768ec087-853b-304c-a6d4-d3a0ef9c0369 | -6.69177 | -43.95899 | 2024-10-08 03:40:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 384385a9-9079-37b4-8f3e-280570226935 | -6.69122 | -43.96217 | 2024-10-08 03:40:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c6a5172-6def-381e-81e2-5d9832eae184 | -7.10004 | -44.58372 | 2024-10-08 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9505bb0-e6e6-3e46-b7f8-33a27ce6bf29 | -7.09524 | -44.57957 | 2024-10-08 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 131557bc-55a6-3147-895e-ded09fc4b871 | -7.09464 | -44.58296 | 2024-10-08 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97415665-5280-3382-94e2-948c12f5a6d6 | -7.08988 | -44.57862 | 2024-10-08 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6aad8536-eddb-3b34-85c1-3ec4329b2efe | -7.08927 | -44.58205 | 2024-10-08 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3294a797-a6ff-34c6-a6e0-4ce70c4a5c23 | -7.08865 | -44.58554 | 2024-10-08 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8ec568c-43b2-353f-8df1-97aedc3fe528 | -7.08389 | -44.58121 | 2024-10-08 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df96da4f-7bae-31ca-b9e0-608ff23d1268 | -7.08327 | -44.5847 | 2024-10-08 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e97c6db-3278-36d8-9669-e37762c49f81 | -7.0785 | -44.58039 | 2024-10-08 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edf1c15d-7824-3dc4-b299-e0d8c2fb6016 | -6.58278 | -44.1811 | 2024-10-08 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0235e4b0-bf2e-3c06-859a-5384e396f72e | -6.57817 | -44.17649 | 2024-10-08 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50aa9aa7-d8d3-314b-8867-fd9d44f1d621 | -6.57759 | -44.17978 | 2024-10-08 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README35.md)
