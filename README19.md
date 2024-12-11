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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 318dcaf0-bffa-39f0-b2ac-669d390aca6c | -15.09669 | -59.64796 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc2560a4-87bf-3ed1-93c3-47c2d06dfb66 | -15.07083 | -59.64952 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 91843cea-0248-3505-aeff-de2e4e16e430 | -15.07546 | -59.6541 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6a432190-576a-391b-87db-360e239eb1a4 | -15.0935 | -59.63643 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96658a3f-20a2-383e-bb80-1067f6d8715f | -17.74529 | -56.32561 | 2024-12-11 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f39a28dd-e40d-3d1d-81be-1f6aa5147093 | -17.67533 | -42.7434 | 2024-12-11 04:38:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10ab512c-9c46-3bdb-ae49-76d0de2f3386 | -6.978 | -42.9977 | 2024-12-11 04:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 5be47c0f-54b7-3b8b-81fd-f11cf907b58b | -6.9594 | -42.9759 | 2024-12-11 04:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 7b5a4b1c-e9e2-313d-9125-dc3f17faffdc | -6.1366 | -42.5544 | 2024-12-11 04:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 82b6e374-7968-362d-8f37-71b2904ce10d | -6.1368 | -42.5307 | 2024-12-11 04:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 122.8 |
| 4ad3dee5-ea48-3a2a-8828-9330ea228d88 | 2.7627 | -60.6378 | 2024-12-11 04:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 81.3 |
| c0c42b11-74c2-3607-bb92-37ff8b9a168f | -6.9158 | -43.5185 | 2024-12-11 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 96e44153-1148-3a06-b046-d5d7bc335678 | -6.897 | -43.5202 | 2024-12-11 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| fe9878e7-ffca-3c02-ae4b-e1c20dfb3e46 | -6.9592 | -42.9994 | 2024-12-11 04:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 8f0255de-94da-3c0e-8d25-07fff7088808 | -6.9161 | -43.4952 | 2024-12-11 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 8c0851be-b9ef-3d1f-8ab8-c68cef8f7ff9 | -6.8972 | -43.4969 | 2024-12-11 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 1a0792cf-25c6-3635-9821-788861a5c93d | -6.118 | -42.5323 | 2024-12-11 04:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| e704cef7-76e4-3e7d-a3c7-db554875e1f2 | -25.56988 | -49.35725 | 2024-12-11 04:40:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e74f4b45-0212-35ae-9f87-9068e2f45a8d | -30.16185 | -55.0029 | 2024-12-11 04:40:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 09a9b010-9bd9-3190-a465-e590f4d107b2 | -25.57139 | -49.36005 | 2024-12-11 04:40:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 86c0e04d-c4fa-360e-9950-171a6c7e7313 | -30.78951 | -52.27604 | 2024-12-11 04:40:00 | NOAA-21 | AMARAL FERRADOR | RIO GRANDE DO SUL | Brasil | 4300638 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 0e2b004a-8fa7-33a9-a923-18dc5aa84383 | -30.16037 | -54.99968 | 2024-12-11 04:40:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| d3fc50dd-037a-34f1-8eff-564ad7ac98f0 | -30.15904 | -55.00779 | 2024-12-11 04:40:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| bd3191dd-bd24-3140-9c06-3925ea96b665 | -30.16252 | -54.99884 | 2024-12-11 04:40:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| bd782d3a-043e-30b2-9249-518fa94abae1 | -25.57048 | -49.35269 | 2024-12-11 04:40:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 509459a7-e2ae-311d-9ea2-064776f5e64f | -30.16117 | -55.00695 | 2024-12-11 04:40:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 69f6a818-4b94-3250-901f-357e522d7539 | -25.57407 | -49.35329 | 2024-12-11 04:40:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a58ffecc-371a-361b-b590-874200729498 | -24.24441 | -50.74137 | 2024-12-11 04:40:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2d5d9b54-5470-3d84-87e0-19f2807b7795 | -25.572 | -49.35553 | 2024-12-11 04:40:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 72106712-402e-3719-a724-8f8aad5d18d6 | -30.16518 | -55.00363 | 2024-12-11 04:40:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 89888be5-2f52-3b83-b7f1-4af8aa89c400 | -25.57347 | -49.35783 | 2024-12-11 04:40:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| cebef290-277e-348c-b2b4-f9cf3ca723ac | -6.9592 | -42.9994 | 2024-12-11 04:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.2 |
| 2eec76fd-fccf-326c-bf1f-ebb8af2077b1 | -12.5425 | -58.3561 | 2024-12-11 04:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 660991ca-5edc-3568-a739-6fc64a675b66 | 2.7627 | -60.6378 | 2024-12-11 04:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 9bdd22d6-aa63-344a-bf2c-7a922321f58d | -12.5427 | -58.3362 | 2024-12-11 04:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 3af18344-3e31-3a5b-a72e-a5f18f685fa3 | -6.978 | -42.9977 | 2024-12-11 04:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 145.2 |
| d3f3262c-6ec0-3eb1-b82a-a274817f96a2 | -6.1366 | -42.5544 | 2024-12-11 04:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| e27a483f-a7dd-336e-89d3-a64757f61ca8 | -6.9161 | -43.4952 | 2024-12-11 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 9422693e-6886-3f5e-8b0a-ae3971c69a28 | -11.1106 | -54.6408 | 2024-12-11 04:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 783a0e52-f83c-300f-b737-4b86608c85cb | 2.7444 | -60.6381 | 2024-12-11 04:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| d419597e-5041-3a59-a495-6ece8e5b2798 | -12.6755 | -45.6672 | 2024-12-11 04:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8c4cbbda-d718-3938-852a-294166d6c1e2 | -2.8196 | -53.0629 | 2024-12-11 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 850bc628-e1f8-37e5-837c-89729aa7ca90 | -12.5615 | -58.3546 | 2024-12-11 04:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| a3c5ef49-5124-3ce0-b7a6-9c2737ec94c6 | -3.1288 | -54.0853 | 2024-12-11 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| cd1de795-25d4-3485-a71d-64d0a033847e | -6.118 | -42.5323 | 2024-12-11 04:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| 49ec13a9-fd75-3b56-a1d2-fa55462d7511 | -6.1368 | -42.5307 | 2024-12-11 04:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| bb24b93f-8440-3972-b518-4468cfb8a935 | -6.8972 | -43.4969 | 2024-12-11 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 54a2100e-4185-3762-9a44-8452047093fd | -12.5423 | -58.3759 | 2024-12-11 04:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| c1039bcf-39bd-36db-b5b6-903f99617038 | -6.897 | -43.5202 | 2024-12-11 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| bfeac7e0-bbcd-373c-b7a9-bcb5e4f2fdd9 | -6.9594 | -42.9759 | 2024-12-11 04:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| eb3a778e-8ff8-3cec-abed-be22954633fb | -12.5613 | -58.3744 | 2024-12-11 04:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 77e6090d-961f-3101-8db8-760b8f79e456 | -6.1178 | -42.5559 | 2024-12-11 04:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 38963b92-083c-3d8f-9497-be95a049f95d | -12.5617 | -58.3347 | 2024-12-11 04:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 24f008fc-12f2-30ec-a0fb-6185d5eacc19 | -3.26251 | -53.27803 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 034cd9b6-6e17-3d9b-9a57-a2ad41214667 | -3.33162 | -53.24702 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5a41b3b-fe98-3379-a568-5825a410ba93 | 1.30436 | -60.40554 | 2024-12-11 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6c84e77-e826-3c12-a405-d4b5bec6c196 | -2.57884 | -54.34667 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d3a8c93-622e-3b82-807e-746a3928c6f7 | -2.81515 | -53.06659 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1cec74e-ec1e-3c94-81a0-e998f1767a1a | -3.5994 | -53.7164 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7baf1c5c-e0fb-3aa2-9074-099ea4019517 | -2.82844 | -53.06866 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18eb9de2-0655-3969-987b-fc6cb9b557ab | -3.0946 | -54.08386 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2641c92f-0009-3dac-b182-7d4948809e56 | -2.45749 | -53.64367 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c96716f4-0fa4-3e8b-add3-39d3c2e5e151 | -2.61284 | -54.24054 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f5e4f35-f368-3c02-b2ce-133a745e54c8 | -1.69204 | -55.67176 | 2024-12-11 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4c1c3c6-35ee-3abc-9352-2c3657be6424 | -1.40689 | -55.19365 | 2024-12-11 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66735f0c-2bd5-3b14-9dee-8d6161c77c18 | -3.73572 | -53.73417 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51691c9c-4deb-3857-9892-938aabc3c5c7 | -2.81569 | -53.06314 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2d02904-ef11-3ed6-a31e-f88cac845ae0 | -2.8218 | -53.06763 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 970dda5c-687e-3baa-9e63-0a9f94100440 | -2.64138 | -54.38539 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef750bac-bfb8-3e6b-b776-ce6fac75c545 | -2.82071 | -53.07454 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b77c80a7-60fe-3c06-870d-648348252b50 | -2.66957 | -54.87181 | 2024-12-11 04:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b22d0689-93e8-3923-8ded-a24ad6aeb665 | -2.82512 | -53.06815 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a1fa03e-729b-3a84-8de3-1e0b413925a2 | -3.29258 | -54.11528 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ed76d52-8156-37ad-842b-0bde7ac904a5 | -3.12067 | -54.07011 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41472975-5711-386d-8884-ed1078963272 | -3.10506 | -53.75904 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c01be8f0-0515-39f7-99dc-07b0b6311317 | 3.22917 | -61.19816 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9cdc1b82-07ff-3a72-bca1-6d7cf9ad437a | -3.09587 | -53.73649 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d41edf62-14d1-31fd-b4b2-064bb2c38c4e | -3.26643 | -53.87693 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d39f01d1-5158-3e7d-94c4-a9236b20471c | -2.79007 | -52.86414 | 2024-12-11 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1aa5563d-06cd-3761-aa53-2663305670f2 | 3.23182 | -61.19362 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2b687f3f-5c32-3d4e-8589-7ce2f0b01c7c | -2.83177 | -53.06918 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddc90a03-e4b0-3936-9d79-1728ddee33aa | -3.92124 | -53.67161 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67d9e630-86d2-3b13-a9eb-3bfd3c2430fd | -3.12012 | -54.07358 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b7e3b6a-e3e6-31bc-8ecd-d92f4b137c33 | -3.13125 | -54.08956 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d93eb3ea-a8c9-3def-bb24-7f675b650637 | 3.23285 | -61.20038 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b45f3e92-58c3-3828-b4ac-2dcdf30edd49 | -3.5129 | -54.17809 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 87d341cf-24a9-362a-a4be-00c63fe50931 | -3.59886 | -53.71985 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b76ee465-c062-3ce7-926a-09c7ae71d370 | 2.74795 | -60.64439 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9236945b-8ba5-3926-9303-8f5bba1da6ef | -2.47883 | -53.63269 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fe18667-1442-376f-90f6-f376c84c2b82 | -3.32884 | -53.24305 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6592c96c-d6f2-3bbf-a248-008b0dd093e3 | -3.60272 | -53.71692 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b71dcfed-b0cb-31d1-9657-ba21ff1b657f | -2.81617 | -53.03842 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcaa418e-6190-3fd0-bbfa-18de9fb87aa3 | -3.10065 | -53.76543 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23c0c8bb-e40b-3344-934a-6e9a6962e803 | -3.06615 | -53.7956 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04360e21-7d2e-35ac-a29a-0a23a3d99a2d | -4.59627 | -47.83657 | 2024-12-11 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 50778b9f-fbfc-3c6d-a225-c7994172638d | -2.58275 | -54.34368 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d2b0892-0e19-3bfb-a8be-ab6c317fca87 | 3.22868 | -61.19478 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a87a4263-a574-3453-8d9d-34b1af47c3d9 | -2.61229 | -54.24404 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8ab5e96-0cb8-3cce-b396-ae27aaf9e96e | -2.80905 | -53.06211 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 378db1ad-205f-3db5-a55a-8a45e806a5ac | 2.74885 | -60.65047 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README20.md)
