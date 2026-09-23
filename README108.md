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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 252bcec6-e7f6-357e-8c4e-2e4b15625f05 | -1.2136 | -54.54638 | 2026-09-23 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a83f846-4946-3fc5-a17a-f9d2c6404eb5 | -10.2884 | -50.54185 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 354d461d-a832-35b6-a0c8-010e8b47a0e1 | -5.80102 | -49.15302 | 2026-09-23 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82005dac-54fa-3860-908c-726e411a97ad | -4.38652 | -60.96613 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a859e55-d532-314c-b8e7-2a2ca844bc5e | -9.80824 | -48.30345 | 2026-09-23 05:23:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22b56d7b-9ddc-33a5-854b-dbe3d97b2dc0 | -12.36042 | -50.153 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8095368d-604c-3e10-86d1-9c4a89050e44 | -9.15134 | -61.19085 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19ee424c-ade9-3bd0-8b9f-05718938e098 | -3.68764 | -60.57963 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| f862b7e6-868d-3bb4-817a-2e6ffa60fbc4 | -3.34332 | -58.17354 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d50a2ab9-cdd1-3e48-9fdc-0590267deae2 | -10.2946 | -50.49205 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2328ea08-3ed1-3833-92a1-bd7f82288be1 | -10.31146 | -50.49068 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81b63f47-f1ab-3453-bbbb-f4a5eea7799d | -3.22877 | -53.95742 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 810bcee8-cd1b-3048-82e5-ebad75a3a10f | -3.69059 | -58.91985 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c1760c2-df6b-3e41-883a-f20023e191dc | -8.9435 | -50.9167 | 2026-09-23 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f6264c4-2163-350f-aa67-72fbcb46b2a2 | -9.10725 | -61.44197 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a675fbce-bf01-37d2-b5b4-bea92598969b | -3.254 | -53.95367 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa151503-924b-34f6-837d-cb6f5f9ca6a2 | -11.69904 | -50.78367 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e052f80c-6f95-3b4c-b213-8668e19d52d5 | -2.72322 | -57.64775 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b49cb531-60c3-367a-b467-ed8e0962b79d | -12.37809 | -50.1629 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 356cb50f-74ed-3f75-ae14-ee2beeeed76f | 1.17075 | -60.36831 | 2026-09-23 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2e9cbeb-e9dd-3ec5-aadd-d5c4913fc270 | -3.13744 | -60.71158 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0c06086-213d-3686-a688-6f35871f7ed4 | -4.0643 | -56.22538 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad7bd364-f986-30c6-928b-d6a874c0e571 | -5.8955 | -52.0931 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27522d97-993c-3f0e-8274-a5295da11362 | -3.65128 | -60.60836 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9dda8ae-2baa-32a3-8be0-66adabac799f | -10.27207 | -49.97614 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ac00cc25-1d30-33cd-85cb-dcc6b24490e4 | -5.35062 | -45.1652 | 2026-09-23 05:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca5cc8ae-72c3-3c43-afd9-8a7f47b324e6 | -10.28954 | -50.52438 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| b18d3d9c-d22a-33ce-b280-8c0f6c2cf899 | -2.97428 | -50.39795 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a082b52-83bb-37fe-afe5-fe035e809926 | -3.1162 | -60.68864 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7112ecc9-0c5f-332a-b86b-f47c300b4047 | -9.56173 | -65.99555 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cf5605d-170a-39e3-b3d7-6fccf37975f4 | -4.14924 | -63.42012 | 2026-09-23 05:23:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 91189f4f-8e71-3717-ae6d-985b543fac9e | -10.2886 | -50.53148 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f2ba62f0-9620-34f2-be3e-c8f9e5fef3cc | -3.25526 | -53.96646 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8fd5691-87b6-3981-9872-7e7f3abde095 | -11.77876 | -50.99781 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d980874-4a25-345e-8194-aa6843aaf3fa | -2.76355 | -57.02854 | 2026-09-23 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9fa737db-a6b1-350b-911d-6d84d46d2256 | -3.07143 | -54.39408 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b503d205-5878-31ed-8059-ffef41af4a2b | -11.70774 | -50.80294 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3762f63-61b7-3259-8334-f63c3f5e91c6 | -9.71692 | -48.33938 | 2026-09-23 05:23:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b80c6021-eeca-3832-b50c-d6a7f0c7a19c | -2.95732 | -54.08054 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fea16dfd-9042-3064-977d-608e3984e902 | -2.85598 | -57.79625 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35766191-2c14-354a-871f-22a2347ce75f | -3.30846 | -57.85676 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5ecbe79-b6c4-3c54-9c87-a7c17c1c5243 | -11.64703 | -50.98079 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81ca9345-d139-3c97-b282-4eac853a488b | -4.50251 | -54.95991 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7a73033-ca0d-3664-9cd2-5c6ca1b6b07e | -9.69962 | -58.13985 | 2026-09-23 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3387016f-c427-34f7-bc41-09cf883e0fb3 | -2.24049 | -48.74829 | 2026-09-23 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41c6cb38-4c23-3bd1-a4df-eee6af8065bb | -3.78564 | -55.87773 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb754182-b768-3bd8-8a90-466e45aa85f1 | -3.46353 | -59.55452 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43eb781d-f814-34d7-b1fe-df57eadd1c59 | -3.06625 | -54.40274 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4e99171-f192-3d56-afca-4b6e5be6d437 | -10.27909 | -50.51942 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a94717a-6638-3ba7-96d5-2c7de8d7a98d | -3.73591 | -59.42524 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a93e5be-bd4f-30de-9a2d-0681ec3d48bc | -11.64164 | -50.98008 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bc41962-2423-3028-82a8-0188954df3f9 | -3.69004 | -58.92331 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e7648d8-b74c-3aad-b081-ac955a9004f7 | -9.1579 | -61.37091 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7054315f-ac69-3218-9695-7d32023f1659 | -10.3206 | -50.50639 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c92c63b-2131-3aca-a0ef-1dbfeecd63ea | -2.46908 | -57.92334 | 2026-09-23 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12228552-36ac-3075-8552-624ee99bea63 | -2.41479 | -57.90033 | 2026-09-23 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa3a4217-11f9-3005-8cd3-ac31000dd635 | -3.79585 | -59.37029 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 904e45c4-9749-3590-903d-c2b834bc2081 | -3.10784 | -60.71861 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c79fe67-5402-3ecb-946b-2cca2bbb528e | -3.94605 | -57.08959 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9819f71-8197-3d7b-9f94-ee58f5155546 | -3.0619 | -51.24381 | 2026-09-23 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa9148d3-e089-3295-937f-3c2297726e64 | -3.13804 | -60.70777 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 860083f1-2152-3de0-b8ee-f87ce0cddfb4 | -11.99085 | -52.45779 | 2026-09-23 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 42d88f21-54d8-37cd-9ba6-e20c61b9e575 | -4.02849 | -59.85011 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88397554-7fce-316c-b2dd-2fe271905458 | -10.28766 | -50.53856 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 49a14168-9b00-339c-95ef-d67ef2438b49 | -9.1585 | -61.36726 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c212d2a-f180-39b1-bf69-c27612d63cbd | -8.371 | -62.94084 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e919400-c94f-309c-9e44-ae0d9cd218c2 | -9.9416 | -48.47625 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aec695fb-9543-3445-9c56-e45717045a53 | -8.92405 | -61.49125 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd7474de-0f21-37b6-bd99-de3afa00d9da | -11.63373 | -50.97827 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c160f2c-1724-328b-a9f1-e2cfa5beccc5 | -3.43044 | -61.32482 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe5e220c-44bf-33c2-b7d1-0059dc15dedf | -2.44083 | -57.86597 | 2026-09-23 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95122c71-ad89-3aef-be97-1bd7270ea28a | -3.7581 | -59.47897 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 928ed8d8-d25c-39d2-a4d1-251f43e81110 | -10.28221 | -50.53784 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 170d3a98-2d00-3e8a-8075-03896d6d453a | -3.15194 | -57.68622 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 384355f0-ef44-32e2-b3a6-f43ba0d250d4 | -3.14479 | -57.71002 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 468cbab0-b252-3e43-9898-640df6e54adc | -9.55959 | -65.99426 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 637eebff-dbd4-384c-9c80-e9b3067f16c7 | -10.44049 | -50.35712 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1d00c32-ec59-3916-9200-e1f5d020e03d | -11.77962 | -50.99086 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 062836ae-80c2-3599-be76-2d2e4c8fb585 | -3.53313 | -59.61249 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 414936a7-9f39-36af-9fc5-6fff6a2821c3 | -3.90622 | -60.59402 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42207f30-7529-3705-b36b-c3a6593f5e22 | -4.83637 | -55.76837 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d45d40e6-a5e7-3309-b006-21578ed10b22 | -2.23995 | -48.75185 | 2026-09-23 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 692a81fe-687f-3978-b687-04bf232973f8 | -3.35761 | -61.30557 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dbce43f-3bc7-37ca-8ce3-45017bff403d | -2.41197 | -58.28429 | 2026-09-23 05:23:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e63bdff-25ce-3eb2-a12d-4fb6d522c6cc | -8.52221 | -67.00723 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60d6970e-2c57-3390-a648-1ef68cfbb275 | -9.09148 | -61.43181 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 782684a3-5907-3f5a-b702-5fda7aa6b719 | -3.46688 | -59.55504 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 238a2765-5033-3292-86f0-f8920d350f1e | -3.73747 | -55.97893 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f3b1974-a8e2-319d-a398-cac48116d90b | -3.39949 | -61.29103 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b981adff-f211-3443-b6f4-1b8cc75e59fb | -3.46144 | -60.26344 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31f7a37d-0613-3e1d-90c2-a8b30ac6adaf | -3.7794 | -59.59737 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdc6a147-c81c-3edb-98ac-8ecaa6280e9e | -10.30331 | -50.51132 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcb7be42-2cea-3950-b6b5-8495dc44de96 | -5.87468 | -52.07522 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f77d9eb6-4e9e-363d-b8de-1d326ccf09bd | -1.49457 | -55.8324 | 2026-09-23 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4284ca0-6e55-31e7-981e-807ba4ed13a8 | -5.88595 | -52.28125 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c4c29d3-791c-3f3b-ad16-264bdbf3e9d0 | -3.78521 | -60.76023 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dca60f00-0151-3d5d-9c53-788eb12723d9 | -9.55671 | -65.99895 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 024e6c3b-d607-3fbc-98dc-6cdccc902f33 | -3.04584 | -61.26345 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a754265-9d84-32c3-b3c4-3cbdd9daa8e2 | -10.44556 | -50.36152 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 69cebaf4-44b6-3c20-bb9c-01096da78766 | -3.48925 | -59.18209 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README109.md)
