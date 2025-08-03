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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb8729aa-57f9-371c-ac3b-7032aa28353b | -6.68408 | -44.34145 | 2025-08-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 434a04c7-f226-3e6c-90ea-21f913c05243 | -6.52887 | -44.53359 | 2025-08-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02a669ea-0fb6-3616-b411-c09bb7a450aa | -6.60982 | -44.04081 | 2025-08-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31b3950e-e106-3d83-ad70-03096f181484 | -4.55892 | -44.20855 | 2025-08-03 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 5802507c-a163-365a-bf2e-07605ec3ea88 | -7.19473 | -44.48618 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f8fde8d-2689-3cb2-ba01-853eb4f6b1a3 | -7.12302 | -44.08747 | 2025-08-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84c21f55-2695-3778-9427-1cf250424c79 | -6.20947 | -46.34819 | 2025-08-03 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60ebee40-8d67-3e18-817e-91e982e56e14 | -4.3144 | -48.10338 | 2025-08-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ae38ecc2-0377-3fa7-89ef-affcb431622a | -6.70759 | -44.27927 | 2025-08-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5939e403-9131-3ee2-a7ef-b799227176d6 | -6.67777 | -44.35993 | 2025-08-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1320d2c1-bb19-3971-83a1-01846781249c | -6.20339 | -46.34372 | 2025-08-03 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99080ca4-05cc-3a3c-b95c-d0d76d4f3710 | -8.03208 | -43.14165 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| f48e7ac3-b9f6-3718-9685-50e1366003da | -7.55661 | -44.41128 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73014b30-0bdd-32c5-8c9c-e0e800c89306 | -8.00014 | -43.18839 | 2025-08-03 04:25:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| cc8af13d-2e40-3736-b436-ea9768fa81f3 | -3.43703 | -48.95662 | 2025-08-03 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43e3ec4c-6a5c-3f10-9cc2-c0a04358e688 | -7.12295 | -44.38256 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8308fde-f0c2-3122-a648-d29c5cec6116 | -8.00471 | -43.15766 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 4281adbb-08ec-399d-a64a-3d62bf117c9e | -7.60001 | -44.98132 | 2025-08-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 868a8054-de76-3d24-98bd-06fcb438645a | -6.2067 | -46.34423 | 2025-08-03 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0d4cd13-3e40-355f-a9b9-92625fd3743d | -7.36367 | -44.66907 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1d7ba48-021c-3208-8b79-7de84532228a | -4.31381 | -48.10715 | 2025-08-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e937d6b9-4b98-3c35-ab27-27654247b7f5 | -7.13125 | -44.05705 | 2025-08-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4a6d7bc-3c06-3b19-9d04-05a62865cbdd | -7.78224 | -43.94272 | 2025-08-03 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 950829ad-bbfe-3af5-9041-e97d093b50dd | -5.07193 | -37.71622 | 2025-08-03 04:25:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e048946-d11a-3779-a8c1-457196f56056 | -6.99774 | -42.10348 | 2025-08-03 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4ce29762-5115-394a-9554-9602bc205570 | -7.1248 | -44.07584 | 2025-08-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7643a84d-7ccb-3307-a5f6-c6546e9cda72 | -7.9971 | -43.18341 | 2025-08-03 04:25:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 93b2aa2a-596b-39c0-a68f-c40b57ac744c | -7.1264 | -44.38317 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90efd75b-3831-37c4-baca-b57e8d73a365 | -8.03354 | -43.11681 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 10ee37cc-d207-33b1-8e19-bad86ae05ba4 | -7.13248 | -44.08039 | 2025-08-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0b1f65f-6d53-3850-b69a-ec98a9116639 | -6.52774 | -42.80407 | 2025-08-03 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5f9caa1e-8dc3-3607-aa00-d6bb8c01bcf4 | -8.01146 | -43.16318 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7c24efb2-650b-3c8b-89d1-9f4c95f45b9c | -8.01713 | -43.15056 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4d11aa69-50f2-3b9a-a2b1-8548803144b1 | -7.63443 | -44.847 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e4ad376-ef3c-37ca-9835-1d26e4ed72a0 | -12.43758 | -44.86563 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce266de0-b5ff-3ac9-ba48-982735ad76d1 | -10.47367 | -46.93551 | 2025-08-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76f69716-0220-370e-ad98-11931d121b4b | -12.65859 | -44.50769 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdd7b381-f85e-3225-96de-867acd38f97a | -7.9617 | -45.11891 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 558e5326-b0ff-3dfb-b426-b685c6394e41 | -13.22996 | -47.24356 | 2025-08-03 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b41d51a3-9576-3814-89e9-31a1a65e2427 | -9.39289 | -45.50046 | 2025-08-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fae71ee1-c820-3574-b6f8-87431bbe07e4 | -12.26113 | -47.00208 | 2025-08-03 04:27:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 490064c0-c29a-3e34-8ffa-1a296c99a69e | -12.453 | -44.85372 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 773ebc46-2429-38c5-b989-08e3194dd1c9 | -10.36232 | -45.18251 | 2025-08-03 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 182876cb-4428-3b19-a2ce-835acefa0674 | -12.03728 | -44.0165 | 2025-08-03 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c5329a7-9a29-3b98-b2f0-0d041604645b | -10.74664 | -48.18589 | 2025-08-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 93a83314-c4a1-37da-af8e-f3b5281f2603 | -8.74814 | -46.40097 | 2025-08-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7278ce5e-a7b4-31a2-9b54-d34143a0e04f | -12.65982 | -44.49906 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c8cdee7d-1ec0-363f-aaec-d100183383dd | -12.43274 | -47.0369 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a281a4db-bd97-369f-9214-53d0b344cf74 | -7.97125 | -45.10162 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 963ba680-93dc-3d00-8e02-760a8a526420 | -9.35661 | -50.73788 | 2025-08-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80d883b8-b4e2-393f-8b95-bc2e67365cbd | -14.37587 | -50.32589 | 2025-08-03 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cc796b4c-7da7-385a-8935-fa88d28caa4c | -13.07207 | -47.43 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1dbae87-fe6a-33f4-935a-9f1d2bb606a2 | -15.65866 | -43.58214 | 2025-08-03 04:27:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e9e16ca-636c-3fe8-8d70-47d6a3782ef7 | -13.07097 | -47.43708 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba4b6f48-00eb-38e7-979f-cdfc9493d190 | -10.36056 | -45.17058 | 2025-08-03 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de7b7759-1aab-3236-a882-21b986c97713 | -11.93716 | -44.94857 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a23b067-0d13-3f93-a455-eb6575b273d7 | -12.44411 | -44.86494 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f25d705-d9c0-33cf-b3f3-fbdc9027220b | -12.42007 | -44.7101 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d6a939b-352d-3a37-9b69-cab984d15fe7 | -12.4423 | -44.85202 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e2e7d46-3cdb-3fd7-9374-c657308ffa71 | -10.4787 | -46.96862 | 2025-08-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9acafc60-dd3a-33da-afe1-582da2ded802 | -13.37735 | -41.3424 | 2025-08-03 04:27:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 96d6f888-067a-300f-bc1e-85abce150be4 | -8.36934 | -46.54071 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2f05cf6-9ba4-3242-a9ac-50bb98f96e51 | -12.66827 | -44.51794 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 186eb463-e733-3fdc-8874-35a829b14126 | -8.37614 | -46.93343 | 2025-08-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 402cf8ef-0805-3590-8dfe-de1a3fa22441 | -11.94359 | -44.95403 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fab29410-af42-3905-997b-d648b35f0579 | -13.03176 | -47.4055 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbf0918d-f677-315f-a950-2b0a5b8c63a9 | -13.08082 | -47.39532 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebcabfc8-e9d0-3944-a390-fa5f15c02876 | -12.63434 | -44.49522 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4e89cedd-b0eb-3781-a67a-470f03360708 | -12.26446 | -47.00261 | 2025-08-03 04:27:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be746cab-ecf2-3f1a-8ef6-01a676dfa198 | -9.81517 | -53.28947 | 2025-08-03 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 372ce583-12b6-3345-a444-99492f28c1c2 | -8.27701 | -47.32707 | 2025-08-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06f55886-811b-3978-99c7-027975d1de11 | -12.65914 | -44.52974 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bb5ecb4f-1fde-3d3c-ab8e-d7bc024f34ca | -10.47426 | -46.95356 | 2025-08-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f0166ee-b325-3142-b66d-5a453d0fa3d1 | -13.61395 | -47.72847 | 2025-08-03 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3e72e1de-2384-3fed-bf7d-b48beb653887 | -10.35887 | -45.18199 | 2025-08-03 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca18d98d-200c-3506-b20a-77bd97d0d6a2 | -11.70835 | -47.49969 | 2025-08-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bea22d3-5188-3c98-9583-be8d5813ed5b | -8.43936 | -45.59916 | 2025-08-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcfe6543-6bef-3416-b639-775a72ffd65c | -13.07815 | -47.43463 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ec88a0c-b265-3ef4-9284-4752a2865eec | -13.6778 | -41.37008 | 2025-08-03 04:27:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3f82c738-8bce-3940-b541-6355f5792457 | -7.75843 | -45.11788 | 2025-08-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d1f12930-3bb3-3fbf-a648-f7e4221cc15b | -10.47312 | -46.93902 | 2025-08-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80490da7-565e-3249-809c-76a9e0048049 | -7.78574 | -45.21158 | 2025-08-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c980da4b-4bcf-3b9e-bfe3-95ce2f71bb1f | -12.68205 | -48.10094 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26535bac-cdeb-3e68-8102-350bda1b7c72 | -12.64583 | -44.51894 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ba553df-01b6-3722-b1e7-bff7c4bdd829 | -12.43662 | -47.03387 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be88949b-a2e4-3d07-b00b-914df90d3d75 | -7.75898 | -45.11423 | 2025-08-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b043f4bf-86dc-3df9-92d9-1897d11a2c93 | -12.61553 | -44.49676 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93079707-4b5b-3edf-b2cb-915625fab82b | -7.88322 | -45.53201 | 2025-08-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59055de5-38d1-3c45-bd2e-4fa21eb42096 | -12.45783 | -47.02617 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 70fd20aa-8d4f-3ee2-a391-fd98053562e0 | -12.43879 | -44.85743 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4eb2d0f5-4dd7-36fb-ad73-4cd31434ad2c | -12.49531 | -47.18147 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d15de6af-6bca-3c4d-9f03-3605f152ebdc | -13.03875 | -49.17315 | 2025-08-03 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0207faac-28c8-3ef6-a705-d932fe8b2979 | -13.68464 | -41.36966 | 2025-08-03 04:27:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 83e609a7-17f5-3a2f-ba75-26949d32b708 | -12.61493 | -44.50106 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98bbef4c-0f2e-3ea0-99a1-08c5c5dfc697 | -7.7863 | -45.20794 | 2025-08-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67857282-3176-3092-9a83-d7d913d3a956 | -12.41451 | -47.06681 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f4b365e-701e-3022-a230-4aa4717f2140 | -10.36345 | -45.17492 | 2025-08-03 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d90f52c1-6604-316a-ab36-6e173f7ec1df | -6.64606 | -59.10978 | 2025-08-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 0d109d6c-eb82-3f9e-bd0c-4594a21127fb | -12.43522 | -44.85688 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f870e43c-e99e-39ae-af52-31021c52697a | -11.94195 | -44.91569 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README16.md)
