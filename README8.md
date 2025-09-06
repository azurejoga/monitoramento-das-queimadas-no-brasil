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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a75cbe6-59f4-341f-bbde-5fff8fc3333c | -13.0235 | -54.8262 | 2025-09-06 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| acdf7ddc-3fa3-3f82-8a6e-0bda3e71b10f | -10.5937 | -44.331 | 2025-09-06 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 4298c6d8-a801-35ad-9a16-0b481ad6f9f8 | -12.5227 | -53.8485 | 2025-09-06 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 2b3d3ab2-8c2a-30e9-bb25-9bb1e9c386f7 | -4.5031 | -42.8854 | 2025-09-06 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 245.6 |
| 664e2cb3-8824-3411-99a5-4dac5b1d28b6 | -15.4562 | -47.1236 | 2025-09-06 00:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5a0ff625-5869-3f9c-9639-72a945fcfefe | -4.5029 | -42.9089 | 2025-09-06 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 648032f1-f6d4-32b4-8b7d-5e2c3859f7e4 | -3.2516 | -50.8082 | 2025-09-06 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 7353976d-67b9-3473-a5ca-60c173023902 | -5.4917 | -60.138 | 2025-09-06 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c92a2c48-ad40-3809-a8d9-34ef56c5da04 | -12.9665 | -54.8116 | 2025-09-06 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| bb486952-3ba9-34cf-b5ae-29fbbe6cb3bc | -9.7038 | -49.504 | 2025-09-06 00:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 69210adf-4f10-3295-8bff-6ff82600e716 | -10.6128 | -44.3284 | 2025-09-06 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 119ffdc0-99e3-35b4-bf0a-a45e3b15b77b | -12.5224 | -53.8692 | 2025-09-06 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 483e6eb4-9880-3bce-82dc-78d3af68acf4 | -15.7186 | -53.5743 | 2025-09-06 00:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 41f2eb03-1495-3d4e-a85a-1b01965c9265 | -22.2633 | -48.7463 | 2025-09-06 00:20:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.4 |
| 1289d716-2143-366e-b425-da8985979b7d | -13.0047 | -54.8076 | 2025-09-06 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 24ba4b29-851a-38b8-be69-17bcd0c27a74 | -15.4557 | -47.1464 | 2025-09-06 00:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 2e381ccf-8a15-337d-bd76-fe5f0a15f719 | -22.2424 | -48.7513 | 2025-09-06 00:30:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.1 |
| ef102b93-4e5c-3a22-9986-8e5802421f5d | -22.2633 | -48.7463 | 2025-09-06 00:30:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.5 |
| 5204a5e6-0f49-3ed5-9ba2-08b13cdaccdc | -12.5224 | -53.8692 | 2025-09-06 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 405a734a-303d-3f17-9f53-b2f7e412bd92 | -12.5036 | -53.8505 | 2025-09-06 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 8bc93ba7-69fc-37ac-8a63-4572bd97885b | -10.6131 | -44.3051 | 2025-09-06 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 1bf03f79-3b97-3dcf-b5d7-2aa0138a4e46 | -6.5393 | -49.5101 | 2025-09-06 00:30:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 76bf5389-a5dd-3392-9ebd-f2945f532793 | -12.5033 | -53.8712 | 2025-09-06 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| c01705f4-7873-3c53-b2fa-c4efc3006224 | -4.5031 | -42.8854 | 2025-09-06 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 170.6 |
| ebad812b-86e0-3591-8166-e737f465ce39 | -12.9665 | -54.8116 | 2025-09-06 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 3700f53a-a2ef-39f8-bd38-8611c79360db | -6.8095 | -52.8154 | 2025-09-06 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 07fab578-5d3b-3983-acaf-5ceb9ac9c4dd | -13.0044 | -54.8282 | 2025-09-06 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 5584a0b5-279b-3d35-bb19-68ccf4118e6e | -15.7186 | -53.5743 | 2025-09-06 00:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 1d8ff135-290a-3d8b-b2fb-7d1fc0a28429 | -5.4917 | -60.138 | 2025-09-06 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 08da59cb-09c0-3f54-9962-7c124f31e34c | -4.5033 | -42.862 | 2025-09-06 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 4746cc1f-c0c3-35b3-9e5c-e1392a1fad98 | -3.2516 | -50.8082 | 2025-09-06 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 833865cb-b358-31d6-a73a-eec4b4777483 | -10.5937 | -44.331 | 2025-09-06 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 664e15aa-8397-3a93-a427-91b38d8ac659 | -9.7227 | -49.5021 | 2025-09-06 00:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 0e749e7a-8093-3e3f-a464-82e14f1f3605 | -9.6877 | -49.2902 | 2025-09-06 00:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 74989975-1fbd-3cf2-87bb-5ab1cfc43b62 | -10.6128 | -44.3284 | 2025-09-06 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 231.6 |
| 2b5f8995-d138-37bc-b14e-38d924190846 | -12.4843 | -53.8732 | 2025-09-06 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ddcf37df-c341-3214-9365-401ca5fe2095 | -13.0047 | -54.8076 | 2025-09-06 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a0c467ce-5f37-32ea-8ca1-0d7ea809fc04 | -12.4846 | -53.8525 | 2025-09-06 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 18834786-7f61-3f12-896e-d465364a4929 | -9.723 | -49.4806 | 2025-09-06 00:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 2a6fe3cd-c99c-35c8-aeaa-1f84f05a7b9c | -9.7041 | -49.4825 | 2025-09-06 00:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 221.0 |
| 222aef2a-ac23-38e0-b458-d95d7767df2d | -12.5227 | -53.8485 | 2025-09-06 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 2d29207e-096c-33ee-81fe-f59287738a4d | -4.4844 | -42.8866 | 2025-09-06 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 8ca417bd-7f31-3a37-9973-169b1d7fda35 | -9.7038 | -49.504 | 2025-09-06 00:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| ea1ab56c-ce12-3bf0-8028-fcc0c1c11cad | -13.0235 | -54.8262 | 2025-09-06 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 4078a64d-2d05-3a5b-9d6e-826768992493 | -3.2331 | -50.8087 | 2025-09-06 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 3f85ba0c-ad06-3f89-b851-89af2ee01060 | -9.5347 | -40.3033 | 2025-09-06 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.3 |
| a1235faa-ce90-32ac-823d-9e9d3a6dac69 | -4.4844 | -42.8866 | 2025-09-06 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 80914ff6-9a05-3ca2-a1e5-438f333945a4 | -9.7041 | -49.4825 | 2025-09-06 00:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 5fc1aaf3-01ec-3223-ad07-cbeefa971e83 | -15.7186 | -53.5743 | 2025-09-06 00:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 28e3b6fc-4d28-324f-847d-0cc936b93a2a | -12.5227 | -53.8485 | 2025-09-06 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 17fad2e7-45cf-319e-845e-b379d375e0a8 | -6.5393 | -49.5101 | 2025-09-06 00:40:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d9a4c11a-08ea-308e-aebf-6133e7aef7ff | -4.5029 | -42.9089 | 2025-09-06 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 059a051b-f3f6-3f38-84b6-225aa5fa2a16 | -9.5343 | -40.3282 | 2025-09-06 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 107.8 |
| e51ef331-e7e6-3438-aed0-369d59b565f6 | -5.8717 | -51.7353 | 2025-09-06 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6f2090c8-21a2-3b6e-8190-04d0d9f04846 | -4.5218 | -42.8843 | 2025-09-06 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 90263d23-7a1d-3eb4-8ade-9de565e4eec4 | -9.7038 | -49.504 | 2025-09-06 00:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 7da11713-fdfb-38c9-b582-e6fc9e8c5f62 | -22.2626 | -48.7697 | 2025-09-06 00:40:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.2 |
| 43fcf69c-59dc-395c-b723-06bf22d57d49 | -15.5747 | -52.9175 | 2025-09-06 00:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 906aef53-6b14-30ee-b88b-8dd6af5851a3 | -10.5937 | -44.331 | 2025-09-06 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 829ffed0-401a-37b8-b79f-97ef5832181d | -10.6128 | -44.3284 | 2025-09-06 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 171.5 |
| dabac164-d85c-37d3-9028-82c56fc60dde | -12.5033 | -53.8712 | 2025-09-06 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 21818307-1a19-305f-ae19-2a7d13b9fd25 | -4.5033 | -42.862 | 2025-09-06 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 151cbe53-f6ef-31ee-9a96-ab8f180bf5be | -22.2633 | -48.7463 | 2025-09-06 00:40:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 291.4 |
| 98efbd95-1321-3f53-bb69-87d330835420 | -12.9665 | -54.8116 | 2025-09-06 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a1bde714-c719-3cec-8744-63955906ce75 | -5.8718 | -51.7145 | 2025-09-06 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| c550df8c-4c08-31f6-98e5-6adf93c39892 | -22.264 | -48.7228 | 2025-09-06 00:40:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.8 |
| 44e74b48-1fdf-34b6-a776-26e768764c7b | -3.2516 | -50.8082 | 2025-09-06 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 366540c6-cc0f-3cda-a637-c871aa6c26ae | -15.7381 | -53.5717 | 2025-09-06 00:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 13fafe66-302f-3155-8900-cc23b32a101b | -13.0044 | -54.8282 | 2025-09-06 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 5da24ee7-8c5f-30e9-917a-1dac7bbeb653 | -4.5031 | -42.8854 | 2025-09-06 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 620.6 |
| 99cc0301-cdd0-35ef-af65-47aa2ed286fa | -22.2424 | -48.7513 | 2025-09-06 00:40:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 195.6 |
| f114469b-85a2-39cc-a799-9ce845a596ca | -5.4917 | -60.138 | 2025-09-06 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0a3d3655-3118-3102-b932-380df617571d | -9.723 | -49.4806 | 2025-09-06 00:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 0301e7c8-05ef-3c52-94d8-5eea73eeaf1a | -14.9015 | -49.454 | 2025-09-06 00:40:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 01593a7f-1add-31e2-8296-072b698c7c5d | -15.5942 | -52.9149 | 2025-09-06 00:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d709deb1-65ad-37e4-9fc1-30edfd4dde9f | -12.4843 | -53.8732 | 2025-09-06 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 9da86a12-6bfb-3960-887a-4a1f509275e2 | -12.5036 | -53.8505 | 2025-09-06 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 13d6bc67-3955-3e77-a739-0b1d195f6924 | -10.6131 | -44.3051 | 2025-09-06 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 9d62958e-6169-3cc4-8b23-eb978f22a464 | -12.4846 | -53.8525 | 2025-09-06 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 91022b80-09d5-347b-aa22-72d63a7e15f9 | -22.264 | -48.7228 | 2025-09-06 00:50:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |
| 78671f31-5760-358e-9ccb-ad022f2f299d | -9.7038 | -49.504 | 2025-09-06 00:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 28d94a0a-8fcc-3380-81ba-f0576973c3af | -4.522 | -42.8608 | 2025-09-06 00:50:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 43.6 |
| e0caf516-7143-3e1d-a242-8e64ef1c3dcc | -4.5218 | -42.8843 | 2025-09-06 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b2bf0ad8-4963-3f24-a381-2592bb2f29a5 | -22.2633 | -48.7463 | 2025-09-06 00:50:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 291.3 |
| d0016d3f-4775-304f-8a8e-762fde0eaa9e | -15.5938 | -52.9361 | 2025-09-06 00:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 18799b24-367a-3814-a557-4d7190adc22d | -12.4843 | -53.8732 | 2025-09-06 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e5d9acf1-7ee3-39eb-a2a9-c116d3cd4912 | -9.723 | -49.4806 | 2025-09-06 00:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 2dd79df5-a45f-3228-95d3-5e3e30b533ef | -12.5227 | -53.8485 | 2025-09-06 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 759c1d8f-8ad9-3fbc-9f9b-749c57931800 | -12.4846 | -53.8525 | 2025-09-06 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 36dd1c70-04e2-3d4d-9b81-2f381c20ccd7 | -13.0044 | -54.8282 | 2025-09-06 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 5d84ee67-cbf1-309b-ab4f-04bef44a7ef5 | -12.5033 | -53.8712 | 2025-09-06 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| f98f03e5-95ca-3720-ab90-5e7bbeb40460 | -22.2417 | -48.7748 | 2025-09-06 00:50:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.8 |
| 1a04bd39-71e2-319f-a64f-285ab968d7e9 | -12.5036 | -53.8505 | 2025-09-06 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 9b0cd982-12fe-3607-aacf-215f549a2065 | -4.5033 | -42.862 | 2025-09-06 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| da9c9995-8420-3f5b-9fa3-dc8c1c97cd60 | -15.5942 | -52.9149 | 2025-09-06 00:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 200.8 |
| f57e5af3-01b1-3af4-a9d1-9f2aca0ba237 | -5.4917 | -60.138 | 2025-09-06 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 1690c8b6-695a-32c4-b410-f07ab261cab1 | -10.5937 | -44.331 | 2025-09-06 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 8408db38-102d-3b2f-9e41-8a6e6db748a1 | -22.2626 | -48.7697 | 2025-09-06 00:50:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.9 |
| e794f87b-c2f4-3e09-9300-89694c1e0dfe | -15.7186 | -53.5743 | 2025-09-06 00:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 53fa9a3b-3df0-3406-afe8-98f4ca32d1f7 | -4.5029 | -42.9089 | 2025-09-06 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |


[Clique aqui para ver as próximas entradas](README9.md)
