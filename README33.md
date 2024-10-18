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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 298f1fa9-9ba7-3de0-9eec-2778d6edd273 | -17.0008 | -57.3971 | 2024-10-18 13:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.6 |
| 09c7a052-8276-3f62-9c7d-4407efea3599 | -17.2081 | -56.6946 | 2024-10-18 13:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| 61bb3768-3c30-30bb-8cec-b5d1816c27d0 | -17.1681 | -56.7407 | 2024-10-18 13:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| b44f0a79-97ea-3281-b5b4-31a30d275ea0 | -17.1529 | -56.4745 | 2024-10-18 13:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| fa6b1de2-cd04-3ace-a7e2-14a907d43fe1 | -17.1784 | -57.3148 | 2024-10-18 13:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.8 |
| 024a751b-b76b-3458-9e9a-810dc5414630 | -17.2277 | -56.6922 | 2024-10-18 13:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.6 |
| 9a4d6eb2-f299-3524-b6d6-17b37d7c47c1 | -17.1671 | -56.8026 | 2024-10-18 13:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.2 |
| a1cbae6f-260e-390f-a675-409d8cd2d8f5 | -1.153 | -49.1696 | 2024-10-18 14:05:13 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| dd33087c-8d3d-32bb-9356-8c77111ae13a | -3.0949 | -44.3677 | 2024-10-18 14:05:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 149c8826-6b96-3437-b1eb-5c4c1f27da45 | -6.6886 | -70.1171 | 2024-10-18 14:05:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 84fb413b-932e-3eaa-8a3b-bfb219f46757 | -6.6703 | -70.1174 | 2024-10-18 14:05:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| fdf31c8c-42f0-317a-bfa3-9e59a793b84d | -10.4802 | -68.1686 | 2024-10-18 14:06:06 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 72.9 |
| b2b93845-0453-3d78-9a96-728a7f2c7b92 | -17.02 | -57.4153 | 2024-10-18 14:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.4 |
| 38c385de-2858-377f-b88c-093000690e5f | -17.0008 | -57.3971 | 2024-10-18 14:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.9 |
| 3f79deb6-1b8a-36ad-a1f8-fa0680c709e0 | -16.9802 | -57.4609 | 2024-10-18 14:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| 2bc392ab-25a1-3d9d-91b2-aa3d86835791 | -16.9741 | -56.6202 | 2024-10-18 14:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.9 |
| 28ce0653-f4d3-3060-be72-92a3227badcf | -17.0204 | -57.3948 | 2024-10-18 14:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.2 |
| d2c1dc11-cc1b-314c-b5aa-41f8ec7931bb | -17.2081 | -56.6946 | 2024-10-18 14:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.2 |
| 88e7221a-b25c-375b-9b41-aa477bb36253 | -17.2084 | -56.6739 | 2024-10-18 14:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.9 |
| cbf21f1c-b8a9-31f0-962b-21f50692c929 | -17.1784 | -57.3148 | 2024-10-18 14:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.6 |
| b431eca4-322e-3e92-a239-b04150f9b755 | -17.1681 | -56.7407 | 2024-10-18 14:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 36a52698-c2ad-3abf-b3d6-0301f22df801 | -17.2277 | -56.6922 | 2024-10-18 14:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.9 |
| 5ab16c3a-1296-38a3-bf0a-d8aec68188a2 | -17.1667 | -56.8232 | 2024-10-18 14:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 6b7fc12f-89dd-3c51-b249-e8d9086e0e86 | -17.1671 | -56.8026 | 2024-10-18 14:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.5 |
| 10078949-e6d5-36a2-9a31-10ef7040b0f3 | -17.6481 | -56.246 | 2024-10-18 14:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.4 |
| 5698c8aa-84c6-3ec3-afb0-0c594cf3d4be | -17.8474 | -57.2751 | 2024-10-18 14:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.3 |
| b8b2013b-fcd7-3cfa-8df2-adaca8a10916 | -17.8277 | -57.2776 | 2024-10-18 14:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.4 |
| d7c58125-602d-3d95-9211-ea12bbc7f8a8 | -0.766 | -48.7042 | 2024-10-18 14:15:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 67c80ae5-644d-3d92-8a85-50fcb973b8d6 | -3.0577 | -44.3692 | 2024-10-18 14:15:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 071edb31-580b-3b0a-aa59-e9629b3e2d7f | -6.6703 | -70.1174 | 2024-10-18 14:15:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 39aee571-5ec4-3149-830a-87d9abf7b3dd | -6.6886 | -70.1171 | 2024-10-18 14:15:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| bfca3b0a-96bf-38a6-860b-2162fae8f449 | -16.9805 | -57.4404 | 2024-10-18 14:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.0 |
| 2066c7f0-43dc-3c97-a391-ff0208cb9080 | -17.0599 | -57.3697 | 2024-10-18 14:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.8 |
| 13d209bd-e4c5-334b-8c30-5c9664a966d5 | -17.0795 | -57.3674 | 2024-10-18 14:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.5 |
| 0b714bf1-fe2c-3ff6-942e-f463518603fb | -17.0204 | -57.3948 | 2024-10-18 14:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.2 |
| 4cb62fab-61cd-356a-bc8a-96996d57338e | -17.0403 | -57.372 | 2024-10-18 14:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.3 |
| 39616dc8-d9e7-39fa-b19c-f48e40cce6a4 | -17.02 | -57.4153 | 2024-10-18 14:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.9 |
| 482527b6-8b0e-3f05-8ab5-73d853cd2895 | -16.9802 | -57.4609 | 2024-10-18 14:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.8 |
| f7a2e1d6-8538-31aa-813a-7a335f2b5273 | -17.2084 | -56.6739 | 2024-10-18 14:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.9 |
| de82571d-3685-3243-b1ab-c25ea2b6d1ea | -17.1647 | -56.9469 | 2024-10-18 14:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.1 |
| f4fbb571-f18e-3584-99a6-463d27fea156 | -17.2081 | -56.6946 | 2024-10-18 14:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.3 |
| a10d962a-88a5-30f1-87a3-861abc4bce82 | -17.2277 | -56.6922 | 2024-10-18 14:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.5 |
| 87ece28e-f262-3150-b478-a80b42b80da1 | -17.1529 | -56.4745 | 2024-10-18 14:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.4 |
| 7ef6142a-0cf5-3066-8bee-573bf21570c1 | -17.1843 | -56.9446 | 2024-10-18 14:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| 0e847f6b-7bd2-3a21-8d25-99182195fa08 | -17.1681 | -56.7407 | 2024-10-18 14:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 9c9f5502-eec4-3889-90c5-ecbf8065b6f4 | -0.7661 | -48.6828 | 2024-10-18 14:25:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| cfbb3ab3-e4b3-3d16-8bce-22a77e3e191e | -3.0577 | -44.3692 | 2024-10-18 14:25:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 205afb4a-516c-3191-9c76-915aa47aacb8 | -3.0949 | -44.3677 | 2024-10-18 14:25:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 141.6 |
| dc769377-14d4-37d6-856d-4c57fde9c081 | -3.084 | -51.2085 | 2024-10-18 14:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 983f6f34-711e-3eeb-a2e5-1fbdfa725c2d | -6.6703 | -70.1174 | 2024-10-18 14:25:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 4efa77d0-e699-3d76-94a0-07ac6c1ec7e0 | -6.6886 | -70.1171 | 2024-10-18 14:25:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 6cbc17dd-d957-33ba-a651-7539380dd76c | -16.7528 | -55.8005 | 2024-10-18 14:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.8 |
| 588a8de6-08f9-3e9a-bbec-e4ae0995476c | -16.9375 | -57.6904 | 2024-10-18 14:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| 0323412e-d533-3744-93e7-ecf0ded7372d | -16.9805 | -57.4404 | 2024-10-18 14:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.1 |
| 5f6f37aa-e2f3-3535-9d44-adf6f2b741ee | -17.2277 | -56.6922 | 2024-10-18 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.8 |
| 24510d7e-dd17-307e-848d-839552a8a5da | -17.1667 | -56.8232 | 2024-10-18 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.9 |
| b6300e03-a07c-30ed-825e-bf77480fb202 | -17.1647 | -56.9469 | 2024-10-18 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.3 |
| 8b0e988c-1a9a-3c15-a362-fe0ec4403f5a | -17.2081 | -56.6946 | 2024-10-18 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.3 |
| 72809749-b55f-35ab-a82d-72637bfadcef | -17.1677 | -56.7614 | 2024-10-18 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 8bfd9c65-3129-3a60-a15c-691ad889653e | -17.1843 | -56.9446 | 2024-10-18 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.9 |
| 6bbd9ca7-e1ba-311a-bc5a-4deddd900fcf | -17.1664 | -56.8439 | 2024-10-18 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.7 |
| f922e943-5487-35e5-87a2-e011e95470eb | -17.1681 | -56.7407 | 2024-10-18 14:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.2 |
| e7aed60f-dee4-3729-ad21-1b487d44e40b | -17.8478 | -57.2545 | 2024-10-18 14:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 1f0f10b1-3efc-3bbe-a96a-28cea5af5534 | -17.8277 | -57.2776 | 2024-10-18 14:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.3 |
| 1e582951-7008-38a7-852e-cfe8f34628fe | -0.766 | -48.7042 | 2024-10-18 14:35:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e4abf738-808d-3bca-8fe6-cd78b3e3fc85 | -0.7661 | -48.6828 | 2024-10-18 14:35:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5a079474-a8aa-3962-895a-a338ffaf39fd | -0.8583 | -48.7248 | 2024-10-18 14:35:11 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 78da9764-e489-34ef-bcc9-39c5095d54c2 | -3.0577 | -44.3692 | 2024-10-18 14:35:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 201b78d6-36b6-38e3-89bb-7983a5c82963 | -7.3638 | -72.8446 | 2024-10-18 14:35:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| d4ed6b0d-d59d-3794-acf7-703f537f4581 | -16.9375 | -57.6904 | 2024-10-18 14:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 35d611a3-debe-351c-a8e4-e96e125190a9 | -16.9518 | -56.7875 | 2024-10-18 14:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| fbc65c17-9ffd-37a5-85e0-b001fc927a70 | -16.9714 | -56.7852 | 2024-10-18 14:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.3 |
| effcef8a-bae1-35d9-879f-7b5e62a251b9 | -17.2037 | -56.9628 | 2024-10-18 14:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.7 |
| 693824d6-5503-366a-9176-c71d81071500 | -17.204 | -56.9422 | 2024-10-18 14:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| cf074597-f6e6-368e-8378-c1b4d78f99f5 | -17.1843 | -56.9446 | 2024-10-18 14:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.1 |
| 0056a4ad-e08e-37eb-823b-6fa8ba2c173a | -17.1647 | -56.9469 | 2024-10-18 14:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.2 |
| bf5ee0aa-dcee-380e-8951-f66745d51c2f | 0.2484 | -51.004 | 2024-10-18 14:45:05 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 6784a683-33a8-31ac-b0df-69fae482ee4b | -0.8583 | -48.7034 | 2024-10-18 14:45:11 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| eaabae3f-bd8e-3a4d-8d66-6224e55caa15 | -1.0607 | -49.2132 | 2024-10-18 14:45:12 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 76ec6871-3271-3f5f-b972-b0d2e1b87f68 | -1.0607 | -49.1919 | 2024-10-18 14:45:12 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c3b8d6da-0eee-334f-b5fe-6be26d26b1b2 | -7.3638 | -72.8446 | 2024-10-18 14:45:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 16353909-5c04-3e0f-9330-2f2ee52f2152 | -9.4019 | -68.3067 | 2024-10-18 14:46:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 5374c90c-d1ff-3cc6-8cc1-a3b626cc7dc6 | -10.4802 | -68.1686 | 2024-10-18 14:46:06 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 80.9 |
| f7ee4d24-1dab-3ae3-8988-9d8da3161d9b | -16.9514 | -56.8081 | 2024-10-18 14:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| d959478d-fb16-3187-9c5d-253ec5989950 | -16.9518 | -56.7875 | 2024-10-18 14:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.1 |
| 9c76d944-cff4-3d26-9854-7c1a34b028f9 | -17.0289 | -56.8605 | 2024-10-18 14:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.0 |
| 5b629513-0609-3afc-ba40-5c7c7b55841d | -16.9714 | -56.7852 | 2024-10-18 14:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.1 |
| 5e54e372-2236-34ad-9eb2-08c8125c07ba | -17.184 | -56.9652 | 2024-10-18 14:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| fdbd1a03-ff0a-3af6-9fca-f2ecc57f5b80 | -17.1843 | -56.9446 | 2024-10-18 14:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.2 |
| ec04dfc7-f681-3260-ae57-cbcdd417aa7b | -17.1461 | -56.8875 | 2024-10-18 14:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.0 |
| 2fd4dec1-85bc-398f-bff3-d78f2efd0b0c | -17.204 | -56.9422 | 2024-10-18 14:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.7 |
| 367fb661-9178-3ef9-b267-52b22c88d3bd | -17.1264 | -56.8899 | 2024-10-18 14:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.3 |


