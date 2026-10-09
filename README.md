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
| e16bc17f-cef2-36db-8266-fe3576fa6f74 | -5.9586 | -55.3648 | 2026-10-09 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ef82d576-efb2-32a2-94ce-1d0a8add70d4 | -11.6173 | -43.7142 | 2026-10-09 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 87b1feb8-52f2-3264-b0bd-40fa6097fc6b | -6.7365 | -55.1474 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7688c635-d6c9-3709-abdc-3b5cb4a78b28 | -13.5117 | -44.368 | 2026-10-09 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9aa1cf19-e8c0-3167-8f84-5e8f04c4e3cb | -3.1101 | -54.1661 | 2026-10-09 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 210.8 |
| a7f3d077-50d5-3d3c-b237-788fc9390aee | -7.218 | -55.1617 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 65a80d5d-a41d-3ed3-8c1e-8174d3a325e8 | -4.2767 | -49.1029 | 2026-10-09 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e1fc9bb9-ae6f-39c2-990c-e7b6dadbb293 | -5.6932 | -53.487 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 885ab283-ff1a-3afe-83b5-1c0844bc2e5c | -3.7346 | -59.4577 | 2026-10-09 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| b267103d-283f-3fa3-b162-15e941a64269 | -4.6362 | -50.9646 | 2026-10-09 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 75289db7-9d30-3e0d-a0c4-cec922bd4a6b | -5.7116 | -53.5065 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6259c09a-c45e-3da1-ad8f-0377e3a7d55d | -8.6301 | -66.7886 | 2026-10-09 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| bbb54f81-15e3-3c2b-87f0-31e5efe985a9 | -3.1109 | -53.9249 | 2026-10-09 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 3e89fe7b-5f08-3f56-b0fa-0cee5fcac0f2 | -3.5676 | -54.6946 | 2026-10-09 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 6b5b1a12-ae41-3613-9d86-72bab133a229 | -9.297 | -47.4313 | 2026-10-09 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 2c8eadc9-0d18-3fea-b4c3-be3aaa11311a | -4.5491 | -47.0328 | 2026-10-09 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 140.6 |
| da646cda-8764-34e0-afc3-8e91222a205b | -13.2015 | -54.3757 | 2026-10-09 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| c811a0c5-8906-3e73-a791-d4b786c6d074 | -5.7119 | -53.4658 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| e6fd2bda-cc30-373a-bd46-6a617c745adb | -9.2781 | -47.4333 | 2026-10-09 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d3780309-3b05-39ce-9b0f-e34b26f37db3 | -7.4442 | -63.5589 | 2026-10-09 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b5629fb1-861b-37fd-a9c9-df173dc5a4f0 | -6.0021 | -40.9594 | 2026-10-09 00:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 288.8 |
| f3d73b0b-094a-34b6-b9a0-bc072b0da3ae | -12.0251 | -43.4609 | 2026-10-09 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 557b3162-2494-3a52-a4a3-d1b16bd190ca | -3.1114 | -53.7839 | 2026-10-09 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| de8007d8-8803-355e-bcc1-89f097878c14 | -3.1284 | -54.1857 | 2026-10-09 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 22bbb95d-67a4-3f9b-9d25-5feb34a6df1a | -12.0058 | -43.464 | 2026-10-09 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 58bd53ed-52bd-3272-b2a8-48167679ef3b | -11.1876 | -45.3117 | 2026-10-09 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 249ef701-834f-3bc9-9f76-82203916f9a1 | -3.197 | -50.601 | 2026-10-09 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 3853aae2-3933-348e-ac16-e0e53cfd9f5c | -11.6754 | -43.6817 | 2026-10-09 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 03f303b8-8b9c-3584-bae6-ae200e17555e | -6.4719 | -62.8559 | 2026-10-09 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 193a58c2-c8dd-35a4-8f00-b2c284ea4823 | -11.6566 | -43.661 | 2026-10-09 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 6c5a5583-6f5e-3456-8623-52fd5b809cf9 | -3.5493 | -54.6951 | 2026-10-09 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 158.4 |
| f49a1c99-04e5-35f7-9b57-0f8d52b8b387 | -2.7428 | -54.1347 | 2026-10-09 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 7a7082ef-003a-369c-96e2-d597da476fe0 | -3.2533 | -50.3899 | 2026-10-09 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| a97ffeba-1a51-3a2b-97ef-70b1f3c039b8 | -4.992 | -44.9764 | 2026-10-09 00:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| dbb6240a-9578-3110-9b80-962bd330bc96 | -9.6867 | -58.0865 | 2026-10-09 00:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 95511b4f-116d-3767-93db-89b9b0578bf2 | 4.4435 | -60.9657 | 2026-10-09 00:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| ce436c90-d67c-3a8b-b366-b2500a4500b0 | -7.2182 | -55.1416 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 3826867c-f1d8-3880-8759-e4254ce0f730 | -9.2973 | -47.4092 | 2026-10-09 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 04828fda-6f6b-365b-bba0-a272882e1b08 | -2.499 | -56.0675 | 2026-10-09 00:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 81633513-7269-3ec0-9afc-7aa90be1e4b6 | -7.5835 | -61.5326 | 2026-10-09 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 38e0e458-aa93-3c4a-adee-6f38875ba083 | -12.2156 | -57.1087 | 2026-10-09 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 141.5 |
| b9990299-8bcd-3c8c-b370-fc267fe774e3 | -4.5306 | -47.0337 | 2026-10-09 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 5f14cfbf-876a-3002-b969-dc431edb9ab6 | -6.0019 | -40.9837 | 2026-10-09 00:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 4cd50362-86ce-39a1-8761-55733da56797 | -1.1094 | -54.1802 | 2026-10-09 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c0062322-2369-39e6-bc4a-2b538075fba3 | -2.7429 | -54.0945 | 2026-10-09 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 03a20dbe-64a1-3753-989f-06b22b04aa51 | -3.3455 | -50.4078 | 2026-10-09 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f2f4fb64-c16a-3853-b1dd-ae669a0ce751 | -13.1827 | -54.3571 | 2026-10-09 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 8711106b-d0d5-363a-9062-13ba8fa2a183 | -4.9918 | -44.9991 | 2026-10-09 00:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| fc407f1c-dae9-3af2-850d-7b17e674fac8 | -7.2187 | -55.0815 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| fee741ff-ca5a-31ff-912f-66deee1b1217 | -4.0838 | -44.1159 | 2026-10-09 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 7b9008d9-1644-3fa5-83b5-2ba3ee04ca31 | -8.6301 | -66.77 | 2026-10-09 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ea73122d-b09a-3794-9d0d-bfc47de12ccd | -3.0007 | -53.9075 | 2026-10-09 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| d7eca76a-1399-3e1c-ae9a-66be19cc426e | -8.5183 | -67.0325 | 2026-10-09 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8c801b30-5fba-3a0c-be40-20dbda286291 | -11.6562 | -43.6846 | 2026-10-09 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 262.6 |
| cc329b5d-56af-3dca-ab05-6a85c2246186 | -3.9299 | -56.034 | 2026-10-09 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 55c308f8-634e-3a9f-aab6-81f9db6d9ae1 | -3.0924 | -53.9656 | 2026-10-09 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 03629d1f-ef44-36c7-a322-bd649ee5de5d | -3.1109 | -53.945 | 2026-10-09 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| a60ba63d-c3cd-379e-950f-0faf8b8aea29 | -3.0186 | -54.068 | 2026-10-09 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 79bd935a-cf94-34e7-9d1c-de42958bd6fb | -3.1879 | -58.6433 | 2026-10-09 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9b840719-bf2e-33a5-afd3-726879a3e018 | -12.2346 | -57.1071 | 2026-10-09 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 55132ccb-dfdb-3461-9022-098ef3d943a2 | -3.1285 | -54.1657 | 2026-10-09 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 189.2 |
| 57462cb8-f246-3238-8fcb-85fec60af42f | -5.7117 | -53.4862 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 7305b9b8-01cf-3e2d-8177-2fb3d12e4be4 | -3.1787 | -50.5807 | 2026-10-09 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| b1403efd-30b4-3bc4-a2b4-cac58d21a9c3 | -8.8961 | -44.9336 | 2026-10-09 00:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 8ba6d836-82f3-3268-a60b-8074327ec1e1 | -10.0253 | -48.036 | 2026-10-09 00:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| ccf48743-f636-3a37-b464-b3f1316444e5 | -13.1639 | -54.3385 | 2026-10-09 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 207fad0a-5d5d-3bb2-beb0-54679a526277 | -6.0024 | -40.935 | 2026-10-09 00:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| db17fed2-1d79-335d-a1d8-3078c6cd57b6 | -9.2549 | -60.8863 | 2026-10-09 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 6a228bd6-70c3-34f2-aed4-49c432f4f889 | -3.1108 | -53.9652 | 2026-10-09 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 704812d7-6f4a-31be-bd47-7bcc88093efe | -6.0262 | -53.491 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| dd1f2a0a-1698-3225-a507-0b704570e851 | -3.5677 | -54.6746 | 2026-10-09 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 88574904-dc4c-3350-9d85-30bf98ea5867 | -3.7739 | -58.5921 | 2026-10-09 00:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f8a43778-93de-356a-a13f-6531ce75a258 | -5.7302 | -53.4853 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e4606d7e-dc2c-365c-8560-2cabc318dd69 | -4.2954 | -49.0807 | 2026-10-09 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a5ef7a28-9ef4-3626-a98e-d04c7e6d7b9a | -3.2031 | -53.8621 | 2026-10-09 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| aaefb5d0-fcb4-3b93-aa8a-a222479a5307 | -3.0186 | -54.0479 | 2026-10-09 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 1a828981-e2c9-3cd4-97b7-8d49d4c27f5b | -4.7404 | -55.672 | 2026-10-09 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 49698137-b578-37bd-9509-9e6ec5e8e504 | -6.0076 | -53.4919 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| f5076736-5b00-3d32-bbb1-92ac3416025b | -1.1094 | -54.1601 | 2026-10-09 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 9c3b16b3-2cd3-3f33-9cc9-7c47c46614d5 | -6.9853 | -47.6639 | 2026-10-09 00:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 93f11ee2-8e20-3943-97fd-98b2a40d6c95 | -3.5493 | -54.6752 | 2026-10-09 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 848c8528-aa6a-3efe-97b8-dec7aa3fd25d | -3.2057 | -58.8546 | 2026-10-09 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 21dfd327-2026-3115-a428-7f26e6c93bca | -2.7428 | -54.1146 | 2026-10-09 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| fe4efe47-ac0c-3715-9462-d12341837e0f | -6.7195 | -48.1201 | 2026-10-09 00:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 54bc28a2-f257-336f-a298-627d846e405c | -3.1971 | -50.5801 | 2026-10-09 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| ff148259-3e27-33f5-ba01-4ab765b3fce9 | -12.2158 | -57.0887 | 2026-10-09 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 79ee9bb3-99e2-3f94-8350-36ab6e5831fe | -3.0002 | -54.0684 | 2026-10-09 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 539caeda-4036-3373-8b06-34568bbd32ec | -3.2057 | -58.8354 | 2026-10-09 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 1d348d80-3895-3892-8f85-1266710c4397 | -7.5688 | -64.5476 | 2026-10-09 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 3ac4bf3d-a422-3f24-9c4c-fc736a20b6b2 | -8.5369 | -66.9949 | 2026-10-09 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 6f966fee-3f96-3b5b-8a1f-f152845fb77a | -3.11 | -54.1862 | 2026-10-09 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| b590f6ac-6d6c-3f86-a136-4b7bf75599a0 | -3.0926 | -53.9254 | 2026-10-09 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 2f6f8909-a6ca-300f-8d7d-02d368cef7ed | -12.2154 | -57.1287 | 2026-10-09 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| e3148d9a-1376-31c7-9ae6-be57fa599cbe | -7.2367 | -55.1406 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| fa487aeb-c3a9-3dd4-b9ac-f83c30a0f324 | -15.3419 | -42.7704 | 2026-10-09 00:00:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 170.7 |
| a885ad96-af2a-3a65-b139-67083b95340d | -2.7612 | -54.1142 | 2026-10-09 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 003bc1f8-e96c-3001-b993-cf3b99f415d2 | -9.2178 | -60.8689 | 2026-10-09 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 9d326909-c777-3320-a08a-8f8955158287 | -5.9587 | -55.3448 | 2026-10-09 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 158bae9f-1500-344c-a4e0-05158664193d | -13.2018 | -54.3551 | 2026-10-09 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| c7cb084e-0cc0-39f3-8497-28985b6580f3 | -8.537 | -66.9764 | 2026-10-09 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |


[Clique aqui para ver as próximas entradas](README2.md)
