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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e116b6ce-dc71-332c-b733-127f692d6d60 | -9.4432 | -60.5692 | 2025-08-30 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f2b537a6-db34-363a-84f8-b4835eb0de6e | -6.185 | -43.3491 | 2025-08-30 06:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 3d573ccb-3b52-3442-b8e2-ab878c210a2b | -13.3632 | -46.9727 | 2025-08-30 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 35faa68d-d45e-3f26-98a4-b8902d32d7c0 | -13.3825 | -46.9697 | 2025-08-30 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 128.7 |
| fc54f198-3d52-360b-9958-9f15b9862a0a | -12.0153 | -43.9818 | 2025-08-30 06:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 4633bb89-a0be-3105-89f4-4992df0f5284 | -11.8952 | -46.398 | 2025-08-30 06:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 286.1 |
| 948fdc3a-bbd9-3e9e-8fab-632499a353e0 | -15.7676 | -49.9555 | 2025-08-30 06:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 132.9 |
| cd2c1124-9339-3e23-8102-fe7d4ffc7951 | -6.7816 | -43.7632 | 2025-08-30 06:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| fd0492af-f21c-3026-a592-96a421ae5792 | -11.8948 | -46.4207 | 2025-08-30 06:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| aee2a275-d072-332d-8e6f-757a00ebc9e8 | -15.7475 | -49.9806 | 2025-08-30 06:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 116.4 |
| b989a218-06b0-32e3-bb40-c90607b3754c | -9.4498 | -62.3294 | 2025-08-30 06:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 299.2 |
| f29c121e-7a0f-3bdf-af5d-a0ef41fcdfba | -6.1853 | -43.3257 | 2025-08-30 06:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| a104d2e4-c2dd-3ed5-9a8d-8bb7dc5df245 | -11.8956 | -46.3753 | 2025-08-30 06:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 4782acfb-2e4c-3112-a9f7-ec63b62c7f2d | -9.0614 | -65.4355 | 2025-08-30 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 2eec42b5-7ef4-3da9-b930-b51258931b78 | -15.7671 | -49.9775 | 2025-08-30 06:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 189.1 |
| da498574-367b-3e60-8b90-f8512841331e | -11.8764 | -46.378 | 2025-08-30 06:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 3b17a74c-d2aa-3e52-a16f-8d128e5066f9 | -6.7626 | -43.7881 | 2025-08-30 06:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b729958e-73c0-3264-ad3b-96eee2589211 | -13.3628 | -46.9953 | 2025-08-30 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 172.2 |
| de257322-9668-3dd1-8781-2e17896c4ef7 | -11.876 | -46.4007 | 2025-08-30 06:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 1c870fc3-4211-389b-9a24-d33e53fc5994 | -9.4499 | -62.3104 | 2025-08-30 06:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 7c556205-e87a-37ab-b332-a090121a0c09 | -6.7814 | -43.7865 | 2025-08-30 06:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 689ba6a2-04b0-3afa-b431-a4551b7739b2 | -13.5373 | -46.9456 | 2025-08-30 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 7d924dd7-e828-3c0f-b2fa-030e35785a33 | -13.3817 | -47.015 | 2025-08-30 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| f07d0e2f-2444-392a-80a4-3cb063bab7bc | -9.4683 | -62.3476 | 2025-08-30 06:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 65de5e92-2a2a-336a-a8c3-7992051640e6 | -9.4684 | -62.3286 | 2025-08-30 06:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 195.3 |
| 59a2964e-7aaf-3efb-ae08-067141adba67 | -6.8002 | -43.7848 | 2025-08-30 06:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| b3e1554d-3e30-3972-ad76-2de0d74806ae | -13.3623 | -47.018 | 2025-08-30 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 142.6 |
| c529c073-9c41-3c70-a41a-2dba906d2a67 | -13.3821 | -46.9924 | 2025-08-30 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| a67e4b65-ce76-38e3-b305-fa3b1ba61a30 | -9.4433 | -60.5499 | 2025-08-30 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 3b703706-7972-3237-b163-3545a499afd2 | -9.4497 | -62.3485 | 2025-08-30 06:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 166.4 |
| f79360a4-1c6e-3173-af15-18856e9eb087 | -15.748 | -49.9586 | 2025-08-30 06:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 3546cf9a-f83d-3396-bc83-44330cb6677a | -9.4498 | -62.3294 | 2025-08-30 06:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 268.4 |
| cbd534f5-7e23-37ad-9d70-cb34d88d44b8 | -13.3821 | -46.9924 | 2025-08-30 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 70d6e6e6-8322-3b79-9c95-5045e6add897 | -13.3456 | -46.885 | 2025-08-30 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 160.6 |
| de42fe67-a6e0-31ee-a13f-8ba11c06f94c | -11.8764 | -46.378 | 2025-08-30 06:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 29d77163-ba8c-30bc-ab6a-7e38c32b7938 | -9.0614 | -65.4355 | 2025-08-30 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 16595452-fbfc-3539-948a-8dfde59ae4fc | -9.1155 | -65.7699 | 2025-08-30 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 69cb23d4-7e01-37de-b062-750e85932877 | -13.3817 | -47.015 | 2025-08-30 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 9642cd37-5e91-3761-84f6-0934daf86057 | -13.3628 | -46.9953 | 2025-08-30 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 310.9 |
| 29d5a8c6-6af6-32a0-a30a-d4dd723ada66 | -13.3825 | -46.9697 | 2025-08-30 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| ec89b54b-e7b4-34be-b634-f23907dac905 | -13.3452 | -46.9077 | 2025-08-30 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 155.0 |
| be4f7974-0c32-35f2-bdd2-3929e0200e2b | -9.4683 | -62.3476 | 2025-08-30 06:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 134.7 |
| d38a2c45-5b7d-3d03-999d-9c20ad7e1bd4 | -13.3843 | -46.879 | 2025-08-30 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 5936343c-d242-38e7-82ad-189bae238d11 | -13.3645 | -46.9047 | 2025-08-30 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 4778564a-3393-3894-a40f-89ec9f17f24d | -11.876 | -46.4007 | 2025-08-30 06:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 66d24ebf-1db3-3101-9eda-ac4efa51a8d5 | -9.4433 | -60.5499 | 2025-08-30 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| e9f66259-3634-38eb-9d26-560aeec3c8a5 | -13.3623 | -47.018 | 2025-08-30 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 2f022391-a3c4-36a8-a0c0-4722dafa6969 | -6.1665 | -43.3273 | 2025-08-30 06:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 28b1adca-f092-31fd-a411-8420ca114828 | -11.8956 | -46.3753 | 2025-08-30 06:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f47e8a75-c366-3605-94be-74e0f6ae6c0e | -6.1853 | -43.3257 | 2025-08-30 06:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| caf343db-ec56-3516-a6aa-3bd10445476d | -12.0153 | -43.9818 | 2025-08-30 06:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6739987b-1a4c-376a-bb32-1e47f5e9aa27 | -11.8952 | -46.398 | 2025-08-30 06:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| e6cf4df4-9183-3bd4-9ef4-d48609e53839 | -13.3632 | -46.9727 | 2025-08-30 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 30b51e14-946b-3914-b463-90fe833d8a86 | -9.4432 | -60.5692 | 2025-08-30 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 4c1d7692-bdf3-3eac-b118-d58f37b13ae7 | -13.3649 | -46.882 | 2025-08-30 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 354.3 |
| 83a7ac6b-a5f1-3c1c-8ba0-513f04aed797 | -9.4684 | -62.3286 | 2025-08-30 06:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 238.8 |
| 533a92c7-ed72-36d2-a6d5-ea5c9e5bd266 | -9.4497 | -62.3485 | 2025-08-30 06:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 173.9 |
| 1f4d0ef2-2098-371d-8e37-483f9da52f96 | -9.4683 | -62.3476 | 2025-08-30 06:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 104.6 |
| cfdf7cf1-d2b3-371a-9040-7d0bd193bf7a | -11.876 | -46.4007 | 2025-08-30 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| efb151a4-9db5-32c2-a77c-464e40f47b46 | -11.8572 | -46.3807 | 2025-08-30 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 693ecab5-8d17-3a54-8d83-ffcc1bfe2d00 | -11.8369 | -46.4514 | 2025-08-30 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 7c8c794a-4a64-359a-a901-86ed71e9d92a | -6.1853 | -43.3257 | 2025-08-30 06:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| bdad009c-d704-3664-82f8-d75d5063bb69 | -13.3452 | -46.9077 | 2025-08-30 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.4 |
| b2eef611-f696-3ac3-b9f7-232f17cfca64 | -11.8752 | -46.446 | 2025-08-30 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1e2a5476-8334-3710-907f-68422b7a8139 | -11.8556 | -46.4714 | 2025-08-30 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 36d13a3b-11ef-3c85-a381-73b2868d4b70 | -9.4497 | -62.3485 | 2025-08-30 06:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 9aaef7d0-b917-32aa-abbb-6a6d756da611 | -11.8365 | -46.4741 | 2025-08-30 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 169.4 |
| da27774d-423a-3774-9bab-63182668d7f6 | -13.3632 | -46.9727 | 2025-08-30 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 147.8 |
| e6fe9700-6ea7-3c24-a590-d68036097b46 | -13.3645 | -46.9047 | 2025-08-30 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 28ef395b-1085-36ba-a587-afca9a4fc14f | -9.1155 | -65.7699 | 2025-08-30 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 4df92f67-1bf7-3fd2-80ae-dd474ad28286 | -9.4684 | -62.3286 | 2025-08-30 06:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 266.4 |
| 99ba31b4-cf67-3337-9e19-331696308d3a | -13.3843 | -46.879 | 2025-08-30 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 403f7c3a-bb3d-3709-a67d-42f731a51d9e | -6.1665 | -43.3273 | 2025-08-30 06:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| d517c349-1624-36f8-9a73-e7c3ca8a0af5 | -13.3817 | -47.015 | 2025-08-30 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| fa6d1245-db21-3918-8f34-05e6057bcbbb | -11.8952 | -46.398 | 2025-08-30 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 7d0b29be-c44f-3bb7-8b17-5d88ed2d7f05 | -13.3825 | -46.9697 | 2025-08-30 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 9fd739f6-1158-3f50-8fae-3cdd7f3399d7 | -13.3821 | -46.9924 | 2025-08-30 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 5b229275-e97b-374b-98d5-1050040b1c9f | -9.4498 | -62.3294 | 2025-08-30 06:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 281.9 |
| 0c7c7aab-0966-308b-a450-39b241a8eccc | -13.3649 | -46.882 | 2025-08-30 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 243.6 |
| e74683ed-c39e-3fbc-8b76-ee9e63385c25 | -11.856 | -46.4487 | 2025-08-30 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 169.5 |
| df98f92e-319c-3a9d-a8ef-92c5427b781a | -11.8764 | -46.378 | 2025-08-30 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 5bf9aeb7-35eb-327b-9cc6-e6ad2d43c1f9 | -13.3623 | -47.018 | 2025-08-30 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 9fb1c00b-4f29-307a-a611-82c822ddbc57 | -9.4433 | -60.5499 | 2025-08-30 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| e24a8a6f-c5af-3242-bdb9-596c30085e48 | -9.4432 | -60.5692 | 2025-08-30 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 465d43d9-7950-3cbd-a06d-1d08c20ada5f | -9.4312 | -62.3303 | 2025-08-30 06:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 4aaf904c-990c-3802-a289-ae00da6adc41 | -13.3456 | -46.885 | 2025-08-30 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 116.2 |
| c180f7ed-c2fb-386b-a55a-2b99de9fa557 | -13.3628 | -46.9953 | 2025-08-30 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 262.5 |
| 7338ca07-c7cd-336c-9f74-3e67a745b6c8 | -6.5661 | -69.9608 | 2025-08-30 06:50:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce91afea-d231-32c2-b030-706b04c5dcf3 | -6.56696 | -69.9546 | 2025-08-30 06:50:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5bd3846-d807-3438-b567-20b6a899b8a5 | -8.66519 | -70.04601 | 2025-08-30 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68a59692-0d4b-3e3b-8cb5-397491f7a190 | -8.85217 | -70.6244 | 2025-08-30 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 429b6f68-087f-3eda-928d-fb2983c6f6d9 | -8.85142 | -70.63034 | 2025-08-30 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6d6ed72b-7c7d-39d4-8ca0-7d66c85551b1 | -8.65829 | -70.045 | 2025-08-30 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2498750-84af-303d-b91f-73e2c02a8cd0 | -8.75585 | -71.06954 | 2025-08-30 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7aa97c00-0a26-390c-ad87-d55c52a3511c | -8.76236 | -71.07044 | 2025-08-30 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6001cbab-7163-360e-b862-955f4e92b849 | -8.04115 | -70.09601 | 2025-08-30 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59d21aec-538c-3751-b7fc-747d0aeb9aaf | -8.04036 | -70.10223 | 2025-08-30 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bca97dd-8931-3191-903d-fcbb9dac360d | -9.4312 | -62.3303 | 2025-08-30 07:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| b6499a6d-ec5d-3493-b135-98c7d4df3320 | -11.8752 | -46.446 | 2025-08-30 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 934f6c73-1c41-3bbe-8247-2857f825e40d | -11.856 | -46.4487 | 2025-08-30 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |


[Clique aqui para ver as próximas entradas](README89.md)
