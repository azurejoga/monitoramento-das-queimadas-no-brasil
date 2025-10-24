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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43b34056-0454-3d97-90bc-6d8f2241d6fd | -3.24043 | -48.76824 | 2025-10-24 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58cbd716-5939-3136-b873-0699b0ece344 | -5.67809 | -48.86676 | 2025-10-24 04:38:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d75acdcd-4e75-38c1-9401-6fefa755b828 | -3.80193 | -51.75033 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed39becf-9b2f-3ae8-94bd-37d2e53aa5e2 | -6.90233 | -43.59249 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0ceae9c-487e-3cd4-b15b-451c8318b718 | -3.02759 | -49.48978 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5fe3904-ecaa-34ac-bd13-cb6dbf9a86b8 | -4.55209 | -49.62646 | 2025-10-24 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8388ac9f-addf-32e8-9ccd-06a7afb5afb9 | -3.48964 | -50.04802 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a7a439b-7878-3f7a-ae0c-82eb7da64410 | -2.87238 | -50.71205 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5e2a82b-2ed2-3eee-853a-469874e1a6ed | -5.4496 | -45.41029 | 2025-10-24 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 21c4877d-0494-3694-a571-a104f49698f9 | -8.32623 | -46.78708 | 2025-10-24 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b47e07a1-3aab-3234-96b3-eb181a0dce47 | -10.11159 | -47.77611 | 2025-10-24 04:38:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f786fce6-8358-3b8e-8f07-ed5dc938efb5 | -7.27149 | -50.00581 | 2025-10-24 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9d3aec6-8ae2-3585-b961-4e9cd1cebf5c | -8.34262 | -46.17785 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2df4cd28-3917-3769-b0c3-2b8e2d90adec | -8.34987 | -49.39576 | 2025-10-24 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd00778a-7475-362c-bc5c-3d41d7ab641a | -9.49808 | -51.82286 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dd28d34-0385-3f57-9efd-974a7fd88832 | -2.58403 | -51.34357 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1681b31-7f2b-3dd4-abbe-406d15b5e4b5 | -2.80793 | -51.34831 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bde20cb-342a-35e6-9b79-bb4e1ba27fb1 | -2.72772 | -49.56183 | 2025-10-24 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 371e8539-1b0c-32fe-a0a4-4e5552fb29cf | -2.81197 | -49.13474 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc5bab9d-996f-39a2-8976-5e1709470554 | -9.23846 | -51.8231 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63529a64-a860-3ddc-b8a3-781cf7b14a68 | -8.50955 | -44.20595 | 2025-10-24 04:38:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 768e157e-57f9-33ff-b272-4badbad22733 | -2.81364 | -49.14564 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| c80b1228-df6a-3f57-a8ab-acd08b4f756b | -8.66327 | -44.77682 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93166b23-a664-33ed-800c-649ccd0e9bf5 | -10.6391 | -42.30112 | 2025-10-24 04:38:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd9d28b6-4317-394a-b853-da9b8059096f | -9.93919 | -47.45439 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0f37d04-2832-315d-8dba-688bc0fa47ae | -8.68414 | -47.54838 | 2025-10-24 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 105fb37a-d90e-3597-8b16-07b7d4dd4c9c | -7.49314 | -42.5747 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6d26ea38-6955-36af-b102-27e249901196 | -6.12942 | -41.73456 | 2025-10-24 04:38:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d41a3e8c-9649-39a7-933b-04f9a7278b71 | -10.89748 | -44.74092 | 2025-10-24 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bd47fec-5bab-333d-b128-311fd4dca980 | -8.69636 | -45.80547 | 2025-10-24 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e73d8708-451c-342a-a3e0-3259d1f86669 | -2.63654 | -54.86876 | 2025-10-24 04:38:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fb5e7e0-b526-34ea-8ff1-ebe2b5a28e26 | -10.46958 | -49.10513 | 2025-10-24 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25448d42-6b38-3e9c-9122-0eed3c89d572 | -7.82017 | -45.38104 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f004fad-57d7-3ecf-aa50-8258570c4bae | -6.88917 | -43.6227 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f315d471-6523-333f-9b1b-eba4ee89742f | -10.63835 | -42.30665 | 2025-10-24 04:38:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 286cdec3-5e19-39f3-8193-f9c33017c196 | -7.83166 | -45.3828 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab39eda0-2cca-3243-b62c-162e25308f7e | -6.77812 | -45.47138 | 2025-10-24 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab614171-2406-3bee-81b7-d76868ce1d24 | -9.97411 | -47.06965 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2842569b-8c2a-3de2-9708-be4037b9bb5e | -2.80424 | -49.14062 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cc1e67a0-3520-3375-b5d0-4b5fbf042b79 | -10.00398 | -48.09695 | 2025-10-24 04:38:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 739f29ed-9540-3425-b281-db6c1d536107 | -6.83833 | -41.56081 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1ba9ce98-1dd6-346f-b733-2afbf77dc801 | -3.25609 | -49.12017 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 980e138f-50ac-3dcc-82b4-161210c22bc9 | -3.13151 | -49.52073 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 66165c81-a578-3b87-84ce-8bef7e0a1711 | -3.80055 | -51.74923 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac25f6bb-f3b7-3ca9-88f3-f3640a99e750 | -6.53622 | -41.68898 | 2025-10-24 04:38:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8f8d6550-4b83-34e7-8cae-24853ee9699a | -9.25867 | -46.47224 | 2025-10-24 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a4bbe1c-e35d-3713-b008-b26d0a17793b | -5.65485 | -49.05751 | 2025-10-24 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46e35571-c22f-3ede-a0ec-fc80c1b06245 | -8.4304 | -45.59161 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f48ab2a-90ff-3bcf-b730-7cf022337621 | -3.08875 | -49.51044 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76ec70f5-8162-3f43-aeac-8eec8354f611 | -7.99361 | -49.75868 | 2025-10-24 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 436fc49a-63e2-3885-86b1-ea2c3fabd39f | -6.94882 | -44.02194 | 2025-10-24 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2255d8cb-eaeb-3263-86aa-5b589d83d00c | -7.39838 | -43.91619 | 2025-10-24 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4477a48-4331-3041-8398-36c7fd78e1e7 | -8.5647 | -48.51333 | 2025-10-24 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ae0287e-d9a8-3c79-a6c5-c62d2772ba8b | -10.01949 | -47.08496 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a9e5ca2-ad9c-3d14-b0a7-99c647687e87 | -4.31366 | -48.23119 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2b11ef9c-c2ee-3daa-8482-d2b47066760e | -4.54987 | -46.74097 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a1e54ed-7142-36ef-8b65-e05c0ac02b2c | -5.43204 | -40.88497 | 2025-10-24 04:38:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ce8bc72-ac75-3c86-aa3d-533cb80f9f50 | -7.49018 | -49.50464 | 2025-10-24 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7191ddaf-084b-3e36-a6e2-9e31745cf14c | -6.44614 | -43.82201 | 2025-10-24 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c23eab36-30c9-389e-96c1-abe5906b32af | -7.62591 | -41.8578 | 2025-10-24 04:38:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7b067195-48ad-3f4c-a5b4-4f32472525fb | -7.30459 | -49.17331 | 2025-10-24 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcc737ef-4071-3b07-a523-f0b6ec733761 | -9.62362 | -50.7069 | 2025-10-24 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90e878f7-fe19-3542-805e-76fadfdb4760 | -6.10994 | -48.10572 | 2025-10-24 04:38:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d863107-b823-3720-a25e-79d06f584dc0 | -5.65834 | -50.1718 | 2025-10-24 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b03933ad-c339-3a1d-8d90-a5d0e0de8a09 | -4.31035 | -48.23067 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 960273ef-8ed0-313e-bf57-be1e8fade5dd | -9.4491 | -46.09835 | 2025-10-24 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab7face4-e6df-3276-adda-4a6b59da2672 | -10.87441 | -44.41339 | 2025-10-24 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbcec62c-c251-3455-8511-4fb179250913 | -5.66692 | -49.79646 | 2025-10-24 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c4fa34d-e41f-3ad2-86f7-2001e7a8699a | -5.65018 | -46.57653 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67355af6-cfd4-34c0-8849-c852adece236 | -4.46157 | -43.23955 | 2025-10-24 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8a31eacd-8395-3d3f-bf9a-327d5da31076 | -6.28062 | -47.01201 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 060b2031-ef6a-39a8-94db-f3fabe1f16b4 | -3.70138 | -47.65009 | 2025-10-24 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b8b52b4-746b-367f-91cf-8bc9b4ea8c50 | -3.02148 | -49.48524 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1675500f-90cd-31c6-9599-641845447ad7 | -2.80373 | -51.35176 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 635e5bc9-fd2c-3a35-947e-8f797665fb10 | -7.85095 | -49.32724 | 2025-10-24 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cc59799-3ccb-3a74-9615-36f171b1713c | -5.40427 | -46.41221 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8c3fb51-49b3-3a5f-a66d-6abafb281a72 | -7.83065 | -45.38049 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c604245b-8d8a-3053-b455-3917ae96dea4 | -3.80347 | -51.75387 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05312b0d-043f-3538-9b5d-c53eb0612228 | -7.55536 | -47.37018 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8255690d-3154-36ae-bf44-40ead382f99b | -6.89881 | -43.61612 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60f09fbf-f4e4-3904-b08f-005f214eafea | -2.95237 | -49.15001 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a90d985c-3890-331c-8e22-2ee4943e98db | -7.12591 | -45.49753 | 2025-10-24 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74ed233f-3409-314e-91bd-f2201944019e | -2.80243 | -51.3598 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d088ba14-5e0b-3d17-8349-df1118db0aa0 | -9.59947 | -46.92051 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0a13c27-9858-399e-a9b8-0ed65bb090b3 | -7.68944 | -42.24265 | 2025-10-24 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 91e5f0b2-f3c4-3bc0-8f56-34f38f40d282 | -2.98008 | -51.33771 | 2025-10-24 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e2b315d-b80f-35e7-a7da-a65ce9e08fbc | -9.63195 | -46.90005 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8cec09e3-c24d-37f3-9dcf-a6cec67fe497 | -10.42499 | -49.3714 | 2025-10-24 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d13c27c7-f9cf-31fb-af18-5e3b15632310 | -2.86832 | -50.71529 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 181a6234-b4a7-311d-b068-46cf96f23ca2 | -4.98662 | -44.14735 | 2025-10-24 04:38:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec9e8b86-d721-3bf8-90f2-653fb2da707e | -2.85256 | -50.74775 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd6a06b2-fd83-3b74-9591-23d763bb1179 | -6.35322 | -47.0619 | 2025-10-24 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cda60a6-4912-3fcc-bff8-f6c2b4de066c | -4.20769 | -48.60343 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3cafa66-09c1-3adb-bef1-490399bf1794 | -2.85722 | -50.74071 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ebdf8b5-6df8-33fb-bd53-08d1c591906d | -5.65583 | -45.9513 | 2025-10-24 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf2a7ec4-5ea7-3251-a021-fea9c467614e | -8.34568 | -46.1826 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| adb44210-392f-3439-8ced-7abf4c132467 | -9.59588 | -46.91995 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84884ab3-292c-3c52-a966-49bad4d04f13 | -9.12964 | -50.77834 | 2025-10-24 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06560e69-d755-38b4-9039-2b205ee115ba | -2.80921 | -49.13076 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4312520-b2eb-3ced-871a-4ed37cc23332 | -7.38368 | -46.54185 | 2025-10-24 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README37.md)
