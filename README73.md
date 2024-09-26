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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6cc8d1b-6060-32df-9501-3e1d03f98b47 | -16.54768 | -46.9381 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 399cb64c-8ef9-399d-9f6d-2ab630c23353 | -16.54461 | -46.9995 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee6c43dd-4779-3761-a1e5-b761db4815ad | -16.54408 | -46.93744 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22ac1cbe-af55-3d08-96af-5063ec1f0ce6 | -16.54178 | -46.99432 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6470e9b1-ea9f-3940-95db-b19a95758c5e | -16.54103 | -46.99873 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 965a9531-397c-30e4-90d8-b26061cbb56b | -16.5136 | -47.00668 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b5b6354-64e5-3601-b091-7c1e7de40fb3 | -16.51072 | -47.00181 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2830f554-6613-377b-8587-11fe18bd2a84 | -16.50999 | -47.006 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e806fa00-30f9-3bc3-80e2-f02eb65891b5 | -16.50639 | -47.00534 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e692bc5-ff9f-3c28-9321-981a12a88a97 | -16.50277 | -47.0047 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9553b768-77dc-3f2d-b15a-272d931233dc | -16.49555 | -47.00338 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a4b62c1-3aad-3cdb-8bb4-c08e1a9b97b6 | -16.49121 | -47.00696 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8db6bf4e-5e3d-38f1-9862-358a8f4a5f1b | -16.48759 | -47.00631 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e280daa1-dfeb-3d4d-b73a-16eff7c375a9 | -16.47963 | -47.00928 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c39aa58-05af-34d5-b4bc-2068d29b014a | -16.476 | -47.00869 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97c9fd17-b4fd-37ab-8fa6-a827885678ec | -16.47164 | -47.01231 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d95098c-dbf1-3e4e-8b2e-e1c5f75e4af4 | -17.63982 | -46.43096 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1640cb73-12c5-3628-be2b-dd5a26535451 | -17.63566 | -46.43433 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee34a0ce-2cc1-32d4-a07a-51435c2e007f | -17.63486 | -46.43079 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 82df599d-85c8-3901-9b2d-dc00dfed2cac | -17.63419 | -46.43482 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 257f51fc-7ba6-3bc5-aa6d-cb2f45d1483b | -17.23666 | -46.28256 | 2024-09-26 04:08:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92a2f275-71a7-35a2-a0ae-27dbe4cf2345 | -17.23598 | -46.28656 | 2024-09-26 04:08:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 50d30a50-d047-3b0a-87c7-087f080b2f01 | -16.59156 | -46.94883 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c657f609-8401-3fbf-b924-10f4cbfc86b4 | -16.59082 | -46.95309 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89a2d8dc-3529-3804-a161-9742d62ee8a9 | -16.58797 | -46.94812 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53fe8528-3904-32d0-9fc1-5c28bfb38b7d | -16.58723 | -46.95238 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 480aeb03-2897-3ecd-9b3e-cf2c6970c832 | -16.58438 | -46.94742 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba94e0f3-f471-3649-a876-87c93b94a8be | -16.58138 | -46.96464 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03360fec-6319-3288-b2f7-6fbd9232fa35 | -16.57719 | -46.9461 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3aa94a8a-7d63-3d68-9274-6ca5733436de | -16.57551 | -46.97698 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a04544a9-4cd7-3ac6-b545-a5991726f034 | -16.57475 | -46.98129 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6cfd8ae1-35c7-3016-9bb0-233d9cb34136 | -16.57191 | -46.9763 | 2024-09-26 04:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a2771dc-d178-31ef-aeb5-98bb23b9c1e6 | -17.89214 | -47.03034 | 2024-09-26 04:08:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a658da4f-dd74-3919-a72e-123ec12a533f | -17.8914 | -47.03459 | 2024-09-26 04:08:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| db908278-6ca1-318c-98f0-1b41115c813f | -17.8886 | -47.0296 | 2024-09-26 04:08:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3babd640-b574-358a-8716-bd382d62257f | -17.50395 | -47.01074 | 2024-09-26 04:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0508f19b-f6aa-3281-9fa6-bcdee8501bc4 | -17.50324 | -47.01488 | 2024-09-26 04:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a02648c-9499-3e2b-9efb-a1a360b2cd86 | -17.41637 | -46.77995 | 2024-09-26 04:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b2563dab-552d-32c5-9b50-8c53c4534583 | -19.27459 | -46.50968 | 2024-09-26 04:08:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b8aaf96-d5f9-3ffb-834e-9cc4f1f7b31c | -19.27392 | -46.51358 | 2024-09-26 04:08:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddfb2324-81cc-3f9a-a53e-6438e4b4fb94 | -18.96197 | -46.5942 | 2024-09-26 04:08:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0333b84a-5727-3fbd-a503-03700acfecb3 | -18.78472 | -46.62877 | 2024-09-26 04:08:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b209e027-c507-3478-81ed-06d3d71107a9 | -18.5993 | -46.41512 | 2024-09-26 04:08:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f97c8793-50ef-38da-80c1-92d3869de5a8 | -19.07208 | -47.28587 | 2024-09-26 04:08:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c52ad331-4127-3d7a-b82a-ecbda551c696 | -19.04241 | -46.80298 | 2024-09-26 04:08:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6880a86-483f-3c7d-ab8b-9e06e472f296 | -19.03895 | -46.80223 | 2024-09-26 04:08:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d90bf61-afa7-3d94-ad16-b07c4df889d8 | -18.66158 | -47.16079 | 2024-09-26 04:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 577474f1-36df-3525-9954-388b5eacedfa | -18.56388 | -47.24428 | 2024-09-26 04:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8f8794d-acc5-3387-b973-7e979b8b45c9 | -18.56316 | -47.24851 | 2024-09-26 04:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd210118-afe3-30cc-a642-ff73a57f9c22 | -18.55961 | -47.24778 | 2024-09-26 04:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cbed299-3e92-3f73-9982-aef7eb1dcca9 | -18.52836 | -47.11035 | 2024-09-26 04:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3db1fe5-a225-32dc-af2a-f4db2cac20c3 | -18.51566 | -47.09932 | 2024-09-26 04:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3bb86bcd-bbcd-3584-8206-69ab84d88184 | -18.51211 | -47.09868 | 2024-09-26 04:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2ccd8183-7ab2-3f44-a8a3-15fdd774e9d4 | -18.50783 | -47.10228 | 2024-09-26 04:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99fe466e-ce3e-306d-be9e-f1cc105775e0 | -18.5071 | -47.10647 | 2024-09-26 04:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd33659d-d839-3af3-952a-2cd65c86f90c | -18.44842 | -47.17608 | 2024-09-26 04:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee949aa5-0b7b-3556-9b51-56b66ef7630e | -18.3541 | -47.56919 | 2024-09-26 04:08:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33dca7a3-f6b9-3def-aa08-8750f5f4518b | -18.08679 | -47.46328 | 2024-09-26 04:08:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd1cb2af-8abd-32a5-bb71-08a551293f44 | -18.08317 | -47.46264 | 2024-09-26 04:08:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f03132b-fe88-3552-81cd-c06c4091209b | -19.651 | -46.87775 | 2024-09-26 04:08:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 339ace72-e435-311a-b9d7-4058d53a8e61 | -19.56588 | -47.79218 | 2024-09-26 04:08:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 408256c7-c02f-349d-b7b5-339d8020c441 | -12.18442 | -46.75322 | 2024-09-26 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d341a5a6-3faa-3496-baf3-59991ef83810 | -12.18145 | -46.74784 | 2024-09-26 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e05d1e33-ed30-3022-b52d-f16c29312a90 | -12.18064 | -46.75256 | 2024-09-26 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc45d860-86cb-356d-982e-c9095dd02574 | -12.17768 | -46.74715 | 2024-09-26 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85618849-f057-3936-a10b-f6ee9a64b606 | -12.17687 | -46.75188 | 2024-09-26 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f772044-e0d5-3afb-92e8-a84647b4701f | -12.17472 | -46.74178 | 2024-09-26 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 535675ec-3c85-3a70-9521-d1ef9c6a13bc | -12.17391 | -46.74646 | 2024-09-26 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d320ff7-f80c-3668-88e2-d5d86d507e69 | -11.84472 | -47.71854 | 2024-09-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4503877-6933-38cd-8627-fd6b1282ccc9 | -11.8441 | -47.72213 | 2024-09-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73e626c3-41f6-368b-9705-c4ae5a627f12 | -13.41342 | -48.04926 | 2024-09-26 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7614266-e97e-3eb5-bc0a-f01ec089e4e9 | -13.40942 | -48.04852 | 2024-09-26 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 931da1f6-3d54-3ace-8775-8df5ed84a947 | -13.40607 | -48.04407 | 2024-09-26 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac743e38-d59c-3faf-91b9-3ea6c95a0228 | -12.40956 | -46.42085 | 2024-09-26 04:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79381423-553a-3d42-a147-41cabfda8cf7 | -13.58263 | -47.65636 | 2024-09-26 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a946bd6-662b-3204-86ba-e4b4e8b37525 | -13.56589 | -47.70621 | 2024-09-26 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4ec275fc-0ebd-3215-bbd6-816e47dd8ef6 | -13.56496 | -47.71152 | 2024-09-26 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a08cb9cb-3572-38bf-bb97-9409bd31d0fc | -13.42808 | -46.93377 | 2024-09-26 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e3e511b-d677-30e2-a22a-91cd2e34e23e | -13.42723 | -46.93861 | 2024-09-26 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39ed5b97-7e49-3887-bff2-6aa4efcfcc9d | -12.97829 | -47.19532 | 2024-09-26 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8227090-5078-3b95-85b7-36ef7a2982ad | -12.91731 | -47.70671 | 2024-09-26 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 570c47cc-a3c4-3e0c-af37-00b9f1bb4969 | -14.15189 | -47.81163 | 2024-09-26 04:08:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 32f35c9a-8e72-3d04-887c-adef36cea962 | -14.02551 | -47.93177 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b39ffa6-0dc5-39f5-9039-a9a2037edb36 | -13.83396 | -48.03794 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b0c0179-12dc-3c43-9cec-dd5ae1800564 | -13.83 | -48.03711 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6bf69224-4d8a-3dae-a5af-7ba9208cc29c | -13.82599 | -48.03658 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe70e5a4-1a92-3b5a-a033-adb5947d1c47 | -13.82509 | -48.04166 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 658bc6ff-f65f-3016-89a6-b53ceb0a4c12 | -13.8235 | -48.05066 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96f751c2-d721-33d2-9fa8-1321c55d66dd | -13.82324 | -48.12197 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3deb770-524e-38fc-83c7-543eedac56e5 | -13.82197 | -48.03614 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 043cd0e0-75f0-3986-ba07-a6db584281eb | -13.82022 | -48.04598 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97437fe5-dc44-3b7c-bc40-f3251b2ff577 | -13.81925 | -48.12121 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5320b2a8-6ba5-3789-b4ce-89afad2de0a7 | -13.81859 | -48.12498 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c832c308-34bb-3793-8ee2-a2a754f61811 | -13.81792 | -48.12881 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0162b053-3de2-360c-8e5f-1e6a7883a8fb | -13.81627 | -48.04512 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af16be2b-6b0f-37b7-9a51-b0ff8354d033 | -13.80194 | -48.07948 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f09c5f8-b96a-3112-98aa-e4564a3b3745 | -13.80172 | -48.12708 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70f1a9cb-5aee-3d20-8ca6-5b69fa88a7b9 | -13.80134 | -48.08284 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 470dd44a-166a-3395-8776-b333cc7e824c | -13.79834 | -48.12286 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1721035-3bc2-3608-aa4d-6f94c5d6996b | -13.79548 | -48.09264 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README74.md)
