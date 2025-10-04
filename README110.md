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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9a81456-1b8b-30d5-8d3a-0ac44ad7d381 | -15.00444 | -56.02268 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b74795d5-92f0-3ccb-88e1-d19d1d64bb42 | -13.73861 | -47.92972 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8d93f20-63ac-3391-bbcc-e949081d8573 | -11.86109 | -44.95876 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76bd65da-03c8-3c01-b663-8a377b97f08f | -14.60248 | -46.72995 | 2025-10-04 05:06:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8f3c0c6-4f22-3f83-9373-987e931480d3 | -13.38998 | -47.55375 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6b3d829b-f4ae-3425-8240-a1ba55b770e9 | -12.27776 | -55.12808 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd3bb2c7-ca74-3df8-9d02-19b6856abee1 | -13.32628 | -50.93998 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c0c2aaa-c66a-3958-b758-5953c4535c44 | -15.73341 | -46.27935 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43539306-c415-3b1e-83d7-ad01a4f2b850 | -13.69482 | -47.34571 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ce86167-4a45-308a-8ce4-a24a66589de3 | -12.03165 | -45.20354 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6280915c-09ae-3fce-a8dd-61c381056119 | -12.93103 | -45.07621 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b48fc00-b683-369c-a897-7b4d09ad0b1f | -11.31547 | -47.83177 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06ffcee4-383e-3e66-afb1-437adbf239d9 | -16.01651 | -50.94902 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1dd95fd5-9274-3410-95df-293b2f3ae160 | -13.69441 | -47.34923 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df784dcf-6720-34eb-9c86-615e5b283a06 | -15.0353 | -46.97905 | 2025-10-04 05:06:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ec7ea480-e706-3530-9a84-ca3e3dcceb78 | -13.23373 | -47.82861 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33632bec-0799-33b2-847b-70f54151a82b | -15.03478 | -46.97548 | 2025-10-04 05:06:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 96b1fc0f-568f-3589-8f87-1abfa6f34ee0 | -11.69552 | -47.50956 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c86c630-da90-3d2b-bd77-a21bdb70c4f3 | -13.12861 | -47.81594 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eaa81cd2-d78b-3977-a7c4-9f0091662825 | -13.7483 | -47.94089 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fed34325-02a4-3e9d-b8f2-36c893b5d011 | -13.3312 | -47.62764 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b8dff7e7-e5dd-3a98-9032-dae80d132cef | -13.13838 | -47.93798 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b5276935-b121-3fa4-ad2e-64bdbf69073f | -11.79569 | -47.92276 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd8609e2-dfd6-3d04-92ad-4db720be4498 | -9.29249 | -62.44809 | 2025-10-04 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e13b7a40-058c-3bba-9858-6e335fa9ff8f | -14.89761 | -48.35659 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0dba9d8-1138-39aa-9037-7f157991f3f1 | -13.2406 | -47.83434 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f9a32fb-fae1-3db7-9271-c488580b4e04 | -10.94465 | -57.18062 | 2025-10-04 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ef422a4-ca05-3f8b-9cfd-4a6945a7261a | -12.28406 | -55.13294 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b4e878c-14ff-307e-a85f-8dcd52aab2c8 | -14.16981 | -49.20856 | 2025-10-04 05:06:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90af0755-9ca2-3efd-b89f-08fa2e623ec6 | -14.21839 | -46.07866 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0c0722d9-ec4a-3110-8138-e0d9aa78785e | -15.33357 | -46.30265 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1071a302-30f2-3c04-b9ee-bef1353d7a49 | -13.9738 | -48.18471 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54aed4b1-66a3-3fcf-95c0-abcc3892fcc8 | -13.31585 | -47.61532 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a0afa028-f497-3623-a402-9a4435c723d2 | -11.54352 | -47.67721 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68399b88-f3e8-37e3-9cf5-4ba769ee4a97 | -11.90905 | -46.35125 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8961799-13f5-399d-9b80-f886efb9f986 | -14.67865 | -48.26191 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0087c597-b6de-3060-9385-35963fa80e7d | -9.90506 | -63.58973 | 2025-10-04 05:06:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a0763ff-a23c-3557-8618-e3472076960b | -12.04584 | -60.55699 | 2025-10-04 05:06:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 626e0944-fc93-3a1c-9771-e565718bd447 | -11.90972 | -46.2456 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4b3430c-8fa6-31be-ac17-8310bf40e18d | -12.87132 | -47.28525 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab6a1008-5504-3c21-9761-fef5b4acfc70 | -13.35271 | -48.06912 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bba76a32-76f1-3dcf-aabe-b6844c0b4839 | -13.18046 | -50.92231 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d07e7610-7af1-39c4-95da-cd2422a32ec3 | -9.90423 | -63.59447 | 2025-10-04 05:06:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7045cda1-e125-35c8-9f89-ce59720cb930 | -11.88532 | -44.9919 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9d786992-8968-3c4b-81db-8b3d17a14b4d | -13.31729 | -47.7924 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5bc1162-cff2-3caa-a2e0-33c3fc953a38 | -16.03142 | -50.9411 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 95cf13ee-a290-38fa-9a0d-1e6fc7faa69e | -13.12622 | -47.8356 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d3a042aa-1d0a-38ac-b563-7fc7bae39d6e | -11.70642 | -47.51076 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a654743d-2b9c-3d02-8b46-9d377529f344 | -12.72031 | -48.56682 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91d12221-d756-3a12-b8f8-06fb9bd8e620 | -13.14913 | -47.93957 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c2e1e7c-6ecd-373f-9ceb-c6aa91b76370 | -12.05908 | -53.84048 | 2025-10-04 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77423745-4611-3fc3-a249-7cb321ff85fa | -13.1045 | -47.87881 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b324adc5-7f69-39ee-89c8-da38921ff396 | -15.0016 | -56.01834 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01921214-7cb0-35a5-b647-638efffd4930 | -13.3171 | -47.25849 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35d4a968-ae76-306e-afec-af3e4eebe0ff | -12.89042 | -47.16674 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4af0fe2-30f7-3680-9610-d3d2782b3d3f | -9.20022 | -59.40405 | 2025-10-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e91efee1-2cd4-349c-807d-98fd0fef5829 | -12.52841 | -45.98223 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dde6f833-ceb9-3d53-b0ec-5cf81cf52bf8 | -11.50512 | -45.01467 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 651928b6-6ee1-3955-b2c6-b4d2a137bdc1 | -13.11052 | -47.9197 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30732a81-464d-3522-ad85-041113793486 | -10.33228 | -50.33412 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 06a8f90e-4edc-35a3-81c1-8483974f4b64 | -13.31513 | -48.12729 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 013027bf-1212-3bbd-80f3-e2744f61c3b7 | -12.87613 | -44.62796 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1ebb4090-d00c-37d7-80b7-726c6e6056f8 | -16.00976 | -50.92791 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 63c9e18e-a77d-30ae-9b11-cc86317a3cfe | -12.30982 | -45.3807 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06108371-0c81-337a-baaf-ddcceb56282d | -11.88429 | -44.98269 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e3df7b7-b83e-3fc4-ba1b-c38e4c272172 | -15.31992 | -46.37156 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e9505f4-d34e-336c-bd95-04d4fea07dba | -15.35264 | -46.29932 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a9b28e87-78e6-35ca-ad95-583a43c37963 | -12.1449 | -54.27415 | 2025-10-04 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f160ab85-3815-3a59-807f-22872937f6bf | -15.24366 | -49.29982 | 2025-10-04 05:06:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8704780c-c10e-3efe-befa-c5e88661d7ab | -11.92239 | -46.38893 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9bebd8e7-11eb-358f-96f8-bfeabbab14fb | -14.66504 | -48.3058 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83bae34b-fa4f-38d3-aab8-f90147dd2b28 | -14.92699 | -48.33723 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b3f760c-34f1-3667-bd8c-2c869da9cf27 | -12.57976 | -54.7413 | 2025-10-04 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6ef998c-b474-3b44-9b61-bb07ff0dcf87 | -10.20816 | -58.25557 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 259b0884-a83a-3bb8-bb76-0b517938af72 | -11.91875 | -46.36139 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca15a09e-5086-3cf8-a66a-373249d4bd40 | -15.74076 | -46.2683 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c320df33-8e12-340c-bbb6-7c9e6bf05205 | -13.54863 | -47.24289 | 2025-10-04 05:06:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff02cea5-bcb1-3ceb-b64f-008e1d8ffeca | -14.75184 | -54.64427 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a3c7231-55ad-3ea1-b3c0-741e202ad257 | -12.72682 | -48.55656 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab99f017-8b58-3dd4-a657-5d01ff0e35f2 | -13.25525 | -47.26782 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91eaa161-7d5d-3547-8461-f6d556aa4479 | -11.91705 | -46.38387 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c076bb7c-f614-35c7-8ae4-66a5d70a651b | -14.4461 | -46.10387 | 2025-10-04 05:06:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10582044-ebdc-3c28-87d6-fa58e9746fcc | -14.58599 | -52.49357 | 2025-10-04 05:06:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de5ad01f-c564-3f54-bde2-7ac7b206c9f9 | -13.33011 | -50.94499 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35740889-3723-33b0-9c57-85b169ea2e96 | -12.64351 | -46.98743 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39488a59-6b50-3769-81b9-27c24039a3db | -11.11102 | -47.75061 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 614f2fab-410f-3940-86b6-8eff95e4a6d8 | -13.23838 | -47.83574 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5d4cc45-4f70-3b4d-bcac-771aa5d433f3 | -16.03659 | -50.93695 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2696dc78-f480-361b-be8a-48ceb196ac98 | -9.19308 | -59.55338 | 2025-10-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffa592eb-4c22-3f2d-a788-79d168ef126b | -12.90781 | -54.74826 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0464f29f-7eb2-3ce5-a56d-9df2bacbfbfb | -14.64349 | -48.30387 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| afefb763-161a-30b3-9ccf-1d431a807a45 | -11.87209 | -44.97594 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f066c00-ca08-358c-843a-d4682c9bf53c | -13.32041 | -47.24961 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3637b169-9e5d-308f-ad93-4ccecff3ed2f | -13.27858 | -47.21532 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be94810c-b35a-3c1b-9070-2d75552eeaab | -15.69122 | -46.27048 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4259a20c-4a6c-309c-ae01-6a00c05852c8 | -14.2008 | -46.06816 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82cd661a-2b36-3d04-a135-d13b9aba3035 | -15.24557 | -56.77246 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21721070-785a-33ca-9eb3-40eb6780ff3c | -13.11327 | -47.85165 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5ce52dfe-c4b9-376c-9f1e-6181cd20b62c | -15.66606 | -48.14355 | 2025-10-04 05:06:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d95a807d-aae0-3ea7-9096-54bda9934865 | -15.32736 | -46.30249 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README111.md)
