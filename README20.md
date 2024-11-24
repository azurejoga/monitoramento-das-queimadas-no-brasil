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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c28860b-2531-3cfc-a02f-1635d789d1da | -4.0848 | -50.36 | 2024-11-24 00:50:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 94359f70-9487-3f7f-ac46-6d3c3a5e3e33 | -3.8304 | -46.0057 | 2024-11-24 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d604a983-10cb-30a1-955e-5431034c7cb5 | -2.4455 | -49.1029 | 2024-11-24 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 7b53cc34-74f9-3df5-bab6-5e52d20c571a | -2.923 | -45.3487 | 2024-11-24 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 74e28e83-7790-3f25-81e6-5248f99cbf47 | -2.7149 | -46.2713 | 2024-11-24 00:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4d4d4b90-474c-3e3d-8d25-767a2ee778c1 | -0.8907 | -52.7481 | 2024-11-24 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 50f52e6e-2c9d-31b5-861a-ad30f66d11f2 | -3.0582 | -53.2192 | 2024-11-24 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7e653003-ee57-3de0-9d6e-33193b3754d8 | -2.8606 | -51.8143 | 2024-11-24 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| a64db03c-cd4e-3008-ae62-043a4f2584b6 | -2.4456 | -49.0816 | 2024-11-24 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| fd992eaa-63f0-326c-b61d-117d24a10f4b | -5.0998 | -43.151 | 2024-11-24 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| b1854445-fe42-374b-9c80-64de0bbd9456 | -2.9229 | -45.3712 | 2024-11-24 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 188.7 |
| 563da7e6-cb44-327f-8945-ee05d1a88ee5 | -1.8239 | -46.6265 | 2024-11-24 00:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 204.5 |
| a134e551-919f-34ed-a2d3-9b922cad4e07 | -0.8723 | -52.7686 | 2024-11-24 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 2ba4fe4d-a4ff-38d4-96b5-a6fa2f793e8e | -2.5842 | -51.8829 | 2024-11-24 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 4793e0f8-6cad-3899-9327-1fe47446da67 | -1.8053 | -46.6269 | 2024-11-24 00:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 48e6f305-75c2-3b8a-a12e-6885fb2061e7 | -4.242 | -48.6978 | 2024-11-24 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 1a82a2c8-48a4-33d1-b8f7-a4166193e952 | -4.2421 | -48.6763 | 2024-11-24 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| c20993f6-6311-3f65-8275-6538d58fa9e9 | -1.3666 | -53.8362 | 2024-11-24 00:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 5c6f61a9-e2f5-39cd-bd14-2f9cd2054fb1 | -1.8053 | -46.649 | 2024-11-24 00:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0398cb1e-d4b6-3dc8-8822-23fa235d875d | -1.8238 | -46.6486 | 2024-11-24 00:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 155.4 |
| 44c970ef-e814-3f91-9f1b-16135d12e7c7 | -5.9556 | -48.0642 | 2024-11-24 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 0adfbb36-049f-3151-9441-91838331889c | -1.8053 | -46.649 | 2024-11-24 01:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 87d913d8-9bf4-3b37-be51-cd62a44ed106 | -2.7596 | -49.1157 | 2024-11-24 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 6935d83c-2840-31ae-a8f2-d5d7f8cd72a6 | -4.2419 | -48.7193 | 2024-11-24 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 716019f1-d235-3936-9c1f-118c0fe2c5ac | -3.0582 | -53.2192 | 2024-11-24 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| e66391dc-a335-3a1c-8beb-381c96bb5c28 | -3.5159 | -53.8132 | 2024-11-24 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 8ed51b07-ce45-3208-9a2c-1fb925b34f72 | -3.1068 | -45.7903 | 2024-11-24 01:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 89.7 |
| a031835f-0409-32ba-95a4-8a25dfd2f806 | -1.5129 | -54.1959 | 2024-11-24 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4430905a-282d-38c2-a582-bc3f5ff13b4a | -4.0848 | -50.36 | 2024-11-24 01:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| ed3e4627-5ee3-3095-b377-6b9553f5268b | -3.8304 | -46.0057 | 2024-11-24 01:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 6264241f-231c-302d-8010-1a590d40731d | -2.4456 | -49.0816 | 2024-11-24 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 3167a252-a775-345c-94c4-50b696d0387c | -5.0078 | -42.9466 | 2024-11-24 01:00:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| dd0bd495-b690-3e45-ba17-6fef1c1a1f64 | -5.9557 | -48.0425 | 2024-11-24 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 209fdf7e-f385-3256-a1e7-3669d52fc17d | -4.242 | -48.6978 | 2024-11-24 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 62d2851f-aa6b-315f-b515-ff518480d2c2 | -3.1069 | -45.768 | 2024-11-24 01:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 72affaae-b147-3b34-8a8f-43643f9883e4 | -1.8239 | -46.6265 | 2024-11-24 01:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 9c2bdd51-898c-39ba-8680-c45c374d39d0 | -4.9891 | -42.9479 | 2024-11-24 01:00:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 045954aa-ac77-3715-8c74-dd2d3db9cc1e | -3.2929 | -45.7161 | 2024-11-24 01:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 4298bfee-ff0e-31ab-a30d-46422a9c4b41 | -3.2386 | -54.223 | 2024-11-24 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 40a2ec38-ea6a-32b6-8ba9-9faa700af1cd | -1.5129 | -54.1759 | 2024-11-24 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 861d9865-78cc-3c7f-8407-a261b2a3ed9a | -2.923 | -45.3487 | 2024-11-24 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 5308764b-9368-3892-9fff-2b4f3d54677e | -2.464 | -49.0811 | 2024-11-24 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 563e7669-c7e0-309a-b970-c37386f774b4 | -2.9229 | -45.3712 | 2024-11-24 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 0283ddbc-b3be-3c08-a098-86567e719b8b | -1.3666 | -53.8362 | 2024-11-24 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 65645d86-8c86-3178-805b-cff5eb65e9cd | -2.7149 | -46.2713 | 2024-11-24 01:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 22f1af26-7fd5-321a-8d88-65fcae43055d | -3.242 | -53.2751 | 2024-11-24 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c164360f-f9b7-3b95-9fa9-357081b244d2 | -2.5842 | -51.8829 | 2024-11-24 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 87c6dbaf-f0a6-33df-95b5-9702e4b59234 | -4.2605 | -48.697 | 2024-11-24 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 6fac2d80-1c0e-3495-bf0f-7f36e5b12361 | -1.8238 | -46.6486 | 2024-11-24 01:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 7c385d23-f10e-3a14-978d-46a658b46c94 | -2.7411 | -49.1162 | 2024-11-24 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 6905cb04-21ca-3ea8-a442-c6005bca09fd | -4.2234 | -48.6986 | 2024-11-24 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 33dfc4b8-3fb9-3692-8cbf-a70cedf27c0e | -0.8723 | -52.7686 | 2024-11-24 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 1bd53c60-5228-323c-abd2-58bdacaf65c6 | -4.1033 | -50.3592 | 2024-11-24 01:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 44f5c691-4030-3fd4-9ec6-ce31fc29cbdf | -5.0998 | -43.151 | 2024-11-24 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 3c399826-f312-3e6d-b7e3-2169ef7ff149 | -3.849 | -46.0048 | 2024-11-24 01:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 97ea60e0-9328-3d46-8c87-73187502baf8 | -3.8417 | -44.0594 | 2024-11-24 01:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| dd88baf3-b9c7-38a2-b726-4fab1f2338de | -2.9043 | -45.3719 | 2024-11-24 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 0b48e736-75ca-35ee-a9cd-f5b0995bd66f | -3.2928 | -45.7384 | 2024-11-24 01:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 1f9504a7-c32f-31ff-8846-50e09893bc3f | -5.1185 | -43.1497 | 2024-11-24 01:00:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 71b22153-9f97-3161-9e76-a7071ffed47d | -1.8053 | -46.6269 | 2024-11-24 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| e73c8876-0350-3b75-8318-bda19cf9ea7d | -5.9556 | -48.0642 | 2024-11-24 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 0157c545-a0c9-3be5-82b9-1defb7b0f873 | -0.8907 | -52.7685 | 2024-11-24 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| c5d74f77-30c0-35a7-bbd3-5e72894994fe | -3.9562 | -50.1969 | 2024-11-24 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| fd3b4c52-64d0-36dc-b596-75bee83f7fe6 | -4.2421 | -48.6763 | 2024-11-24 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| c6724e6a-d84c-31d8-8240-61e9d0c9c08d | -4.0848 | -50.36 | 2024-11-24 01:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| ce7b3efd-c674-307d-ad10-1506a9bab040 | -1.4732 | -46.0357 | 2024-11-24 01:10:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 95880508-6a76-3955-982a-32313a757bf9 | -1.8239 | -46.6265 | 2024-11-24 01:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 61914bad-6975-3846-804f-11337f17efff | -5.0078 | -42.9466 | 2024-11-24 01:10:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 401dc9b0-15ca-3a3f-8d9e-8b4742cc68cb | -2.7149 | -46.2713 | 2024-11-24 01:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| fc7c4e3e-a1d6-3251-885a-3bb4030d9b14 | -5.9556 | -48.0642 | 2024-11-24 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| bae883c9-e799-3715-9a36-c2015d6b028b | -9.6642 | -36.1177 | 2024-11-24 01:10:00 | GOES-16 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 79.6 |
| 46d9142c-4ae9-34b1-9f32-bbdcde206219 | -3.3114 | -45.7377 | 2024-11-24 01:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7e3c7f9f-af2e-3126-bd68-2ef26e4c5247 | -3.1068 | -45.7903 | 2024-11-24 01:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 6f566653-84be-385b-a028-82eae41cdb4e | -4.2419 | -48.7193 | 2024-11-24 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 72b48c70-c702-3642-b505-18ee0f697e57 | -3.5159 | -53.8132 | 2024-11-24 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| bf387fc3-d592-3b76-bff1-de61467519bd | -2.923 | -45.3487 | 2024-11-24 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 978f6edd-2091-3607-a02b-6168b3a7ce3c | -1.8238 | -46.6486 | 2024-11-24 01:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| f57881fa-1791-304f-b29f-0bd1224a9e9b | -4.242 | -48.6978 | 2024-11-24 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 855243e6-611b-3578-893d-5236bc028a2d | -5.9557 | -48.0425 | 2024-11-24 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| f25140f4-b3f2-3167-8276-39625da44bbd | -3.5343 | -53.8126 | 2024-11-24 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| dd859e2e-f320-33a2-a929-e46548a15490 | -0.8723 | -52.7686 | 2024-11-24 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 329f201b-07fe-36a5-b350-7895d3797555 | -3.2929 | -45.7161 | 2024-11-24 01:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2940f78a-3cbd-38c5-97ce-43ae40dcf571 | -2.8606 | -51.8143 | 2024-11-24 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 73609a07-8b55-3eca-9bf5-855b2227a0bd | -3.1069 | -45.768 | 2024-11-24 01:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ba80ce14-5ca1-33a2-9ecd-1483c9afc412 | -3.8417 | -44.0594 | 2024-11-24 01:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a17abd13-fe6e-3ce9-a349-ff8273254706 | -5.0998 | -43.151 | 2024-11-24 01:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 8ee5093b-aaf9-39ef-8c29-c8e2acdb670a | -1.3666 | -53.8362 | 2024-11-24 01:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| a9968a30-03aa-3512-809a-d1b622703ae0 | -2.9229 | -45.3712 | 2024-11-24 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.4 |
| d1e60b76-508f-3e31-a4c3-c2ebf84d9dfe | -3.5158 | -53.8333 | 2024-11-24 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c2ad9d32-e34e-39dc-b5e5-4ce084a53ed5 | -3.2928 | -45.7384 | 2024-11-24 01:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c592ee62-7c99-3e83-934e-6e4d0baf4202 | -3.0582 | -53.2192 | 2024-11-24 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b5f6934c-2c4f-36ab-b007-a663f4e55239 | -2.4456 | -49.0816 | 2024-11-24 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 090ea946-f132-38ff-b121-af50e9231408 | -0.8907 | -52.7685 | 2024-11-24 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 653efd7f-ba73-3f42-b9d9-ffb56b8de74b | -3.2386 | -54.223 | 2024-11-24 01:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f5990116-b78a-32e6-8832-7f7ba24402b5 | -3.054 | -49.4471 | 2024-11-24 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 041fd046-2118-315b-befb-6bd1f14cc3f5 | -2.4455 | -49.1029 | 2024-11-24 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| f5c1585a-b908-39a9-a145-9bca16f7dce2 | -4.242 | -48.6978 | 2024-11-24 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 5bbf52ed-72f8-38ab-8b46-fd9f25bebb49 | -5.0998 | -43.151 | 2024-11-24 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e78af209-8a7d-3912-bc2c-5bda091be0b0 | -3.5159 | -53.8132 | 2024-11-24 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| b2ffa906-1f0d-3def-9847-af97e7db509d | -5.0078 | -42.9466 | 2024-11-24 01:20:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |


[Clique aqui para ver as próximas entradas](README21.md)
