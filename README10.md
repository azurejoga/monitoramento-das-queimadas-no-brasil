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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc9d85bc-44f5-3b14-be00-5bdb8bac5b78 | -11.95572 | -47.33296 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e78c70a-9dfa-3d4e-bd12-bdccd2074f4d | -9.92885 | -49.26839 | 2026-08-12 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad440890-44f4-304e-871e-ef9aa9dcb8e4 | -11.46836 | -44.56419 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88274a43-0a3b-394e-8029-56411e1f8f27 | -13.83454 | -53.81866 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b505e9bb-0141-39a4-8785-3b6585d989b3 | -10.4262 | -46.32792 | 2026-08-12 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cbdf295f-e38d-3951-bbb5-1f8abaddfed0 | -9.13372 | -46.39298 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4955a4f5-063e-39d9-a2a1-6f3577e2ac04 | -13.29115 | -49.69513 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 040b4daf-9b3b-3e33-b3c2-6a7386ae3322 | -12.17941 | -50.15869 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 992c0b4f-95e9-313b-9cc5-b508d06c256d | -11.65556 | -50.14143 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9b437d9e-3715-3a44-9bba-ebd49580dfd7 | -19.0805 | -47.85733 | 2026-08-12 04:17:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6e34f80-c48d-3276-93d4-09d408cd65a6 | -13.57598 | -46.25682 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b7c7d5cf-b18a-3b8f-b3d6-1b98318173dd | -12.61147 | -47.86361 | 2026-08-12 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3429462-c040-322f-9be1-eac07932ac2f | -11.89072 | -45.82753 | 2026-08-12 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cb8c231-77a9-3249-af61-a85431d6c13c | -13.87204 | -53.82703 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d949c9d-04bd-3b3d-821d-904e40e6b4bb | -11.78867 | -51.84808 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72787ca6-4700-3234-a520-a53cef02f408 | -11.95774 | -47.32066 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55fd795a-598a-34b8-880e-61ea94545325 | -13.88358 | -53.82264 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| edb47f4d-4379-3009-9c59-23bdca649923 | -13.29918 | -49.70954 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a76149e6-a9dc-3d66-8258-fb58a2e15ee5 | -13.9038 | -53.80097 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d02b3d15-58f1-3c01-b7b7-6b54b2df65a1 | -11.81811 | -49.50457 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d011f3c-9536-34e9-8868-99ddff2fe396 | -14.9851 | -46.59677 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e49cac05-b0ea-3373-bc3b-2c0cc8782bd0 | -20.65439 | -55.40668 | 2026-08-12 04:17:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 254861cd-bb35-3334-95df-cba31559a8df | -15.30498 | -48.88175 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5fcfb71-523f-3d5b-92ce-9031b50596d8 | -14.28011 | -45.28159 | 2026-08-12 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 915fb32c-406a-3003-997e-e81dcb999b2b | -11.47719 | -44.5728 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 71478d22-41b5-33be-a45a-7b9e99e0b0dc | -12.18426 | -50.15558 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c562e87b-61fc-33e7-aa8d-1b41adefc62a | -13.60647 | -46.23941 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a54fbb4-14f6-33c0-9685-833c611f974d | -11.98678 | -46.36736 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40bf482a-fea4-3b01-9726-5fbab606f19b | -15.05921 | -45.32289 | 2026-08-12 04:17:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28b2017e-9f67-356e-a919-7c7537f39ed9 | -15.29966 | -48.87341 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ea77c283-5d69-3e75-9359-cde91973cef0 | -11.47222 | -44.56121 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 73dc1396-eb0a-35f5-abcb-80b78d412dee | -10.71737 | -47.91568 | 2026-08-12 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eae1d556-fc9a-3fc0-89ca-a2f8b5ca9451 | -11.80446 | -51.81448 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8580655-1e9f-3e1c-8313-12a4978eeeb0 | -20.95304 | -48.89748 | 2026-08-12 04:17:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fbe927b2-ba16-3bfc-b064-3b6d5a3d348b | -13.82862 | -53.82172 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97027523-5ed4-3ec0-99cc-1198a59da11f | -11.80671 | -51.56659 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e121913b-c89c-3adc-8f07-702e18ef4fb7 | -14.97657 | -46.60669 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8552a9be-cfa2-3586-add9-b7ccc298cfbf | -14.58377 | -46.75523 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb4a464c-b5d9-37a1-8128-e6c83bc34c91 | -9.92689 | -48.67443 | 2026-08-12 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73de2ca5-31f8-3dd3-8f75-0cb829d22481 | -11.48674 | -47.60347 | 2026-08-12 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e0a06fd-8de6-3f0b-9e29-c0c613d192e9 | -10.22347 | -45.93385 | 2026-08-12 04:17:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2473dfcc-2f71-3264-9a30-59131c2ca82a | -13.8293 | -53.81819 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e28b5e78-ef91-3013-bc72-b33f70b33986 | -9.5828 | -48.42114 | 2026-08-12 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 163ef1e5-af16-3563-a20f-da19e57c0e3c | -11.8242 | -51.8389 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 32d31f97-21b8-391d-b62f-25b6b343459c | -13.30304 | -49.69733 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 47042399-34fc-3526-b9ee-e34f96b25231 | -14.9732 | -46.6061 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 044293f8-758a-32c7-ac86-68e92978e288 | -9.45549 | -51.81314 | 2026-08-12 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94c198ac-3fc2-341e-b781-1f0eccfaf905 | -13.30012 | -49.70433 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 77449a6d-fffe-3170-830a-fe5afd2e098c | -13.90199 | -53.83766 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0ef0cbd-f297-3260-bf31-d1836be33b92 | -13.53182 | -46.28387 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 007e4fd2-270a-3dc2-b792-1f8dad93ad06 | -13.86008 | -53.82463 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bca2aa5-3716-32c7-ad31-cbe007c2ba36 | -13.43414 | -57.05339 | 2026-08-12 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87dfc8c4-b8f6-3f9c-9cb9-630458e08eac | -15.04999 | -46.52789 | 2026-08-12 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95533854-7e7d-3f9f-8f34-89cff6ca5a23 | -11.94728 | -46.3301 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 10607ab1-575e-3fc7-b7bf-c1e7ce4ca3a1 | -11.97399 | -46.38129 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cadb5bdb-3e77-3acb-a7a0-42fde07b09f3 | -10.09605 | -46.21924 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 884e5c49-466e-3eb1-9a1a-5fdac2f9b929 | -15.27828 | -48.8655 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d557f11c-8dab-3ac0-932e-1734fb081af5 | -11.79335 | -51.84898 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f79b30f3-883e-3c1d-af78-544ab8bac053 | -15.02665 | -46.5966 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be3faa47-7c14-3624-91d9-8474e5ab7ff7 | -13.29205 | -49.68992 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b806c800-c994-347d-9c9f-b4b8c07f6b66 | -11.49297 | -54.60801 | 2026-08-12 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef4ddee8-147f-35e5-88ff-39c88d8e945c | -11.47388 | -44.57227 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 49da0d8c-61c7-37a0-bf39-14c68f75ace9 | -11.95223 | -46.34265 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7fc75157-b3a1-335b-a66c-568977ecc467 | -15.30178 | -48.88322 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb72127c-5e08-388a-90ff-f93505a0e03a | -11.88988 | -46.80841 | 2026-08-12 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86dc1171-0205-3e1a-9f4a-4c5d31efa958 | -10.36839 | -46.3855 | 2026-08-12 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b823a17-7599-387e-a10c-c11d1ce72098 | -13.87063 | -53.83419 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91f6b773-5f65-3435-b71d-efcf71018c29 | -9.34661 | -47.49043 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bc6f9524-9dd3-324b-96ad-d932b9b23a9d | -14.27792 | -45.27395 | 2026-08-12 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ede5b24-669a-3e24-a8a6-27cf3f4f5cef | -11.97898 | -46.39379 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7927f153-aa9a-373c-9f65-5cb04b0926bf | -12.35126 | -48.20647 | 2026-08-12 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5e7945a-2a18-3ae1-808d-312195d76bc6 | -16.67403 | -45.03588 | 2026-08-12 04:17:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abeed79f-c609-335b-a87c-614f979ac27c | -11.95594 | -46.36285 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af347dbb-f5d4-384e-8eb5-23c2a0a1452d | -12.31505 | -49.79518 | 2026-08-12 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 583b3bbf-990b-3234-a43b-7a561a5a2852 | -9.6255 | -48.33218 | 2026-08-12 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a57d935e-f04d-3604-85e9-0f97d8441420 | -14.30723 | -51.98863 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17488f4d-ff43-3018-b267-e0e9927c7af9 | -13.86546 | -53.8333 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27fe20e9-1bbb-3cf1-9b82-d52ffdbaacdd | -12.10727 | -47.18559 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51deafe7-6a27-35b5-8b36-d96fdac3a929 | -22.26605 | -48.66029 | 2026-08-12 04:17:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2c93e713-72d3-367c-a251-138bb2828609 | -12.72383 | -48.44423 | 2026-08-12 04:17:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae2421b2-4897-3a26-a78a-8cf0e421b9cb | -14.29764 | -51.98317 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27165dce-c063-36cd-9145-0f9cf384523d | -11.48436 | -44.57035 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 1a51f12c-eab8-3d1f-87a3-dafb1e8d671e | -14.30543 | -51.99808 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8055ede-9d01-3acb-a429-328063cd04bc | -15.29595 | -48.87296 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 922b198c-7712-3344-af6c-766983f1a744 | -11.95073 | -46.33044 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d66d1236-1639-3745-aced-33ecfdf10545 | -11.47443 | -44.56876 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 8c69c57f-fecd-30f1-91e5-d388f22baeaf | -13.85275 | -53.81661 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9f9a2c5-2400-3e01-926e-615481efec11 | -13.30408 | -49.70504 | 2026-08-12 04:17:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 149dca0f-4931-3f8f-86f6-ef608c6114c9 | -11.95096 | -46.35037 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1972981a-2935-3ffb-8ecc-358a7aa76f15 | -11.81651 | -49.50674 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 246f8ed1-4b8e-3085-8607-629f3b741658 | -14.4009 | -52.0684 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 4c69bddd-497e-3621-a176-063332e39a5f | -10.22063 | -45.9297 | 2026-08-12 04:17:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 7aecbc27-3d26-3903-bc62-ffe401f606a1 | -10.63892 | -47.48721 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 95a9b0fa-0403-33e1-adc3-dada1a60a6dd | -16.1052 | -49.89102 | 2026-08-12 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 99dc389e-0fd5-3fe9-acea-1bb9a50310f1 | -13.5682 | -47.63552 | 2026-08-12 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70be6d9f-e0de-308f-b685-9724f85c0206 | -11.95627 | -46.38229 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c6856c5b-47ec-32d9-80d1-8004fe388eca | -10.22369 | -45.91068 | 2026-08-12 04:17:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25e340a1-1e2b-3fc3-b0ab-844a7ee738a5 | -11.984 | -46.36286 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3eea584-ce4f-3dfb-bf28-b446395143bb | -14.53843 | -50.39182 | 2026-08-12 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06e5cbe5-cd53-3fd9-a56b-9b4c60781f77 | -14.5506 | -50.39417 | 2026-08-12 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README11.md)
