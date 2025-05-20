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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5dc2d8d-918c-3a99-b96d-4ebf302869dd | -14.01961 | -55.13014 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6496c8e-12e8-3cdc-a5bd-52b3e3013304 | -14.02551 | -55.12092 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c2db2465-d98d-369c-9830-21d94b32607c | -20.95776 | -56.60661 | 2025-05-20 05:25:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9f069a70-f905-3b79-98c1-3bff8f8c0ab4 | -13.71096 | -57.47708 | 2025-05-20 05:25:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20b6c984-b0e0-3037-8269-864915c3669b | -14.03258 | -55.13457 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5df9bef6-92bf-3d46-aaed-0364419330ea | -12.46813 | -57.19108 | 2025-05-20 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48090224-af63-3159-9b2c-11db77f7fb43 | -22.21487 | -56.19885 | 2025-05-20 05:25:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95936f7a-f105-3781-80b3-93688e79ac3c | -13.02605 | -45.06794 | 2025-05-20 05:27:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 17d72021-b9b4-3ca8-bea0-cb3a27d5b4bd | -17.50538 | -46.74244 | 2025-05-20 05:27:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3578c181-3bb1-3106-9e8c-2eec69911cf4 | -12.2909 | -52.46519 | 2025-05-20 05:27:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| d894c8f3-00a4-335b-93cb-09b6b35dce1e | -17.50707 | -46.73201 | 2025-05-20 05:27:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ae4966b5-0005-3c1a-86ba-136da1361eac | -9.6559 | -67.24046 | 2025-05-20 06:14:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22c3583f-da36-3667-aa4a-dfd71fc4cb0c | -12.48 | -57.1863 | 2025-05-20 10:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 99607848-fc9e-3bd6-92a9-725fa86e941b | -12.48 | -57.1863 | 2025-05-20 10:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 172.3 |
| 1d07e9e9-443f-300d-b233-ea30e66a3d76 | -12.48 | -57.1863 | 2025-05-20 11:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 191.7 |
| fe9eb934-0c8f-3be1-a4f4-f16f515f085a | -12.461 | -57.1879 | 2025-05-20 11:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 180017a7-b945-3498-baf0-e2a8252afe61 | -12.4798 | -57.2063 | 2025-05-20 11:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 58e2b763-8b6b-384d-8475-31546f2003a4 | -12.461 | -57.1879 | 2025-05-20 11:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 9cdcc056-aa23-3dfc-9ccf-bdb54fb2c281 | -12.48 | -57.1863 | 2025-05-20 11:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 273.8 |
| cd0bfd88-d445-35ed-b76c-3fb0aa6c542c | -12.4798 | -57.2063 | 2025-05-20 11:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 2ee76cd5-e248-3ab4-9281-8f5f1881ee28 | -12.4798 | -57.2063 | 2025-05-20 11:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 173.1 |
| 7529fd2c-7c85-32e8-a2c4-a41a9ffbe133 | -12.48 | -57.1863 | 2025-05-20 11:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 416.3 |
| 167345ce-6c63-37f4-8594-be7a8ce38e4e | -12.461 | -57.1879 | 2025-05-20 11:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 6feb820a-eb68-3faf-a46f-4643ac928d84 | -12.48 | -57.1863 | 2025-05-20 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 476.0 |
| 8b65cf91-cbf9-3a01-a2ab-9de0d2252bce | -12.4798 | -57.2063 | 2025-05-20 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 208.3 |
| cdcc3cf4-031b-38c5-92a6-514392a24580 | -12.461 | -57.1879 | 2025-05-20 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 3caef794-6a72-39b6-a6c1-a27ffad94e56 | -12.48 | -57.1863 | 2025-05-20 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 636.0 |
| 8a74c551-3211-3014-afe1-326601c46fc2 | -12.461 | -57.1879 | 2025-05-20 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 93016c8a-43ec-3624-868c-6a64604cd9a9 | -12.4798 | -57.2063 | 2025-05-20 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 156.1 |
| 13792c22-411d-32bb-9988-f17a250d2f3f | -12.4798 | -57.2063 | 2025-05-20 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 11c29e3f-7da7-3e4c-82af-0c667969f383 | -12.461 | -57.1879 | 2025-05-20 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 3e3a3496-33ca-3cef-9314-c5979a4d06ec | -12.48 | -57.1863 | 2025-05-20 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 532.6 |
| 78baaae0-72a0-344c-8814-823ac0ff045b | -12.48 | -57.1863 | 2025-05-20 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 590.8 |
| f4324a07-cb11-319d-8525-28a41f7d68cd | -12.461 | -57.1879 | 2025-05-20 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 9b0fa7a5-7096-3a7e-b46e-d1366f686b04 | -12.3519 | -49.9617 | 2025-05-20 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 66edd0cd-decd-3435-8138-a41d9cc95c6f | -12.4798 | -57.2063 | 2025-05-20 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 226.4 |
| 2448ceb5-486a-36b4-a6c4-9d68da960951 | -12.3327 | -49.9641 | 2025-05-20 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| c775f8be-ce37-3995-b6f4-3411e8f3eee4 | -11.6999 | -47.7909 | 2025-05-20 12:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e71ac480-59a5-34bf-816b-2f97c43836f8 | -12.461 | -57.1879 | 2025-05-20 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 196.9 |
| 8deb6a29-4f18-3318-b379-5125adc0baa3 | -12.3327 | -49.9641 | 2025-05-20 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 952083cf-14e8-34e8-9337-072766dff1b4 | -12.4798 | -57.2063 | 2025-05-20 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 05ab5d3a-0a5e-34f4-a3a9-055b281f1529 | -12.48 | -57.1863 | 2025-05-20 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 657.5 |
| f282064e-d155-3e45-a567-58eabd49d52d | -12.3519 | -49.9617 | 2025-05-20 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 0869b295-5150-3bad-8100-64e00e52c568 | -5.98071 | -43.7544 | 2025-05-20 12:19:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9f0e8af7-e8c8-3ada-989f-8a909ace3d7c | -4.82524 | -44.35312 | 2025-05-20 12:19:00 | TERRA_M-T | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f6dd0501-97b1-34e7-97af-f2997a507fdb | -7.06215 | -44.3842 | 2025-05-20 12:19:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8ac9028a-13bf-3c52-a52c-28f0be9b0c20 | -6.23869 | -43.3642 | 2025-05-20 12:19:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e1b2c32e-6776-341c-868a-1fa2b42d2713 | -5.69186 | -45.19099 | 2025-05-20 12:19:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d78dbf39-3049-38de-9d3f-db1c88af012a | -6.20605 | -43.3305 | 2025-05-20 12:19:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 70e9e770-f8f8-3b9e-8600-5bca9d3a79f5 | -7.35548 | -46.93615 | 2025-05-20 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 470e051c-78a9-3442-8f91-102eb9cb055b | -5.97941 | -43.7636 | 2025-05-20 12:19:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 449829c6-c09d-3d87-a29d-a403f7c16dc1 | -6.61816 | -44.77321 | 2025-05-20 12:19:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 957f6b39-6a9b-3ab2-8d6b-6e227dc2f4fb | -6.20739 | -43.32095 | 2025-05-20 12:19:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| dea96377-99fa-39f5-bb4a-a0a294d243e4 | -6.6875 | -44.16263 | 2025-05-20 12:19:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1dc9bf7c-ba92-3929-a595-bddfd8b1f9e7 | -7.06343 | -44.37516 | 2025-05-20 12:19:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| faefe4bc-2e43-38aa-b678-bec525cba342 | -6.88289 | -47.8275 | 2025-05-20 12:19:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| d49a9321-2688-3af9-a96d-4ff6e29c6621 | -3.13602 | -40.98766 | 2025-05-20 12:19:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 69.1 |
| b9fd87ac-cf4d-358e-bdcd-213f5b82f38d | -8.26833 | -42.88646 | 2025-05-20 12:19:00 | TERRA_M-T | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 9928a02e-a47e-3ec6-a3f0-5de4faac972d | -7.11697 | -47.8482 | 2025-05-20 12:19:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 40d870b6-e5bf-36a5-89fd-21124b57d1f9 | -5.9704 | -43.76236 | 2025-05-20 12:19:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9e3b9e6d-d5c2-3e09-872e-389886af302b | -6.60931 | -44.77199 | 2025-05-20 12:19:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 099ddfa7-1cca-312f-bf1f-3bdc2d7fd41f | -6.21656 | -43.32222 | 2025-05-20 12:19:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| e798cbf8-1bec-39bd-ad02-d50427f1c629 | -7.35406 | -46.94577 | 2025-05-20 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9d9fc7fe-bd7f-3dc2-bc31-dade74e98b0e | -6.88608 | -45.22367 | 2025-05-20 12:19:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 5aa89366-f008-3361-afe5-59de0de54894 | -6.23222 | -43.34383 | 2025-05-20 12:19:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a851efae-117f-35a9-8d72-3bd5562e0621 | -6.68879 | -44.15357 | 2025-05-20 12:19:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 71f8be38-9f72-31aa-a38a-4b9830f0431e | -6.61058 | -44.76313 | 2025-05-20 12:19:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4bad8a37-1159-361a-aa6c-271efc8f1126 | -6.23087 | -43.35347 | 2025-05-20 12:19:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 24dd06be-b2f1-331e-ada8-9158e95710a6 | -6.8813 | -47.83814 | 2025-05-20 12:19:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| bcb4bd98-4d1b-309a-bcf5-5c8ee814d12a | -6.21522 | -43.33178 | 2025-05-20 12:19:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| b226f35c-8e43-309e-b7f1-16068c1d6dab | -3.1344 | -40.99931 | 2025-05-20 12:19:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 3d1d6c15-c483-3c3a-aa1b-29737f1386a7 | -6.61943 | -44.76436 | 2025-05-20 12:19:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 65d2eb66-acc0-3949-8885-4404289265cf | -8.27301 | -42.88233 | 2025-05-20 12:19:00 | TERRA_M-T | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 7a4ff798-1364-31bb-b671-0e306bf1b7a5 | -5.76036 | -43.48846 | 2025-05-20 12:19:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7c139e86-880d-31cc-bdcd-8a1fd9bfae86 | -12.4798 | -57.2063 | 2025-05-20 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 6609b487-39bd-3da5-a729-b8af94402aa2 | -12.461 | -57.1879 | 2025-05-20 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 163.1 |
| a35cafa9-d662-34ce-9e64-7194469474b7 | -12.48 | -57.1863 | 2025-05-20 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 715.0 |
| e0e1e87d-edce-3ce1-b43a-af9107023a52 | -11.8863 | -46.9179 | 2025-05-20 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| eb0c8942-2cc7-3d3c-a4e4-7871d6418da0 | -12.3522 | -49.94 | 2025-05-20 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| d5009cb3-8b31-3a2c-a7b3-9b36fd4449e0 | -12.3327 | -49.9641 | 2025-05-20 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 210.8 |
| 62ee12fd-a4a4-3d83-8328-83737d864b36 | -12.3519 | -49.9617 | 2025-05-20 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 595c0160-f56f-302b-a3b3-d68d6a066cd0 | -11.8859 | -46.9404 | 2025-05-20 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| fa7b6827-6158-3b7e-8da6-5f0e5d67938d | -11.6999 | -47.7909 | 2025-05-20 12:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 24c20123-67be-3287-91d7-7bd8d3448e65 | -10.62252 | -46.35578 | 2025-05-20 12:21:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1d1704c5-98a4-3fb0-acd2-8e65b49c5024 | -13.1558 | -44.93126 | 2025-05-20 12:21:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 63f7e751-571c-3867-b084-82d47a8927e0 | -10.64172 | -47.04869 | 2025-05-20 12:21:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 3f97387b-8a43-38c6-b53a-b477772adbc5 | -11.88439 | -46.93924 | 2025-05-20 12:21:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b6abfb4a-d68f-3173-b87a-f0f74e456b1c | -12.11088 | -49.30687 | 2025-05-20 12:21:00 | TERRA_M-T | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aa3211dc-da76-3990-9d6a-7857f537102e | -13.68044 | -45.26642 | 2025-05-20 12:21:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 56cb65ad-e6ef-3150-9e0b-7efd827a757d | -9.18309 | -45.34233 | 2025-05-20 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| bf81f0f4-c213-3676-8300-c695e6a681c5 | -9.01839 | -49.1623 | 2025-05-20 12:21:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 250aaf07-a383-30b2-a830-7a5383467c24 | -9.25912 | -47.90769 | 2025-05-20 12:21:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c0a3c1cb-c7da-358d-8dce-54a7d6c7f910 | -11.88573 | -46.93011 | 2025-05-20 12:21:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 210.9 |
| bed9608d-2e2c-3f25-b169-f893ba9c29e4 | -8.53993 | -45.90326 | 2025-05-20 12:21:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 262aaf2c-fba8-374b-b04e-bf092b620e4d | -9.62006 | -47.7711 | 2025-05-20 12:21:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 25661690-ec1f-3775-b0a3-e70a61a5dcf1 | -14.02205 | -53.0163 | 2025-05-20 12:21:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 8f29cb2b-67d7-3ccd-91da-b17e94309208 | -10.36588 | -47.97326 | 2025-05-20 12:21:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f7b5f009-925d-388b-9937-5894040555a2 | -10.2333 | -48.05 | 2025-05-20 12:21:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 2d5c0b05-422f-3040-a9d3-5f9182fdbabd | -13.0272 | -45.06673 | 2025-05-20 12:21:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fda3f753-0086-35da-b47c-4934d1ec10d6 | -10.1071 | -46.47952 | 2025-05-20 12:21:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README15.md)
