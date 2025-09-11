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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 862dccbe-61f2-3faf-95bf-d78ff8af1fc9 | -18.0552 | -50.7138 | 2025-09-11 07:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5f0d1518-81da-306c-b3d9-761cf543a3f4 | -18.0547 | -50.7359 | 2025-09-11 07:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 9fe01acd-394c-3c6d-b1d1-0785c841d7e6 | -15.1371 | -52.4252 | 2025-09-11 08:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 215236e4-8e00-3a32-b1a6-82dd738a4404 | -15.1211 | -50.1438 | 2025-09-11 08:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 3dd3bc13-27d5-3352-bb01-36a2429ea0f4 | -18.0547 | -50.7359 | 2025-09-11 08:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| e4be7893-b4c0-35d6-8638-2afe1099a3c4 | -15.1211 | -50.1438 | 2025-09-11 08:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 287c5441-cb64-3a39-a72f-ccf276ba71e3 | -11.5076 | -50.3847 | 2025-09-11 08:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c048bba3-914b-3c91-84d1-61a22ad420d5 | -18.0547 | -50.7359 | 2025-09-11 08:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| ce299cb7-dc3f-38f2-8c4b-5f385c47aa49 | -15.118 | -52.4066 | 2025-09-11 08:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| f108455d-44d2-3893-a245-2fca1cae46ec | -10.0695 | -50.3881 | 2025-09-11 08:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 84eec107-dc91-3144-839d-9d8f711320a5 | -10.0698 | -50.3668 | 2025-09-11 08:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 416dc919-7d22-327e-99f6-09d196e0e961 | -15.1012 | -50.1687 | 2025-09-11 08:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 61a99e19-e1af-3a51-91f3-580bc7976c7c | -15.1016 | -50.1468 | 2025-09-11 08:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ad4f96ea-9d9e-3eb9-b869-adb1dafaa9a7 | -15.1211 | -50.1438 | 2025-09-11 08:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 122375a3-5b97-35fe-afc3-e044ed510def | -15.1371 | -52.4252 | 2025-09-11 08:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 4923571f-beb2-32ad-8885-d15920ff9c81 | -15.6732 | -47.0389 | 2025-09-11 10:00:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 170.0 |
| f471c188-a9fb-3b74-8ec3-91e98cc0eb7e | -14.1297 | -45.4043 | 2025-09-11 10:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 996a8492-bdae-3e18-ac67-29c9b996ad36 | -14.1297 | -45.4043 | 2025-09-11 10:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 4442565e-534d-3843-9f8b-ee69cf7242a3 | -8.8755 | -49.5613 | 2025-09-11 10:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 68e12822-4a18-36eb-aa15-49484778e0c5 | -11.4285 | -43.5544 | 2025-09-11 10:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 6fb79f8c-168a-3335-ab17-594b4bf8be97 | -12.6632 | -45.3008 | 2025-09-11 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| d99f6c70-578e-3794-94d6-9c60366af282 | -10.1844 | -46.1927 | 2025-09-11 10:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 954395cb-da46-3ea7-8453-dac3d35e50b1 | -9.0942 | -47.076 | 2025-09-11 10:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| eaac5937-d8f9-3d06-a036-c6ef9848fd67 | -14.1297 | -45.4043 | 2025-09-11 10:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d680a21b-a282-3826-8da5-5a434b786940 | -11.4285 | -43.5544 | 2025-09-11 10:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 9ee9cf4e-cc33-3484-ad97-5d00faf439df | -8.8755 | -49.5613 | 2025-09-11 10:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| b023bffa-ca6a-3411-b461-1d2238659f71 | -9.1145 | -46.9629 | 2025-09-11 10:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| c4aec9b5-c5e4-3d37-9910-bb0a3ee04f4f | -11.4285 | -43.5544 | 2025-09-11 10:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 265eaf1b-e82f-3caf-bfba-face7d75816a | -8.8755 | -49.5613 | 2025-09-11 10:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 56216039-d85a-3c87-a68a-c33e87eb2672 | -10.4077 | -50.5032 | 2025-09-11 10:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 216.4 |
| bcc38693-a8d0-3dbd-bd87-d57fe89723a4 | -12.6632 | -45.3008 | 2025-09-11 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| c03eeec0-1ebe-3386-a8cf-fd301dc5a1de | -19.9994 | -47.6271 | 2025-09-11 10:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 3eb1d287-b048-3c5c-8c87-0ac1d9724d97 | -10.4074 | -50.5245 | 2025-09-11 10:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 70987612-69e9-36fa-b234-aac50e7c2c5a | -10.3888 | -50.5051 | 2025-09-11 10:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 49f2e3f9-a192-3d9a-8713-6d8a68770672 | -9.0579 | -46.9688 | 2025-09-11 10:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b88103fc-4504-3e22-8f0b-0a7cb12131d9 | -10.4077 | -50.5032 | 2025-09-11 11:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 81087c0d-44e9-3c93-8699-e589f3ebb1f5 | -12.6825 | -45.2977 | 2025-09-11 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 3478e4e9-6b3c-3c8f-8a2e-af0da03bc2d6 | -20.717 | -46.0636 | 2025-09-11 11:00:00 | GOES-19 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 104.4 |
| a1ea5d33-c490-3b27-af10-8ed215457073 | -14.3122 | -45.046 | 2025-09-11 11:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e0774cd8-91fa-3242-bf9d-dfd05d1c867f | -12.6632 | -45.3008 | 2025-09-11 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| fff087af-5b4b-38f7-8403-963b3f931a05 | -10.4074 | -50.5245 | 2025-09-11 11:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 6ad68e1f-2a46-3a8e-a284-c145a1496d23 | -19.9994 | -47.6271 | 2025-09-11 11:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 5ce96f92-1d01-37ad-873d-e8ebf411652c | -19.9797 | -47.6084 | 2025-09-11 11:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 252.0 |
| 3e9c4b49-13d5-368b-a303-97214eae52e8 | -19.979 | -47.6318 | 2025-09-11 11:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 375.0 |
| 0d6763f1-b48c-36b5-a58c-335b63d0aaeb | -12.6829 | -45.2746 | 2025-09-11 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| ae1994a6-c623-3253-85c6-6ac12803d9d2 | -11.4285 | -43.5544 | 2025-09-11 11:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| b6c5743c-ad04-307b-b707-d24ef77a1a67 | -19.979 | -47.6318 | 2025-09-11 11:10:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 8c68601b-deb7-375c-8856-60c9fbee4b8d | -12.6825 | -45.2977 | 2025-09-11 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| f65eafa8-2092-3a53-9450-cf8b4a054fce | -10.4074 | -50.5245 | 2025-09-11 11:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 6b3361a0-cfe8-302c-a95d-33762c748312 | -9.0579 | -46.9688 | 2025-09-11 11:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 18d5f033-b9fd-34be-8e7d-4be2afc3e2ab | -20.717 | -46.0636 | 2025-09-11 11:10:00 | GOES-19 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 75147332-c189-3227-9db6-0e738b1c3cdc | -12.6632 | -45.3008 | 2025-09-11 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 07384dc1-82bb-32eb-8b08-64d4c0daad47 | -8.8755 | -49.5613 | 2025-09-11 11:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| f3e112f4-59c1-397a-95b9-4564faf7147a | -12.6825 | -45.2977 | 2025-09-11 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 606988c6-24e6-3ef2-a5ea-29631040b6e7 | -15.6737 | -47.016 | 2025-09-11 11:20:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| c88a69d8-eff3-388a-b000-750cf2716d2a | -11.4093 | -43.5573 | 2025-09-11 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 91579474-73ee-32d5-874f-e3c7adccf884 | -12.6829 | -45.2746 | 2025-09-11 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 5b4120e8-fc6a-3ad7-928c-4e54a3047fd6 | -9.8154 | -46.8195 | 2025-09-11 11:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 5e6dd273-4998-3752-99d0-5c710b784f45 | -15.8703 | -54.9358 | 2025-09-11 11:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 94304823-dbae-3c20-9341-5e4637f475f6 | -15.6732 | -47.0389 | 2025-09-11 11:20:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 28906f2a-2563-36ef-bf58-3156318e7c3d | -12.6632 | -45.3008 | 2025-09-11 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 216.2 |
| c81f2734-85d3-3946-9cb8-a7d52016f9f0 | -9.0579 | -46.9688 | 2025-09-11 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 4598eca4-9181-32a7-990a-43c2f4ea64c7 | -15.1565 | -52.4226 | 2025-09-11 11:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 76ea2495-a18c-36c0-9a97-e42d42c851b7 | -10.1844 | -46.1927 | 2025-09-11 11:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 6d1713ce-be31-3b96-9c32-72b2e4c92a11 | -11.4285 | -43.5544 | 2025-09-11 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 11ac85e2-d1c3-3073-ac27-d203a7e00497 | -10.184 | -46.2153 | 2025-09-11 11:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 2470eb52-2b2c-356d-8eeb-64b6a1d4f5ee | -8.1649 | -46.0983 | 2025-09-11 11:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 964fb7bd-edf9-3ca6-8606-a19570c543af | -10.1844 | -46.1927 | 2025-09-11 11:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e6728894-4534-30c0-8fe7-9f523699c210 | -12.6632 | -45.3008 | 2025-09-11 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 181.9 |
| b888b190-2fc8-3cda-823d-a7225a4f5c4d | -8.8755 | -49.5613 | 2025-09-11 11:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 3d8e4189-8eb5-3e20-9ff2-22dcd27a0667 | -12.6829 | -45.2746 | 2025-09-11 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 51776d55-1db1-35eb-b2ad-069ac042f6c2 | -19.9994 | -47.6271 | 2025-09-11 11:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 99.0 |
| f1a32628-0cf4-384e-8ab6-3d1daf1442b6 | -9.0579 | -46.9688 | 2025-09-11 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 27c266d4-37eb-3bb0-ab02-fcc6d4d84d16 | -19.979 | -47.6318 | 2025-09-11 11:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 157.1 |
| d1fd2b45-9594-3f65-8868-37e427248596 | -15.6737 | -47.016 | 2025-09-11 11:30:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 315.6 |
| e0bfd7a9-a947-3423-9581-92cd57457844 | -12.6825 | -45.2977 | 2025-09-11 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 108a22b2-27ac-36bd-b940-bed6619d4f8d | -15.6732 | -47.0389 | 2025-09-11 11:30:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 16444f6d-94d8-3d29-8cbf-01857a290996 | -15.118 | -52.4066 | 2025-09-11 11:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 7a5aaed7-e944-3c6c-bad7-0deba0313405 | -11.4093 | -43.5573 | 2025-09-11 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| a934beae-8f04-33fc-8480-d5272c1e2ae9 | -19.9994 | -47.6271 | 2025-09-11 11:40:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 781c5e07-4896-3c8f-a740-8e401cf1c8a1 | -9.0579 | -46.9688 | 2025-09-11 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| c61bafca-d5b8-3ff0-84c0-d43d9a2c3c60 | -14.5128 | -53.9158 | 2025-09-11 11:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 81aefcc9-3426-3b08-8161-3061c57e5f69 | -15.6737 | -47.016 | 2025-09-11 11:40:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 372f081b-a02a-3214-a77a-e8e1ed982882 | -15.6732 | -47.0389 | 2025-09-11 11:40:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| dcd3dcae-6959-3cb1-a485-9b30074fcf25 | -12.6829 | -45.2746 | 2025-09-11 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| c823cb7f-0007-3f6e-a13d-f2eb71230e5d | -15.118 | -52.4066 | 2025-09-11 11:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 98ad039c-ac67-3c33-988e-40f42d16db0e | -8.8755 | -49.5613 | 2025-09-11 11:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 8c6008bc-91ae-3a0a-a108-56af72e24931 | -12.6825 | -45.2977 | 2025-09-11 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 96256a70-f30c-3dbe-ae74-75d34f1c75ee | -19.979 | -47.6318 | 2025-09-11 11:40:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 4b3587ba-4a39-3961-9e81-77174fb82e77 | -12.6632 | -45.3008 | 2025-09-11 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| d012a31a-07da-36bc-b9b9-f8ea7a38798d | -8.7411 | -45.2248 | 2025-09-11 11:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| fafc48b7-3cbf-3d09-bb71-c5b7c9e713e0 | -11.7211 | -46.5127 | 2025-09-11 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 6aca3bc0-d921-334e-a2d4-54d3fb96c684 | -15.6737 | -47.016 | 2025-09-11 11:50:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 6339a3e0-0999-3758-a93a-9a34b2f100b1 | -9.0579 | -46.9688 | 2025-09-11 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 3f78eff2-7900-37f8-93f6-27d8a868b0b8 | -15.6732 | -47.0389 | 2025-09-11 11:50:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 904d20b1-7fbd-3cfb-bcf9-9b2d82c4970a | -10.203 | -46.213 | 2025-09-11 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| ae20d4f3-8182-3a97-af41-236f92dea97e | -9.039 | -46.9707 | 2025-09-11 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 0b7f8d04-722b-3623-99b0-e6549fe0e537 | -19.9994 | -47.6271 | 2025-09-11 11:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a86a55d8-5385-3c87-b90a-d3529c81df0c | -11.4285 | -43.5544 | 2025-09-11 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 32b14a09-8535-3302-8a28-ba4ccbab9162 | -19.979 | -47.6318 | 2025-09-11 11:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 92.0 |


[Clique aqui para ver as próximas entradas](README132.md)
