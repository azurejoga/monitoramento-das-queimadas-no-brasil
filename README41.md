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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae13c7ac-3768-315c-a5a8-5cbb82a4a9da | -3.2899 | -50.4516 | 2024-10-04 02:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 313.7 |
| cdc424a7-d29e-36a8-87b6-d7aea8ece08b | -3.29 | -50.4306 | 2024-10-04 02:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f99bc0a8-881e-3817-8a1e-0f3e8ee3dc98 | -3.3083 | -50.4719 | 2024-10-04 02:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 130e550a-aa88-37dc-b7b2-f25f2944f430 | -3.3084 | -50.451 | 2024-10-04 02:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 261.2 |
| c6f03056-ab8e-3033-b3e4-23561b468057 | -4.0949 | -48.4894 | 2024-10-04 02:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f53cd218-d05b-37fe-96a2-3336f2fb0eac | -4.5375 | -43.304 | 2024-10-04 02:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 0c7962b0-13b6-3339-a83b-fe5678af2d68 | -4.6684 | -45.8961 | 2024-10-04 02:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 5a77fb44-b890-34b9-8472-c7e367c5e6d7 | -4.6686 | -45.8738 | 2024-10-04 02:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 260.7 |
| e369354b-97fd-30bb-8e41-e34425a7d84b | -4.687 | -45.8951 | 2024-10-04 02:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 262.7 |
| d3150dc7-a402-3ee0-8af7-6036cc0538f5 | -4.6872 | -45.8727 | 2024-10-04 02:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 631.4 |
| 858417fe-c145-3a9f-a2d0-839619bd0a09 | -4.6873 | -45.8504 | 2024-10-04 02:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 94.9 |
| cd1ef577-3ad4-3e27-bcfb-5fb719624761 | -4.7058 | -45.8717 | 2024-10-04 02:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 61e64e04-193b-30a4-9a70-0bf1f9be5b39 | -5.8214 | -44.1426 | 2024-10-04 02:05:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 63e1291e-ae01-3b9b-96ce-39d94ecf9a7d | -5.8216 | -44.1196 | 2024-10-04 02:05:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 24655745-07d5-3f29-89e9-d9ea943c9aff | -7.0529 | -71.7544 | 2024-10-04 02:05:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 174cc321-bd39-34a6-840d-2cd008176c7c | -7.8539 | -45.3611 | 2024-10-04 02:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 2fc05ab1-f22c-34c8-9f9d-a214f7fb7e4e | -7.8164 | -50.543 | 2024-10-04 02:05:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 5349cd6b-2327-3d69-8802-121025ed0b83 | -7.8166 | -50.5219 | 2024-10-04 02:05:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 0ef7907e-57be-3d5b-8507-fb7b1d776aed | -7.8351 | -50.5416 | 2024-10-04 02:05:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 56ab4576-a962-3346-85c5-76f2f54cb121 | -7.8353 | -50.5204 | 2024-10-04 02:05:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 26bc36c9-1a13-3f5a-909c-afc3e419a0bf | -8.6448 | -50.0518 | 2024-10-04 02:05:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 6f9fac70-cbb5-35b8-b916-6e07b0e13d57 | -8.6636 | -50.0501 | 2024-10-04 02:05:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| cd15b58a-8f46-3127-b41d-60d2b14f5217 | -9.1041 | -50.902 | 2024-10-04 02:05:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| ae0aef0b-d92a-38c9-abf6-08471691c5a2 | -9.0162 | -67.3904 | 2024-10-04 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 258e79b8-19d3-36d0-a769-0cde42e3fa7b | -9.0163 | -67.3719 | 2024-10-04 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| d6a85da0-f1f3-306b-81c5-a000b2497d65 | -9.0347 | -67.39 | 2024-10-04 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 5459fb77-3ab8-3f7c-a64f-faa942d11b60 | -9.0898 | -67.5183 | 2024-10-04 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| e55dd841-d1c2-3e72-9a34-fb81dd16c81a | -9.0898 | -67.4997 | 2024-10-04 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 124.2 |
| a165bd12-0ed9-3288-8b80-ddf3262e5ffe | -9.0899 | -67.4812 | 2024-10-04 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 22338a27-39a6-3b0c-bab2-2f77c659a17f | -9.1084 | -67.4993 | 2024-10-04 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 1a366c3d-3d01-3fbb-a313-7624720bd302 | -9.3118 | -50.7991 | 2024-10-04 02:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| ef6527e4-5b52-3aa4-9439-442f4ca43024 | -9.3303 | -50.8186 | 2024-10-04 02:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 4c23055e-0644-363f-a613-63094f70577e | -9.3306 | -50.7974 | 2024-10-04 02:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 80d3163b-033b-305d-b798-648ec80f18fd | -9.5866 | -68.5058 | 2024-10-04 02:06:01 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2121db94-8f39-33a3-9541-e9233b03c71b | -9.8349 | -46.7726 | 2024-10-04 02:06:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5292d2f0-61d2-382f-b6ac-49449367f710 | -9.8353 | -46.7502 | 2024-10-04 02:06:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| fc5f7387-339f-3f3e-9938-114a9e034b69 | -9.8539 | -46.7704 | 2024-10-04 02:06:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| bbeb263f-ac69-30b2-8ec7-cd7473a44f23 | -9.8542 | -46.7481 | 2024-10-04 02:06:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| bf3a8a3f-2491-3d37-a204-4ad12d3a128c | -10.7118 | -47.7149 | 2024-10-04 02:06:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| e9a26b1a-320c-3e71-8f11-885ef521d619 | -10.7309 | -47.7126 | 2024-10-04 02:06:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 60501391-cd9e-326d-a906-3ccbbe36df34 | -10.7168 | -46.1489 | 2024-10-04 02:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 9e84ae42-e73b-3921-87be-66dd596bd2bd | -11.0532 | -46.5344 | 2024-10-04 02:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| c5ca7067-8d96-3ef9-8f4f-eac12900a132 | -11.0536 | -46.5118 | 2024-10-04 02:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 12fba2a1-9fb0-3478-be5f-e7ac18206a51 | -11.0723 | -46.5319 | 2024-10-04 02:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 434aed29-fe1a-3f93-8387-91b8c5275eec | -11.0727 | -46.5093 | 2024-10-04 02:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 10bc7838-1405-3a80-80dd-c876b0f16243 | -11.0918 | -46.5069 | 2024-10-04 02:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| c096c16b-beea-3376-80ef-332396877b5a | -11.0921 | -46.4843 | 2024-10-04 02:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 326779a8-aa8c-3667-bee0-b7f8b9916c0c | -11.8242 | -56.6009 | 2024-10-04 02:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| e3cc61fe-40fb-3e4b-98ba-db8aa79892d0 | -11.8244 | -56.5808 | 2024-10-04 02:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| fe376e16-dc8a-3cff-bd18-ab8f77715bd1 | -12.5898 | -53.1359 | 2024-10-04 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| c5daa8bd-05ba-344c-9b9b-68a4104c1897 | -12.5901 | -53.115 | 2024-10-04 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 167.8 |
| 10452559-6e9a-3572-a6e8-171d55ac230c | -12.6092 | -53.1129 | 2024-10-04 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| a34c6548-f2c7-3201-8172-4413eec700a6 | -12.6089 | -53.1338 | 2024-10-04 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e9add556-e1e4-390e-ae05-f509fca348c5 | -12.6486 | -63.1022 | 2024-10-04 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| b3e176a9-3a34-33a2-998f-810b49f28ff5 | -12.6484 | -63.1214 | 2024-10-04 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9d8121c6-8c1f-325b-ab27-6278557d9464 | -12.6296 | -63.1033 | 2024-10-04 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 7f0fc543-df84-3bb7-854a-ff5d9b07bd81 | -12.6295 | -63.1225 | 2024-10-04 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 55e8f685-9234-323c-97b9-7c9167a770c1 | -14.7939 | -48.0275 | 2024-10-04 02:06:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 57ddb69e-c6f8-321a-b661-d4127dfb0ee9 | -15.3567 | -58.143 | 2024-10-04 02:06:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 537e1c15-7344-3918-901b-ce96a538d77b | -15.3564 | -58.1632 | 2024-10-04 02:06:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 7fd36951-4ad3-3ddd-90a2-3924ab3e4394 | -16.0732 | -50.3014 | 2024-10-04 02:06:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 61b0e4c7-b47f-3c56-b8f3-884e2a5e7f85 | -16.0737 | -50.2794 | 2024-10-04 02:06:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 502e0bf8-e7a7-3925-b532-a51821e230ad | -16.0929 | -50.2983 | 2024-10-04 02:06:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 60df1a65-7d99-31ea-a11e-1e8391feefb5 | -16.0933 | -50.2763 | 2024-10-04 02:06:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 7f809155-fec3-34bc-99b8-c9e8d255e2ae | -16.5928 | -57.2397 | 2024-10-04 02:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| aeaf668f-c8fb-3cf9-8227-7d527259c926 | -16.5925 | -57.2602 | 2024-10-04 02:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| 4106516f-942a-3774-822a-dfcef7ae1801 | -16.5736 | -57.2215 | 2024-10-04 02:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| e5081b4d-c0c5-34f0-bb0d-dc20fcd3eb31 | -16.5733 | -57.2419 | 2024-10-04 02:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 7de082f1-bcb5-3681-88db-18a2684ba2e2 | -16.573 | -57.2624 | 2024-10-04 02:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| ef9d341c-5df2-3abc-8755-2a790a6e3d9a | -16.4151 | -57.3823 | 2024-10-04 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| 22124a10-8836-337a-88d9-239037a13b76 | -16.4148 | -57.4028 | 2024-10-04 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| b75f01e7-2247-30af-83ff-7f4de005bcd0 | -16.5938 | -57.1783 | 2024-10-04 02:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 9743315d-03f3-373f-80f8-2685890dc483 | -16.5935 | -57.1988 | 2024-10-04 02:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 766adac5-3302-34c7-b7ab-0f061e7476f7 | -16.7606 | -57.7512 | 2024-10-04 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.0 |
| f9823221-1aad-3750-b71c-5b1ed30c22c8 | -16.6133 | -57.176 | 2024-10-04 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.3 |
| 8d89f8ac-1c38-3542-b77c-658dd85f5aba | -16.613 | -57.1965 | 2024-10-04 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 73c66a9f-1a2e-3713-8cbb-66d7c3cc1584 | -16.9283 | -55.8405 | 2024-10-04 02:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| bb2ce472-9452-3d03-9d31-bd1030b75151 | -16.9087 | -55.843 | 2024-10-04 02:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 8a35c506-3a5c-3225-afb9-ca28b94fcaa2 | -16.843 | -57.4767 | 2024-10-04 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 2e2db274-71d3-3e0f-919f-b8838a472d3d | -16.8055 | -57.3788 | 2024-10-04 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 6ff129d4-6bad-3e5c-8a1b-eeb5be70e29c | -16.7859 | -57.3811 | 2024-10-04 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 5bbf53fa-bb3c-3712-8ea1-14c6613b3b27 | -16.9287 | -55.8197 | 2024-10-04 02:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 719aa776-546b-37d0-801e-10a33bed4734 | -17.3844 | -42.6235 | 2024-10-04 02:06:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| c013e5d9-bf95-372b-a3e8-8dcebdaadd48 | -17.1288 | -56.7455 | 2024-10-04 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| b2507369-0c63-39ce-b447-fda40d3570c3 | -17.0512 | -56.6932 | 2024-10-04 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.3 |
| 894ce7f6-4c49-39e1-a845-585d829d0d1e | -17.0509 | -56.7138 | 2024-10-04 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| a3a11252-fc41-393f-a063-b0d2970c69c4 | -18.0854 | -42.5976 | 2024-10-04 02:06:46 | GOES-16 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.4 |
| 83ea842d-e30a-33dd-a72d-6bf635ba0426 | -18.8413 | -42.8985 | 2024-10-04 02:06:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.7 |
| ca4f76af-fe8d-344d-b659-c43fce3c0658 | -18.8617 | -42.8932 | 2024-10-04 02:06:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.9 |
| af92132f-e9dd-3de1-bf86-fa52e5c1f56b | -18.8613 | -43.5837 | 2024-10-04 02:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.9 |
| a95dad40-3a76-3e14-88de-fe64226dee9a | -18.9081 | -42.0315 | 2024-10-04 02:06:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.1 |
| c2bc9591-5d07-353b-8f69-f9f3dc1fd8a6 | -18.9089 | -42.0061 | 2024-10-04 02:06:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.7 |
| b4c99d33-fac2-3a4b-bbd2-4a7f4135f815 | -18.9285 | -42.0259 | 2024-10-04 02:06:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| b6ce99c9-567a-3715-865b-3e70f90cb7c8 | -19.3159 | -42.5976 | 2024-10-04 02:06:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.2 |
| c4328ab4-32ff-310e-9b08-39176766299b | -19.4899 | -42.8746 | 2024-10-04 02:06:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| 67ff86dd-e839-3dd0-89fa-ab8e68580ad2 | -19.8516 | -42.3738 | 2024-10-04 02:06:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 176.5 |
| 9a356d23-9ab4-32c1-8273-f4bdb0641d90 | -19.8524 | -42.3484 | 2024-10-04 02:06:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.1 |
| 747c125f-9cb6-33db-a881-24c3ac62a100 | -19.8721 | -42.368 | 2024-10-04 02:06:55 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.3 |
| 838f72e6-7e10-326f-8e6f-5b3d9b9c7bc5 | -20.121 | -43.5219 | 2024-10-04 02:06:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| 56f82843-b84f-3fc1-af05-83360eb194bd | -20.1416 | -43.5162 | 2024-10-04 02:06:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.1 |


[Clique aqui para ver as próximas entradas](README42.md)
