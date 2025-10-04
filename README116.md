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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2b77ba8-a594-37fc-9e9e-64083c647526 | -15.6029 | -52.4927 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bd5226c8-6719-38a4-81e1-05f550e36a53 | -12.87275 | -47.2859 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cf0f7dd-73ff-3c8c-bccc-5cb46293d5ce | -15.32087 | -46.30577 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 304f5460-ada8-3504-958d-bfa221ae6776 | -11.24921 | -47.80207 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8c91fc0c-8eb3-3896-86ac-395c8b753c76 | -11.45114 | -43.50168 | 2025-10-04 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e717786-4aa4-3006-ba04-695575c4a87a | -11.95821 | -51.47623 | 2025-10-04 05:06:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a1d9590-dc45-38fd-ad01-cb2a18deb32b | -14.66463 | -48.30924 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| dea2da01-ed11-3998-acec-88102ae5803b | -15.59455 | -52.4602 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 459dbd74-f1a0-37b3-b014-1f1e64fd8f81 | -15.23862 | -49.29899 | 2025-10-04 05:06:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6807d665-d994-3f5b-80d9-62f1197e7373 | -14.65898 | -48.31101 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 92fc7db0-70ed-33cd-9e39-53dbae26bfca | -13.99448 | -48.19402 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5693051-b89b-3c62-a43c-3b6a21c16ab4 | -10.22291 | -59.15364 | 2025-10-04 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24ab73cb-7dcf-334c-b4d1-91bba8516f7f | -15.21236 | -56.83382 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01df8943-c607-34e1-a95d-b7d879f59ce7 | -11.91086 | -46.37847 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0efb458d-71c6-3225-a29b-6535d1784628 | -12.71693 | -48.55216 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffc966cf-0b91-3480-a066-9cc6d91ef9ab | -11.55922 | -47.68241 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 475442c4-bbec-3ee3-b3f9-08ede27871f2 | -13.33504 | -48.08083 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8be42447-4f82-3517-b109-b5c230910447 | -16.04078 | -51.05293 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c17ef27e-a487-3cfd-8f7d-8d3e44de7acd | -15.32639 | -47.33197 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8783a473-a361-3bfd-9709-209cca4b8b02 | -16.82001 | -46.73018 | 2025-10-04 05:06:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e29edd38-ddcb-3df9-b33c-cc10f8a6d6ae | -13.76207 | -48.05443 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44b2f6d1-a0a0-3d20-ad4a-737f7eb4df7f | -9.90537 | -63.59259 | 2025-10-04 05:06:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90b424e4-0e45-325f-a1e9-213696eb5a78 | -11.16969 | -47.75623 | 2025-10-04 05:06:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ec78c58-9f64-3d99-b677-82bb9ab51c93 | -13.11367 | -47.84834 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8688354b-2f26-3ed2-9b03-5792260ac2ee | -10.33908 | -50.3174 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5073f3c-251d-3a20-9536-7e04a3a0ca56 | -12.47322 | -54.42842 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c46d081e-ecbf-34ce-ac0d-33858b971fde | -11.47899 | -45.01754 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f22c04ca-fdda-3205-a2ee-3e55ca446cf5 | -13.60187 | -48.17979 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d79158ed-29bd-3708-ba84-768dedfd7899 | -14.23105 | -46.0769 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fce94a73-38a6-39a3-b49b-104293f2c806 | -13.10828 | -47.84742 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1ddc9a89-8f56-335a-8a41-5b2da22cb1f6 | -11.08393 | -47.88457 | 2025-10-04 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cddf080e-852a-3b08-9aa5-cbedb3363c56 | -13.99485 | -48.1908 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d411448-e062-3be3-97a3-82a63af6a726 | -14.93698 | -46.85629 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c76503b8-1b39-380e-8768-90663276f0c4 | -13.45239 | -47.25436 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f07cec7-f09c-31e2-8399-c423bea81c32 | -14.65823 | -48.3174 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1ade15e9-ae3a-3484-9f79-b4a7b5d9e1e8 | -13.75132 | -48.05283 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1557418f-8e83-398c-a78c-c768e5f42c27 | -11.8918 | -44.99203 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62a5c959-c9f2-34a9-8d4c-4f8015677e20 | -10.76154 | -46.60226 | 2025-10-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8d5f8f74-856f-34e8-8fb5-263ba8d971fb | -12.93305 | -45.06981 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0df51498-a84b-3aff-9d39-9288a87e1bd1 | -11.34824 | -55.08591 | 2025-10-04 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abd7cf6b-a2a3-366d-a45c-6a22b999dc26 | -11.56982 | -47.66798 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c50c352-9dd4-3c89-b853-997b2e275c81 | -13.70635 | -47.34508 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbba392c-5f8c-31a6-91f8-fe521af6b8f7 | -14.69986 | -48.19587 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d5a2763-6566-358d-951c-8e623dc069f7 | -11.99702 | -47.19404 | 2025-10-04 05:06:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7db863f4-0e8d-3e84-8276-171e041e08c2 | -13.17952 | -50.92921 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 686f0963-50fb-32fb-81e6-b290d2b08c02 | -15.20569 | -56.83278 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45641317-e241-32a9-aee9-2adfdbe0e14e | -11.43462 | -55.04852 | 2025-10-04 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61191c04-620b-3069-825c-96e38886fd22 | -13.629 | -48.66695 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cf567a0-1919-3e71-ac9c-ba2ae4688a8e | -11.90647 | -46.37269 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5456df96-4938-3f21-825d-93d575acf403 | -11.96607 | -51.48093 | 2025-10-04 05:06:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b24eed02-1c12-35d0-9ed1-d447631e9376 | -14.69704 | -48.09513 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 686913f2-62ce-3251-a11e-cfbd2e39428b | -13.31724 | -48.11012 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ac56934a-a660-315f-9828-af18601ce7c3 | -11.92301 | -46.37645 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e69e2ead-b3b5-31fb-b4ac-3046f414e94b | -14.63288 | -48.25416 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a6cd564-44a2-3456-9263-174d80c03b3f | -11.12865 | -47.18012 | 2025-10-04 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5bb6096-64e1-388b-9c13-c117736e3bc1 | -13.75331 | -48.05759 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9cce6ce9-2673-3479-9878-3b8a33ade6dd | -13.33081 | -47.63088 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 12f7ee59-ca3a-3023-ae8b-d9a71d9650f4 | -15.7914 | -46.26318 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b962a7ab-d53f-3619-8745-f0b0ead1076a | -13.50782 | -47.27143 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88056803-9e81-30da-8158-f7906218f086 | -15.24735 | -56.85061 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8be79d44-a2b9-3e26-ab95-50bf837228cc | -13.13402 | -47.81683 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfeaf2d9-5361-346f-858b-9ca62133ac56 | -10.5748 | -48.69391 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f0090a7-67cb-31c9-b48c-8d0df7f68b18 | -14.57538 | -52.48061 | 2025-10-04 05:06:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95db7eb7-4cbf-31ad-96ef-27f9dabd10b6 | -14.9424 | -46.86149 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3bedf288-6487-34b0-9f42-c6c452917315 | -12.03226 | -45.19827 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| add4cab6-5c89-3a5c-8044-eaec2d5c53c7 | -11.49871 | -45.01429 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd3b7ca8-44fd-3dce-aded-8f49e495d073 | -10.58304 | -48.722 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b404c7f-b626-3827-b435-dbe497665a6e | -11.91878 | -46.41343 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 640f8a3b-1cd1-3461-85e6-dfb38a0874e3 | -12.5933 | -47.00154 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e1c26fb-cec5-3c44-a4a6-ada55836fa64 | -14.23521 | -46.09617 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbbd78e9-50bc-37a8-9ba8-f3d9309fbf8d | -14.89046 | -48.38801 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8db49457-2511-3837-9174-c6d047c60bce | -14.74947 | -54.6351 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60578048-f9d0-3bf9-b9af-555d1fdf2071 | -13.47374 | -47.26842 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3391eb2b-11cd-3c28-89e5-de6f9be4eb4b | -13.31792 | -47.25113 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ced2c589-8e74-3679-8dc9-8532a4119bcf | -9.52653 | -59.38475 | 2025-10-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1642ea1-bc2d-31db-8a33-b2976952ee7f | -12.70617 | -48.55463 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c8921b85-fddb-351c-b327-2113323a130b | -11.17382 | -47.7663 | 2025-10-04 05:06:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcef7ca2-ebc8-3a56-a35f-0830646dc7db | -12.23457 | -43.77075 | 2025-10-04 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b77a915-f521-3b88-bebd-3d2a22714ee8 | -14.9287 | -46.87704 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d892b12-5446-3f54-86b1-1f61f9564f51 | -13.70119 | -47.34023 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8952f1e-1311-376a-a7ef-9ca96a49beda | -11.45191 | -51.50916 | 2025-10-04 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a2f9900-2f17-38ea-827c-06a0df933d9f | -13.24568 | -47.83805 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e22fde8-cda4-33c7-b3aa-0d28bdf7ea88 | -14.91571 | -46.88632 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b687e7e8-a68d-3df0-b54f-67c5405c093a | -11.90361 | -46.34685 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 295e1ac3-d544-3eaf-8c31-ebe6e4a17b3f | -11.552 | -47.68011 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e9910427-4624-38b0-a697-fc3bc98b2aed | -13.31809 | -48.13354 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 249644aa-6e3d-3eba-9493-8aa3a314bdc6 | -9.45203 | -56.65374 | 2025-10-04 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e44166c-2fcb-3fa6-8f09-090e397f726e | -13.13493 | -47.80928 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4f886eca-d907-3c8c-99ac-78da197ea04a | -11.93002 | -46.37517 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d0e38123-1d9c-33a4-9a46-659240620c52 | -12.3501 | -54.15523 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95a95e63-26b9-385d-88c0-69c9d9409ebc | -13.13667 | -47.80959 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 98f879f2-e8b1-341d-88f5-7a183179f4da | -13.32003 | -48.11673 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9278ffcd-0acf-31e5-a2af-b6134223e52e | -15.59117 | -52.48638 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 72593214-c68e-34bd-b9c6-3a2acaec8099 | -14.24733 | -46.09924 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 37c03f88-310f-343b-95fd-4472482dcb5b | -13.12454 | -47.93926 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 15075820-91d9-3c96-be9f-9b5c50928ba3 | -15.18985 | -52.78793 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b86cc69-d773-3ec1-9cfd-77fecfe89b0e | -13.51569 | -47.28081 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 15f51ed2-4e1a-378f-af75-95790cd0f921 | -11.25069 | -47.79014 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2b9bb3ad-f2cf-3cc4-9d70-4bf93d1cd718 | -14.74724 | -48.13913 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04c70919-3dbc-3b50-be0a-ad4382eebe43 | -12.29897 | -45.36394 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README117.md)
