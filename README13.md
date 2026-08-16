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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c87a18e-ad1d-3127-98a1-fffa58f8dace | -11.09605 | -47.24483 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 208efe56-efd8-30b5-a5e7-6e1e9a3994d0 | -10.67961 | -49.00093 | 2026-08-16 03:55:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2ccc47d8-ebbf-362e-90c8-18b73dc5247e | -10.41413 | -47.84163 | 2026-08-16 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 812213d2-dc16-3192-bd4b-f5960d266f1b | -11.09012 | -47.24726 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50f36ba4-ebb2-3a04-b0c8-6304c1ba396b | -11.87839 | -50.61837 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55960122-4759-3f4d-ae66-bbfb559f1a7c | -11.45171 | -46.61456 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ee74ebe-32ee-3824-9a4f-64084a4f569a | -11.06504 | -47.26398 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0786c2b9-d307-33d0-944f-ec7fce7df084 | -14.37271 | -51.89983 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c523033-9311-3ed8-aada-12462332f19b | -14.15694 | -42.76685 | 2026-08-16 03:55:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 29ba8305-b562-3306-947e-f1210ea3fe97 | -10.53278 | -44.85162 | 2026-08-16 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee692361-9ffb-3000-aef5-46a69e871159 | -11.09546 | -47.24798 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bef9abca-de18-3249-8fad-6946e0cc997b | -11.48949 | -46.60268 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d9eaf4d-5a74-376d-9f2a-daef7ceb8c24 | -11.8077 | -44.80581 | 2026-08-16 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3194a801-3010-3198-ab39-74921a7324a5 | -12.67484 | -48.44923 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27f15a83-e088-35c5-8ba9-4fbe1055a5c0 | -11.55729 | -46.84242 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68efcfe2-51d8-3d13-ba25-5256729b3697 | -9.1072 | -46.39151 | 2026-08-16 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c53b4141-8877-3b96-b511-e91c39100672 | -11.90775 | -45.9827 | 2026-08-16 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd893f48-80b7-3625-89f0-4cf8bd720045 | -11.32392 | -46.22459 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32b2760b-c787-3bbb-8978-6e7aa21283af | -13.49875 | -48.23062 | 2026-08-16 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23a79837-169a-3b04-9db4-629f3234bcc9 | -12.67979 | -48.45333 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17a48831-95f6-3144-a1a3-fc70945b8861 | -11.47507 | -46.59636 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a831c761-9f13-3ca4-8e82-e899a3309fdd | -10.17942 | -46.4128 | 2026-08-16 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a6e0a38-bbdc-37ac-9f48-1be8426e38ee | -14.38854 | -51.9222 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c642774e-c64d-3579-b7f0-f29f6a699e8d | -11.80687 | -44.81027 | 2026-08-16 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 124ce1cc-94ff-35fa-a266-9bd7c8fd10f7 | -13.44094 | -43.84391 | 2026-08-16 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b5191219-363f-3b6e-ad78-2e6450d9fcb1 | -14.90021 | -46.63154 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 656757fb-cc7a-3d10-a77a-dcea7d54f779 | -12.02673 | -46.44207 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| e78299f9-fd3d-3982-a6cc-5f49441b06a7 | -12.01274 | -46.42858 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 562fdc47-8b94-3fd3-85ce-07d45ac823db | -11.10204 | -47.24209 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4141aab3-92fc-3b14-81eb-f2c9d706af66 | -14.91154 | -46.62368 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2e93363f-ed02-3988-b6c3-3e616b3bd6e8 | -11.47172 | -46.59079 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc4f3f11-cc67-3514-a302-f05f1f8a2081 | -10.51828 | -44.85386 | 2026-08-16 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2f56fc66-127c-362e-86cf-45fba1e77043 | -14.90592 | -46.6274 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6b302ae5-851d-3c47-a59e-721fbc9be3d0 | -14.40833 | -51.94201 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2d2099d-747a-394f-8475-50451a317e12 | -12.69374 | -48.4411 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb9ab80f-8abe-3e72-b0c0-902e54a0bad6 | -12.43981 | -46.65805 | 2026-08-16 03:55:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b65bc629-c4c6-3b4e-9033-abccd1b22d0f | -15.70044 | -47.62777 | 2026-08-16 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a8890b3-48a5-34d4-ab48-fba0f7439d57 | -14.41539 | -51.84413 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 39c82d24-84e0-3543-b449-744b18a3a353 | -14.90111 | -46.62687 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7080fec3-3b78-3dba-8436-f5d216615bbd | -14.37516 | -51.90279 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59e2ae48-b254-3b9f-89c0-d57e247bb7c0 | -11.48506 | -46.59859 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 958c57d9-bcbb-3d8d-8cae-7981f368ba8d | -12.68675 | -48.44732 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48fc8b3b-1e83-3f39-b380-3d5a5193b31f | -11.46051 | -46.6179 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75b79af7-f282-3613-a67b-e64aea3a83d2 | -11.90862 | -45.98133 | 2026-08-16 03:55:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0da0f3cb-9b60-30cf-99ad-13156dea39de | -11.48063 | -46.59454 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 360738f9-a8d2-334a-86b9-c7d7c0f409de | -9.10208 | -46.39026 | 2026-08-16 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8c3f94f-903e-303d-a518-308629de9652 | -13.70512 | -51.88398 | 2026-08-16 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffb64383-0343-3711-bd26-cb223f899355 | -15.09629 | -48.71983 | 2026-08-16 03:55:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a31717b5-4243-3d6c-9a60-aca17aabe0a0 | -15.72231 | -42.25134 | 2026-08-16 03:55:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b8fc21b-cd5f-3c5d-8384-b3680448410b | -14.41626 | -51.95385 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e2107618-ff93-35a3-96ba-e62a0d08a79d | -12.68611 | -48.4798 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3088fd1e-7b68-3559-b7e5-cf527ff5a869 | -11.06844 | -47.27494 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3869fc7-670e-38e2-aabd-112266fcb334 | -10.27274 | -48.2938 | 2026-08-16 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c729876c-58ff-39c4-b838-5f3526275c66 | -10.51742 | -44.85859 | 2026-08-16 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f2070d08-f735-3a51-87e9-9590a44d9113 | -15.16589 | -50.06614 | 2026-08-16 03:55:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 56f0521b-7328-3648-8cbf-c66775162fd3 | -10.67872 | -49.00539 | 2026-08-16 03:55:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2f307b17-62f9-35db-b95e-42479ab65848 | -12.23938 | -47.00855 | 2026-08-16 03:55:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 517d42ae-4f85-3b2a-9edc-986f3c31e004 | -14.92858 | -46.61152 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 380b3816-aca0-34bd-8cfd-15b8f6c1c42d | -15.56874 | -42.36094 | 2026-08-16 03:55:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7806555a-c630-3e9f-84df-37a307b35a54 | -11.33459 | -46.21276 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4989742f-b86d-3b46-8788-b75a50dd30a3 | -12.70202 | -48.487 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4364250d-9bf0-32a3-8bf5-ace82a06b4fa | -13.50676 | -48.21838 | 2026-08-16 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3d1f98c-7de8-32b8-82cd-d963ae3d5032 | -11.0842 | -47.24965 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9656c52a-bd01-3224-8bd8-28c02d365e06 | -10.52824 | -44.85078 | 2026-08-16 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5ee0df5-09e6-3daa-b187-21db64bd8e18 | -15.06634 | -47.0284 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d3b80aca-0c82-3f39-a909-fceeaf34f870 | -12.00387 | -46.42149 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d3775eb7-7714-335f-8306-ba443abf8ae0 | -14.4796 | -45.6872 | 2026-08-16 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07388383-d022-38dc-935e-e00d154751fa | -12.74543 | -48.43547 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dbb91c55-7476-3fe8-a7e0-8d9d8c3d58bd | -13.44162 | -43.84016 | 2026-08-16 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1170de2-9a89-304d-bee8-e656ee307b86 | -15.05297 | -47.01944 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e974d3d4-92a1-335f-b8ad-e5a4c51f3087 | -14.3977 | -51.88084 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49c1359c-ba67-3642-a166-eea3821109d3 | -12.71723 | -48.46823 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dbfb427-44cd-3978-aa0a-ca8738c8e5fd | -15.57088 | -42.3701 | 2026-08-16 03:55:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6f49fe2-1b82-3104-a8ba-6b106282901f | -11.13989 | -49.04325 | 2026-08-16 03:55:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18dc5d5d-8cd1-3200-a7f0-b9e31cb7fff0 | -12.66616 | -48.46389 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59513212-cbbf-3213-ab9e-deb81c363c2f | -12.68049 | -48.44982 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a571ddd8-85e6-3d09-a9d0-c147c051f5b5 | -10.53648 | -44.85713 | 2026-08-16 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d486c839-11ec-3437-8cb1-591ee81c7e9b | -12.68283 | -48.46717 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1138b0d-e448-3830-b3d8-9fcb9e604e2c | -10.52738 | -44.85552 | 2026-08-16 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 45539f22-33f4-3d5d-a6a7-e17ffcba0b94 | -15.18011 | -49.50657 | 2026-08-16 03:55:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 965efdd3-81a9-31fa-b34f-9ecd3574f5d7 | -12.02785 | -46.43625 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d4cbf90f-40e3-3b6c-80cf-baa38b88794a | -10.15669 | -48.08868 | 2026-08-16 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38372edb-edf1-399d-bf76-689c5db80c5e | -15.06515 | -47.03465 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acdc6c28-caf2-39b1-b7fe-364b6c1a6119 | -10.71439 | -52.10999 | 2026-08-16 03:55:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| edf60eac-ce41-3d1b-a19e-498c5fc89f17 | -12.56976 | -47.85496 | 2026-08-16 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94057068-33ee-3738-a848-6532faaebd68 | -11.09487 | -47.25108 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bbc14d41-9741-3ab2-a529-4c519e0c361a | -11.32352 | -46.21781 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abd2efca-b318-3ab4-8543-71963b4f1101 | -14.38985 | -51.91631 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b4a8fdd-106a-3cde-8d7f-a2cbd33ae4db | -12.70597 | -48.46684 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5fffd9c8-2a0f-3952-8234-356c1d8d2f88 | -12.71647 | -48.4721 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e0c1d0d-8ce2-3b62-9e3f-bd4ef3256445 | -14.727 | -42.66505 | 2026-08-16 03:55:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84c9d375-63d1-306e-8a1a-b227fca5a60f | -14.39342 | -51.88227 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbde1c31-76d1-3edb-9f3c-c7fb4466e092 | -12.71306 | -48.46007 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a344881b-7d0a-3f81-98a2-ea959868a363 | -14.90676 | -46.62299 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f544f083-25db-3f1b-ad7b-59d9315d63a1 | -15.568 | -42.36521 | 2026-08-16 03:55:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f15317c9-7fb2-3e21-ac7b-c8d7f6130a2a | -14.39237 | -51.91942 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6989f083-b779-3f0b-b4e9-23311f94b1fd | -10.35736 | -46.68009 | 2026-08-16 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f57e50aa-567e-32f6-9fb2-19a4fe0a0c10 | -14.75575 | -40.85879 | 2026-08-16 03:55:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dfd09ad9-5f8b-364c-bff7-adcadd88ff5a | -10.71844 | -52.11197 | 2026-08-16 03:55:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6c02da81-8025-3c08-8800-c46681269f14 | -11.90384 | -45.98042 | 2026-08-16 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
