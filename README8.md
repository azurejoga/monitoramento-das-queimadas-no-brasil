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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0f427d9-8d9e-33e5-8a40-785dad37dc9c | -12.4279 | -50.675598 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fbdb5b64-fd39-33f5-900a-633161644d5f | -12.6196 | -50.868401 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7602cbd8-7daf-3731-ad02-73d17b5763b1 | -12.2926 | -50.7565 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 060e6b15-fda2-389f-b480-2db1f148ef18 | -16.562 | -43.988098 | 2026-09-18 00:39:00 | METOP-B | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 948521ae-ff10-3f7b-96a5-be89aa645fc6 | -4.4269 | -55.070999 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7762e05f-ce4b-3661-8c79-3373014ec338 | -3.9233 | -55.751801 | 2026-09-18 00:39:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 449c976c-b55e-3c73-bd69-fb151b6a4f76 | -12.4598 | -50.679199 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20e1948c-c368-3c5d-8978-0712d1dd2d1d | -12.3413 | -50.744202 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8cbf485f-90ce-37a3-b353-0ad341b130e6 | -5.8968 | -59.938301 | 2026-09-18 00:39:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d80206e3-a96f-3fe0-9b6d-cad5b3ee5ab2 | -11.2885 | -43.423199 | 2026-09-18 00:39:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77b55da8-57cf-31df-adb7-0e0fb5f517a2 | -12.3872 | -50.720901 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 44f0c713-e014-3e56-a30f-4f5cd3c66bf0 | -10.6322 | -50.261799 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c8a1e57-fc16-3459-987b-e4357da77d7f | -12.3191 | -50.738201 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4054a37f-a28e-36b3-8a3c-c34b57a03ff1 | -2.8936 | -54.183899 | 2026-09-18 00:39:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f58ca7c3-57a5-36b9-913e-0440f1795971 | -12.6319 | -50.876598 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| feb808fa-bb87-3a8e-8235-db3caebb648d | -13.2536 | -46.906799 | 2026-09-18 00:39:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 97cd7d93-73c1-32f9-a4c0-48fca7c899bf | -3.0517 | -57.992802 | 2026-09-18 00:39:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ad1f77b-d7f7-3008-b5ce-eb926f99b232 | -8.9141 | -62.426601 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f2c156da-d89a-3828-80b8-107be0f6f860 | -5.8699 | -53.557098 | 2026-09-18 00:39:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 954c8b13-8451-33ba-b83b-59eed1d7ca2a | -9.9076 | -46.5298 | 2026-09-18 00:39:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc716002-41ed-3f8d-ac4f-45f05c658301 | -8.954 | -51.468601 | 2026-09-18 00:39:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46782867-0060-36e4-bb53-0d3d3d1b652f | -12.3085 | -50.821701 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed89ec10-42c4-388b-b703-60b56402c69e | -6.3615 | -58.280499 | 2026-09-18 00:39:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6e92261-649a-3285-ba85-925723c82f6f | -2.9034 | -54.181702 | 2026-09-18 00:39:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b2412a9-9e3d-3286-a2a5-0ad4dc6b5a40 | -12.4138 | -50.702599 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 05983010-d689-3e56-9a7a-55ed765c3483 | -12.6293 | -50.866001 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5dce9013-c7ab-3217-84c2-3ab9b63d0730 | -9.0823 | -45.725101 | 2026-09-18 00:39:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d73ba232-7202-3062-92c4-f9e1ae5611ba | 1.4074 | -50.894299 | 2026-09-18 00:39:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| af88cbbb-d84a-37cc-a9a1-86a1897a95f2 | -4.5641 | -54.905701 | 2026-09-18 00:39:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfb624bd-4e45-35c5-bd08-f6909910fd32 | -9.7184 | -54.806499 | 2026-09-18 00:39:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 874138f5-3e57-311e-92c8-89fa47b8216d | -12.3802 | -50.734402 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e924950f-9834-352d-8b12-20575dd429ea | -4.3866 | -55.030102 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2b4f5c1-0ea0-3b7a-8cee-9f1fd8afb38d | -3.3583 | -50.4454 | 2026-09-18 00:39:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97a38cc7-74fb-363e-bd90-4fee5108b748 | -8.8872 | -62.396198 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8dc080e4-2501-30cf-8bca-9fbc5ee2b2a6 | -3.45 | -58.204899 | 2026-09-18 00:39:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab6e3400-5f7d-3430-9396-f82de824c596 | -13.3847 | -57.055199 | 2026-09-18 00:39:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98f17593-7999-33e8-98bb-0ba0f8fdd281 | -13.38 | -57.033501 | 2026-09-18 00:39:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b24a536-4113-3a8b-8896-92a3ee3e20c3 | -3.0447 | -51.380699 | 2026-09-18 00:39:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0326a11d-76db-3de1-bc4e-212b410ba49c | -9.9316 | -45.323502 | 2026-09-18 00:39:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c83f7a61-a017-37b2-8684-2e7b16a2a281 | -10.8108 | -50.190399 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3867856e-79b3-3650-a738-b956cd4af3fd | -12.4332 | -50.697601 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d7fb055-ee10-3284-8bf3-3fae9115fc2e | -2.5587 | -54.742901 | 2026-09-18 00:39:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cbc20a3-d7e6-348b-acc2-621e8196286e | -9.3953 | -46.856201 | 2026-09-18 00:39:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4a29493-50ff-366c-bfc3-d4195ac49877 | -11.2743 | -54.1259 | 2026-09-18 00:39:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce8c0ec6-24c2-3ac6-a9e2-8f305df521e6 | -12.3341 | -50.7575 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad5d9d6d-66fb-3d34-9434-4504e872df4b | -16.552401 | -43.9911 | 2026-09-18 00:39:00 | METOP-B | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5407ca7f-5a7e-3058-b2fc-6da96be82358 | -12.4473 | -50.6707 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 72143e76-407e-38d1-bb87-ae9219a1ccef | -10.8139 | -50.202801 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db9e1445-88f2-379b-8d65-297b9482ddbd | -2.8247 | -50.487202 | 2026-09-18 00:39:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edceeb90-06e5-3ffe-ad77-04cd8fee2b27 | -8.8823 | -62.4212 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1afac912-ab7b-3dc7-889a-1fdda4996f64 | -19.1875 | -48.783298 | 2026-09-18 00:39:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| be77be1a-ef35-3349-b86a-7f521c24df42 | -11.669 | -54.450699 | 2026-09-18 00:39:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8f09bcf-0421-3315-9cbf-203b0bf50db3 | -2.0556 | -52.159302 | 2026-09-18 00:39:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e498c1ab-3e3b-32f4-82dd-e5dc2c63738f | -3.3307 | -57.8591 | 2026-09-18 00:39:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fbe7d2d8-632b-34ac-8b32-63624082a9c9 | -7.1106 | -55.127998 | 2026-09-18 00:39:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3e075d8-f612-3b23-a2ff-e87f454b32ce | -10.9878 | -49.735699 | 2026-09-18 00:39:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6776c236-579b-3580-89b6-0bb8949da73e | -2.0459 | -52.161499 | 2026-09-18 00:39:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8d83b5-596c-3b72-aafa-143e8e23525b | -12.6468 | -50.895302 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d4b48894-64c5-3fc9-b537-87a429d0f411 | -17.768999 | -46.4706 | 2026-09-18 00:39:00 | METOP-B | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e0343eac-e7cf-375e-93d2-d7316fece824 | -3.4516 | -58.2117 | 2026-09-18 00:39:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3ded392-7a98-3687-8b49-fcbbe6c75907 | -2.7028 | -57.589401 | 2026-09-18 00:39:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce5ebc79-642c-3a58-8a16-2552f2030803 | -4.5129 | -56.075699 | 2026-09-18 00:39:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5df8333a-2fea-3b93-96b7-87f7a45e5c57 | -12.4571 | -50.668201 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cba75225-1002-36c6-9e9e-43e0d0da8a1f | -11.3265 | -43.374699 | 2026-09-18 00:39:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0be0cb13-9369-39c6-82b4-5566488fc2a0 | -12.3889 | -50.685501 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 69ebf7c0-2bf6-3584-9555-3a70b2871b0d | -12.3722 | -50.7015 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 49b234c2-f804-3043-871b-d1cdcbdde2fa | -12.3845 | -50.709999 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e786c51c-520c-3321-b2bb-e54ecc605241 | -12.397 | -50.718399 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 13682c85-44f9-356e-8ff4-6e3bd77994d4 | -6.4446 | -58.145302 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff991d75-1d7a-30ee-84e4-a4b286f8cfb1 | -12.6371 | -50.8978 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 71cdf03e-049b-3fb5-a96d-b0865f061312 | -8.8945 | -62.430698 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 292e499b-d502-309d-ab0c-3046a077d6ad | -5.7454 | -57.6003 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7798c2a-22b4-35fd-a081-e265d838a17d | -12.4306 | -50.6866 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 19f697fb-ab89-3a41-a499-c30e10c61f39 | -12.3775 | -50.7234 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6bea7e26-47b1-3aa2-ad5f-a0f945fe0d03 | -10.6568 | -50.488701 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72865215-61db-32b7-8b47-839d04f01663 | -11.2884 | -43.3857 | 2026-09-18 00:39:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4681e950-ec01-3e08-97db-816a5a90b86d | -10.8042 | -50.2052 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b17b1c84-f4de-3d98-9387-1113d98211c6 | -3.4485 | -58.198101 | 2026-09-18 00:39:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3e64c58-3469-3379-8259-bbb34a663dff | -1.8381 | -54.923599 | 2026-09-18 00:39:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceda9c57-2a45-3b48-b89d-11162a4e5d08 | -6.3729 | -58.285198 | 2026-09-18 00:39:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3fa858d-a656-3f7a-bb90-60a25d5e3e42 | -5.749 | -57.570702 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0d3d977-981a-3fc2-af0b-c918aff7f7f4 | -4.4284 | -55.526402 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6676e5e5-aae3-3c3d-83fd-4a01a4575450 | -8.9514 | -51.4576 | 2026-09-18 00:39:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b76280d-af13-3d74-b354-11307263dbd5 | -3.9669 | -56.122501 | 2026-09-18 00:39:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e56165f3-74fb-3060-97ae-ac4755e4bed1 | -2.821 | -50.471298 | 2026-09-18 00:39:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db0aa6e9-7242-3aa0-a311-540b164aff17 | -3.0318 | -51.369301 | 2026-09-18 00:39:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bfad7a9-af6f-3a32-b701-bfd2a72ba2bc | -9.7167 | -54.799099 | 2026-09-18 00:39:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a06d711-9a2a-3015-8469-6ccd64951b3b | -10.6644 | -50.2668 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af6394e0-3eed-3573-913e-62d34568acb6 | -12.396 | -50.672001 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77ce5668-8667-3e9f-a08d-41168fecbfbb | -3.3292 | -57.8522 | 2026-09-18 00:39:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a4e3795-4d05-3331-9537-32906ad6af05 | -11.2726 | -54.118301 | 2026-09-18 00:39:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c0b5a10-766c-3f5c-aa93-b71621f5c0f2 | -5.865 | -52.0453 | 2026-09-18 00:39:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9829dd5-78dc-38a1-9062-bf8121719063 | -5.7357 | -52.239101 | 2026-09-18 00:39:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe005f42-88e9-324f-ba2a-39064ecd0637 | -6.136 | -59.950901 | 2026-09-18 00:39:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bac33981-f343-39da-8104-fc0ecf9caad4 | -3.2637 | -54.270302 | 2026-09-18 00:39:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6609e107-cd78-3fb9-b3f9-38b5bdefce11 | -12.5351 | -47.082802 | 2026-09-18 00:39:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63ea3c67-43ac-33a1-bcd1-ac8602b6930c | -3.4671 | -54.706501 | 2026-09-18 00:39:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee3d3d98-07fb-3464-bfe7-f52b0ac6f042 | -6.1245 | -59.945301 | 2026-09-18 00:39:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c7ed0f2-b951-3dc4-ac23-8014199c8383 | -12.2952 | -50.767399 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 76ca5848-cbe3-3365-bc44-678875d6e949 | -9.3896 | -46.834202 | 2026-09-18 00:39:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
