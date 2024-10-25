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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 341e06ab-7d8c-3653-bf25-3e3a37c363f9 | -11.07352 | -47.89578 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a487136-edc4-367f-93f3-757c4896a867 | -10.9427 | -48.04139 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b958cf7-8c83-3345-8829-9e1d604b05ba | -10.94223 | -48.04506 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 162c8c36-7104-3623-8ca2-320b1d26fc24 | -10.94147 | -47.80206 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 79462c24-b15d-3075-8e4e-b52a061dc182 | -10.94132 | -47.79888 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74f38f8f-833e-3067-afda-a2cbcbb7858f | -10.94089 | -47.80235 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89972a78-07bd-3f94-a6a7-a26fb00e1afd | -10.9366 | -48.04788 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c80eb70-5e2d-36ab-86a7-1f7d366f72d3 | -10.93614 | -47.80177 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74a655da-0980-3da7-b485-85ae2a1abe43 | -10.93568 | -47.80529 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ca555d0-7058-3e99-9f32-725d932d0e1b | -10.93558 | -47.80194 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e194ee7-57f4-3e06-b787-204a0678247f | -10.93514 | -47.80548 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d310b27-1bf9-32b0-889a-5ecb2f6559d6 | -10.91955 | -47.96766 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7d7414f-4703-3928-b768-68c6d3839344 | -10.91914 | -47.97076 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d4aef34-e968-3624-98a4-cb61d55197f4 | -12.07642 | -47.98752 | 2024-10-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dc88706-c89d-31a6-97ad-9d35056da175 | -12.0761 | -47.98498 | 2024-10-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37791e37-cee3-32e7-8c84-2401342434d7 | -12.0757 | -47.98833 | 2024-10-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21d1643d-0236-302f-9400-8c0b68eedd2d | -12.07114 | -47.98681 | 2024-10-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22675e5a-121c-3826-bdf8-1ae42296a147 | -11.42525 | -47.81662 | 2024-10-25 05:04:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7effcc5f-b771-3453-b3db-a4a871bc5434 | -11.42483 | -47.81993 | 2024-10-25 05:04:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbd9ef5e-e290-3f48-83ad-df125a047bd2 | -9.43962 | -48.88876 | 2024-10-25 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a589c25-afe7-3ef5-954c-2de16b89a968 | -9.43486 | -48.88791 | 2024-10-25 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba898daa-d30a-3ce3-8a89-00888e94be7c | -8.9804 | -48.82177 | 2024-10-25 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfbfcaac-c03c-3425-9ed2-41b4bc01351b | -8.9802 | -48.82074 | 2024-10-25 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c166f734-1e54-302f-87fe-56622f9c46fc | -8.97972 | -48.82693 | 2024-10-25 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f0513e2-0354-3683-a959-7a07ba3c2235 | -8.97948 | -48.82589 | 2024-10-25 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49fe36d7-7f8d-32d6-9e93-35d5c360038f | -8.97563 | -48.82105 | 2024-10-25 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bf8149e-b3bd-3d4a-9537-c587673fe9f9 | -8.97543 | -48.82003 | 2024-10-25 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a46432f4-f370-33bb-9396-78cbec85e4bf | -8.97494 | -48.82621 | 2024-10-25 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12c2fa71-fefe-3bd3-9e53-c4293d7f1478 | -8.97471 | -48.82518 | 2024-10-25 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a720f9c6-b3d4-3ba3-8af0-68cc81fbec68 | -8.88666 | -48.82849 | 2024-10-25 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a15f5c2b-4658-38fa-8778-0b511adfc1b5 | -8.75167 | -49.79018 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 534ec3fc-a149-37f7-acca-a35b762b467f | -8.74723 | -49.78947 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7ed028b-5e2b-31a2-b280-982f3b165d93 | -8.68196 | -50.03481 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d92100e3-1761-348c-85fa-da7252885f93 | -8.68135 | -50.03908 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cc9e79ce-382d-3f99-bc54-2b4f0dcf7015 | -8.67759 | -50.03418 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ecf267c-d8bf-372b-9ba1-01918d26d8e7 | -8.67434 | -49.09285 | 2024-10-25 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ccbe46d3-46db-3002-9359-04c5e41df440 | -8.67367 | -49.09776 | 2024-10-25 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9efd281-60b1-3479-9112-aaa559c32fd5 | -8.58136 | -49.22691 | 2024-10-25 05:04:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 085dcfa4-37d8-3ed0-a412-f80d6278452d | -8.58069 | -49.23168 | 2024-10-25 05:04:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85fceb2f-d4d7-3c06-a4c6-a517c387768b | -8.54463 | -49.55118 | 2024-10-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7398115a-0ca1-39e3-aead-0730a528c573 | -8.54011 | -49.55056 | 2024-10-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2af70dc5-5e1c-3780-bd67-d76c10efad63 | -8.53948 | -49.55505 | 2024-10-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ce24de0-f5b7-3d26-b581-69938ffc7ce1 | -8.53883 | -49.55956 | 2024-10-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95486dfe-83c1-3b28-9624-b9610010fefe | -8.5356 | -49.54994 | 2024-10-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e1df1965-ceaf-3f6f-9b8d-892bece9cd20 | -8.52178 | -50.02623 | 2024-10-25 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 798f00e3-0abe-35f7-81a7-d3f4431e5837 | -10.87497 | -49.53513 | 2024-10-25 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a28d758-6014-338f-8e3c-77206f5312a5 | -10.8743 | -49.54015 | 2024-10-25 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46475c85-4664-3565-979b-a6268ba5e0ef | -10.37468 | -49.9206 | 2024-10-25 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f6f5e1e-1c31-345c-bf09-78c27b5a1b75 | -10.17757 | -49.50727 | 2024-10-25 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cf180af-080f-3be6-8e0d-116c5fcc12f0 | -9.82196 | -48.98378 | 2024-10-25 05:04:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3e85a93-cc2d-35dc-8e9f-f8e87dfe327c | -9.82135 | -48.98659 | 2024-10-25 05:04:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75da7a28-2a15-3531-ae3a-09eac9f8cb5b | -9.58451 | -49.64525 | 2024-10-25 05:04:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 894bc050-0568-330e-b140-adacf85c6f80 | -9.58386 | -49.64997 | 2024-10-25 05:04:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4407945a-a525-3ae6-a3b9-5d52835979c4 | -11.15148 | -49.69866 | 2024-10-25 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 136febe6-5d39-3c1b-ad57-985f060cc15a | -11.03346 | -49.60033 | 2024-10-25 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d00d2961-b161-3f28-81ec-f84fc3dc239b | -9.35862 | -50.64132 | 2024-10-25 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 578d218f-ab9a-3149-8db2-46d85927beae | -9.25292 | -50.68713 | 2024-10-25 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 311aa005-e189-3dc3-8b38-d5bb5124342d | -9.25261 | -50.68908 | 2024-10-25 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76b88f16-b412-3839-ad9e-82ee125305a4 | -9.25238 | -50.69106 | 2024-10-25 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6867313d-0091-37f6-8374-dd3d041374e3 | -9.25204 | -50.69299 | 2024-10-25 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba9bbd1e-515b-399e-a56c-f09fa8f1ebba | -9.2484 | -50.68842 | 2024-10-25 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de789bbc-4779-321e-a598-d0e15c35d499 | -10.49126 | -51.66039 | 2024-10-25 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8878499f-1117-3107-aeb8-2b21fa688394 | -10.34389 | -51.47084 | 2024-10-25 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be88e665-4c38-3973-ae7e-c535fcf54f78 | -10.10157 | -51.12593 | 2024-10-25 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8fefb9a-9f75-33c3-afc7-34fb16c74516 | -10.09742 | -51.12531 | 2024-10-25 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbb8ea10-354a-370a-bc7e-ab5701e7090e | -10.09689 | -51.12913 | 2024-10-25 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01d32b8b-bb93-3737-933f-53f9fb371d17 | -9.91159 | -50.5452 | 2024-10-25 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba46024a-984c-35f2-8f32-6a0953a68f38 | -9.91101 | -50.54929 | 2024-10-25 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a191971-8fca-37f8-bb13-a98813c7122e | -9.90728 | -50.54462 | 2024-10-25 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a2f5e40-46bc-30a8-a5a4-f1fdc392b524 | -9.9067 | -50.54874 | 2024-10-25 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5ae86eb-0194-34ff-8d4b-58c979b4c9b4 | -12.54471 | -52.49498 | 2024-10-25 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 567fe6ef-079c-3987-a09d-67b0478fa70d | -13.78481 | -52.80501 | 2024-10-25 05:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ddcff0b-84e7-39ae-b723-4659cea27d0e | -10.6101 | -52.4208 | 2024-10-25 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d0dc40d-bb95-3dca-9959-b2f711bd9f49 | -10.60936 | -52.8267 | 2024-10-25 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f242f0c6-09aa-3eff-85fd-b6b3111ac05f | -10.6087 | -52.83128 | 2024-10-25 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10316607-5455-3088-b79a-fc381f46d5be | -10.60625 | -52.42024 | 2024-10-25 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 991b8367-ade1-3102-883d-ae454442b4e7 | -10.6056 | -52.82613 | 2024-10-25 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 883500a3-7dd4-3d94-9ced-eac5b29f61e2 | -9.71219 | -52.80957 | 2024-10-25 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3f2abc6-ba25-35e9-b2ec-b0d7fa37d4f2 | -10.99498 | -52.88153 | 2024-10-25 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09cf873b-ad70-352f-a957-69133868c4f8 | -10.99213 | -52.87918 | 2024-10-25 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a3c471d-395e-3dec-9f72-bf39061f0b1c | -10.99148 | -52.8838 | 2024-10-25 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a34edb34-2380-3bda-ae79-7da9006faf95 | -10.99122 | -52.88101 | 2024-10-25 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59b36578-f8ce-3040-87f5-36554f23eb8a | -13.17449 | -53.77063 | 2024-10-25 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3b03abc-3336-3a54-baa7-a8953101ef92 | -13.17081 | -53.77008 | 2024-10-25 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24e5f1f8-4c86-3368-99eb-1a90cb7f1ec1 | -13.17018 | -53.77454 | 2024-10-25 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ce7af8a-9690-3261-8307-8e583c53785e | -13.16955 | -53.77899 | 2024-10-25 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee7f7547-3ac5-3704-bfde-6ac45d1ceff2 | -10.7005 | -54.56864 | 2024-10-25 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 029fa48b-8d44-3579-8c47-d21f84173f4f | -10.69705 | -54.56815 | 2024-10-25 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91639377-739d-3db5-be9f-78831e940ae9 | -10.656 | -54.8641 | 2024-10-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6cd4ebd-f267-36a1-af6a-959ac755f78b | -10.48243 | -54.87655 | 2024-10-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 139493c2-f361-3851-b96d-55e2ebca640c | -10.45306 | -55.09882 | 2024-10-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1e72864-8896-3154-abf5-9d86a17b8b5f | -10.4525 | -55.10249 | 2024-10-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bc54c71-72bc-3bc8-873c-6bf5f914d048 | -10.45187 | -55.09869 | 2024-10-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f35b1b62-c7e1-3d8c-b900-6b65cfc8545e | -10.4513 | -55.10236 | 2024-10-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a70bd77-c505-36ab-9bd0-a29f2b17b17a | -10.43466 | -54.45552 | 2024-10-25 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b720173-c33c-39ec-94b5-571515668ccf | -10.43408 | -54.45933 | 2024-10-25 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a841f306-d83e-3a8e-8193-e6a60bac05ca | -10.22535 | -53.87833 | 2024-10-25 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc146f92-ffa6-3458-95ce-97678e0bd245 | -10.18135 | -54.20077 | 2024-10-25 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70c7d466-266c-3c47-b0de-da9a43d9fcec | -10.18077 | -54.20466 | 2024-10-25 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0558a1e-8330-383e-9965-e137793acf7f | -10.07287 | -54.36703 | 2024-10-25 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README98.md)
