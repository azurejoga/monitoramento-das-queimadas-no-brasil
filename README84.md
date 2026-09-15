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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b3d9e56-5323-393c-83ff-896bffef44ec | -6.0256 | -59.9293 | 2026-09-15 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 44b06e3b-fdce-3ca9-a33e-a49f7f213d5c | -9.1337 | -65.8253 | 2026-09-15 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d3beaa09-251e-3ab0-b15b-b4a36e424637 | -12.6636 | -54.6782 | 2026-09-15 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c283b9e8-9338-35e5-8d6c-9d30fe7cc4d2 | -8.6191 | -44.4588 | 2026-09-15 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| e4d63ab0-d7dc-355d-a007-6dd5bec446ad | -11.5045 | -45.771 | 2026-09-15 15:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| bf1eea7a-1138-3e52-989c-ab06c39abcae | -15.2821 | -42.8075 | 2026-09-15 15:00:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 7170947f-bc87-344f-a62a-2a32757ae649 | -9.4931 | -56.7564 | 2026-09-15 15:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 096c4a77-f8a9-3b4b-8f7c-a907f07ac58a | -6.7463 | -59.4416 | 2026-09-15 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| a9bff225-f125-3a53-86cb-5def5f43b089 | -5.5286 | -43.3771 | 2026-09-15 15:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 33042a3d-ed72-3a96-b35c-035a005b1bc6 | -10.2926 | -45.3161 | 2026-09-15 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| d7432dd1-1179-3db9-94d3-6add7f1d3991 | -12.6818 | -54.7379 | 2026-09-15 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| e3da500e-5c12-3cbf-97b2-aba16e486136 | -13.3 | -51.6649 | 2026-09-15 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d064dccf-4650-3f8f-a80a-94d10320679a | -8.9601 | -60.5165 | 2026-09-15 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 99c5662e-d996-3f42-9e4d-8f90b7845782 | -8.8361 | -62.489 | 2026-09-15 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| beefa21d-7325-3f1c-9816-fd73c42346ba | -2.7767 | -49.4765 | 2026-09-15 15:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 0b1ea2fc-574c-3240-a7db-b789b8ca5900 | -5.2537 | -59.9732 | 2026-09-15 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 8d6933f9-0267-3116-8a15-5753a548bde8 | -10.6962 | -47.4953 | 2026-09-15 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ee81edb5-a916-31f6-984b-8bf2606d097b | -8.114 | -45.6301 | 2026-09-15 15:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 147.5 |
| c5365fe5-c33c-3c08-9ec7-5c0840c42c08 | -11.4357 | -51.4351 | 2026-09-15 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 9b117fde-8fef-3f87-a5c8-5fdbe7c3d3d8 | -10.3116 | -45.3136 | 2026-09-15 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 941d59cc-c1df-395a-842d-570ebba749ec | -10.2922 | -45.339 | 2026-09-15 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 87fe1530-22d0-3881-be3b-7f68ced0ad08 | -10.6335 | -50.5651 | 2026-09-15 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 3053f032-3b99-321f-ad03-73bc66c363ec | -10.6641 | -54.1491 | 2026-09-15 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 318df0f8-c27e-30ec-a0ce-be3a081bfff4 | -3.4943 | -54.6567 | 2026-09-15 15:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 3cfcebbd-2d1b-3aef-ace3-d4fcb04223d4 | -11.955 | -49.7295 | 2026-09-15 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 2615e880-8c85-3053-a4af-00c6e199f6f2 | -15.5974 | -53.8426 | 2026-09-15 15:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 2306f48a-7351-37f5-9b89-44b62f9ed4c9 | -8.4852 | -44.5885 | 2026-09-15 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 97aa295f-62b4-3e2d-8f71-dd1269a10bba | -5.8136 | -52.0897 | 2026-09-15 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 633086c0-3bd9-3f58-8382-559bbf1663ec | -6.0169 | -52.1614 | 2026-09-15 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a483efeb-9fb2-322d-943e-ca0827eb683d | -10.6417 | -46.0906 | 2026-09-15 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.5 |
| f404bca2-9c5b-3bcf-b79d-c792edb0f8c9 | -12.6633 | -54.6988 | 2026-09-15 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 6a910c32-1de4-3c44-ad45-5580ecd3666b | -10.0988 | -45.5685 | 2026-09-15 15:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| edeb8be4-31cc-391a-9eea-05ac1fa17c34 | -12.3273 | -47.9735 | 2026-09-15 15:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 95bde52c-c9a6-3aef-8bd7-2bfdfae6144c | -11.8154 | -46.5899 | 2026-09-15 15:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 2dd895dc-0809-319a-8436-0c085993abb9 | -11.436 | -51.4139 | 2026-09-15 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4cc8138d-ff6f-3403-b740-139c44832fd5 | -8.8137 | -46.905 | 2026-09-15 15:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 417d4f4e-0652-3a39-aa6d-86bc28ebe25b | -14.1822 | -51.7653 | 2026-09-15 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 86cc7dcd-04d5-3c28-8721-58a0767d1415 | -11.3642 | -43.9407 | 2026-09-15 15:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| e30b84b7-8fcb-3427-978d-41406918dde9 | -9.18567 | -35.54808 | 2026-09-15 15:07:00 | NPP-375 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 623f0bd9-35b8-393c-9a48-d87743584e3a | -7.10665 | -34.95698 | 2026-09-15 15:09:00 | NPP-375 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a5643eb3-9464-333f-9578-e95e89d0f72e | -10.6958 | -47.5175 | 2026-09-15 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 2f20b95c-4c8e-3194-9f53-620b247e06d2 | -10.6525 | -50.5631 | 2026-09-15 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| f236eb90-29b9-3bb7-ac46-3c0a8dd274e8 | -15.5783 | -53.8241 | 2026-09-15 15:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| bc42c9ec-09d4-39bb-a1c5-6860eeee75a9 | -12.0905 | -50.8307 | 2026-09-15 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 19216526-c6b4-30bb-a238-8866659601b8 | -15.5779 | -53.8451 | 2026-09-15 15:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| f95ab4a1-e186-337e-846e-c355395f9152 | 1.0951 | -50.957 | 2026-09-15 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 80.2 |
| f3a40e7f-e430-3f11-b00d-3b17174afdcf | -13.4085 | -54.6009 | 2026-09-15 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| efff1a86-14e0-3998-8fee-9b4f66808dfa | -14.1822 | -51.7653 | 2026-09-15 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f9bff9da-629c-3487-8862-6a9d63393134 | -8.8134 | -46.9272 | 2026-09-15 15:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 9ce45ae5-28a0-3020-a314-c77922c082bb | -12.6821 | -54.7174 | 2026-09-15 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 23629b83-cdbe-3952-b889-62810c650e5f | -9.1337 | -65.8253 | 2026-09-15 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 081f722b-859c-3368-8c60-6073f341c105 | -13.4468 | -54.5968 | 2026-09-15 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 9ad3552f-df81-3891-840f-034cebf73864 | -10.6827 | -54.1679 | 2026-09-15 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 47fc67bf-e2cb-3f8c-a340-9204c7f37dfb | -6.7114 | -51.166 | 2026-09-15 15:10:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 54aff871-8ac8-3f9d-8183-ff53348e7b96 | -6.6767 | -58.7105 | 2026-09-15 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 67f30bf1-f537-3dc8-9b48-9070c6c2e777 | -10.5924 | -57.3151 | 2026-09-15 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f34a0f8d-2e6d-327c-92ea-846d474959e8 | -9.4234 | -47.8588 | 2026-09-15 15:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 89035c43-df91-311f-aaf5-6efb6d47918c | -8.7949 | -46.9069 | 2026-09-15 15:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1bb602ac-ce72-33e9-9b88-5f8ee9f97036 | -6.6766 | -58.7299 | 2026-09-15 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 02342c61-35e7-3459-9683-2651cd397626 | -10.6335 | -50.5651 | 2026-09-15 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 0d2689a8-ea88-31e4-b797-c57d23956e95 | -11.3642 | -43.9407 | 2026-09-15 15:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| af9bafd0-58dd-302e-affa-cc10dd03941c | -7.5608 | -62.33 | 2026-09-15 15:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 188.2 |
| 412fbba8-f934-3c50-9c19-77b237504a82 | -8.7889 | -45.8999 | 2026-09-15 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5eaf4ae4-2add-3f9e-bc0f-c3d9bc13761d | -8.8456 | -45.8939 | 2026-09-15 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 99f082ad-d87a-306b-833a-fea3c249397d | -5.2023 | -49.3348 | 2026-09-15 15:10:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 178a3146-50c1-36ae-b75f-c50670d99995 | -12.1265 | -44.199 | 2026-09-15 15:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 2999baf0-c8db-35fa-aabb-ad5175a68f0b | 1.2243 | -50.7475 | 2026-09-15 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a44d373d-c2ae-38ed-ab6b-49a20782c775 | -8.638 | -44.4567 | 2026-09-15 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 645.8 |
| c43afc78-b84f-33f2-a788-6e439977563a | -13.7722 | -48.8087 | 2026-09-15 15:10:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| afae6ffc-41da-380b-9062-0b553a64bcf4 | -10.6962 | -47.4953 | 2026-09-15 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ccb23c0a-cb74-3080-a6c3-6db0b2a1dd03 | -15.2859 | -53.9037 | 2026-09-15 15:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 32af6f24-035f-3193-ad98-ecaf0eca7397 | -13.414 | -57.0225 | 2026-09-15 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| d5de3e62-2936-33d0-a733-0763c1185ade | -15.3602 | -52.9678 | 2026-09-15 15:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| b54e3127-104d-362f-bab2-45748f8384ac | -8.6191 | -44.4588 | 2026-09-15 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 9b1c1700-a0ca-37f0-898a-e844cafa7468 | -10.3113 | -45.3366 | 2026-09-15 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 304.6 |
| 6487c31a-226d-34a9-ad4c-7665f1064438 | -3.5726 | -58.5581 | 2026-09-15 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 59179bc7-ea39-34b2-9b9f-41e2f1f3c6a8 | -6.1362 | -59.8871 | 2026-09-15 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 21ad10a0-ec64-349c-a7f6-d6ffc5d4fbae | -11.383 | -43.9614 | 2026-09-15 15:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| b6d7a2c2-5db0-3c09-a3b7-3e6ff6817696 | -15.597 | -53.8636 | 2026-09-15 15:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 51153fd2-e87e-32f1-a40d-9be6fdf44a0a | 1.0951 | -50.9778 | 2026-09-15 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c33c5632-1679-332a-baa9-a12b0d03ff6b | -9.7358 | -47.0958 | 2026-09-15 15:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 185.1 |
| dc083496-ae53-3c01-99ad-35f145b5ea17 | -12.6636 | -54.6782 | 2026-09-15 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e2cc0e01-8215-3020-8167-d67973e8f0e9 | -12.6824 | -54.6968 | 2026-09-15 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| a502730a-d15f-33d1-ad75-db743b6ede86 | -6.8408 | -43.5021 | 2026-09-15 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| c83454b6-bbfc-3e51-a14c-74bb050786d6 | -7.5609 | -62.3111 | 2026-09-15 15:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6e542a64-cfad-3fce-8b1f-8c5cfb8f98fb | -6.7648 | -59.4408 | 2026-09-15 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7028091b-cb7f-3a00-862c-d8a20b89f7ce | -12.126 | -44.2225 | 2026-09-15 15:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| c6ae004a-6a89-3ac1-b9e3-86dfd4c57619 | -10.9595 | -50.2529 | 2026-09-15 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b7c1b5ac-7d8b-3b8e-8538-89635a2516e4 | -15.5584 | -53.8477 | 2026-09-15 15:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| f2ef7246-cdb4-3cc5-92b1-b8fedb5f3bee | -10.312 | -45.2907 | 2026-09-15 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| ed5e79e5-5395-3c6c-8025-b27ecdd2b9f6 | -6.6952 | -58.7097 | 2026-09-15 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d56c85b8-d213-31f4-aa5c-395ed10bf27a | -8.8459 | -45.8713 | 2026-09-15 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 7e2fd181-7ac1-3ba5-945b-9fd646825d85 | -2.7768 | -49.4553 | 2026-09-15 15:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| fdd6305e-2142-3030-8458-b4afb0599fe9 | -12.3273 | -47.9735 | 2026-09-15 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 209.2 |
| 5c1d4dac-7f07-3b53-8df0-d3399bb7e372 | -2.9024 | -50.4423 | 2026-09-15 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 233ef690-345b-3787-bae7-a9c74e103c65 | -6.6953 | -58.6903 | 2026-09-15 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 334b988c-6ebd-34a2-a732-0842d49c82e5 | -10.3109 | -45.3595 | 2026-09-15 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 341.3 |
| 5ae11428-8fdc-306c-ac8f-3c486c4f882c | -9.1523 | -49.9853 | 2026-09-15 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| cb08d3fa-a1e5-30f8-99b3-69c06c172343 | -6.3574 | -44.9023 | 2026-09-15 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| bd009551-be34-30ac-89c4-1c5ab08f0a39 | -9.7687 | -46.1067 | 2026-09-15 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |


[Clique aqui para ver as próximas entradas](README85.md)
