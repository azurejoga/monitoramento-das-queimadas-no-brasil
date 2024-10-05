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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0746a76-2b33-3145-85bc-c8af790c15bc | -11.15981 | -46.50758 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0744d398-f83f-3f4c-827f-6b761d33bb6d | -11.15916 | -46.51104 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c8f02d35-dbdb-3f97-bd0c-5b03059d31fa | -11.1585 | -46.51455 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 3b90d605-87c3-3bd7-aece-c34a06805206 | -11.13742 | -46.51463 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88dcd7f2-c1d6-38c1-85c0-739cfcdf8dff | -11.12158 | -46.51482 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1a81017-207c-3643-9beb-6675c3344cf0 | -11.12098 | -46.51797 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f15d6d8-5f58-3dea-96ae-c7d3f1dcb3b8 | -11.11709 | -46.51074 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d9033663-7a03-37ab-8e66-30ec6c53168d | -11.11648 | -46.51394 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3685b4c5-412f-3cc9-a7d2-01a2834e9ba0 | -10.92282 | -46.67115 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3cfee9ec-1453-3f9b-9676-7fbb613672f9 | -10.92224 | -46.67424 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 237ffb21-4a25-39fc-9a7b-cca8b63abddf | -10.91708 | -46.67328 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7da3be07-ce11-38e6-a933-7cf82568f871 | -10.9165 | -46.67638 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| acb5a6ca-083a-3d86-b541-2e12fdad894b | -10.91133 | -46.67544 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3abc30ef-94d4-3550-b0ff-c45de33e51e0 | -10.88743 | -46.63239 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99c48cbd-03d4-378e-91dd-9a4937b1e57d | -10.88684 | -46.63554 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4ca29b9-c3f2-37af-832d-c5da7c848cb0 | -10.88411 | -46.62183 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3227405f-2a19-3e02-96f3-5dee9201c1b4 | -11.72041 | -47.10081 | 2024-10-05 03:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fd6b3b4-7ab7-30e7-9762-dd68088ac9b8 | -11.41563 | -47.19576 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65f64470-6046-36c9-87ea-b1d53216b154 | -11.41482 | -47.19276 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bd8dc9f-c70f-370d-b42e-da2803c65541 | -11.41415 | -47.19617 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| efe826b3-a16c-36a1-b10e-35af377301eb | -11.41217 | -47.2064 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef7dcb3d-589c-3712-add4-231a728f04cb | -11.41152 | -47.20971 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c830b2b0-b879-30e7-9677-125f7383a858 | -11.3595 | -47.20236 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8265179-5b26-3683-801e-70f7e273c818 | -11.35885 | -47.20578 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 06b8b8ac-acbc-373c-a4c2-f2502fc5bdc6 | -12.84152 | -47.47962 | 2024-10-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93f23fea-b9f7-3842-b7e2-b6dc8092903c | -12.84087 | -47.48298 | 2024-10-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d696bdb7-388f-3ada-a4e1-8cf55571af04 | -12.84022 | -47.48634 | 2024-10-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97b0523a-c014-3b3f-9db9-b8a4cfc016fe | -12.83627 | -47.47857 | 2024-10-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 011aaafe-2552-3bcf-b05d-b3e11ab0491f | -12.83562 | -47.48193 | 2024-10-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecfe8f0d-f4e2-3d43-98a6-ded8d72560db | -12.8264 | -47.47322 | 2024-10-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b433ed59-ac21-3d8a-81fb-b66f77c2f767 | -12.77952 | -47.43587 | 2024-10-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0eddd424-0b2e-3e56-98a3-8e821eb5b242 | -12.7791 | -47.43637 | 2024-10-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d173515-4bfb-3c8c-9695-09baac86bd6a | -12.77889 | -47.43922 | 2024-10-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da227618-f948-33d2-8d02-27f185e1db00 | -12.38036 | -47.67878 | 2024-10-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69d0acac-a371-3cc1-ba28-0c0fb585b580 | -1.19612 | -46.58629 | 2024-10-05 03:49:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fdf8d02-75a3-3740-9013-d33742a5e3fc | -1.19537 | -46.59083 | 2024-10-05 03:49:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09865f8b-40ab-3e61-977e-8c3b85863fe6 | -5.99437 | -47.45407 | 2024-10-05 03:49:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d7dde81-21d3-360b-b045-2a5ce12493ca | -5.98545 | -46.65667 | 2024-10-05 03:49:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37a83acb-c7a3-3e3d-82c8-9a4c2a59b526 | -5.9836 | -46.65577 | 2024-10-05 03:49:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 60aebfbd-0dee-3b2a-a925-2f189e09b541 | -5.97986 | -46.65556 | 2024-10-05 03:49:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ded7741f-a919-3fa9-ade8-2f95e498becd | -5.69599 | -47.38563 | 2024-10-05 03:49:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e91b36c0-03df-38aa-9545-75f8b26ca84d | -7.46355 | -47.17845 | 2024-10-05 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e27d9c1-687b-36b3-8e48-bb9b301f26d4 | -7.46283 | -47.18241 | 2024-10-05 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d75f12b6-178c-3e0d-b6d1-af1253a7a604 | -7.4621 | -47.18637 | 2024-10-05 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4dcabdd5-b4ee-3aa8-a8b9-7073b65edbc4 | -7.24779 | -48.00422 | 2024-10-05 03:49:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 23ad3f99-3a0f-313c-b9fc-a420453fe6fb | -7.19282 | -47.8342 | 2024-10-05 03:49:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bac099b5-8f39-32a9-be46-2af8d111ed8f | -7.1896 | -47.83286 | 2024-10-05 03:49:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0e9f2a03-7419-3a6a-b71e-94c49d05b4b6 | -7.18686 | -47.83326 | 2024-10-05 03:49:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd09d0ff-0c94-3a97-bda0-83138f70d5f1 | -7.18603 | -47.83772 | 2024-10-05 03:49:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d248249-bc89-383e-965e-117b1943bf43 | -8.86839 | -48.32784 | 2024-10-05 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b500966b-0cc3-33d7-a44c-fc4a366768a1 | -8.86327 | -48.32236 | 2024-10-05 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ac5c50d-4ba5-3692-a9f7-8b9c86355f5f | -8.5974 | -47.131 | 2024-10-05 03:49:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1f3a9c0-85e1-3b5b-b30b-00fbe272aebb | -8.59232 | -47.1318 | 2024-10-05 03:49:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dbdf330-1ede-3523-9f2e-a666e4d21092 | -8.59165 | -47.13549 | 2024-10-05 03:49:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2ac7ac1-d95e-3325-bc85-3b759369e8e6 | -8.49771 | -47.30133 | 2024-10-05 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f13c02a-ff23-32dd-8d1f-beb83ba5288a | -8.49702 | -47.30503 | 2024-10-05 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1011c962-34a7-345d-badb-340cc9a1920b | -8.4914 | -47.30403 | 2024-10-05 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7625a526-c8c5-35c9-979d-2b76e7dcb571 | -8.49019 | -47.31054 | 2024-10-05 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e49a72cd-6f60-3cef-9b3b-0851c3f351a9 | -8.48954 | -47.314 | 2024-10-05 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68f95e46-7ff1-3883-881b-5c0789442b83 | -10.85086 | -48.13021 | 2024-10-05 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aeabbee1-aaf4-36a8-b272-45abc896f873 | -10.72807 | -47.73299 | 2024-10-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c47c4a01-750a-3ec3-a619-16fc78626b9a | -10.72732 | -47.73694 | 2024-10-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 310abedd-f98c-3a38-a45a-cf2837026b07 | -10.72393 | -47.72456 | 2024-10-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ee425bd-ca22-3483-ba9e-f070adcf98e6 | -10.72324 | -47.72817 | 2024-10-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| deeaa9b7-82d0-391c-bafa-f97333ff7709 | -10.7225 | -47.73207 | 2024-10-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2ada73f-cd2e-3644-bcc6-d4ae9de7ad2c | -10.71836 | -47.72364 | 2024-10-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b00f0f01-d022-3335-9ad6-a662e4834ce5 | -10.7177 | -47.72709 | 2024-10-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20ead513-67a6-39fe-800f-cedc2a2a1cd6 | -10.71701 | -47.73071 | 2024-10-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65541d92-7993-3871-b23c-d74889b20a56 | -10.60032 | -48.05265 | 2024-10-05 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f1a8cec-8c10-3b0a-a32d-e6f9016c7993 | -10.59946 | -48.05724 | 2024-10-05 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6c00074-e177-3f3d-ba56-9d8b64e41130 | -10.59686 | -48.05102 | 2024-10-05 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0243f4ee-b105-3af1-9287-dc8cc6ef9ab5 | -10.59606 | -48.0551 | 2024-10-05 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5c45296-c949-356b-8345-3d87e59e4de0 | -10.59472 | -48.05117 | 2024-10-05 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50e08d16-b0c6-3706-9d74-cea32bc1b1ef | -10.4613 | -48.34405 | 2024-10-05 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c634ad2c-8036-3f0d-b54f-fc2897ef5ab4 | -10.46048 | -48.34827 | 2024-10-05 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a22ff927-4cb5-3457-801e-92038f532bdb | -10.23898 | -47.73533 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd0da717-8019-3670-8de5-70465d102256 | -10.23829 | -47.73904 | 2024-10-05 03:49:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df100736-f6f5-3e66-937f-72191aa77c40 | -1.26471 | -47.66716 | 2024-10-05 03:49:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| acb5b405-98fb-3f5c-a406-8d6a8c86a53f | -1.06094 | -47.93079 | 2024-10-05 03:49:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2e7e064-105b-3f81-bca7-e54e87a79df0 | -1.06 | -47.93639 | 2024-10-05 03:49:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b80e994f-5e6d-3da3-b0bb-7673c7f2ac35 | -1.05534 | -47.92892 | 2024-10-05 03:49:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e464616f-47ed-305c-9ca6-acb14fefc02d | -1.05444 | -47.93453 | 2024-10-05 03:49:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6e586f2c-39e9-3845-be72-b761b0d807fd | -1.05437 | -47.92981 | 2024-10-05 03:49:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1ca83635-fce1-3b15-87af-f403912316b9 | -1.05343 | -47.93539 | 2024-10-05 03:49:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 20eef081-57ce-3fcd-9edc-634c8c5ea4c4 | -0.73567 | -48.04282 | 2024-10-05 03:49:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 009a2c9b-4004-3644-8099-32a2942242b4 | -7.751 | -49.21858 | 2024-10-05 03:49:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15965120-97c3-3517-a3f1-1c1aa272b1b1 | -7.74461 | -49.21734 | 2024-10-05 03:49:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44d23a83-bee8-3b16-b675-50d1334e7237 | -7.74361 | -49.22267 | 2024-10-05 03:49:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85cfaf41-6ee1-3ccb-81ad-3c67edebf106 | -7.73822 | -49.21611 | 2024-10-05 03:49:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d758053a-d864-346a-bfe1-f0734365b23e | -7.73722 | -49.22141 | 2024-10-05 03:49:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d82678aa-3102-3e30-91b4-0d326959dd13 | -7.3676 | -49.60902 | 2024-10-05 03:49:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb10f405-98ae-3ef2-a9a1-e3b763400dc6 | -7.30699 | -49.26033 | 2024-10-05 03:49:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a4bf1a8a-1286-357a-8c9b-7942c203fa8b | -8.98612 | -49.81831 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f3bd37dc-3a2f-3439-a200-a635732d0f9e | -8.98071 | -49.81155 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0de48a0a-7b8d-3970-8eca-31bb0a4aee0b | -8.98021 | -49.81532 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8cc7578e-6703-3750-85d2-f4a9cc82abae | -8.97963 | -49.81706 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e3b92e48-5817-30c9-a5e0-a1bc95f135f4 | -8.97916 | -49.82086 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| cffc60e2-adf3-3a02-b524-bc27ede27c5a | -8.97853 | -49.82261 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4f92e942-8070-354f-afab-ceb820bbd274 | -8.79838 | -49.95644 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 17a603b9-b9a3-3bd4-9797-b904c68b6414 | -8.79727 | -49.96218 | 2024-10-05 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README43.md)
