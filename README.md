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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8048014e-bf7c-3719-b40c-14ff3c8ab101 | -5.7941 | -45.104 | 2025-07-15 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 9e928ba0-7c00-3e4b-8a64-f6c73471112c | -11.478 | -45.0868 | 2025-07-15 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 3112716b-ec35-3464-919f-5f4b7945721c | -5.5241 | -43.8878 | 2025-07-15 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 3d8fa063-cffc-3e43-a826-9e574b1dc679 | -6.3879 | -43.7045 | 2025-07-15 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 665af9dc-850c-3987-b7b7-fb03a3e6f5bb | -11.4397 | -45.0923 | 2025-07-15 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| d641294a-96a8-3e36-ab99-ef7569b5f70c | -12.0825 | -43.4753 | 2025-07-15 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| a9511600-5e64-3b1b-a33a-e0e038d2e878 | -11.4592 | -45.0664 | 2025-07-15 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| e82e72a7-9b23-3608-a3cd-5e9fcd5113c4 | -6.7039 | -47.7945 | 2025-07-15 00:10:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 58a17ff3-5d84-365d-a43f-c79aece12a5d | -5.5429 | -43.8864 | 2025-07-15 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 9e54ad48-645e-3876-95a5-4b1b5366305f | -6.7037 | -47.8164 | 2025-07-15 00:10:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 10d3fb3a-d370-34aa-bb55-6f665d8814bb | -11.4393 | -45.1154 | 2025-07-15 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 5d783c90-aee0-31db-abd3-11b460f503d4 | -11.4584 | -45.1126 | 2025-07-15 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 08e76260-f644-3309-a094-427120e45731 | -6.3877 | -43.7277 | 2025-07-15 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| b9f93634-9ca6-3559-abc9-ac869375dbb1 | -5.7754 | -45.1053 | 2025-07-15 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 75b5eea4-6b98-3004-9c05-adf7495bae98 | -11.4588 | -45.0895 | 2025-07-15 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 247.3 |
| c01b6b0f-0063-38e3-8d8f-b2e87fb63856 | -10.5776 | -49.1316 | 2025-07-15 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| a11495e2-329e-3fe9-b99e-0cacd359e6df | -10.5586 | -49.1337 | 2025-07-15 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| f8a11fc1-e01f-34a8-80ff-a9d9fa3dbb6e | -14.4996 | -58.9251 | 2025-07-15 00:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| eb5225c6-c32d-361e-93a5-6d293399bcb7 | -14.5188 | -58.9234 | 2025-07-15 00:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 7f5fbfb1-d644-3c86-83ea-b960041fd05e | -11.4592 | -45.0664 | 2025-07-15 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 9d0690f2-c1f0-32c5-b22a-11dc9c4c0997 | -11.4397 | -45.0923 | 2025-07-15 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d3a587da-7cad-3458-ad00-553c5e20694b | -9.2928 | -63.719 | 2025-07-15 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 94c6d889-94ac-3c5f-a058-6e3c4951fc0c | -5.7754 | -45.1053 | 2025-07-15 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 08e21db1-2a7c-3a38-84ed-589be87d5008 | -12.0825 | -43.4753 | 2025-07-15 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 870ef6d6-0116-3327-8132-ab4a630c2219 | -5.7941 | -45.104 | 2025-07-15 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| a62fd3a6-b08c-3fb0-aaa9-7622c90e2216 | -10.5776 | -49.1316 | 2025-07-15 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 18e4ef81-f280-383f-819e-7ceba8cee8d7 | -5.5429 | -43.8864 | 2025-07-15 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| cd72a0b2-eba8-3c08-8c8a-ac95129d2860 | -6.7039 | -47.7945 | 2025-07-15 00:20:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| bfa57c63-4111-3721-9598-b4859aec9f0f | -11.4584 | -45.1126 | 2025-07-15 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 84e26f13-305d-34ba-8cd1-601f7e29e2bf | -5.5241 | -43.8878 | 2025-07-15 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b01ed1e7-5d8b-3daf-ae77-d9fecbc0332c | -11.4588 | -45.0895 | 2025-07-15 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 254.1 |
| 51fb0dc2-2b3d-3db9-a6bd-3a92f0478d22 | -11.478 | -45.0868 | 2025-07-15 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9526ace5-c57d-3bca-9486-fff761130cdf | -11.4393 | -45.1154 | 2025-07-15 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 2a9de5ad-a4e4-386c-924e-33e90490cb51 | -9.2927 | -63.7379 | 2025-07-15 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 5002b7ef-66d6-34a8-a68c-0a878dafce03 | -10.5586 | -49.1337 | 2025-07-15 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 6c50c4f5-6b35-3420-b331-f0bed034ed71 | -9.2927 | -63.7379 | 2025-07-15 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 2a334067-1316-3363-85b8-1c078d1a8d53 | -11.4397 | -45.0923 | 2025-07-15 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 361f7d71-a708-3974-b630-13a10cae273d | -10.5776 | -49.1316 | 2025-07-15 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| dbf7d2a6-ab08-3594-8e18-06f44e33ed55 | -11.4588 | -45.0895 | 2025-07-15 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 339.0 |
| 1a18556e-d76b-38a5-9d7b-625edb00e6eb | -5.5241 | -43.8878 | 2025-07-15 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 8f9b3539-b576-3771-b73a-9af4370ceef8 | -11.4393 | -45.1154 | 2025-07-15 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 0813ac4b-fe02-34be-9012-b05bac749fba | -9.2928 | -63.719 | 2025-07-15 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 121.7 |
| b5bebf30-cb1f-301c-806b-8a3f70246695 | -11.4592 | -45.0664 | 2025-07-15 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 0162e219-edd5-33f9-ae30-5a9321aebbd2 | -11.478 | -45.0868 | 2025-07-15 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 002b323d-a288-38f3-b1ca-cd91330a99fb | -10.5586 | -49.1337 | 2025-07-15 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| ee59631f-4d1e-37e2-8912-1e9c39ae93d4 | -5.7941 | -45.104 | 2025-07-15 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 7a148c0a-b16e-30c7-bab4-ea08901f50db | -11.4584 | -45.1126 | 2025-07-15 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 69c6252b-ef75-3f15-9d68-492888833dc7 | -5.7754 | -45.1053 | 2025-07-15 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 6d8e3bf2-7832-3e03-9a7b-a1bde50fce1b | -11.4389 | -45.1385 | 2025-07-15 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 7fab0223-8aa8-3bc4-b185-42dcfde97276 | -6.7039 | -47.7945 | 2025-07-15 00:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| b26b45ab-625b-3f88-b644-0a442a4e4ef0 | -5.5429 | -43.8864 | 2025-07-15 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| ecca1e0e-8e8a-311b-a63c-868d21bbf9ff | -23.34076 | -46.13812 | 2025-07-15 00:39:00 | TERRA_M-M | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 40f4be2a-5569-3427-b5c8-de7d75f99e8b | -23.5079 | -47.33387 | 2025-07-15 00:39:00 | TERRA_M-M | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 0ae5c341-b4ee-3184-be03-1d543677fd33 | -11.4588 | -45.0895 | 2025-07-15 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 277.2 |
| 104b6e29-a43f-3f8b-8329-74a7ba53d7d9 | -9.2742 | -63.7197 | 2025-07-15 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e11b9c37-5011-3b26-acc1-f7a53bda9916 | -10.5776 | -49.1316 | 2025-07-15 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| a784fe7c-18f7-33e4-9e63-9015d11f2b93 | -9.3114 | -63.7183 | 2025-07-15 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 426fa07b-26a9-3e1e-9e7b-146a1c0173f0 | -5.5241 | -43.8878 | 2025-07-15 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 24484c37-8540-382a-8845-4d18b30557d5 | -5.7756 | -45.0826 | 2025-07-15 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 06a85adb-819c-3e21-81ea-814c7abea694 | -11.4397 | -45.0923 | 2025-07-15 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 95e1ffba-fd66-3e2f-a472-3f0ecdeeb6ea | -9.2927 | -63.7379 | 2025-07-15 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 435e9205-67c3-3fcd-a9eb-7a5c29b27a6b | -5.7754 | -45.1053 | 2025-07-15 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 16fce701-f2d3-336c-b71b-c00597131fb0 | -5.5429 | -43.8864 | 2025-07-15 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 1659f671-fc30-394b-b330-f9778fd57f5c | -11.4592 | -45.0664 | 2025-07-15 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| e925c1a4-d277-35ef-ac5a-a2d3fd72f1d2 | -11.4393 | -45.1154 | 2025-07-15 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 523ca5a1-f9fd-3ca4-b793-c8e188f85d65 | -10.5586 | -49.1337 | 2025-07-15 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0ca70e90-9225-35ac-86cf-0a9f4e1f4d92 | -11.4584 | -45.1126 | 2025-07-15 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 2d3e7f34-4e81-36bd-8b4f-914fba052e9c | -6.7039 | -47.7945 | 2025-07-15 00:40:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 3cd0e97a-6bd0-3be2-995b-b555ea7c4175 | -11.478 | -45.0868 | 2025-07-15 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 0011592b-d568-3472-98bc-2e9c022b6bb7 | -9.2928 | -63.719 | 2025-07-15 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 225.1 |
| 0fadb132-92c5-3838-816c-b78e95845bae | -22.40143 | -49.79913 | 2025-07-15 00:41:00 | TERRA_M-M | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 506e03a8-f42e-3896-b4fe-707e3123797a | -21.77518 | -52.75209 | 2025-07-15 00:41:00 | TERRA_M-M | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 22.0 |
| c387283a-2ef3-3dde-a7b0-a5ccd7134217 | -23.30688 | -47.40861 | 2025-07-15 00:41:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 880c5ba2-a83d-3fc9-b5a4-ad446f999986 | -21.76358 | -52.75372 | 2025-07-15 00:41:00 | TERRA_M-M | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9057c984-d1d1-328e-a268-e1b2717bd980 | -23.01392 | -50.42081 | 2025-07-15 00:41:00 | TERRA_M-M | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| ce5ce223-8a18-3cdc-81eb-b51d8656b9ae | -23.12528 | -49.99343 | 2025-07-15 00:41:00 | TERRA_M-M | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| fc4ed5fc-29c4-32b7-878d-4d2579f1204a | -23.30819 | -47.41827 | 2025-07-15 00:41:00 | TERRA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 7a5f42d7-8bc3-3217-9ce3-ad05499c7d14 | -21.76541 | -52.77092 | 2025-07-15 00:41:00 | TERRA_M-M | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7d5be33e-d5bc-3c61-8882-f302e2ad59ef | -23.00481 | -50.42846 | 2025-07-15 00:41:00 | TERRA_M-M | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 1f1693b2-525d-3eb0-a711-edd34c8014d1 | -23.12671 | -50.00517 | 2025-07-15 00:41:00 | TERRA_M-M | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| bcd67f0b-fe49-344a-85c6-2a84933e7068 | -21.77704 | -52.76939 | 2025-07-15 00:41:00 | TERRA_M-M | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 9a1ed04b-d5cc-39c3-9d2f-a3d2f0adbff7 | -15.77979 | -48.68618 | 2025-07-15 00:41:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b7fa8050-4bcf-3da5-95a0-e1dc7d1cdfc2 | -23.01485 | -50.42715 | 2025-07-15 00:41:00 | TERRA_M-M | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 261eb3f7-aa47-3f61-9ba6-f9248f9cda15 | -23.01536 | -50.43334 | 2025-07-15 00:41:00 | TERRA_M-M | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| e18e52dd-783d-380c-a3ce-94433c038657 | -11.45121 | -45.08819 | 2025-07-15 00:43:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 236d4d8b-2f75-39b9-8abf-97fafbbadd17 | -11.35619 | -48.73218 | 2025-07-15 00:43:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c32fad1d-3e02-3ad7-813b-6306add6b9ab | -15.0801 | -49.49118 | 2025-07-15 00:43:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 48.2 |
| e393cad3-56e0-389d-9446-0c8ac4fdb22d | -10.57591 | -49.14383 | 2025-07-15 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 00c800a6-6787-3a32-bab8-b3efc95b3f37 | -15.47868 | -50.06047 | 2025-07-15 00:43:00 | TERRA_M-M | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b49162c6-c43c-3b08-8cea-c532e11f3667 | -12.0747 | -43.48018 | 2025-07-15 00:43:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 0f46e78e-77fd-36c8-b614-486b91177e0b | -9.8048 | -47.75316 | 2025-07-15 00:43:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c54ec4ee-982a-3d01-9c44-1f237108fcd1 | -10.28428 | -47.619 | 2025-07-15 00:43:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 293a1540-7a67-3d79-b2eb-39593d3f1f67 | -10.56575 | -49.13607 | 2025-07-15 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1e6e0d5e-8f8c-34ce-a941-4865b746b38b | -10.64143 | -45.21602 | 2025-07-15 00:43:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 975a1159-249d-3abd-8068-aa7a0938746f | -11.46539 | -48.52536 | 2025-07-15 00:43:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3ab6a75f-5341-3141-976c-973cdd5475f9 | -12.40561 | -45.3672 | 2025-07-15 00:43:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 534bab0d-5d60-3465-a17d-98645b28e0b8 | -12.34931 | -49.3092 | 2025-07-15 00:43:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 173f9dd9-6655-3b3d-ab77-4aeedd7591ba | -10.64364 | -45.23025 | 2025-07-15 00:43:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c0353a5c-28b7-3127-8764-78779e65a1ec | -12.0705 | -47.98976 | 2025-07-15 00:43:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| da029e6c-d53b-34ff-bd7c-512591f2f824 | -10.88275 | -54.05575 | 2025-07-15 00:43:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |


[Clique aqui para ver as próximas entradas](README2.md)
