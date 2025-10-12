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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad84c8bf-38ff-353b-b23e-f3846f980069 | -3.728 | -44.3858 | 2025-10-12 14:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 9790a667-8645-3ed7-9bbc-d71de64ebe3a | -8.2182 | -43.3403 | 2025-10-12 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 365.7 |
| 2322a85d-7e4b-3fc1-b28f-f2ef5b16633a | 1.1688 | -50.9147 | 2025-10-12 14:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 3ffa5676-de25-30d6-b13c-e0168ceec655 | -9.1024 | -45.0477 | 2025-10-12 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 46b16df4-2a39-3dd6-85ff-df8ba8929e03 | -3.7465 | -44.4077 | 2025-10-12 14:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 97b64f68-af8f-3f90-9007-afc7b208fee1 | -18.0777 | -45.0066 | 2025-10-12 14:10:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 3ffbe475-e261-36ca-a9bf-033c8bdf94fc | -9.1028 | -45.0248 | 2025-10-12 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 4d7074ca-76b8-3497-9a50-a675eea07f1d | -3.7466 | -44.3849 | 2025-10-12 14:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| dc51fa2a-f0c4-3a88-8118-94eff6fae94f | -17.6397 | -46.4929 | 2025-10-12 14:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 9ad765d2-ae3f-3f53-9bba-f9fac72ddbbf | 1.1504 | -50.9149 | 2025-10-12 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 600f9403-0f66-3ef6-ba02-21294efd2cdf | -8.8595 | -44.846 | 2025-10-12 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 5ebdf374-f7b8-3678-9aff-b43c1e219f10 | -3.7466 | -44.3849 | 2025-10-12 14:20:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 055e8019-b8d4-3104-a742-ae004d065c71 | -6.2218 | -41.5688 | 2025-10-12 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| f5205292-00ce-393a-9c8d-81dd54f87f4e | -5.566 | -41.3113 | 2025-10-12 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 08233092-141f-3b72-ac59-4969fd334c91 | -4.4094 | -42.9146 | 2025-10-12 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 0da77a56-cb00-34ae-8f75-3da55f2571de | -8.1993 | -43.3424 | 2025-10-12 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 140.9 |
| f3c6a86f-77a2-3fb8-94fb-ab0872dbff9e | -3.9147 | -44.3309 | 2025-10-12 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 7bfece3c-718c-375b-a1de-e65e0fe5e0d8 | -5.4721 | -43.4045 | 2025-10-12 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 4fa60b6f-29f8-34cf-80b3-d2859306b1ed | -8.2185 | -43.3168 | 2025-10-12 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 62d07fc5-44e8-3743-a2ac-e94bc478f22b | 1.1689 | -50.8939 | 2025-10-12 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 4162fbdb-ebb9-3d81-a22d-ffc6349b1ff0 | -3.6006 | -43.841 | 2025-10-12 14:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 8c70eaf0-f9f8-363a-bb0c-de4abdfda252 | -17.8219 | -57.6277 | 2025-10-12 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 28174810-fcf8-310d-9dc0-bbe60ac5ee7a | 1.1688 | -50.9147 | 2025-10-12 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 2089f23f-c036-3218-8e6e-8bc96c864f31 | -5.341 | -43.414 | 2025-10-12 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 162.4 |
| c3af659b-9344-3ae1-9618-db43650f229c | 1.1504 | -50.9149 | 2025-10-12 14:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 78fa5193-990f-31af-bb9e-b65d8d9381b7 | -7.8451 | -44.5171 | 2025-10-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 278.2 |
| 080bc8b0-c7d3-3e8d-a1de-41034d68ef54 | -4.8193 | -43.123 | 2025-10-12 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 8bf9135a-47c1-3430-b7eb-34204b43b7e4 | -7.8457 | -44.4711 | 2025-10-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 75b32883-30c8-3f61-a50a-cb78a0ccd436 | -3.7466 | -44.3849 | 2025-10-12 14:30:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 34618913-ac97-3e0f-9050-f70e011b9444 | 1.1689 | -50.8939 | 2025-10-12 14:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ce6700dd-c047-3f6e-9011-ff9fd2eb5915 | -7.8642 | -44.4922 | 2025-10-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 3a209bbf-0d23-3a9b-9fe5-813d2c2d68bd | -19.012 | -57.5408 | 2025-10-12 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.7 |
| 37c3ea38-e184-30df-b0b2-61ef376168cf | -7.915 | -44.9683 | 2025-10-12 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 2e5bc611-2467-3c02-b0f6-f2c83a77d2cc | -5.8708 | -42.8593 | 2025-10-12 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| f0ff0dcb-0755-3d77-a655-bb362e2eec5d | -17.8219 | -57.6277 | 2025-10-12 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 1dd1b474-5889-3bf1-8ea6-e1a513f00585 | -7.7956 | -42.4179 | 2025-10-12 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 949f8648-93b1-383d-9231-9bef3a902fc0 | -7.8645 | -44.4692 | 2025-10-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 63fca4eb-9dc2-3deb-bdcc-4ef43c0af8ee | -3.6006 | -43.841 | 2025-10-12 14:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 4621cd44-b8bd-3d9a-8e3d-82b7b732706d | -5.4187 | -40.9841 | 2025-10-12 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 139.0 |
| fac27512-6a63-3409-b415-a1015bb8d2b8 | -7.8454 | -44.4941 | 2025-10-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 21eb0b83-c9ce-35f1-bdc2-738a9c25443a | -4.819 | -43.1697 | 2025-10-12 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 1aeafd93-3258-3f1e-aa9c-c2a351ec0f3d | -7.864 | -44.5152 | 2025-10-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 263.7 |
| 6a0d66f1-fa07-373c-a553-2a102550d2b3 | -5.4721 | -43.4045 | 2025-10-12 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 35260aa7-fabb-389c-b8ac-5701ce773a2a | -6.2637 | -42.9913 | 2025-10-12 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 0324c5e2-6637-3372-a597-8e538c6b127c | 1.1504 | -50.9149 | 2025-10-12 14:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 96b980d1-71e8-3898-b99b-0ed159b56e53 | -7.8645 | -44.4692 | 2025-10-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 88e66556-4f0e-3dca-8551-d70b92829907 | -4.4094 | -42.9146 | 2025-10-12 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 840be705-0f4f-3058-9afa-d8eb121c9e4c | -7.8828 | -44.5133 | 2025-10-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 48bc6409-7af6-3bf2-9115-80f8cfac9404 | -3.7465 | -44.4077 | 2025-10-12 14:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| e0ec4d40-2009-34db-bc60-020e04bc18ed | -7.8687 | -44.1227 | 2025-10-12 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| adaa20ba-4c01-30ce-8bff-b347a15977c0 | -4.838 | -43.1218 | 2025-10-12 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| be73cb55-3eee-3a7d-9307-1bebc5395de7 | -17.9602 | -57.611 | 2025-10-12 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.3 |
| 6c7aa279-aeff-3e50-a463-f22befe83829 | -5.4721 | -43.4045 | 2025-10-12 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| de1e5158-5ca2-316e-afcc-502357d2037f | -4.4054 | -43.4746 | 2025-10-12 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 5ea70084-9d39-3f1c-83c3-0b2ce649ec26 | -17.8219 | -57.6277 | 2025-10-12 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 729dae95-c59e-3588-af23-90267e4cb533 | -7.8454 | -44.4941 | 2025-10-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.2 |
| c1dbcf0e-6137-3d67-a9a6-bb3fe79cf8f4 | -7.7924 | -44.1998 | 2025-10-12 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 3df99ba5-eb74-3620-a74e-9fd07cc787ce | -8.4034 | -45.0783 | 2025-10-12 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 154.0 |
| bf29a84c-e395-3c53-862c-e5f938692472 | -6.2634 | -43.0148 | 2025-10-12 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| babcc433-7825-394d-88e9-d0651123299f | -8.2266 | -44.1548 | 2025-10-12 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 2bb3f433-484c-3f1f-8856-22308d85e276 | -7.8642 | -44.4922 | 2025-10-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 34841b7a-ced5-39ad-a635-5fc191d870d5 | -7.8831 | -44.4903 | 2025-10-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.8 |
| a928da46-5565-3c3e-a267-8caa9e8e1a74 | -7.864 | -44.5152 | 2025-10-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 1524159a-0ab9-3646-b5c7-9fdd41cf598a | -3.6006 | -43.841 | 2025-10-12 14:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |


