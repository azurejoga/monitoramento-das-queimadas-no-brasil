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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19791590-fc04-3bc0-8d12-0d6634c0c9d2 | -11.0377 | -45.1487 | 2025-09-04 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| d19f67b7-b926-3b48-b870-75dc23f5df93 | -9.4833 | -47.6104 | 2025-09-04 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 58d82e9b-cb84-339c-9e20-793d8a57e186 | -18.1305 | -51.7971 | 2025-09-04 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 4ce9130a-3e20-338a-95fa-dcc2a5eef976 | -7.6306 | -63.1203 | 2025-09-04 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| cfc2b662-aa88-3c70-84a5-f6689859a19b | -2.962 | -49.3437 | 2025-09-04 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| b8600497-6d70-36fe-9061-2d5da57c4b26 | -2.9619 | -49.365 | 2025-09-04 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| f8b389aa-8b80-3ccb-b740-6f829e93374d | -8.3639 | -48.3552 | 2025-09-04 00:40:00 | GOES-19 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 4196b844-bce8-3e93-bd5e-3574cc264f71 | -11.0568 | -45.146 | 2025-09-04 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| afe85e9b-12fc-3b78-a97d-37e4410035cf | -18.1505 | -51.7937 | 2025-09-04 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| ae1eaf9e-6d51-330f-a758-fef3cef173b4 | -12.9199 | -56.927 | 2025-09-04 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| abaa9f71-1cb9-3336-95e7-872a40f3c634 | -11.6409 | -54.5315 | 2025-09-04 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 48184798-7956-3cf2-bfc4-409fb9741051 | -5.6266 | -45.0252 | 2025-09-04 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 0d648547-ed74-38a7-9f41-e09a14342799 | -16.4622 | -49.5095 | 2025-09-04 00:40:00 | GOES-19 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0eb5bbf0-575a-3fa6-9766-1fbb85ac6353 | -8.6604 | -68.7473 | 2025-09-04 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 2f9cadc0-8852-389d-b25c-2b349577777e | -5.6079 | -45.0265 | 2025-09-04 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 277.2 |
| 06c1a01a-811a-34b1-a4be-c853878afda8 | -7.6307 | -63.1015 | 2025-09-04 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| bbae2814-cb92-3856-a428-24f9e6e4faf9 | -8.3641 | -48.3334 | 2025-09-04 00:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 226c5e22-bfa5-381e-a419-fe399dad8ef2 | -13.75 | -46.9346 | 2025-09-04 00:40:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 754600eb-3d5b-31e4-9c94-6d2e29200bc1 | -11.6338 | -52.193 | 2025-09-04 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 139d79b8-8f2a-30a0-85b1-6571c2e1fd28 | -7.6492 | -63.1008 | 2025-09-04 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4d373a70-6c95-394f-8833-16443e2f01a1 | -7.6491 | -63.1197 | 2025-09-04 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 2753af0d-c9fd-38fc-b169-b49f22128bfb | -12.9006 | -56.9488 | 2025-09-04 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 235.8 |
| 67091782-194f-372c-a87a-1699711997f3 | -16.4819 | -49.5061 | 2025-09-04 00:40:00 | GOES-19 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 633ddf25-0d97-3a43-80e8-12aa65e697b6 | -6.7465 | -63.1297 | 2025-09-04 00:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 135.3 |
| a16f6b4e-7967-3337-b611-ed16421d52f2 | -22.6567 | -43.6825 | 2025-09-04 00:40:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 111.4 |
| 588ed7f6-dbd0-3b89-ac75-a9f6f5bd7868 | -5.908 | -57.7311 | 2025-09-04 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 0243d037-1039-37e8-ba7d-1f2e7187c9db | -5.5892 | -45.0278 | 2025-09-04 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| b442be04-0433-35c2-8790-f01b8a2328dd | -10.5316 | -57.7747 | 2025-09-04 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 63f28d9c-e4eb-3901-9bd3-960ae5f9223e | -11.6599 | -54.5297 | 2025-09-04 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 7a4b7517-3b34-39c4-85c0-70ee5291a06b | -12.8816 | -56.9505 | 2025-09-04 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| abde37f6-7f8a-3c0c-94fe-c980fd64123b | -12.9197 | -56.9471 | 2025-09-04 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 8943f5d9-0659-3d17-9550-e7282d35026d | -11.0565 | -45.1691 | 2025-09-04 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 744687fa-f00e-3707-92e4-c0fc6f066fbc | -18.151 | -51.7719 | 2025-09-04 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f7d0314b-092b-34d4-a110-e43099005f1c | -6.7782 | -44.0876 | 2025-09-04 00:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| eb35e236-c9d8-36af-b26a-cff07c0916f3 | -12.9009 | -56.9287 | 2025-09-04 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 157.4 |
| cbbca6b4-953b-3649-83ba-8ff6057b0d14 | -10.4469 | -50.3926 | 2025-09-04 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 24fb8c8d-6be8-3fa6-bf16-670e3143ce8f | -7.7066 | -50.3188 | 2025-09-04 00:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| d1199397-1cd5-3e14-85f4-ed6b72137fd9 | -6.7833 | -63.1286 | 2025-09-04 00:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 65e76769-f73f-32be-b7a7-b2953b0197a8 | -7.6306 | -63.1203 | 2025-09-04 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 0ed3c550-7188-3f02-9496-6adfe82c4adb | -5.9081 | -57.7116 | 2025-09-04 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| c45ecf0b-889c-3973-8144-48cc0f78f20d | -17.1688 | -46.2651 | 2025-09-04 00:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 90825f27-8d26-3cbd-87cc-cfa986b8e2a5 | -5.6077 | -45.0492 | 2025-09-04 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 2169bb94-2ec0-3269-8908-cd48c2e34c97 | -4.9951 | -56.256 | 2025-09-04 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| f2657aaf-73f8-355a-ae07-082b828276dc | -6.797 | -44.0859 | 2025-09-04 00:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| f6af534d-4ba8-3d32-9b8a-9f999c82b66b | -10.4469 | -50.3926 | 2025-09-04 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 03687544-073b-3e9d-99c9-7e56dc5f68ab | -7.7066 | -50.3188 | 2025-09-04 00:50:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b0eea09e-9600-3a0c-83ce-24bb0a9e935f | -2.962 | -49.3437 | 2025-09-04 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 92b81d74-25be-3f4d-b503-f150c6c4c198 | -18.1505 | -51.7937 | 2025-09-04 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 3bb15536-214e-3740-9319-0678fcd8b768 | -11.2005 | -55.0195 | 2025-09-04 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| b5c82b7f-2880-3043-a020-28e2699c743e | -16.4622 | -49.5095 | 2025-09-04 00:50:00 | GOES-19 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 2fa3c150-3387-3b63-a9e3-172984266d40 | -13.75 | -46.9346 | 2025-09-04 00:50:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 8f4d5da7-adfd-3b76-86b8-960637c9380c | -11.0572 | -45.123 | 2025-09-04 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b776eea7-eaf8-394c-a1a9-e30ec97cf8b2 | -6.7782 | -44.0876 | 2025-09-04 00:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 4f5e847d-14f5-362e-8140-94a9f651d3d0 | -11.6599 | -54.5297 | 2025-09-04 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| a7ce7b0b-fe06-3bc2-b2d8-598a3dc72782 | -8.3641 | -48.3334 | 2025-09-04 00:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 32c94170-aa55-3a03-9dc3-1447af475819 | -7.6491 | -63.1197 | 2025-09-04 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 004c4d6f-fd44-3051-ba40-4eb2d65c4cf5 | -11.0568 | -45.146 | 2025-09-04 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 209.9 |
| 6468c35e-4fe8-39f2-9a49-ed108dc7628a | -6.7649 | -63.1292 | 2025-09-04 00:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 124.0 |
| c0c576bb-c4ee-3a08-a7ec-149782adbc18 | -11.0565 | -45.1691 | 2025-09-04 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| eb917e98-3c8d-3f0e-9099-358591ae33fe | -12.9859 | -54.7891 | 2025-09-04 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d7a443d2-9b80-3226-aef1-c7f020676751 | -11.0377 | -45.1487 | 2025-09-04 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d543179c-3f42-3715-befe-4483efd00e39 | -2.9619 | -49.365 | 2025-09-04 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| fbbb68a5-5400-3244-a14e-3291070250c3 | -12.9189 | -57.0074 | 2025-09-04 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 440fc049-3353-3ea4-b14d-e1f0ed241edb | -5.908 | -57.7311 | 2025-09-04 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 11ed24d1-2097-3b4b-a629-e0eeef5b24c2 | -6.0923 | -57.7238 | 2025-09-04 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 3714cff8-511f-3a4a-8b03-c511d8f6c2f6 | -5.6079 | -45.0265 | 2025-09-04 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 311.1 |
| acfc6cf2-87bd-3408-a16a-f47d6d82108e | -6.7648 | -63.1479 | 2025-09-04 00:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 0bc37033-df1c-3d5c-8c78-6fe9142aee27 | -11.5779 | -52.115 | 2025-09-04 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 50c0436f-ef47-3ecf-9ee4-718c8d820173 | -5.6081 | -45.0038 | 2025-09-04 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| a3a348f7-6080-3879-9fc4-c27be1c04840 | -6.7832 | -63.1474 | 2025-09-04 00:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| dc43b90e-3fa6-30f1-a76d-a3dc97ba4e06 | -11.6409 | -54.5315 | 2025-09-04 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 2344d828-ce24-3248-b790-623128576a0c | -18.151 | -51.7719 | 2025-09-04 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| b5e1b138-85e3-3247-9d35-950be7b69329 | -5.5892 | -45.0278 | 2025-09-04 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 8ef38f8a-566c-3250-bdc4-faaf47960abb | -10.4472 | -50.3713 | 2025-09-04 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| eeb394ae-2124-3bcb-a69c-ff554d4fa705 | -5.6266 | -45.0252 | 2025-09-04 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b3332444-cb34-3548-af54-4d8d777e13c9 | -2.8491 | -49.335899 | 2025-09-04 00:57:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 559a3100-fa50-30f0-83de-65fb1fc82390 | -15.2068 | -52.755199 | 2025-09-04 00:57:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d494789a-7788-342a-bfd7-b30c3f21a39d | -7.5891 | -48.748299 | 2025-09-04 00:57:00 | METOP-B | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 278b8d27-8133-358a-9ce4-174a567a9346 | -16.3626 | -49.511002 | 2025-09-04 00:57:00 | METOP-B | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5990d42e-817f-3b1e-89de-9d15b78e45fe | -5.8095 | -57.728401 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf3d713d-24cb-38c5-9ea7-a5679776ccd6 | -11.1035 | -55.031101 | 2025-09-04 00:57:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2c136dc-ac5a-385e-96b9-5d06089b1166 | -20.086 | -48.711399 | 2025-09-04 00:57:00 | METOP-B | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9a1f385f-3c53-3415-8482-fea82e9c7677 | -4.9329 | -56.114899 | 2025-09-04 00:57:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fb9fdc2-d02d-3e8e-aabd-c5af32c2dd71 | -10.8767 | -49.7556 | 2025-09-04 00:57:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54b85798-927f-3278-89ca-25ae3a2256fc | -14.486 | -53.0229 | 2025-09-04 00:57:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 63a4eb75-78dd-333b-91e2-0cb6b68ef49a | -10.3908 | -53.6464 | 2025-09-04 00:57:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95428b16-f2fb-306f-8aa7-53fd82d55d4a | -12.8224 | -57.011002 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14c7dcfb-8c7a-3137-9dc1-a26323481118 | -16.4529 | -55.1138 | 2025-09-04 00:57:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c151736c-a283-3211-87ff-c3d9d8d783c2 | -8.2464 | -48.316101 | 2025-09-04 00:57:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb812838-7f7a-3485-a18e-3bc77e1c8f55 | -12.5511 | -56.997501 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3750c26-d043-317a-b9ba-a0e4781b69e4 | -7.6343 | -48.7649 | 2025-09-04 00:57:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 15cc0686-9df3-3d96-b29d-4d87c7b598e8 | -18.0459 | -51.795898 | 2025-09-04 00:57:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 75554f3e-0492-36dd-94f0-73f691b9a315 | -15.0807 | -52.3689 | 2025-09-04 00:57:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c8fd1b8-83d4-3b4e-a878-53a0aff8836d | -17.763399 | -51.536701 | 2025-09-04 00:57:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e7ed310b-c65a-39b6-9120-6aa0353e7108 | -12.809 | -56.952202 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5036e07-d492-3a0e-9e57-b67fdc84efa7 | -11.1013 | -55.0219 | 2025-09-04 00:57:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42a14da6-0b03-349f-b564-7d36889a9478 | -11.7772 | -51.558102 | 2025-09-04 00:57:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7f83ce3c-4170-35c4-bfb1-1cbf60ae4e0b | -7.6054 | -50.318401 | 2025-09-04 00:57:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe400b53-fe3b-3471-8099-8b30470d3b2a | -15.6496 | -53.641201 | 2025-09-04 00:57:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0b9a76b-edc5-359c-961b-8c2e8f8ebc90 | -4.9046 | -56.2593 | 2025-09-04 00:57:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
