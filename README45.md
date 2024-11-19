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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f23e9ed9-44db-3947-a42d-fcfd58eeb30e | -4.10979 | -51.05202 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56e2cdfe-1c9c-342e-97f8-e286e16648a1 | -0.95951 | -51.73176 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1109f896-51d5-38a7-a0e0-8a2d013a2df3 | -2.60183 | -51.79193 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32fdd4c5-c008-30e5-bc50-e51c03a8cf7f | -1.78496 | -53.59299 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0f0f5b2-2b82-3b1b-8c11-fa42e0069221 | -3.09091 | -51.04081 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f748993e-db49-3732-adba-22cf50b72df6 | -0.88857 | -51.80815 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1d58ce3-6c40-319f-858d-084fe6017905 | -3.08247 | -54.66168 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2739a941-4ae0-39cc-b0b0-4dce0a5d54e9 | -2.93066 | -48.33199 | 2024-11-19 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91ddadc0-f302-3b8a-81f4-705f0e228cc4 | 0.61768 | -51.77333 | 2024-11-19 05:08:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 11a58db9-8a0f-34c1-ac06-b0cfe2897a5f | -3.55518 | -51.53107 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b2db2b3-fcc7-3912-8c14-40645275c7cf | -4.48436 | -46.71453 | 2024-11-19 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54350e21-70e8-3fd2-abc0-c07813e6f9a3 | -3.05024 | -54.40194 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a856522e-59de-3ac7-aff7-b074ecd102ef | -0.85844 | -51.86408 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e9f20841-6af7-3845-a6a9-b8c988be16a5 | -2.72554 | -51.81441 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef33bfae-551f-389e-9ad3-17f51e159aa9 | -1.58331 | -53.8008 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bcc02cf7-4194-32cb-89aa-e7ebeba57e2e | -3.10616 | -53.743 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9dd23da4-19d9-34e7-988b-c63fbde9ada2 | -0.935 | -51.63465 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d705e367-0fc5-3d38-b717-238f7f7d79f6 | -4.55235 | -48.01765 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| e4ed8202-1a31-3925-ab20-af39b7e3829f | -3.57908 | -53.11642 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2635ef22-a9f2-379b-bfa6-27b721634a87 | -2.00012 | -45.35105 | 2024-11-19 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3a9107c-6b86-3c3b-aa12-fd0a7a6b0b5a | -2.34831 | -53.90953 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc460833-38a0-32cb-8de2-4aca2758a725 | -3.34325 | -45.36285 | 2024-11-19 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c6b76f9e-c97a-3d75-a67c-ba68003fa4ba | -0.39431 | -51.54053 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cfb4960-ec10-3cda-8ff1-b1e2cf7593eb | -4.55713 | -48.02151 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5f61eba7-b540-3a4a-94cc-eb1ebfb285eb | -1.34721 | -55.73925 | 2024-11-19 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36cf9c42-4726-3b74-8980-6e36b79e2c5e | -1.41833 | -52.82161 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2adb827-c22d-3355-a725-e7bab1b1ac69 | -0.3505 | -51.4076 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 487f1a90-4bde-3bf6-ac93-d93f8ef4d19f | -2.77632 | -48.58199 | 2024-11-19 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e17e365-9fe8-3384-9bc6-f9fae5ad0587 | -3.55206 | -54.58428 | 2024-11-19 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3bc4ec9-228e-3031-b6f7-043d25faffbe | -3.20141 | -54.32025 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc2a99d8-479a-301d-8c0c-00042f4b6392 | -1.40207 | -47.45267 | 2024-11-19 05:08:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0302932d-b88b-3d99-b508-a32945d5d7b3 | -1.64713 | -52.6431 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26862aa6-5248-3269-9e0e-149dfeedede1 | -3.55113 | -51.53041 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d90b8fd3-5518-389e-9f72-e20291994736 | -0.85466 | -48.75163 | 2024-11-19 05:08:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 241d8f6a-1550-3a8f-b5ee-52fd1914a64d | -1.5862 | -53.80517 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 324ab945-a773-3cdb-999a-31982f989873 | -1.1312 | -51.68471 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa083eb7-ca2c-327a-a920-bbddf69fd4fd | -5.9788 | -45.3621 | 2024-11-19 05:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 57d1bc4d-0296-32a5-876e-526eb0c995f5 | -10.45893 | -45.07116 | 2024-11-19 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e827522e-165b-3b17-b7b3-0afe803b0bf8 | -9.71894 | -48.37822 | 2024-11-19 05:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4866360-48c8-31f5-b9b6-284beeb7cb8b | -9.71946 | -48.37424 | 2024-11-19 05:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 070bd8e0-f163-3475-82a4-aca328eb0ad9 | -9.3101 | -46.18482 | 2024-11-19 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 85676f6f-a70d-30ec-82e7-08a5234ee683 | -8.00514 | -44.38667 | 2024-11-19 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 159ee303-781f-3c39-95e1-281ddc5e6171 | -6.04604 | -46.60414 | 2024-11-19 05:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8981afd3-5c6a-3dca-99a3-44fb63fd9d0d | -7.47046 | -47.36776 | 2024-11-19 05:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f289d1a5-adb0-3673-acd3-f1b20851b178 | -9.51192 | -47.2458 | 2024-11-19 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0ee2498-01c9-3a6d-95cf-33364b1d1a6d | -10.45968 | -45.0649 | 2024-11-19 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f2ea2b7-e109-392d-9909-b0b5e5e54f28 | -8.26799 | -44.02771 | 2024-11-19 05:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0b9d8b0-93fb-31c9-9e45-0a448448b369 | -9.06884 | -49.21578 | 2024-11-19 05:10:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf75a933-aa49-3f9d-b1dd-ba2110c222ef | -8.26623 | -44.04156 | 2024-11-19 05:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c3cb846-4f4a-3017-96a5-e80516065ca0 | -6.05196 | -46.60475 | 2024-11-19 05:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7067ca1b-7c30-3c82-8617-890b44550672 | -8.00531 | -44.38755 | 2024-11-19 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63af7de1-b4b6-3f6a-ae51-db584e588e7b | -9.50602 | -47.24485 | 2024-11-19 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0499879e-51ce-3eb8-9dfe-3b456d9d6f7d | -6.38873 | -44.73621 | 2024-11-19 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2fb58d76-121e-358a-90c3-ece47c09c9d5 | -10.19346 | -58.81897 | 2024-11-19 05:10:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1baab2b-83d8-336a-96a8-5586050bca1a | -10.241 | -49.58723 | 2024-11-19 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a4c40d8-baac-3feb-872b-7920ce2fdc3d | -6.04747 | -46.6044 | 2024-11-19 05:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e436fdd-b13b-3feb-8c08-d04692b56510 | -6.29014 | -46.1255 | 2024-11-19 05:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d49a3a8-df9b-3c62-9134-98064f58d69d | -10.45964 | -45.07367 | 2024-11-19 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31bc06f6-9df8-32cb-b6f1-ae05ae7972af | -11.41884 | -51.27768 | 2024-11-19 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2d3b824-2084-3634-824c-b486613fd72d | -10.85454 | -47.65641 | 2024-11-19 05:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a893e1b7-457f-3052-b639-6e0dfb78072d | -10.46035 | -45.06742 | 2024-11-19 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab51bf5e-2beb-3e1f-85e8-e2857e0aeeb6 | -7.99394 | -44.36634 | 2024-11-19 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8eb3202-409d-376a-b790-dc91accf1b77 | -10.2406 | -49.59029 | 2024-11-19 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 513d4a83-93d3-3748-a2ec-3a4a7141fc87 | -6.48364 | -47.50373 | 2024-11-19 05:10:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da001d2e-ff64-35e2-ac25-376aecd41d46 | -10.258 | -59.13583 | 2024-11-19 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2961f131-3dc4-30c9-b389-a1fe7218bf2b | -8.00449 | -44.3939 | 2024-11-19 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4c9fbf3-1edc-35b5-955a-9c2c7b98da1c | -8.00085 | -44.36742 | 2024-11-19 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3888845f-a50e-36bb-8829-900b8deabc82 | -10.85508 | -47.65212 | 2024-11-19 05:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e2a9f25-6401-34f6-9cc0-4337b1b3dff6 | -8.00436 | -44.39304 | 2024-11-19 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9256d0fb-7716-3514-9489-cdf3a0c75a8b | -7.47565 | -47.37239 | 2024-11-19 05:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 419bd947-b58f-3946-9fa2-cd7f6e5eddd3 | -8.26566 | -44.02264 | 2024-11-19 05:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e95010c1-9569-37bb-a7c4-4c8d76e30985 | -7.92651 | -63.51949 | 2024-11-19 05:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5403b12f-5d94-3f7a-9e2f-854ac8ae86ee | -8.26711 | -44.03467 | 2024-11-19 05:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a6e336b-f766-3af9-914a-c4b4c8459592 | -6.48416 | -47.49999 | 2024-11-19 05:10:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0340feec-dfa8-3d6a-b116-2496981a4f6b | -7.14542 | -49.30085 | 2024-11-19 05:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fb88a75-971e-308b-8315-c03e7c310055 | -8.00003 | -44.37378 | 2024-11-19 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5837d739-6ad8-3d24-8102-e8d091a972b7 | -6.3953 | -44.73763 | 2024-11-19 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf17d0d5-e54b-3b49-b4d6-c582b398bdb5 | -9.06843 | -49.21883 | 2024-11-19 05:10:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ece9aa9-f695-3b93-80b6-6cee08396a64 | -7.99922 | -44.38015 | 2024-11-19 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2f605fb1-a64e-36a0-9377-d138182be40f | -7.9272 | -63.51545 | 2024-11-19 05:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8175b346-2b78-3b3e-bb89-17467fd6b084 | -10.26136 | -59.13636 | 2024-11-19 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53c717c8-da4f-3e1f-b9d9-f62a947cefa5 | -13.25356 | -56.81696 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92158d70-0cd4-3a64-92c0-8b9c7fe16918 | -12.5846 | -62.00431 | 2024-11-19 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6de4d8b9-47b2-390b-97c5-3ec9d15d7322 | -13.25012 | -56.81644 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a5744352-40de-3fc7-b923-b946f67fd80e | -16.4502 | -55.97709 | 2024-11-19 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6327dc70-6aeb-31b9-b6ea-4fd8207da7ff | -13.25126 | -56.80881 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6a433074-a2b3-3fcb-99be-410a682c89da | -13.25701 | -56.81748 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9cea4a0-1d73-39ff-943c-11f05bb3f9cd | -13.26045 | -56.818 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfceb3d2-72fd-3652-9e19-c74e40d02dd1 | -13.26447 | -56.81471 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1138eef-0f2e-363d-a5c6-33bab7907203 | -13.26102 | -56.81419 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 39dcffb2-7fff-3be8-b911-aa596fc3aff9 | -13.25069 | -56.81263 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f72b57ff-1aa1-3a4d-88b0-5720e272f792 | -13.25471 | -56.80934 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a664bf6e-0ee5-3165-96a0-07ba80ca2375 | -13.25414 | -56.81314 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| edaa9963-6363-39ca-a21d-f7befb3b0547 | -13.25815 | -56.80986 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 72424130-a12a-396f-853b-682b164d48dc | -16.44959 | -55.98158 | 2024-11-19 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5dec70ea-54ca-3bdc-9584-32a51c992fac | -13.25758 | -56.81367 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4bc89d86-737c-3257-9056-66e1550a8748 | -13.26159 | -56.81039 | 2024-11-19 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 677922b2-6c13-3664-9d1f-76b40668ab9d | -23.95859 | -54.11798 | 2024-11-19 05:14:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 35030ac3-64ff-3246-bc10-60a0e612ddbc | -23.97362 | -54.15015 | 2024-11-19 05:14:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| bfd62b24-907d-3d86-971b-50d8e6f2f06a | -22.30125 | -49.76335 | 2024-11-19 05:14:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |


[Clique aqui para ver as próximas entradas](README46.md)
