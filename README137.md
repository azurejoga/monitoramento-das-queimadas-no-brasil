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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eafd9fc1-a74c-38ef-87bc-a5d575cb9996 | -12.1073 | -43.1861 | 2024-10-14 14:36:14 | GOES-16 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 151.2 |
| 8e3cacf2-d604-3b79-8567-240b683b1db0 | -12.4182 | -53.1544 | 2024-10-14 14:36:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e3bdc8b3-4e5e-3b1f-8c73-f2b615d4b61c | -12.4432 | -47.9133 | 2024-10-14 14:36:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 862a79c8-03cb-3d56-9338-fb8fe01042d1 | -12.3807 | -53.1167 | 2024-10-14 14:36:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 142.8 |
| a3bd226b-38a2-3a19-bda7-8fc2202b095f | -12.4185 | -53.1335 | 2024-10-14 14:36:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 293a1729-5ec2-3d29-8b9e-4b31f4386aa6 | -12.3997 | -53.1147 | 2024-10-14 14:36:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 895ebdc6-b4c2-363b-9447-6618f05c81a6 | -12.4376 | -53.1315 | 2024-10-14 14:36:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| ca741c88-e047-388b-9ce6-c6a4a6da7c55 | -12.5962 | -44.7783 | 2024-10-14 14:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| a5e26c30-f651-3127-bfef-8bcb1700e178 | -12.6104 | -53.0294 | 2024-10-14 14:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c7fbbb58-5c1a-3d2f-8d89-f7b1d86279a8 | -12.4566 | -53.1294 | 2024-10-14 14:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f7a964ac-f762-3ef1-b046-fe4c684ecaaa | -21.5621 | -48.0058 | 2024-10-14 14:37:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 134.7 |
| e2830676-0c30-322f-80c2-b4a35b0d59b0 | -1.3927 | -49.2939 | 2024-10-14 14:45:14 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 6f5cbb6c-a095-3842-8701-824c0921393d | -1.7664 | -55.9805 | 2024-10-14 14:45:16 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| b3920392-2a9c-3101-9f96-b67eae217e5b | -2.6303 | -49.0767 | 2024-10-14 14:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 2262648d-9402-3afd-b8ba-7f35baa87734 | -2.6119 | -49.0772 | 2024-10-14 14:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 176694cc-a055-39c8-b087-1f20f41e88ee | -2.6118 | -49.0985 | 2024-10-14 14:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 70684228-a722-392c-8c7b-98bb49ac45c2 | -2.7769 | -49.4341 | 2024-10-14 14:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d2f0fe0e-ed43-3cbf-bcdc-1c975ebdc8d0 | -3.4169 | -43.3403 | 2024-10-14 14:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 8a8814fd-0858-3dde-97cd-cd6fad48cd70 | -3.7789 | -45.2459 | 2024-10-14 14:45:27 | GOES-16 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 71610102-9ca5-336e-9d3b-d7db68c3da14 | -3.9219 | -43.1525 | 2024-10-14 14:45:28 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 98420103-64de-3592-9d7b-4d6a9242ceb1 | -3.9416 | -49.4365 | 2024-10-14 14:45:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| d01e98c1-ecb0-320c-bf9a-3d9c8c47bf77 | -4.0957 | -42.2969 | 2024-10-14 14:45:29 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 869c31aa-7503-38fd-adef-5cea0993f9bc | -4.0348 | -43.0296 | 2024-10-14 14:45:29 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 34e9f246-e3b4-3d74-b9c7-983a5d87e66c | -4.1149 | -48.2299 | 2024-10-14 14:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 04473cca-1bd4-3d20-8aed-936686599d8a | -4.2038 | -45.7644 | 2024-10-14 14:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 93ae613c-9670-312d-82f7-e0b5a69f4307 | -4.1716 | -48.0327 | 2024-10-14 14:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 25e46563-4d07-310f-b667-1eb8be0bee48 | -4.2794 | -48.6317 | 2024-10-14 14:45:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a4685ea3-9e32-3f14-965a-8f8b714894fa | -5.23 | -48.0434 | 2024-10-14 14:45:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ca2e7c53-803a-33c9-8a12-e38345f4e785 | -5.2486 | -48.0424 | 2024-10-14 14:45:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 52893143-7d7c-3ffc-901c-e8a233c5ce31 | -5.2797 | -46.3725 | 2024-10-14 14:45:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 29bd033d-bc6a-3cd4-bc16-95b6cbc140e7 | -5.5669 | -43.281 | 2024-10-14 14:45:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 9d304e2f-ec8c-3f04-bee7-07621d2723d5 | -5.675 | -43.7611 | 2024-10-14 14:45:38 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f2a433a5-cc91-303e-88b5-2e023247c605 | -5.5903 | -44.8914 | 2024-10-14 14:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 0b9738aa-a021-3cbb-99e5-71f45926be57 | -5.7376 | -43.0575 | 2024-10-14 14:45:38 | GOES-16 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 51.2 |
| 801a1558-affe-38c3-9fbb-cf1060a11ac2 | -5.9971 | -45.4059 | 2024-10-14 14:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 1241dbbe-0deb-31d6-bdcd-e1e18d35f68c | -6.221 | -43.5092 | 2024-10-14 14:45:41 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| e8c1d46f-1642-303f-80a7-1661b07c78c7 | -6.2734 | -43.8994 | 2024-10-14 14:45:41 | GOES-16 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 0b694a8c-a43b-36c4-8119-bf62d7a5bf16 | -6.24 | -43.4844 | 2024-10-14 14:45:41 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 5ba209bf-9ffb-3d12-9882-2fef21c88f0f | -6.2547 | -43.9009 | 2024-10-14 14:45:41 | GOES-16 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 258448ea-51ba-3b75-8ef6-f55181353284 | -6.3608 | -42.6768 | 2024-10-14 14:45:42 | GOES-16 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 416d3a0b-a734-3782-ab50-7765a320b399 | -6.9313 | -43.8194 | 2024-10-14 14:45:45 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d815fee0-bbf4-38c4-99cd-0ed556b14946 | -7.6362 | -44.6754 | 2024-10-14 14:45:49 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 55e163a4-42e2-3dca-a41d-536904607f2d | -7.599 | -44.6331 | 2024-10-14 14:45:49 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 0efc85c0-89f7-3365-824a-1d103e5f372b | -7.8516 | -43.9855 | 2024-10-14 14:45:50 | GOES-16 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 327d383a-3243-3b0f-ad7d-7c52a9beb079 | -7.7506 | -44.5495 | 2024-10-14 14:45:50 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 6297a73f-6818-3ec4-bc46-b84f76bc3851 | -8.5241 | -45.9725 | 2024-10-14 14:45:54 | GOES-16 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| e029cde1-e013-3930-8222-867417b5a8f8 | -8.7814 | -46.4847 | 2024-10-14 14:45:56 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| a260463b-a87d-3fe6-943b-a8aec1252ecf | -9.1216 | -46.4265 | 2024-10-14 14:45:57 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 9abd6387-0b6e-3e6c-b774-4c662f41c817 | -9.1046 | -47.7377 | 2024-10-14 14:45:57 | GOES-16 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| d1090a3c-84f9-3e5b-9095-c38f9e2b71ae | -9.4885 | -45.8454 | 2024-10-14 14:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 9f33b686-dec8-3967-a761-71c148c61789 | -9.4175 | -45.5134 | 2024-10-14 14:45:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 42ce083f-d923-35a0-af4b-f9e1a0ca4346 | -9.4696 | -45.8476 | 2024-10-14 14:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9913fffc-2467-3dfa-a4dd-325276e062a4 | -9.4702 | -45.8023 | 2024-10-14 14:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ed2c3c96-7f1d-3a67-bc83-9ad64cc8fed8 | -9.4365 | -45.5112 | 2024-10-14 14:45:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 2a844822-4f1e-3803-b3ea-a9a9838a0792 | -9.4888 | -45.8228 | 2024-10-14 14:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| f9352b20-9ca8-3dc5-ae5e-2977936042ad | -9.4699 | -45.8249 | 2024-10-14 14:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 8107a51a-f693-3971-bd2d-0ae97c8d4868 | -9.437 | -44.1554 | 2024-10-14 14:45:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 15b4db2a-112e-3882-8e4d-4c4700d04b0e | -9.3149 | -46.0908 | 2024-10-14 14:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 99b0a84d-8684-3ef1-a6e7-b55fce917e0e | -9.9411 | -47.2949 | 2024-10-14 14:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 932cae16-1352-31ad-9cca-e9d72d71483a | -10.1637 | -46.3079 | 2024-10-14 14:46:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| e46dbcbc-117e-38db-a2eb-f98542d58e55 | -10.3303 | -46.58 | 2024-10-14 14:46:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 4e8606d0-3d34-394c-a9e1-4f5896e76210 | -10.7584 | -51.1254 | 2024-10-14 14:46:07 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 2a00c711-c235-33e8-b33b-a9525dfb22df | -10.8627 | -45.356 | 2024-10-14 14:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 9c0d7f05-9e52-36a3-830b-bf1529336b06 | -10.8433 | -45.3815 | 2024-10-14 14:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 95d83931-4f0f-3f1d-8dc7-ebc8ed84134f | -11.1542 | -51.2324 | 2024-10-14 14:46:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| f4221290-67a3-34e6-bff5-2a9ee3c83e4b | -11.245 | -44.1924 | 2024-10-14 14:46:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| f62dc3f6-f7fc-3ecc-8d05-b1f3243ea341 | -11.2637 | -44.213 | 2024-10-14 14:46:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 88f23838-caf5-3144-af1d-a31899d133bf | -12.3167 | -45.3314 | 2024-10-14 14:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| a3cbef97-8cb3-3ca4-9d09-dced0da14a7b | -12.3807 | -53.1167 | 2024-10-14 14:46:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 5ae33c76-bccc-36bd-a6ea-3852e9ce73f1 | -12.6104 | -53.0294 | 2024-10-14 14:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| bbab4af0-dfd6-32d5-9141-b27795176e6e | -12.4566 | -53.1294 | 2024-10-14 14:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 7f98cb6c-0744-3f30-a822-08e7328cce6e | -12.5962 | -44.7783 | 2024-10-14 14:46:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 74c44725-e457-38cf-8797-f093af362928 | -21.5621 | -48.0058 | 2024-10-14 14:47:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 129.0 |


