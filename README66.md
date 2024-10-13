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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74c31792-3ade-356b-b44e-d74309ef449e | -6.92364 | -49.94839 | 2024-10-13 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00545c2b-a9f5-39ca-a3b2-299ba5c19694 | -6.91251 | -51.02443 | 2024-10-13 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e081631-4f4f-343c-a1c3-306c96ec5171 | -8.10572 | -51.0983 | 2024-10-13 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 639240b0-b34f-3b9b-b0bc-55e48d2d1a61 | -8.10515 | -51.10187 | 2024-10-13 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52b48bc4-d247-3f46-b556-dbe609e528ad | -8.10065 | -51.10854 | 2024-10-13 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 177e7948-7026-32e6-8556-12d6957fd4fa | -8.2859 | -50.30909 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0059bc4-f90f-319b-9dab-55c6584bac63 | -10.82296 | -51.13691 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be361f4f-3253-39e7-8a6a-e1ea38c0e6dc | -10.8224 | -51.14043 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8d8a270-3b11-3d20-bbe6-739fafefc525 | -10.82184 | -51.14395 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f26ec9f-f515-3074-86ac-1e292f4e98d5 | -10.82128 | -51.14748 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7ae00b6-de4c-314f-ae05-6eef722eb184 | -10.81964 | -51.13637 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d51556ac-57d2-3f88-b99f-93c19e0cea35 | -10.81908 | -51.13989 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e3a44f7-5d69-37f3-9217-2ea4ec28d40a | -10.81852 | -51.14341 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5670bc93-70df-3106-8693-41f2467dc762 | -10.81796 | -51.14693 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15a26155-1edd-3aea-b02f-01ab42fa563f | -10.81577 | -51.13936 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3b35662-1071-3b71-ba19-19bc4151bb02 | -10.81521 | -51.14288 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50d4650f-9c0b-3d3a-9d09-d49e8c3fda92 | -10.81245 | -51.13882 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bfd42e0-4b17-3465-b7d0-6037a2882a8f | -10.79588 | -51.13614 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f30ea75d-0b87-3e2d-99d4-c3e8c3aee29e | -10.79312 | -51.13209 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26381b58-5f64-348c-a34b-45947a751680 | -10.79093 | -51.1245 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 813e526d-d5f7-3318-a2e8-dd34b70ade3c | -10.78981 | -51.13154 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7c7a0c6-83fe-3199-b2c3-7ef962d57970 | -10.78762 | -51.12396 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd333a33-a476-33e0-974d-eeeee2130722 | -10.78706 | -51.12749 | 2024-10-13 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd97e285-651d-395c-a71c-8040fb103020 | -10.70128 | -51.13115 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c71ea0e-d00f-3dd4-95c7-6cfa58b2cba9 | -10.66781 | -51.53322 | 2024-10-13 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7951125-aef8-3a62-a9e6-a400231e3fe8 | -10.66724 | -51.53679 | 2024-10-13 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1ac8676-0dcc-3a77-abea-83225abeab5e | -10.65346 | -51.80813 | 2024-10-13 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4027201-1bf1-3397-971b-2514e3efb45c | -10.64817 | -51.14422 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31d68515-c0b9-3f29-9c6f-c99cc675f3e4 | -10.64486 | -51.14368 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8fd360b-969b-3662-945e-c2a2596c686f | -10.64212 | -51.13953 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7db9e05-ea7c-344b-92e3-ff4a29dc072b | -10.64156 | -51.14305 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60204fef-a280-3c2f-b7c8-4c03dd6a5905 | -10.63936 | -51.13547 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e027f9d6-4321-3c84-a7f1-5a947cb6dc34 | -10.60178 | -51.77326 | 2024-10-13 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca4e2531-2315-3000-a316-6c3543aeaaa8 | -10.59843 | -51.77271 | 2024-10-13 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dde12a13-77e4-367b-9419-9558f1cd03b7 | -10.59448 | -51.77581 | 2024-10-13 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba5e01f8-43f7-3f48-836e-8d4c421f8f1a | -10.58777 | -51.77471 | 2024-10-13 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8556fffc-215f-3686-bc6e-ab73ce8e98e0 | -10.55333 | -51.05652 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 376bac97-7b93-30be-9385-f0931320b75f | -10.55002 | -51.05598 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e32a6b01-07d4-302e-a0e5-493caa6caf57 | -10.54702 | -51.05194 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2440922a-2fe9-3e7f-a070-18047042e480 | -10.54647 | -51.05546 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e415a22-6056-3007-abdf-05b542ded9f3 | -10.42075 | -51.65113 | 2024-10-13 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01785715-1027-31c2-aa0e-4c712f577e40 | -10.4174 | -51.65057 | 2024-10-13 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86276b73-3e1a-30ec-bdd0-ea5d8db783ef | -10.06544 | -51.40184 | 2024-10-13 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd1994ce-8768-3473-948c-5f71df56d646 | -10.06487 | -51.40541 | 2024-10-13 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ad1fa09-217c-3317-86a5-b84263f05b16 | -10.05819 | -51.40433 | 2024-10-13 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8f45c05-9027-3d26-be49-c3429ee90db6 | -9.7494 | -51.93386 | 2024-10-13 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1c24bcd-459d-3d27-8680-27141b83095f | -9.45653 | -51.79569 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a79c46d8-c01d-392a-9157-0bdce4f925d3 | -10.43292 | -50.82792 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0aeaf1cc-9119-3a8a-b972-2a08e2d94dbb | -10.43237 | -50.83141 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fac9fd8e-fccf-3181-bbc8-7ead79947369 | -10.42223 | -51.0024 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 730b672e-455b-38e0-997c-07550195f42f | -10.41947 | -50.99834 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91dd725d-57a7-336a-844c-798d7c91a665 | -10.25142 | -50.59822 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25bebaa5-dbeb-3c77-bef9-6fe5fa8ed77a | -10.25087 | -50.6017 | 2024-10-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26f3536f-5de8-32ed-b59f-11d15873bf0b | -9.73313 | -50.64631 | 2024-10-13 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ec6820f-ef88-38d8-8a97-b78aadac6e12 | -9.72982 | -50.64579 | 2024-10-13 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99422067-046f-399b-8a78-d966ad0c68e9 | -11.50455 | -51.81446 | 2024-10-13 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57202d6c-c8fe-388e-b31a-d63a0881630f | -11.26951 | -51.43112 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3846351-7e59-3969-b875-020f37c598df | -11.26894 | -51.43467 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51222941-7b4f-379c-ab6e-0d9eb467c990 | -11.26561 | -51.43412 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2c771a9-66db-3654-ad93-03d28647259f | -11.26229 | -51.43358 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e21b196-7b76-39c3-a8b3-deaa71dcea9f | -11.25233 | -51.06992 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef44b304-6875-3006-8d1e-f0ceb852d237 | -11.24902 | -51.06938 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76d96321-8efb-3935-a274-b70ee9dd12e9 | -11.24846 | -51.0729 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7072b630-4aaf-3a69-922d-d53342d35fd6 | -11.07634 | -51.57508 | 2024-10-13 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66d49195-c17a-3c5c-96d5-7fd62ed0eac9 | -11.27785 | -50.95168 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b0fdc01-b9a7-36db-ac0b-be682865c818 | -11.2773 | -50.95519 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 480613e5-3c0f-3b74-a0a3-90e1835f4fca | -11.26743 | -50.91046 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa8b2ac8-d76b-33f6-b6be-b0932ad63276 | -11.26688 | -50.91396 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29523152-eef1-3453-bd55-05f50c2defcc | -11.26632 | -50.91747 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6abf115d-38be-3da6-970e-a55fc9e05978 | -11.26413 | -50.90993 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a652303-e577-39e7-8207-338326176e7e | -11.26357 | -50.91343 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ff2519e-146f-3cbe-95cd-25b62c4b3283 | -11.26302 | -50.91693 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0ec15e6-9f85-3fad-8be8-69b6a41c3744 | -11.26027 | -50.9129 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ad53722-b69e-39d8-8f7b-12a0fce81f2a | -11.25969 | -50.93796 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcfc6c35-cf12-3a17-aed2-83de0bbb203a | -11.25913 | -50.94146 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4906486e-1e78-3396-9336-77da33bf0bb8 | -11.25805 | -50.92691 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 059d6454-8ae1-3935-a7e2-26b8ac05ea92 | -11.25752 | -50.90886 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62d41c42-cdbc-3f2a-a2e3-ffc2cdf77f6e | -11.25749 | -50.93041 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9128139c-a57c-3d4e-94f4-7955b6dcef11 | -11.25694 | -50.93391 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07502073-3498-30d6-be8d-8ec7e1074a2a | -11.25638 | -50.93742 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4204943-348b-320e-85bc-cd80f14056ae | -11.25539 | -50.79371 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae43469f-92d6-3808-bac8-c454aea2f4a1 | -11.25484 | -50.79721 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20d5761b-fbcc-3c34-80af-ab39f3ca26d2 | -11.25477 | -50.90482 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abc29885-2f66-30ca-8da0-db300994c36c | -11.25257 | -50.89728 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2847ecb-f68d-379c-956b-3aebb9bf7e78 | -11.25202 | -50.90078 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a81c5910-1007-332b-8e6a-2e80588b6b02 | -11.2415 | -50.9458 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8692978a-d8a3-37c0-b3d0-796114352b47 | -11.24094 | -50.9493 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1899948-108b-3dcd-a841-2b036e6ec193 | -11.1837 | -50.94374 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13b2840d-5e6c-355b-b11b-7eff1865d667 | -11.18039 | -50.94321 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49fdfe73-f8f2-3009-bc1d-79e060111167 | -11.17984 | -50.94671 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55c05fee-f21a-3f59-8b08-1c0bce07c733 | -11.10251 | -50.81145 | 2024-10-13 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db38e6f2-3ee6-337b-9fbf-90002ed207e6 | -11.66658 | -52.61897 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 651d4fed-6fdb-3109-91ec-94b90ca25404 | -11.66596 | -52.62273 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cfdf489-87a9-30bf-96c3-ce9145608feb | -17.27405 | -56.73547 | 2024-10-13 04:42:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6967271e-b42a-3bb0-86b2-55dc10bac5ce | -17.07471 | -56.02126 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4c36d712-1018-3e64-af61-1ef7d556e453 | -17.07387 | -56.02599 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5622568a-1800-37dc-8572-b439d0461fc3 | -17.07349 | -56.00634 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f4dff4d2-5bb2-3123-873f-e82c53bf7fcf | -17.07303 | -56.03072 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a26e83a6-efa4-3a94-9fc1-b0704073bcb1 | -17.0718 | -56.0158 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 852503f6-e26a-3cfe-af61-2941cd614e92 | -17.07096 | -56.02053 | 2024-10-13 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |


[Clique aqui para ver as próximas entradas](README67.md)
