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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0665fd1e-ace3-311b-9b85-40ef30c01bbf | -2.92133 | -54.57642 | 2024-12-20 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 447cb219-dc43-3c58-a4fb-71b1e86f1861 | -9.45159 | -62.04988 | 2024-12-20 05:29:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3a1f2cc-209f-3acd-a7cc-f8004dce0d90 | -2.90661 | -54.49515 | 2024-12-20 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee62ff17-ed4b-362a-8270-7bd2a146eec9 | 0.8767 | -59.60738 | 2024-12-20 05:29:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 764e2e25-d92a-3f6a-acbb-57d830784f4b | -2.76371 | -47.39071 | 2024-12-20 05:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2efa72dd-985d-3cfc-a38c-3ad83e25f6f3 | -9.44769 | -62.05291 | 2024-12-20 05:29:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fca2f5a9-2194-3c03-a0d6-d7a856ebe552 | -2.50992 | -48.05927 | 2024-12-20 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac739a37-ba51-3353-a4f8-e165bb393211 | -1.25789 | -53.4815 | 2024-12-20 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06d4df86-f5a9-3c24-b1d8-099ef47c9775 | -1.25149 | -53.52354 | 2024-12-20 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0030c2d-3b3f-3f46-be7a-5ef565115aae | -1.25304 | -53.48095 | 2024-12-20 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91123b93-7d9e-3187-809e-b404b8a9d74d | -3.50139 | -53.95808 | 2024-12-20 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac80c5aa-ba9a-388f-b46f-6e15f7adc6f4 | 0.88004 | -59.60685 | 2024-12-20 05:29:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d3f4aa91-5ee9-31d5-a0f8-820549ad7146 | -9.45104 | -62.05344 | 2024-12-20 05:29:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d0b1d02-642f-3d31-a687-b903afc79349 | -2.7659 | -47.38554 | 2024-12-20 05:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe451774-22d0-3b7c-bf4c-e4544971cbff | -2.90198 | -54.49454 | 2024-12-20 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c902652f-73dc-396d-96c4-0e9b59d0655f | -2.58421 | -51.92226 | 2024-12-20 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9094fc9-4310-3ee5-9fc9-d2be602624cf | -1.28328 | -53.18213 | 2024-12-20 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23a9b1d2-a7fa-3e0e-9049-b3b7dbe0e849 | -2.46144 | -51.83909 | 2024-12-20 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8508868f-c3d7-36c4-b562-8d7502b6ef32 | -2.77098 | -47.39179 | 2024-12-20 05:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99505076-2878-335e-a7c1-c4ddec78c855 | -9.44715 | -62.05646 | 2024-12-20 05:29:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7d6dceb-a866-3a75-82d2-6bd92fa9c724 | -1.25632 | -53.52418 | 2024-12-20 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2c2b6f0-9670-328b-9f4d-0bf415e97d47 | -2.76485 | -47.39289 | 2024-12-20 05:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bab83999-8049-356f-95c6-89558f08b24d | 0.8288 | -60.27338 | 2024-12-20 05:29:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f88e8f29-50c2-34a7-b8be-88998a6331bf | -2.92203 | -54.57172 | 2024-12-20 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d382bc0c-b1bb-3be2-901b-f82490d5721d | -2.23664 | -53.74629 | 2024-12-20 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de00bc14-b8a9-3df8-b81e-59c7cefad975 | -2.50799 | -48.06487 | 2024-12-20 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c72539e2-764c-3ea3-9dee-71a89d7550e5 | -11.94148 | -63.17226 | 2024-12-20 05:31:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9bb52b6-334d-3a87-905a-9c15998bdd8d | -12.18604 | -64.06298 | 2024-12-20 05:31:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aaf77a4-0e33-33f5-9960-fba8f6b1e886 | -11.90495 | -63.93735 | 2024-12-20 05:31:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23554074-9005-3619-9153-092269d10b62 | -14.52723 | -59.97011 | 2024-12-20 05:31:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3510617a-8da8-3845-b4e8-dba3341ff8d5 | -11.972 | -63.18771 | 2024-12-20 05:31:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0725bb52-672e-3466-b4b8-5112787c8675 | -12.18327 | -64.05888 | 2024-12-20 05:31:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c89066e-f940-3e33-9569-de1934c5dd72 | -11.99377 | -57.20301 | 2024-12-20 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91658124-fa5e-363f-b76b-1ed0f4d9cffc | -12.30696 | -64.21826 | 2024-12-20 05:31:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63c83220-e362-3bf5-8283-1f54f3bc35d3 | -12.30362 | -64.2177 | 2024-12-20 05:31:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e09748f9-65fb-3dc9-b696-fcbea373273b | -12.18271 | -64.06243 | 2024-12-20 05:31:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b7c5bfc-8f7a-3583-89c1-a9d202031d52 | -11.93815 | -63.17173 | 2024-12-20 05:31:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc7e9ed1-cadf-35e3-be0b-c8f82ec7c876 | -11.97255 | -63.18417 | 2024-12-20 05:31:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f6a3bb99-a24a-3b9d-9e3b-a1674ce7dbe4 | -12.18356 | -64.06422 | 2024-12-20 05:54:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c495e2e2-279c-3c86-9409-60143ab3f94e | -12.18408 | -64.06037 | 2024-12-20 05:54:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b71b48eb-34bd-380f-a865-ad5cd7fe353a | -11.88684 | -63.74376 | 2024-12-20 05:54:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e84f7e84-4b00-369a-b58f-f34365234943 | -12.33281 | -64.23939 | 2024-12-20 05:54:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49e71c53-c83d-34ab-90f9-b8c8c09e3302 | -11.94067 | -63.17388 | 2024-12-20 05:54:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37e4c0a7-0cf2-35cf-b8f4-97bf660f5c8c | -12.30399 | -64.21725 | 2024-12-20 05:54:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a218e41d-c7c3-3fa0-bf08-8c5c40b362f8 | -15.07842 | -59.63419 | 2024-12-20 05:54:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3351282a-f402-3495-a708-048a233f0070 | -15.07796 | -59.63842 | 2024-12-20 05:54:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d643905-616e-3381-940e-8f2387c23b5a | -12.18073 | -64.05643 | 2024-12-20 06:33:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2be86050-d1e2-3e9a-bcfc-944505d24946 | -3.94 | -43.2447 | 2024-12-20 07:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| df518b25-a617-3718-8cee-6cf5cd625d95 | -3.9587 | -43.2438 | 2024-12-20 07:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 06b7d2ee-4653-3e1c-bbb7-d4002274cb25 | -3.2321 | -46.7836 | 2024-12-20 07:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d89fb518-e586-3f0f-8d6c-6d4e554a96d7 | -3.9587 | -43.2438 | 2024-12-20 07:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 29ff093c-dcca-3b46-bf34-eb69798fb060 | -3.232 | -46.8056 | 2024-12-20 07:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5e35749b-8a0d-3000-ba7a-56dbdb220387 | -3.9587 | -43.2438 | 2024-12-20 07:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 5c2fb928-c924-3b65-ae0f-417348f9f55b | -2.7207 | -44.8366 | 2024-12-20 07:50:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 9255e118-2d78-344b-a7ef-c864e085bbb0 | -2.7206 | -44.8592 | 2024-12-20 07:50:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 36.2 |
| e5530dec-ed01-329d-bbda-645e747f2233 | -2.83943 | -42.1288 | 2024-12-20 12:25:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 90e40fe2-844d-3662-acf0-58cc339e4fb5 | -1.92928 | -46.44928 | 2024-12-20 12:25:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 80af2de3-f955-3c3a-a46c-3e457724c5b7 | -2.86636 | -42.06797 | 2024-12-20 12:25:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ae04a7d9-7446-32ec-b2e1-6ac70c7abb5a | -2.72649 | -42.52639 | 2024-12-20 12:25:00 | TERRA_M-T | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 552e7510-9500-3a02-9842-69e7280838c8 | -0.92603 | -47.61004 | 2024-12-20 12:25:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 4448beed-0e12-3409-a49e-f38982c1ada3 | -2.92714 | -41.19051 | 2024-12-20 12:25:00 | TERRA_M-T | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 2b86b5b8-534d-3659-877f-78c31e41e2dd | -2.83814 | -42.13783 | 2024-12-20 12:25:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 5de7d78e-2631-3260-b565-5cbb57e054ce | -2.92853 | -41.18074 | 2024-12-20 12:25:00 | TERRA_M-T | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 81d4786c-217b-39eb-901c-297b45eb8c54 | -3.0375 | -39.76501 | 2024-12-20 12:25:00 | TERRA_M-T | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 59b224b2-811e-3c8a-8d2e-0b45e5b5e0be | -3.95576 | -38.28989 | 2024-12-20 12:27:00 | TERRA_M-T | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 8532f730-5e74-3e99-a567-927a3c64603b | -3.92095 | -40.54165 | 2024-12-20 12:27:00 | TERRA_M-T | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| fefe7c88-5e35-38e9-9eb1-e8c654c4a2bd | -5.00049 | -43.84683 | 2024-12-20 12:27:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dbbd73d1-aea2-3d67-9b0f-b40a8571ab30 | -5.05684 | -42.93994 | 2024-12-20 12:27:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 1c8693ee-d7f5-3fa6-b75c-26a0d7bfc133 | -4.39851 | -43.85346 | 2024-12-20 12:27:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d6f4d8fd-f9c9-3626-bd5f-957ea8a5a9a8 | -4.52026 | -44.09956 | 2024-12-20 12:27:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6c928771-a119-386b-bdd9-37a2869b1295 | -5.00712 | -39.17265 | 2024-12-20 12:27:00 | TERRA_M-T | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 2f59ce75-2cd7-3d23-8c8e-43a0d3941f5e | -3.60972 | -40.48809 | 2024-12-20 12:27:00 | TERRA_M-T | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 43e72b4b-ddfa-397d-ae20-8a495de8e097 | -4.12019 | -43.55317 | 2024-12-20 12:27:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 12241d39-65e2-3825-9975-86b5735ef9dd | -3.317 | -41.81852 | 2024-12-20 12:27:00 | TERRA_M-T | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| c00d1d32-c3a8-35d7-a20b-b55945308ab3 | -3.65319 | -42.30714 | 2024-12-20 12:27:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 70780862-6fe4-3dcc-8a64-bd45a08317af | -3.0094 | -41.52147 | 2024-12-20 12:27:00 | TERRA_M-T | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| c24b1061-3bcb-3cb0-b864-c355905fc406 | -4.42456 | -44.69175 | 2024-12-20 12:27:00 | TERRA_M-T | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 41609693-8d55-31fe-ab93-2f7665a8c0c5 | -3.46341 | -40.72952 | 2024-12-20 12:27:00 | TERRA_M-T | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| b14dd485-548e-365a-88f2-cd49d6dbc37e | -4.75845 | -38.54759 | 2024-12-20 12:27:00 | TERRA_M-T | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 81df68c7-6e56-3f43-a7ea-33759b8cf52c | -4.04337 | -43.24343 | 2024-12-20 12:27:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f4da2482-0fe3-31aa-a083-9c893d2e4bed | -4.53685 | -44.04766 | 2024-12-20 12:27:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 16a51c68-41ba-3ddc-a4d7-3ee7fe15f6e0 | -4.3473 | -43.5079 | 2024-12-20 12:27:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2a292571-09e3-30da-9243-12e99a0fb1f1 | -10.05535 | -37.829 | 2024-12-20 12:27:00 | TERRA_M-T | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 38b4762c-5da8-3ac8-8ac7-d15a60d8d7a9 | -10.46675 | -42.61349 | 2024-12-20 12:27:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 61e5fd5b-2bce-3edf-b600-ac0863a58f92 | -6.85418 | -35.22499 | 2024-12-20 12:27:00 | TERRA_M-T | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 38.2 |
| ef2ef87b-4b4a-39c5-ab2e-0d3d7e7b3bef | -7.86078 | -42.93424 | 2024-12-20 12:27:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 56f58152-324c-3a31-bd97-fb05c489ea6d | -3.95789 | -38.27423 | 2024-12-20 12:27:00 | TERRA_M-T | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 6cde0095-ac12-3694-8256-e45d7695c9db | -3.23097 | -46.79641 | 2024-12-20 12:27:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a90af915-f6a8-36e6-a721-f4a63bda799d | -5.39445 | -43.61303 | 2024-12-20 12:27:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ea2281e8-8776-3162-9d2e-89e2e789b9da | -5.65203 | -43.3559 | 2024-12-20 12:27:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 318713dc-26f2-33fe-8f09-2ad62532c204 | -4.67817 | -44.4073 | 2024-12-20 12:27:00 | TERRA_M-T | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 16081dfb-9f98-388e-8abf-0986cd3d8be6 | -5.81093 | -37.0449 | 2024-12-20 12:27:00 | TERRA_M-T | PARAÚ | RIO GRANDE DO NORTE | Brasil | 2408706 | 24 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 0ee99397-1b89-3d8f-b9b3-dc2ac062818c | -4.42322 | -44.70088 | 2024-12-20 12:27:00 | TERRA_M-T | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 5ce645fb-a4cf-3417-b041-3f4548a9298b | -2.75695 | -43.71782 | 2024-12-20 12:27:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 85a87a93-377a-3242-a3ff-9bca052d09fe | -3.86687 | -43.06287 | 2024-12-20 12:27:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8adf5070-097a-3ca0-ac54-2a298a78228f | -3.84148 | -41.56244 | 2024-12-20 12:27:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| d97ad30b-8a99-38bc-b34d-7e621836ade3 | -16.08758 | -43.61961 | 2024-12-20 12:29:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5108644a-54b3-35a7-80ab-1e5e10377a89 | -12.87897 | -39.69744 | 2024-12-20 12:29:00 | TERRA_M-T | MILAGRES | BAHIA | Brasil | 2921302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 31b675ff-a269-3ab3-bcd5-124b54209095 | -15.08262 | -48.81316 | 2024-12-20 12:29:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 691d02f4-45c2-32ac-b948-f47df1044bc0 | -15.73423 | -46.10814 | 2024-12-20 12:29:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |


[Clique aqui para ver as próximas entradas](README12.md)
