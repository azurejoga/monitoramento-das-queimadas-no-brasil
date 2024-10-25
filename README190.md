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

## Dados Diários - Página 190

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 082ae92f-e9a1-3c9c-941a-10eb7bcade61 | -19.5461 | -56.7192 | 2024-10-25 17:46:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.7 |
| ecf8264f-360f-39dc-ba09-365759c6905f | -19.5666 | -56.6954 | 2024-10-25 17:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| a9101bd9-711f-3def-9807-fdf012ea67f2 | -19.6253 | -56.7709 | 2024-10-25 17:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.6 |
| f1501e11-8565-3697-b207-e73833975937 | -19.6245 | -56.8129 | 2024-10-25 17:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 129.6 |
| 9655e7a7-6507-38ea-9e9d-f54d53a6f805 | -19.5862 | -56.7136 | 2024-10-25 17:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 131.5 |
| e19cca16-3e34-337e-a6d5-3eb43555d9d8 | -19.5669 | -56.6744 | 2024-10-25 17:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| f06ef468-2403-363b-8a02-67e42f8dc8dc | -19.604 | -56.8367 | 2024-10-25 17:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.0 |
| e343b56e-41a1-3e53-b811-1c1bf052f9a8 | -19.6249 | -56.7919 | 2024-10-25 17:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.0 |
| c5a2e6c4-51a6-300a-b179-19521da4acbf | -19.6643 | -56.8283 | 2024-10-25 17:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| f6228a27-8a64-34ae-a8f5-40fe8353d064 | -1.5878 | -53.3089 | 2024-10-25 17:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 649af0b5-8574-3a88-8c02-c2393ca0b1a8 | -1.8654 | -52.3077 | 2024-10-25 17:55:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0bee0488-4b9e-336d-89cb-b5cc2a43a5a9 | -2.1125 | -49.2809 | 2024-10-25 17:55:17 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 0d6c9e17-3aef-3aa0-9034-bf449492bc4a | -2.1829 | -50.502 | 2024-10-25 17:55:18 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| f16cb5d8-68e8-3556-81f9-701f286427ac | -3.4222 | -54.2783 | 2024-10-25 17:55:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 720e6d20-1573-3bc3-9f8d-f7243524b42f | -5.2663 | -41.2141 | 2024-10-25 17:55:35 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 251337f6-af20-356f-a4ff-75f42f93dcc0 | -5.7014 | -45.0199 | 2024-10-25 17:55:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 193.4 |
| eba9690d-d104-303c-a666-96ada4d9c669 | -6.9593 | -41.3296 | 2024-10-25 17:55:44 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| b77c5995-1874-3c22-b23e-80839b7f8794 | -9.6156 | -47.5962 | 2024-10-25 17:56:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 7b3ee74b-aac9-3592-b623-cf05a6c6eb33 | -10.3016 | -42.3886 | 2024-10-25 17:56:03 | GOES-16 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 5daef603-4aec-3623-86a7-0c3145481c72 | -10.2825 | -42.3914 | 2024-10-25 17:56:03 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 56150185-9f5b-3462-81ec-06f4d9210c10 | -10.3545 | -47.5135 | 2024-10-25 17:56:04 | GOES-16 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 97503a15-dd03-3a6b-a5a3-c17b05aa9f8c | -17.7831 | -57.5914 | 2024-10-25 17:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 163.9 |
| c50a77f3-1525-39b7-aeed-c7ee5b386496 | -19.5666 | -56.6954 | 2024-10-25 17:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.6 |
| aeda154a-8cdc-37d5-b22c-d9c460c33abb | -19.645 | -56.7891 | 2024-10-25 17:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 117.6 |
| 721bea60-f0dd-3b2a-a91f-8e33ce175746 | -19.6453 | -56.7681 | 2024-10-25 17:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 128.4 |
| 0df129fe-d700-3b45-9e5f-4dd3db0dfbfe | -19.6245 | -56.8129 | 2024-10-25 17:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 251034c7-b22d-3a19-a663-bab9be071259 | -19.6044 | -56.8157 | 2024-10-25 17:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 97.4 |
| b189b890-9b31-3dd5-8670-e4f5d1ad3e0f | -19.5862 | -56.7136 | 2024-10-25 17:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 125.9 |
| 5d0a8699-634e-3bec-8820-66b5d87f9213 | -19.5669 | -56.6744 | 2024-10-25 17:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |
| e9dc7a4a-6d4d-3e7f-93a8-544efaea3da3 | -19.604 | -56.8367 | 2024-10-25 17:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 7ae9a1d3-65ab-3dff-857a-c78627f04f4c | -1.0368 | -53.5171 | 2024-10-25 18:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 178.1 |
| a732cf2d-fd31-3e0e-9c32-82010f0a4433 | -1.0733 | -53.658 | 2024-10-25 18:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 94be739c-c3b8-31b9-bc47-d8ec9b038cfb | -1.3637 | -55.8472 | 2024-10-25 18:05:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| cb4ebf47-7eaa-38ff-8f6b-84cbbbf3f724 | -2.0403 | -48.6853 | 2024-10-25 18:05:17 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| c9841c58-d465-3066-900e-513805179d14 | -2.1829 | -50.502 | 2024-10-25 18:05:18 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 70c8276d-93a0-32ca-a7ec-3801d0a368fb | -4.1085 | -43.189 | 2024-10-25 18:05:28 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 9f2bbeb2-fadb-3d39-80f0-497ab4dcc5ac | -5.3553 | -46.2344 | 2024-10-25 18:05:35 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| c3d28a1e-c1a6-32e8-95af-a2051f6040fb | -5.8164 | -42.6516 | 2024-10-25 18:05:38 | GOES-16 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 5e7eaad3-2377-3aaf-9348-dac863cd3fc3 | -5.9394 | -47.7607 | 2024-10-25 18:05:39 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 507fe13a-a10c-3d50-ab98-afc0767ed4fe | -6.3287 | -58.298 | 2024-10-25 18:05:41 | GOES-16 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c31609b7-3bba-3f83-98e0-9f179b5a57dd | -6.7107 | -47.07 | 2024-10-25 18:05:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| b24208f1-332d-31b4-8197-5ff30602600b | -6.5219 | -60.0457 | 2024-10-25 18:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 998b4c56-58c8-3268-9efc-295985750e54 | -6.7045 | -43.9554 | 2024-10-25 18:05:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 206.3 |
| 353b2725-0021-3bac-ab9f-62024aacde0f | -6.8452 | -39.795 | 2024-10-25 18:05:43 | GOES-16 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 2a0037c7-f628-304f-bc9f-231433a913b7 | -6.9593 | -41.3296 | 2024-10-25 18:05:44 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 0a79808a-0f8b-30d4-8038-77c2c7bdc3d0 | -6.8927 | -38.987 | 2024-10-25 18:05:44 | GOES-16 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 102.4 |
| c22c9658-424d-3f79-be2d-d92690a4e10e | -7.0105 | -45.1889 | 2024-10-25 18:05:45 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| d49ea3d8-c8e2-3259-8601-11027a746514 | -7.0695 | -46.7319 | 2024-10-25 18:05:45 | GOES-16 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 0a479f37-7ea4-3dff-adb3-0b9d0207b724 | -7.0833 | -47.2171 | 2024-10-25 18:05:45 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 69add554-d218-386f-99a7-a535ecc4a6c6 | -7.5477 | -45.8417 | 2024-10-25 18:05:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| d50845d4-c276-38c3-888b-9548be764947 | -7.5289 | -45.8434 | 2024-10-25 18:05:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 0203d786-e7e2-305b-aea6-76fd45cd62d2 | -7.796 | -40.923 | 2024-10-25 18:05:49 | GOES-16 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 22af30ad-003e-3006-9f69-c74cb2aa78de | -7.7771 | -40.9252 | 2024-10-25 18:05:49 | GOES-16 | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| 088b0453-1516-3cf0-b2b1-119de26b355a | -7.9277 | -47.1008 | 2024-10-25 18:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| b93d12e2-67b8-3a11-bea8-f40c971067ce | -9.3537 | -43.3711 | 2024-10-25 18:05:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 6db208c6-51dd-3688-bece-e865a7681913 | -9.6156 | -47.5962 | 2024-10-25 18:06:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| f4292194-eca7-3d9f-86a9-128ecc89fa48 | -10.3012 | -42.4127 | 2024-10-25 18:06:03 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 364dde51-ab19-3d8f-83eb-fe60d60e33b4 | -10.6292 | -43.3416 | 2024-10-25 18:06:05 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 63.0 |
| d9825078-3c04-3dc2-817f-1ee3585b2146 | -10.6249 | -55.9757 | 2024-10-25 18:06:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 8dd528bd-0358-332c-961b-e14df356dbe9 | -10.8997 | -47.847 | 2024-10-25 18:06:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 602e752b-c6d3-3c8a-9ab6-e612ee1d11ed | -11.9028 | -43.8348 | 2024-10-25 18:06:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 2148472c-8d1a-35ff-9e6d-fafea554c677 | -12.3118 | -43.5565 | 2024-10-25 18:06:14 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 7547f64e-ed6f-3d7f-b291-7666bdcfa41e | -17.2966 | -57.2803 | 2024-10-25 18:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.1 |
| 85c32582-f4c1-3d57-b76f-2d6ac43df330 | -17.7831 | -57.5914 | 2024-10-25 18:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 156.3 |
| 8980bd6a-2676-35ad-95eb-393b3ca1aed5 | -19.6024 | -56.9206 | 2024-10-25 18:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 50fe55f1-a53c-389c-8949-27b3a2fed3fa | -1.3637 | -55.8472 | 2024-10-25 18:15:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 7a858c67-c361-3e95-937b-969233267aa9 | -1.5651 | -55.9041 | 2024-10-25 18:15:14 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f98d7801-35cc-3180-8ea8-4caa8e80c308 | -1.4918 | -55.9443 | 2024-10-25 18:15:14 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 230cd5ed-1a24-3ae3-8d90-e57611bdfed7 | -1.7367 | -52.3302 | 2024-10-25 18:15:15 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 346cf9f0-eb13-37cf-993a-76df3a51b7fa | -2.133 | -55.857 | 2024-10-25 18:15:17 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 1d04c0aa-0d03-30db-9aab-9769557c56c1 | -2.3057 | -46.615 | 2024-10-25 18:15:18 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 513e2230-ec52-3c2a-8dde-bccf71c68e5c | -2.1829 | -50.502 | 2024-10-25 18:15:18 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c8489bcb-4e26-3d51-ba2e-10b3498ebdf9 | -2.3516 | -49.5935 | 2024-10-25 18:15:18 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 650de1cc-fad3-3b54-9a06-5a60ec332292 | -2.5117 | -46.0333 | 2024-10-25 18:15:19 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| dcf66a29-f1b3-3400-a6ed-0a4ff3e78b7b | -2.6473 | -49.5225 | 2024-10-25 18:15:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 9b1c36ee-f477-3e3f-9059-d0ce0e796d3b | -3.1116 | -53.7234 | 2024-10-25 18:15:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 225.6 |
| 04679461-9260-37b4-94a5-24247ecd7ae7 | -3.2912 | -46.0731 | 2024-10-25 18:15:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| dc38948f-838f-3371-81bf-e8fca38ed542 | -3.3305 | -54.2005 | 2024-10-25 18:15:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 402b7460-8a20-3ddd-8cb9-5509c4076710 | -3.3041 | -43.5078 | 2024-10-25 18:15:24 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 48f35a99-11b6-3092-b64c-04f008419b3f | -3.8976 | -44.0796 | 2024-10-25 18:15:27 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 02779c64-e158-3bcb-9025-b557aa2f2eba | -3.8144 | -48.9729 | 2024-10-25 18:15:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 25048486-6c42-398c-8667-b2c33375f285 | -4.0896 | -43.2134 | 2024-10-25 18:15:28 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 9c191f07-88d9-35c0-b3c1-0cba2e800833 | -4.1085 | -43.189 | 2024-10-25 18:15:28 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 174682d5-55e0-3a0f-861a-930af6324e7d | -3.9629 | -48.9027 | 2024-10-25 18:15:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 369914f5-eb83-34c7-822a-0781e8e46c1f | -4.2558 | -43.5064 | 2024-10-25 18:15:29 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 1d35fabb-9ca6-3928-a836-a67c23b4938d | -4.2861 | -50.7498 | 2024-10-25 18:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 5033977d-fba8-3669-b9eb-888bf900006e | -4.5912 | -56.0924 | 2024-10-25 18:15:31 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 19b22fa8-2b8e-3ed2-8af7-62e2c2a56576 | -5.0769 | -43.6644 | 2024-10-25 18:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 337.2 |
| 56b3e08a-b72d-3849-910e-bf3d42ef8e67 | -5.3025 | -50.9748 | 2024-10-25 18:15:35 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2d259d49-d778-39a2-9b8d-d0d29835f763 | -5.2663 | -41.2141 | 2024-10-25 18:15:35 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| 71b4bbd7-1c4d-3ba4-a6da-08e9cd4da266 | -5.8164 | -42.6516 | 2024-10-25 18:15:38 | GOES-16 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| eae829bf-6628-381a-b496-98a42190b71f | -6.1944 | -42.4073 | 2024-10-25 18:15:40 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| db6d0064-fad7-316a-88b1-693b5880900c | -6.3287 | -58.298 | 2024-10-25 18:15:41 | GOES-16 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| f628b5c7-731b-3474-a6a6-aa7717b74118 | -6.2744 | -47.8253 | 2024-10-25 18:15:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 8cb1fdaf-cbcc-34fa-af5f-41401d08130c | -6.3286 | -58.3175 | 2024-10-25 18:15:41 | GOES-16 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 103.2 |
| ae2ed87c-b4eb-3193-897d-3644722fd202 | -6.5149 | -48.0479 | 2024-10-25 18:15:42 | GOES-16 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e1590207-f60b-3416-99ae-6d6f2c84fbab | -6.5266 | -62.9483 | 2024-10-25 18:15:43 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 4c314b18-2c21-3a4c-9eea-2f0d734edcfc | -6.7045 | -43.9554 | 2024-10-25 18:15:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 749ac8a4-6489-3db6-950d-1432be830d04 | -6.9655 | -39.2313 | 2024-10-25 18:15:44 | GOES-16 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 6b4140a8-43d4-3e48-aef0-88a268d01f63 | -6.8927 | -38.987 | 2024-10-25 18:15:44 | GOES-16 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 166.0 |


[Clique aqui para ver as próximas entradas](README191.md)
