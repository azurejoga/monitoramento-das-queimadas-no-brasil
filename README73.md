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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4087627-1d6c-37b5-9d47-d2ff5ca6b0bb | -11.4418 | -47.2461 | 2026-08-20 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| f30dde95-7445-3b72-8e2b-6e932a87cf4f | -5.8088 | -55.7095 | 2026-08-20 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 202.9 |
| 762ab5d9-5c4e-3c59-8260-28ce2e34abd9 | -6.583 | -58.9658 | 2026-08-20 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 78b29501-7872-3739-9cf9-b926bfd28eb2 | -7.4444 | -60.0092 | 2026-08-20 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d61b5bad-b8a3-3632-bd64-4f2b206acfa4 | -5.961 | -52.2056 | 2026-08-20 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 941fb349-fea8-3bc9-b4be-894c2079bb2c | -7.7703 | -61.1443 | 2026-08-20 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 7c3114dc-08db-3887-a1a3-deb720b422e5 | -11.3989 | -46.3759 | 2026-08-20 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 256.9 |
| 895d8d7b-95bf-3ac4-889b-930d8070d52f | -9.207 | -59.7903 | 2026-08-20 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| fefe7a76-8a71-3487-86f7-c55be76a778b | -22.7788 | -47.533 | 2026-08-20 14:00:00 | GOES-19 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.4 |
| a96165ef-8e68-3814-9802-85d4c4611017 | -6.6938 | -58.942 | 2026-08-20 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d15e9797-19d6-3cf7-a644-5e2080076b8d | -11.3801 | -46.3558 | 2026-08-20 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 7bf065c3-8d65-3502-85f3-24d2a87dda18 | -7.4615 | -45.1484 | 2026-08-20 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| b5985919-a90a-3d41-bb9d-9d1876fb7188 | -5.9425 | -52.2066 | 2026-08-20 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| b6a0cd25-a8ce-3892-91f2-17c90190df1e | -5.7904 | -55.7103 | 2026-08-20 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| af2e17f1-b51f-383b-84d3-bf0cece3aa89 | -6.4392 | -52.7138 | 2026-08-20 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 359.9 |
| 0abc3b57-45fc-3792-b659-c7975498b564 | -17.4418 | -44.912 | 2026-08-20 14:00:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 478.2 |
| cc8d7ba0-a1f0-3910-8587-2967f16a4486 | -9.4256 | -60.4353 | 2026-08-20 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1a7034e2-faee-3831-b3c9-1d5435a1b177 | -8.4742 | -46.9609 | 2026-08-20 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 18d041da-e5d2-3eb6-ac42-91ca7e21e8f0 | -5.8087 | -55.7293 | 2026-08-20 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 199.3 |
| c72c71a3-8e8c-3bb8-a7a3-29a83cade4de | -11.1939 | -53.9993 | 2026-08-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 291.1 |
| 41ceefba-ea79-37ff-89c2-912fcd7bf26e | -8.3292 | -46.5077 | 2026-08-20 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 40887f16-41b2-318e-828a-36581d3d130c | -15.7151 | -47.8036 | 2026-08-20 14:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 98c24599-12c1-3e85-89a7-d46fb011b205 | -11.1936 | -54.0199 | 2026-08-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 212.3 |
| af33541d-8f14-3ed0-a647-9986ec7d1ad0 | -14.5086 | -52.9943 | 2026-08-20 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 4ba7c25e-f47e-3497-9f43-0ed7f03ff6b8 | -10.4085 | -61.1915 | 2026-08-20 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 4084d46b-4960-3d9b-8585-81119eb137b3 | -5.7903 | -55.7301 | 2026-08-20 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| cb5e0efd-cab8-3050-bafd-e7a252931957 | -11.2128 | -53.9976 | 2026-08-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 173.7 |
| a5e87978-d92a-3f03-aef1-1b2441b21c0b | -11.4227 | -47.2486 | 2026-08-20 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 606f1785-4c5a-31cb-93e0-f1537cce937a | -10.3898 | -61.1925 | 2026-08-20 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 11afbcd6-134f-39aa-99b9-0686fbf60175 | -6.1668 | -45.2576 | 2026-08-20 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 2b66a132-914d-31ea-9c90-99e93e667bc9 | -9.2071 | -59.771 | 2026-08-20 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 8a23baac-36b7-3e2f-b52d-53bd1c277ed4 | -6.6015 | -58.9651 | 2026-08-20 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d690e9f5-a0cb-3261-af36-331a28303faa | -14.1611 | -53.0377 | 2026-08-20 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 858c9d4d-7792-3a2b-8588-b3e8e94a7fea | -14.3347 | -53.0162 | 2026-08-20 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 67f07cd8-d1ec-332e-a186-20e9bd9204d4 | -10.8451 | -50.3081 | 2026-08-20 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 8c43a8de-993e-3d2b-a596-2a60df0e3509 | -6.4389 | -52.7548 | 2026-08-20 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 2c444569-00cc-3be1-9968-0854b595ce90 | -11.8377 | -58.8445 | 2026-08-20 14:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 03fa94b9-96dc-3a0b-8928-2753ec5931e1 | -10.4084 | -61.2108 | 2026-08-20 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 5b0d06da-3aab-311c-a9a2-ad0beb31ee55 | -6.2353 | -55.4118 | 2026-08-20 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 8c67da83-c19b-3671-a420-af2c5935f76b | -11.3797 | -46.3784 | 2026-08-20 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 12fc6ac9-aa01-37e8-8605-2338a6ef2e51 | -14.5275 | -53.013 | 2026-08-20 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 54ad5bcc-3b9a-3a8a-8611-7bb4203ead61 | -7.344 | -55.6741 | 2026-08-20 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 78e5cc24-cb06-369c-99fc-f903865be14e | -6.4391 | -52.7343 | 2026-08-20 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 560.8 |
| 1a383376-92c6-3377-9a79-7cbbeb27f41f | -11.1939 | -53.9993 | 2026-08-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 408.1 |
| ad5fc001-ac32-3fca-aa18-672a1d851f5f | -6.7647 | -59.4601 | 2026-08-20 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 30507ac8-ba31-371c-ad35-1acb1531fcf6 | -5.7904 | -55.7103 | 2026-08-20 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| e6076e0a-7c38-3a3a-99b0-9ae18be7eba7 | -5.8087 | -55.7293 | 2026-08-20 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 275.9 |
| 52dfc528-73ff-3f70-bf26-c6b4a76b0c22 | -19.5213 | -46.6147 | 2026-08-20 14:10:00 | GOES-19 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 91da1540-9b6e-3b3f-a5e6-06ce3b76a13d | -8.3292 | -46.5077 | 2026-08-20 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 6f720391-7b7f-3b1f-8df0-139a6ab1a812 | -5.8088 | -55.7095 | 2026-08-20 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 241.2 |
| de548398-c36b-3120-9f20-1122a2d86cb3 | -9.4256 | -60.4353 | 2026-08-20 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| e633b69a-7ae6-33c0-b64f-0ed197a57021 | -14.3335 | -51.9371 | 2026-08-20 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 65b6042a-ddca-3b4a-97ab-88b738adb55f | -7.4615 | -45.1484 | 2026-08-20 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 243dcf63-91a1-30ab-b92d-c506fcf5a12a | -8.9748 | -50.7232 | 2026-08-20 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 1bbbe5b2-c94a-3d44-bb42-92e6a7fd9a1b | -11.9102 | -50.1663 | 2026-08-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 8dcab5b8-3fc6-3bdb-b9ae-7c5a20bdb507 | -6.8991 | -55.7176 | 2026-08-20 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3ba95e18-5f37-3d11-87db-e5bfdef47828 | -11.1747 | -54.0216 | 2026-08-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| a8d1c7fb-ebeb-3294-8711-44608bb08308 | -6.583 | -58.9658 | 2026-08-20 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 49e21f0c-0571-3a8f-b62c-3ddae39d9971 | -14.3537 | -53.0348 | 2026-08-20 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 70a0b058-06c8-343f-9345-bd76873cc84d | -5.7903 | -55.7301 | 2026-08-20 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| a3ab79fd-6e95-306a-9ee4-4c2fb9e6d7fa | -7.4444 | -60.0092 | 2026-08-20 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 81084295-a624-34c3-8eb5-0415abbe3a11 | -10.4084 | -61.2108 | 2026-08-20 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7744f88a-affc-3699-83ca-0ec1625baa82 | -5.9425 | -52.2066 | 2026-08-20 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| fe740649-26c5-3be5-b92f-8da07601029e | -9.2071 | -59.771 | 2026-08-20 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.7 |
| a277d91d-713e-3c59-b7eb-9f0f9919b3d3 | -7.1366 | -47.4986 | 2026-08-20 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| cd1c9e2d-a239-3206-9334-401c55469c5d | -9.2258 | -59.77 | 2026-08-20 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 07ed374e-edd4-3677-85d1-c24da0071f82 | -14.1611 | -53.0377 | 2026-08-20 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 77b7d537-228c-341d-8ed7-faae2af87d44 | -6.7123 | -58.9412 | 2026-08-20 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a7b17407-b3c6-3f85-adfe-ebb1ced06975 | -6.4389 | -52.7548 | 2026-08-20 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 184.1 |
| 42070ca3-dddc-3325-aab2-025339aefeb5 | -11.3797 | -46.3784 | 2026-08-20 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 18ec4a57-51e0-32cb-9cc2-0c064dce95ce | -10.8451 | -50.3081 | 2026-08-20 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 8a061496-7b43-3531-92cc-081c72abce2a | -7.9673 | -46.9201 | 2026-08-20 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 4375e7a1-2855-346c-ae8a-3b0915a2db2d | -14.3532 | -51.9132 | 2026-08-20 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 143.6 |
| dc0adf8f-3856-3ba2-bc3e-9368afd8fa37 | -7.7703 | -61.1443 | 2026-08-20 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 7e1ff2f1-6ce6-3691-b734-9fb5440d2d77 | -10.3898 | -61.1925 | 2026-08-20 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 07617298-ddee-37e3-954c-e4affcd33158 | -6.6014 | -58.9844 | 2026-08-20 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 3d39d199-093c-356c-9f96-a85d4043a35e | -6.2353 | -55.4118 | 2026-08-20 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 3afb9ed4-cc3e-3ca9-87e4-8fc54a23ecb2 | -22.7796 | -47.509 | 2026-08-20 14:10:00 | GOES-19 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.5 |
| 15339f07-d396-312d-947c-513d68ef0565 | -11.4227 | -47.2486 | 2026-08-20 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 45647725-72ec-3f09-a1f5-25d9a834125b | -6.4576 | -52.7332 | 2026-08-20 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| d80e99ff-915b-3eb3-8ca1-d50bd7be9e22 | -7.022 | -45.8878 | 2026-08-20 14:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| b0041722-2d5f-3c5f-98c9-6c26f69ec647 | -11.2128 | -53.9976 | 2026-08-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 0b387955-72c2-30a7-88ac-752d86b7ed5e | -15.7151 | -47.8036 | 2026-08-20 14:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 87.2 |
| ee2e6e3f-a184-3b6f-a98e-f3811656c50c | -11.9099 | -50.1878 | 2026-08-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| dfc4844d-e884-303f-836e-45e786c93c6c | -11.2125 | -54.0181 | 2026-08-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 42f56c36-bfcf-3e2d-9e7e-4792a09a7a7d | -6.6745 | -59.0973 | 2026-08-20 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 0cd562ca-3160-3846-b671-e6672714ab5d | -11.1936 | -54.0199 | 2026-08-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 318.2 |
| 981c0c4d-1c28-3b61-a35a-15592968d57b | -11.3801 | -46.3558 | 2026-08-20 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| e3e6268c-e64b-38e0-9368-da7f98848889 | -6.6929 | -59.0966 | 2026-08-20 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| e18bdcef-9ffb-3148-b3c1-e43c6fb16932 | -5.961 | -52.2056 | 2026-08-20 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6c8946fe-83c5-38bb-84a6-d7f2b54e23fd | -8.3104 | -46.5095 | 2026-08-20 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 7a5cb26d-7a0d-3cd0-b6f0-63e3bf69c10e | -8.4742 | -46.9609 | 2026-08-20 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 1ecdee43-73ae-3ebb-83d1-4c48b2982e14 | -6.4392 | -52.7138 | 2026-08-20 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 642.1 |
| 2fca0851-32ca-3ec3-acde-a931dc570ea3 | -11.3989 | -46.3759 | 2026-08-20 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| e915984b-c6f3-3452-8be6-b355e1af220a | -6.6142 | -45.4486 | 2026-08-20 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 4802e2ff-74ec-30a0-a0f2-f9de8869fa8a | -13.6047 | -51.7969 | 2026-08-20 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| bcc0416b-269f-3625-9881-c16fcb4b0c0b | -10.3897 | -61.2118 | 2026-08-20 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 184.8 |
| fbd4927b-3cc6-3375-9cc8-8fa603721e5c | -9.2256 | -59.7894 | 2026-08-20 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 12218306-f907-325e-b068-4eb439f2a2b7 | -6.4391 | -52.7343 | 2026-08-20 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 987.3 |
| 0ffc4376-6061-3368-9976-d97e6c9d0475 | -22.7788 | -47.533 | 2026-08-20 14:10:00 | GOES-19 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 160.9 |


[Clique aqui para ver as próximas entradas](README74.md)
