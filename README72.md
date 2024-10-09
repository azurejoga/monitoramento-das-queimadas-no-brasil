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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dd59306-ff27-37fb-ba40-8e1d987b50fd | -7.6327 | -42.40745 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fc6ebcea-88e4-30d6-814a-3d700e005182 | -7.61666 | -42.42298 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 273b1054-7d51-3917-806e-cbfbf9a1d14a | -7.61502 | -42.43356 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 69e008d5-1612-3dae-a8bd-c74a2f8ce544 | -7.15356 | -42.62288 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c3ab7061-78ab-3096-9ef3-bb8ccc257f3a | -7.15301 | -42.62636 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 16a23448-f886-373d-a118-6522dbc399bd | -7.15187 | -42.61192 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e9868e66-bd0c-3408-9b3a-73abfb15d8cc | -7.15133 | -42.61541 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 71b17cc0-4e67-3608-a9f1-1f13bfa79ceb | -7.15031 | -42.64373 | 2024-10-09 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1775f1ef-2b31-3e64-8de1-0a03afcfbf66 | -7.14646 | -42.64669 | 2024-10-09 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 289d47a3-fe10-3d13-b574-d56b8f4decb7 | -7.13929 | -42.64914 | 2024-10-09 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3169bb93-d33e-36be-9e65-5ebf28786ca4 | -7.13598 | -42.64863 | 2024-10-09 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2d543bf1-1e3b-35c8-a2bd-4b8311f7bb80 | -7.13267 | -42.64811 | 2024-10-09 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5ae9f573-1f25-32b8-9ffb-44590c17fe4e | -7.12936 | -42.64759 | 2024-10-09 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a9503b22-2b1c-37a7-8943-df0d357e94a9 | -7.12673 | -42.51164 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 02205783-edda-3c3c-8d42-9b7a09378fd8 | -7.1266 | -42.6436 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8fef9e30-5808-356a-b5d5-976b9f66201d | -7.12606 | -42.64707 | 2024-10-09 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 856f1dca-55f8-3071-8ca0-ae4cafae8d48 | -7.12275 | -42.64655 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 726f34c3-12e6-37b4-bb1a-3ba7508161e3 | -7.1222 | -42.65003 | 2024-10-09 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 85f18832-704d-3b63-b92c-3afd008e4479 | -7.11504 | -42.65248 | 2024-10-09 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2cb1d4c6-1a7d-358a-abd6-6db3b0911dce | -7.11173 | -42.65197 | 2024-10-09 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b42ce45d-1a78-3cae-b932-f1fff31a20c6 | -7.11119 | -42.65544 | 2024-10-09 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2e8867ca-38ef-3ce0-9a1a-8752213c5fa9 | -7.11051 | -42.61615 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c4ee2b3e-2cc1-3681-b026-e273ed17a5f4 | -7.10666 | -42.61913 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cc26a880-5544-3cf2-a35c-985179a0530a | -7.1045 | -42.63305 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4d208426-b29c-317b-b339-befdece66c07 | -7.10396 | -42.63652 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 529f562c-be05-3b09-afd7-5c76bdc64200 | -7.10342 | -42.64 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| aeba4a71-2a07-3e4a-b306-45c3eb22da30 | -7.10335 | -42.61861 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d4d435cb-0cee-32ff-9c2b-a2d63e8f01c9 | -7.10119 | -42.63253 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 15e3d7f3-fd3c-32f0-ae17-b113fbae8d30 | -7.10065 | -42.636 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9131f0d8-b4b8-3276-8b1a-54e1c2297fe2 | -7.10004 | -42.61809 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7d792ff0-d22b-38e0-9130-be0a0e97185e | -7.09958 | -42.64296 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b7cc62cf-380e-36aa-9222-dfd3c252b519 | -7.0995 | -42.62157 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2732b9ca-94f6-35aa-b34a-fb21d2bb13a0 | -7.09842 | -42.62853 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 475b5360-a4b9-374c-abb1-eccd607d18ba | -7.09788 | -42.63201 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85d98a5b-9882-39af-a689-50d5361486cf | -7.23462 | -42.29875 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4bcf8891-b7f7-308a-ae95-7e8c44332425 | -7.23184 | -42.29471 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ffa2baa8-a5c2-3500-b118-73a933be71f4 | -7.23129 | -42.29823 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 446ae8af-bb8e-36da-8142-782a444b492f | -7.09565 | -42.62453 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bfe2b0c9-5113-3484-8a95-e2246b8f0972 | -7.80512 | -43.82934 | 2024-10-09 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83841cdd-a83b-3c23-9d97-db2084a44da9 | -7.62778 | -43.70164 | 2024-10-09 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 77dd0fdd-c2d1-3397-9d8d-d1840e0157e7 | -7.35097 | -43.66794 | 2024-10-09 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e175291-d72d-3772-b0a7-7b0049c62c12 | -7.35042 | -43.6714 | 2024-10-09 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e0b4be5a-cf86-3217-b068-0ba6cc2922cf | -6.66669 | -43.49456 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b90fad08-082c-3f4b-9688-ca6c5e42f0c8 | -6.83822 | -42.81471 | 2024-10-09 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 806a58e6-0857-39c5-8fe1-1d85563bb366 | -6.83768 | -42.81817 | 2024-10-09 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 195ad67c-ed76-3dc7-9b65-84b6f99e636c | -6.83377 | -42.79984 | 2024-10-09 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4c6a1ce7-393e-3fe9-8f1b-0bd5cdede291 | -6.48591 | -43.34522 | 2024-10-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 633f9317-d690-3731-b1f5-10fcd3d3a776 | -6.48537 | -43.34867 | 2024-10-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe1c7d37-aa20-3756-9837-af2233820fa2 | -6.48483 | -43.35213 | 2024-10-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b442e2b4-2183-3eb2-8549-4150be8c1463 | -6.48404 | -43.24963 | 2024-10-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb0731ed-5707-33be-aa76-d6c148ab3b1c | -6.48316 | -43.34126 | 2024-10-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 269dd961-142f-3b55-a65b-de6cc98f9414 | -6.4708 | -43.22637 | 2024-10-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a17c2d4-2b70-3015-88dd-eaf421d181ec | -6.46996 | -43.33919 | 2024-10-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f3b3bebf-fb82-30b5-92bb-72621ea4747e | -6.48374 | -43.35903 | 2024-10-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e26219e-1dd0-38c0-846c-7473e9bbfdb4 | -6.65929 | -42.12622 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c7ee77aa-ad7c-34e2-8b2c-1c9f954aaf19 | -6.65153 | -42.13232 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c36fcd7e-3a96-351f-90bd-87f080c0e79b | -7.32584 | -42.21513 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 136d21ec-6527-3a1e-ab3e-c6e8a9e0ccca | -7.31038 | -42.24886 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 451e9697-973d-3931-a6e0-3c93fa669088 | -6.67085 | -42.09558 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3c8c0285-210c-39b0-8450-9b103d2131c8 | -6.65486 | -42.13281 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 028d8ffe-63b8-3c57-9917-ccae196d2f63 | -6.65098 | -42.13583 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3cdda3ff-6533-3bb0-aef1-f2b2150e1afd | -7.30535 | -42.23722 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 31b4f689-e6d8-35ce-8adf-939fa02702c0 | -7.3048 | -42.24077 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6237e0f1-fd2c-397c-94c3-410830f6b6d4 | -7.30202 | -42.23671 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf4c13bc-2f99-3392-ba5a-7a3b9dacfb3d | -7.29868 | -42.2362 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a55323de-04be-383b-bd1b-ff637f1de1a4 | -7.24172 | -42.29598 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f9fee73a-0ceb-3aab-b9ba-c7add8114107 | -7.23839 | -42.29546 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 99ecb2c9-65f9-324f-ad3f-74d7e6be6461 | -7.23785 | -42.29897 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cf223cad-5e3b-3d9d-b876-d5b92e4af022 | -7.22851 | -42.29419 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9a8578c9-75c8-3ca7-b600-c2665fa7b623 | -7.22797 | -42.29771 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2c689671-5a32-37ce-9d6a-3056ed25b12c | -6.67419 | -42.09605 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d4063fc0-2bb4-3741-9e4f-074bfd73a13a | -6.6565 | -42.12219 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 263bc498-8212-30a9-83be-720548d680c5 | -6.65044 | -42.13934 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 445e7cd7-2616-32d0-9bdd-250d32966a4e | -6.64765 | -42.13533 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 70d22514-ec0a-3252-be90-a8877f818511 | -9.3063 | -43.34869 | 2024-10-09 04:14:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 96019ff1-939c-3db6-9fc6-95c98073f878 | -9.18775 | -43.25821 | 2024-10-09 04:14:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ed073175-5fd6-3a15-a25b-9d3cf91d4ca0 | -9.15188 | -43.15968 | 2024-10-09 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f3c4c5df-c91b-3922-9b58-6826b1a364ca | -9.15133 | -43.16316 | 2024-10-09 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 44642c84-b8c8-3069-bbfa-dad3591fe1bd | -8.1488 | -42.96146 | 2024-10-09 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2c0f5fa0-1837-3ff7-8f66-eb126bac420b | -8.14826 | -42.96494 | 2024-10-09 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b4ee5891-f5bd-334d-b022-75152fda697f | -8.14549 | -42.96095 | 2024-10-09 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d57ac481-2406-3462-bd4c-2cefacbe0988 | -8.14495 | -42.96442 | 2024-10-09 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cfec04c4-5601-38fa-9e64-2e0d522f7413 | -8.09205 | -42.51534 | 2024-10-09 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b670fa0b-5e1f-3e48-ada7-369c9399c51d | -9.26159 | -43.52687 | 2024-10-09 04:14:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 732c1e2e-33fe-32da-b5f8-a5a3e60bd931 | -9.25938 | -43.51941 | 2024-10-09 04:14:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e8328558-e05c-38d3-a063-c284dfab8863 | -9.2583 | -43.52635 | 2024-10-09 04:14:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b21ef3f9-8e98-3996-a622-3552c598808b | -9.25775 | -43.52982 | 2024-10-09 04:14:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97e401ae-58ec-3425-8e6c-00612c9d9d0a | -9.25278 | -43.51836 | 2024-10-09 04:14:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 93196ec2-4ed1-3549-b3fb-70a01e3a5d58 | -9.24948 | -43.51784 | 2024-10-09 04:14:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 10d3266c-9b7d-3fa4-bac1-0fa518ad028c | -9.24894 | -43.52131 | 2024-10-09 04:14:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e3205033-5683-3b47-abc9-36ef30beab37 | -9.2484 | -43.52478 | 2024-10-09 04:14:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9710933e-7e90-387e-8e66-69e31ddbf6cb | -9.24786 | -43.52825 | 2024-10-09 04:14:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1f2c984a-d51c-398a-a3ff-80ac2735431c | -8.49575 | -43.91539 | 2024-10-09 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c1ef72d8-26a9-39df-b6ba-cb63d6d5e8eb | -8.13039 | -43.79615 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 84f19943-9abe-3239-9119-b9c51f0bae06 | -9.52817 | -42.99283 | 2024-10-09 04:14:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 112da07c-3618-36ab-8ac9-0ad5043022a5 | -8.00266 | -44.36515 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7aded07a-4551-3a94-8684-a7ee6b2e9c10 | -8.17061 | -44.44339 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07f222da-638b-3634-af1c-827722f4d171 | -6.16605 | -43.71245 | 2024-10-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 322afff1-008b-360f-ac01-6ae230accb26 | -3.46751 | -43.36269 | 2024-10-09 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb269714-4c10-3edc-a33e-18b4d72f2bdb | -3.46473 | -43.35869 | 2024-10-09 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README73.md)
