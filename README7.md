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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94861368-ba4c-36ac-aa44-6bd9b5f195cf | -18.43431 | -54.71053 | 2026-05-05 05:48:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56660c60-6dc1-3f5c-abdc-950ce1e4eeb2 | -21.23448 | -56.92346 | 2026-05-05 05:48:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ead7e0b8-26cf-3b3a-8a49-60db66a1fdcb | -18.43378 | -54.71579 | 2026-05-05 05:48:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4c46630-a1eb-3386-8860-ea704903eee7 | -18.43903 | -54.70121 | 2026-05-05 05:48:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b43b1d8c-1e7e-3bf3-9d95-dc121f834bd5 | -21.22886 | -56.92255 | 2026-05-05 05:48:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 634f8380-5cc5-380c-b6fa-b51e683bb2ef | -18.43225 | -54.7059 | 2026-05-05 05:48:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9dd489f-d82e-3b89-9607-845743f14c0d | 2.73375 | -61.35859 | 2026-05-05 05:59:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d8bd01b-be83-3f11-9c23-992ed38cd498 | 1.23252 | -60.57424 | 2026-05-05 06:01:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00528374-12f0-36c0-9274-f2ec81dee5a2 | 2.36042 | -61.05809 | 2026-05-05 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02ae8822-afbf-31a0-9ae3-9f195eae331a | -9.24949 | -60.33306 | 2026-05-05 06:03:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5457274e-969c-3f15-9ef8-6e31fe52a733 | -9.24896 | -60.33717 | 2026-05-05 06:03:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 501ce05e-0098-3bee-a462-6d22bc0b68e2 | -16.59775 | -58.24061 | 2026-05-05 06:05:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8906bbc5-4d77-3568-9507-03f6be0c3792 | -9.25066 | -60.33382 | 2026-05-05 07:22:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2e9706f9-b4b6-3471-8a8b-a994274a2bd6 | -12.3321 | -50.0073 | 2026-05-05 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e01c358b-e387-3b54-84cb-c07f06c83d4a | -12.3321 | -50.0073 | 2026-05-05 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 34f27cf1-c2d1-3d1b-a6a2-f2bf1c665a1d | -9.5204 | -46.2704 | 2026-05-05 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 37fa4e2c-9505-3d84-bc4a-773ed9bca8f2 | -12.3321 | -50.0073 | 2026-05-05 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 85f27f40-1a2b-314a-97bd-ae67ba54b7a6 | -12.70976 | -46.96053 | 2026-05-05 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 150f3dd9-5032-374e-ae62-c3b3519535e2 | -12.72751 | -55.01054 | 2026-05-05 12:19:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c0eeada6-df67-3fe3-a473-34b598f11547 | -14.01551 | -47.60203 | 2026-05-05 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 32.3 |
| a0f47ef2-4b12-398f-a1bf-0e66bc789beb | -9.50918 | -46.2702 | 2026-05-05 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 976207b8-d934-38bc-b32e-4b7c72fe4b12 | -9.41917 | -47.38359 | 2026-05-05 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 105587be-d776-322f-8b54-a180528a501c | -13.93087 | -47.5451 | 2026-05-05 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5b0b1e32-0e83-3878-9463-6073c6ca6c4f | -12.71988 | -54.99974 | 2026-05-05 12:19:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d380d129-45f1-34ac-9c07-d0b75e6350b8 | -12.06203 | -45.33687 | 2026-05-05 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 3804b537-7ebb-335e-9412-5955b9d739ce | -12.00234 | -45.32489 | 2026-05-05 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 5407a7b4-8071-300c-b622-78c130864dc4 | -14.13132 | -45.35614 | 2026-05-05 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 8ed885fc-40f4-335b-b95a-4d42571082ed | -11.99923 | -45.35218 | 2026-05-05 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 367e9920-7ab1-3d86-abc4-f283ab44fe09 | -12.34619 | -50.00458 | 2026-05-05 12:19:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 201.5 |
| ada9da1e-ddee-3cfb-980c-a3bf39db49fc | -14.1445 | -45.36436 | 2026-05-05 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| c68ad453-9847-3758-a6bd-14d0a97ff775 | -9.42506 | -47.39009 | 2026-05-05 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2e829d17-1ce9-3daf-b78b-6a66557f7482 | -12.16116 | -46.65652 | 2026-05-05 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 82dc671a-bd13-374e-aac7-3c9353be9996 | -13.93301 | -47.52677 | 2026-05-05 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 3c21e7c3-618e-3fc5-8756-978d84217684 | -10.5803 | -46.68187 | 2026-05-05 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 6bf42ddd-e8fa-3668-9d83-24becaa6ac0a | -14.12941 | -45.36261 | 2026-05-05 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| a454aa7f-0eac-3da8-8991-94931e2617f2 | -14.01785 | -47.58198 | 2026-05-05 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 43.1 |
| da759db4-fed0-359f-afcf-9c783fcec00b | -12.72892 | -55.00112 | 2026-05-05 12:19:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 99b7aed7-0468-358c-a855-087cce36e620 | -12.15754 | -46.6627 | 2026-05-05 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 8e56e02e-d5fd-3cb5-9363-64d957246d33 | -13.43548 | -43.85487 | 2026-05-05 12:19:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 0f6e763c-59ea-3f90-a46a-30490ddfee12 | -13.43074 | -43.84862 | 2026-05-05 12:19:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| b0828491-a09b-31b3-a8f9-d33587ae27db | -11.62038 | -48.06477 | 2026-05-05 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 3f449155-811e-3058-af4c-1f5ba28f8981 | -11.31999 | -51.82809 | 2026-05-05 12:19:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 72f83805-a126-35dc-a70c-98513ff64153 | -14.69131 | -46.15888 | 2026-05-05 12:19:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 41.3 |
| c21a182e-253b-3ba9-94ce-2cfcf7d57a1d | -12.06115 | -45.33113 | 2026-05-05 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| be40e5ff-f44a-3e8e-9697-e45b14bf5067 | -12.34461 | -50.0167 | 2026-05-05 12:19:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 96833f59-3f64-3670-9b11-d0f4465e755f | -11.79759 | -43.6053 | 2026-05-05 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| b44bddbe-0e45-3664-8827-f6557e064dfc | -12.33598 | -50.00322 | 2026-05-05 12:19:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 63094728-3a1d-37d7-b860-c9fd0e17ad83 | -12.33442 | -50.01536 | 2026-05-05 12:19:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| adf2dd4d-3f57-3b04-aab8-ae042d718995 | -9.52224 | -46.2721 | 2026-05-05 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| db90e33e-b3c2-32de-8b9c-feefc99f7486 | -12.14791 | -46.65503 | 2026-05-05 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 60b24262-900e-3ed2-a241-b961ba6cc1c9 | -12.3321 | -50.0073 | 2026-05-05 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| bd901696-bfc4-3bb1-bdd5-7f48616b8401 | -9.5204 | -46.2704 | 2026-05-05 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 84e99832-59f9-363b-b23b-d8afdd22be68 | -18.93224 | -53.42815 | 2026-05-05 12:21:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b3ee4669-22d1-36f9-8b1d-e0f8bc52e9f9 | -14.69744 | -46.13873 | 2026-05-05 12:21:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d17af39e-7f70-3788-90b3-3aa5a5c53ab8 | -16.11782 | -49.23168 | 2026-05-05 12:21:00 | TERRA_M-T | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e117a239-8ed1-30f7-a1d4-a3ca14103f4c | -15.71936 | -53.6378 | 2026-05-05 12:21:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cdad9865-afff-3196-9381-802f1283d852 | -20.71501 | -52.07313 | 2026-05-05 12:21:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 37d9176c-ce33-3422-93c7-e770f5fc6ca9 | -20.7135 | -52.08527 | 2026-05-05 12:21:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 5edf738e-e98c-3663-ba57-692ec4e5642e | -20.71737 | -55.17267 | 2026-05-05 12:21:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b5079da1-ba1c-3fc5-9cde-0929d0b89c17 | -18.44242 | -54.70744 | 2026-05-05 12:21:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0ad30cb1-b5e6-3c7d-a70c-17860f5bd28a | -21.38295 | -48.96456 | 2026-05-05 12:21:00 | TERRA_M-T | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 2e153263-c3a8-323d-8e14-0b8de0995313 | -15.37857 | -52.23377 | 2026-05-05 12:21:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 855d6883-e5a3-39e0-940f-6c13f74f285b | -18.07136 | -52.65022 | 2026-05-05 12:21:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 701466c3-da08-3a1c-99a9-63ec0ddc59bc | -17.04656 | -49.28169 | 2026-05-05 12:21:00 | TERRA_M-T | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 43806694-721d-32ba-896c-6bd1c23de70d | -20.71604 | -55.18209 | 2026-05-05 12:21:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5248959b-3a54-3af5-a783-e475b75f4eac | -15.71806 | -53.64706 | 2026-05-05 12:21:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cf031f1f-421e-3fd0-9e97-22cae09c1af0 | -15.85011 | -46.5294 | 2026-05-05 12:21:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 4441c11a-2299-3676-82f3-2ddfecb81386 | -21.38334 | -48.97115 | 2026-05-05 12:21:00 | TERRA_M-T | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 44.9 |
| d6ed1126-6a7b-3504-96d0-a412ecf84a4b | -13.99805 | -56.62447 | 2026-05-05 12:21:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2562d812-85d1-33d3-8b5d-7d8052d948c6 | -22.84582 | -52.7085 | 2026-05-05 12:23:00 | TERRA_M-T | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 46.0 |
| 08314343-9725-3aea-b23b-8622e1480081 | -22.84435 | -52.72036 | 2026-05-05 12:23:00 | TERRA_M-T | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 465a6f1e-ab6f-337b-91d1-bee316dd8c8d | -23.76383 | -49.16343 | 2026-05-05 12:23:00 | TERRA_M-T | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b483ce05-acf0-352d-8eca-77da105f9e47 | -22.95657 | -53.20928 | 2026-05-05 12:23:00 | TERRA_M-T | LOANDA | PARANÁ | Brasil | 4113502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| d959eb66-2418-3909-8454-16934d99dd0f | -22.95799 | -53.19806 | 2026-05-05 12:23:00 | TERRA_M-T | LOANDA | PARANÁ | Brasil | 4113502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 878e7fcd-5531-3714-a325-2308b92c89db | -23.76596 | -49.14157 | 2026-05-05 12:23:00 | TERRA_M-T | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 26.3 |
| b96c0d72-81cc-3b15-b04e-c24a282ba110 | -9.5204 | -46.2704 | 2026-05-05 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 4bb259cf-1ecc-3243-9d94-6af03a53a8be | -12.3321 | -50.0073 | 2026-05-05 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 8124d43b-6cc5-3008-a176-abd9c6e74973 | -12.3321 | -50.0073 | 2026-05-05 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 201.0 |
| e209539d-a814-305d-8e49-6a112fa1d0d1 | -12.3508 | -50.0266 | 2026-05-05 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 3430a8b2-bcc3-365d-9352-9cdc7af64b86 | -12.3321 | -50.0073 | 2026-05-05 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 6bf9a2ca-af0f-3b4d-a0c1-bdb1ef528c8b | -12.3508 | -50.0266 | 2026-05-05 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| c349f040-40a3-3d9d-89a2-df0c63d8f7c7 | -12.3321 | -50.0073 | 2026-05-05 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 180.4 |
| cacb6489-e59d-3902-88ff-8894eb7e5598 | -12.3321 | -50.0073 | 2026-05-05 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 170.2 |
| e2287993-fcbb-3f3c-be4e-0569ed94efb8 | -9.5204 | -46.2704 | 2026-05-05 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 6436bf4e-3275-3c77-9e1f-11cc014614a8 | -12.3508 | -50.0266 | 2026-05-05 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| c42f7421-c17a-376e-9083-cc55174ee315 | -9.5204 | -46.2704 | 2026-05-05 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 443f57d4-6f52-3444-90be-ad79824f4349 | -14.0267 | -47.6124 | 2026-05-05 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| aabf82cc-f3ef-393c-a0e6-603fe125308d | -12.3508 | -50.0266 | 2026-05-05 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 1203c027-df9c-3566-a452-90760c79b33d | -13.9924 | -56.6437 | 2026-05-05 13:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c255c24f-1dbf-3dee-9dbf-dd7a80849607 | -12.3321 | -50.0073 | 2026-05-05 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 221.2 |
| b7723621-6b33-384d-955d-a3ee8c967533 | -12.3321 | -50.0073 | 2026-05-05 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 265.5 |
| a6299672-d385-37f9-8b8e-9fcff473055a | -9.5204 | -46.2704 | 2026-05-05 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| cd08495b-cb31-34dd-b15a-b19fb7a37e26 | -12.3508 | -50.0266 | 2026-05-05 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d1b9672d-94be-3146-91cf-f52e7f663427 | -13.9924 | -56.6437 | 2026-05-05 13:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| c684a821-ac1c-3b75-9e19-4c7b9ed87cb2 | -12.3508 | -50.0266 | 2026-05-05 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 84ace924-1743-34dd-8eed-7bf30e034e08 | -14.0267 | -47.6124 | 2026-05-05 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 04faed7c-c365-349f-be89-94be2fd651af | -9.5204 | -46.2704 | 2026-05-05 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 97b26fad-ed4f-3189-b84f-f7d66fb9246c | -12.3321 | -50.0073 | 2026-05-05 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 225.7 |
| 984c7464-bbe6-3040-9c20-a704201f46bf | -12.067 | -45.346 | 2026-05-05 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| adc39e65-182c-3805-81ed-6158d746b4fc | -9.5204 | -46.2704 | 2026-05-05 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |


[Clique aqui para ver as próximas entradas](README8.md)
