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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50a23847-3878-3828-ab42-a679b571bd36 | -14.5067 | -48.8085 | 2025-09-08 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 143.0 |
| e6f76e35-a6f3-3df9-b6bc-71a5504f21c4 | -12.6343 | -56.9725 | 2025-09-08 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 35fc9ec1-7f61-3e75-9aca-1cbab63c8f6f | -9.4345 | -61.8156 | 2025-09-08 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 75a863e9-2cd6-3c88-95a7-b75f1dc99ad3 | -9.4531 | -61.8147 | 2025-09-08 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e1314600-2ae9-39cf-9d28-8943b9f5ef15 | -22.3395 | -51.9287 | 2025-09-08 01:50:00 | GOES-19 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.2 |
| d2700650-d4e4-37dc-8e9a-32f3a2dbcfdb | -8.6219 | -40.2058 | 2025-09-08 01:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 11a4c8d9-e465-300e-9950-4f78d0af55fd | -14.5266 | -48.7833 | 2025-09-08 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 1a3e613f-589b-3464-a6de-b767e5cc6dda | -12.6151 | -56.9943 | 2025-09-08 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 71d7a952-3081-30fe-a6af-89163c189361 | -9.481 | -60.4902 | 2025-09-08 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| cb36e9e4-c0ed-3ffc-80b8-d0df2f38d2a7 | -7.3984 | -61.6156 | 2025-09-08 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 2a0d8dda-1ce8-3d63-ac50-215f3a8d381d | -20.9259 | -45.2635 | 2025-09-08 01:50:00 | GOES-19 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| b2e2fa56-e53a-3423-b543-ab50dc562ba1 | -17.1564 | -44.4266 | 2025-09-08 01:50:00 | GOES-19 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 8a0739c5-dfcc-32e8-a3fc-87f691323f0d | -11.3745 | -50.3997 | 2025-09-08 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e4c3ceb2-03af-367c-9080-bf55ded497cd | -12.6153 | -56.9742 | 2025-09-08 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 5c305758-9e2a-36db-970c-e8fdb23aed82 | -7.4168 | -61.6339 | 2025-09-08 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 119.6 |
| c11418c1-f891-3cc8-842f-fbf04d77a3b3 | -5.8791 | -43.9769 | 2025-09-08 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 064016ad-852c-38ef-8aaf-8dcd34b0e4fb | -11.2007 | -54.9992 | 2025-09-08 01:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 672bf3eb-4f90-3213-b08a-3bb8bf5b23b4 | -14.5072 | -48.7863 | 2025-09-08 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| a85e9449-27cc-3451-a5d4-43556b1a81ae | -12.9474 | -54.8135 | 2025-09-08 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 5df97c88-f439-3666-83a3-3fbd9e7d97d8 | -11.2005 | -55.0195 | 2025-09-08 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0e784e30-71ca-35f2-8b95-eea4d194b869 | -14.527 | -48.7611 | 2025-09-08 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 970c49b7-a56b-340d-9388-d10b9d25f5ef | -14.5067 | -48.8085 | 2025-09-08 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 7c03fc87-1d68-37fc-a52a-c4bc87f4ecba | -12.6151 | -56.9943 | 2025-09-08 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e61218e6-3636-34c7-828a-53e4e6445469 | -7.3984 | -61.6156 | 2025-09-08 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 7e34bc51-7792-3fd8-bf54-c89ef3f4539d | -7.4168 | -61.6339 | 2025-09-08 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| ad315f04-3a76-3cb1-8db5-12e96f6dd2c7 | -9.4345 | -61.8156 | 2025-09-08 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 638202f9-360c-3106-b0e2-aed78a0c5617 | -9.481 | -60.4902 | 2025-09-08 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 32a2fb03-a459-3460-b058-39bbe757a0dd | -9.4531 | -61.8147 | 2025-09-08 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| fb46e7f0-e22f-3872-91ee-9ed625cd3f3e | -14.5266 | -48.7833 | 2025-09-08 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| fbefdae6-067f-38bc-8d38-6c44c2cc2bc2 | -11.3745 | -50.3997 | 2025-09-08 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| e1b46b49-b95f-310e-88ac-a5bbdb8eaef1 | -6.4605 | -43.9532 | 2025-09-08 02:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| afda1679-ad10-37b1-85d0-1e30f1d3f1c5 | -12.6343 | -56.9725 | 2025-09-08 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| f619d5a2-f865-3ea1-832c-21cf23e3f93e | -17.1564 | -44.4266 | 2025-09-08 02:00:00 | GOES-19 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 135.1 |
| f9627768-eb9e-3030-9f7b-4aa1007bdeb3 | -7.4169 | -61.6149 | 2025-09-08 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f6caf345-457c-3c71-81b1-1c5ffc81eaba | -11.2007 | -54.9992 | 2025-09-08 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 91eef0bf-720a-3a68-9e43-11116db6dc1e | -3.316 | -48.7134 | 2025-09-08 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| bec1e915-29c7-330f-ace3-9aaa1c23689e | -14.5072 | -48.7863 | 2025-09-08 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d94571a7-03c5-338c-a141-6d5633dc83e3 | -7.3983 | -61.6346 | 2025-09-08 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 181.9 |
| 49e37423-c3d7-30ab-9078-8d732cdfd555 | -12.6153 | -56.9742 | 2025-09-08 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 27c87115-5b78-37ed-b0e6-9e1c002f24e7 | -11.3748 | -50.3783 | 2025-09-08 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6842222b-aefc-36ef-a8ec-f3837cd144ce | -11.3742 | -50.4212 | 2025-09-08 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c3c1c8dd-79c8-3e63-8fbe-8489f74789be | -12.9477 | -54.793 | 2025-09-08 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 9ab34e1e-16d9-3ffc-9378-04ad86c082bf | -12.6341 | -56.9926 | 2025-09-08 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 948c7014-ee0a-319b-b84f-74d9813dd789 | -3.316 | -48.7134 | 2025-09-08 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 52015648-8839-3fb9-a5cd-95fa2a377493 | -12.6151 | -56.9943 | 2025-09-08 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 501cf4ea-e87f-3100-bf91-6a1512cf778a | -14.5067 | -48.8085 | 2025-09-08 02:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 7ad5bc9d-8224-3b6e-bfff-8e14ff48c00f | -7.3984 | -61.6156 | 2025-09-08 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 9b9b5f81-3261-3f24-8e76-a8dbe70f8b25 | -11.3745 | -50.3997 | 2025-09-08 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| e392cda9-db6c-30e1-91d6-8398f3fa3d2a | -9.481 | -60.4902 | 2025-09-08 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 487522f9-9f2e-307b-894b-80f6f089ab5b | -9.4531 | -61.8147 | 2025-09-08 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 735232c0-b03b-3636-8484-1c1601ca21e4 | -12.6153 | -56.9742 | 2025-09-08 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 5a875f7e-a297-3a99-90b6-a641c94dd45f | -12.6343 | -56.9725 | 2025-09-08 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 87fe0b12-eb66-305a-b0b3-91c5779bf2f4 | -11.2005 | -55.0195 | 2025-09-08 02:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 1fec2047-499d-3a26-93c4-ba247b12d534 | -17.1564 | -44.4266 | 2025-09-08 02:10:00 | GOES-19 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 9b9ece47-0629-3a8c-bcea-8ae4e831f2f7 | -7.3983 | -61.6346 | 2025-09-08 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 163.4 |
| c2da4881-465a-3d26-ae1f-40f581a32d3c | -14.5266 | -48.7833 | 2025-09-08 02:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 5dc6be18-0061-3177-b67f-73510e99bc46 | -6.4605 | -43.9532 | 2025-09-08 02:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 40e3763c-4cd2-3255-a1f1-7306fc7fe146 | -12.6341 | -56.9926 | 2025-09-08 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| a5d8b609-15cf-3f64-98f8-fdba16165569 | -4.9013 | -42.2226 | 2025-09-08 02:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 54.5 |
| 9bc19e22-92c5-3f8c-9842-e2fb874fcef2 | -12.9477 | -54.793 | 2025-09-08 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 797a65b0-2368-39e7-a042-fddfad26d1d5 | -5.8791 | -43.9769 | 2025-09-08 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 04c029d1-ef31-360b-a566-73f6012e9bc3 | -11.3748 | -50.3783 | 2025-09-08 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 978d3779-cbf8-35b0-a5a3-a920ae49bc95 | -11.2007 | -54.9992 | 2025-09-08 02:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| ed8d8851-0396-34a3-8531-9b4c6eb2cf28 | -14.5072 | -48.7863 | 2025-09-08 02:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9b37d62f-7a20-394c-bc02-2164b4670c9f | -9.4345 | -61.8156 | 2025-09-08 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ff6c1e65-19a0-35ba-ae9c-10d3cc062e85 | -11.3742 | -50.4212 | 2025-09-08 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f59e5cf6-6d11-3658-a42a-e1aed565f234 | -7.4168 | -61.6339 | 2025-09-08 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 4b4fef10-3b38-3a22-9768-93e3e6c94d5a | -12.6153 | -56.9742 | 2025-09-08 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 0d000999-c1e3-3f4b-be4c-4c1788a51fdf | -12.6343 | -56.9725 | 2025-09-08 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 4a11c057-223d-38a8-9a23-eeaa5c424928 | -7.4168 | -61.6339 | 2025-09-08 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| d68a5e3d-bdf1-3345-9687-bb89c94c2a87 | -9.4345 | -61.8156 | 2025-09-08 02:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 5b3e5f4a-1f38-3ef7-9e79-67a172d7f875 | -12.6151 | -56.9943 | 2025-09-08 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| aaf47cc0-bfe6-3052-8e3f-6dd0ff41befc | -7.3984 | -61.6156 | 2025-09-08 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9b05a0c9-9ca1-33b5-b525-dba6843f515b | -11.2005 | -55.0195 | 2025-09-08 02:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2d80d841-a350-33a6-bdda-81a53d6a170d | -12.9477 | -54.793 | 2025-09-08 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 8d154f80-2f2d-3e78-b2f4-4ef2c7d7ac1b | -11.3742 | -50.4212 | 2025-09-08 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 41277755-7485-3170-8072-b966e9abacd7 | -14.5266 | -48.7833 | 2025-09-08 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 6ec2bce7-5a90-3706-bd20-4ed5369129ef | -3.316 | -48.7134 | 2025-09-08 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| f40d5271-12ad-3f5d-9654-e28d670f91df | -5.8791 | -43.9769 | 2025-09-08 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e1d5d431-c2f1-376e-b377-2eee18db0d62 | -7.3983 | -61.6346 | 2025-09-08 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 143.8 |
| a9e032f3-873a-344f-8949-a4bb1593731e | -9.481 | -60.4902 | 2025-09-08 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9b569a79-5e7d-3189-aca3-39f8a13fa002 | -14.5072 | -48.7863 | 2025-09-08 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 2c42723b-b210-32a4-9ce2-291876e07b49 | -14.5067 | -48.8085 | 2025-09-08 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 8b26acb5-1c7f-3b9f-bc60-0d8d5c8c8d9e | -17.5532 | -43.7332 | 2025-09-08 02:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 0348da82-e72d-34c4-b18b-e34e8e01b423 | -11.3745 | -50.3997 | 2025-09-08 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| e8a9eaae-48b7-3c4d-890b-82f328a3ddde | -11.2007 | -54.9992 | 2025-09-08 02:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 703decf9-afdd-32a8-a52b-f3eda7afe6de | -9.4531 | -61.8147 | 2025-09-08 02:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a832925c-ffff-3491-a1cf-06121fec6aa3 | -12.9477 | -54.793 | 2025-09-08 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ff09834a-09b5-3098-b70c-f045e08eda84 | -11.2007 | -54.9992 | 2025-09-08 02:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 865c5812-e137-36aa-891e-a3197e9feda4 | -11.4268 | -43.649 | 2025-09-08 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 5d1c6b71-f168-3354-8fc0-e5832f3bc13a | -14.5266 | -48.7833 | 2025-09-08 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| deaee0a9-8929-310e-80e2-fda19d9a7fa4 | -9.4345 | -61.8156 | 2025-09-08 02:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| cb8e3732-e66f-370a-9f98-7e4d63fa5183 | -9.5478 | -59.0727 | 2025-09-08 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b4916757-e538-35ac-ad4d-16685b535a78 | -14.5072 | -48.7863 | 2025-09-08 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| e1b6e6c3-2920-335e-99e4-54850467117a | -14.5067 | -48.8085 | 2025-09-08 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 62e44a6c-4062-39ab-9337-3eb65bed35d0 | -12.6153 | -56.9742 | 2025-09-08 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 4897bb05-025f-3eb0-946d-b656fd2b3c58 | -14.5262 | -48.8055 | 2025-09-08 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 4d8b85d9-1f22-3a89-bc9e-1467c3d89899 | -5.8793 | -43.9538 | 2025-09-08 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5cff5d4f-9ca3-30b3-9181-2f3e4a5d95a4 | -7.3983 | -61.6346 | 2025-09-08 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 148.5 |
| d9ca2b2c-5b69-3a84-aafd-d8025cabc70a | -12.6343 | -56.9725 | 2025-09-08 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |


[Clique aqui para ver as próximas entradas](README17.md)
