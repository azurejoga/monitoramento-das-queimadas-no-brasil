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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2b78ba3-23dd-32ae-ac0b-e1933ceff82e | -4.56151 | -45.47194 | 2024-12-03 05:08:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e52e47c5-b901-3b26-af9b-7e3aafa7e039 | -10.64865 | -44.48361 | 2024-12-03 05:08:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8961d5f3-96a3-3232-8233-18580e5fd6ff | -5.11817 | -43.21014 | 2024-12-03 05:08:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| cd30fa33-f61a-39f9-b7f9-60f7e68a6a4f | -6.03519 | -42.52353 | 2024-12-03 05:08:00 | AQUA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 63de7ef1-0454-3fe9-9da8-03dc446d85b9 | -6.11009 | -43.96597 | 2024-12-03 05:08:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d2a039c3-f512-3caa-be49-4fb01f4e6f21 | -6.18557 | -43.41519 | 2024-12-03 05:08:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 50b7200b-c214-39ac-bea1-1bc37f57dfc8 | -5.8066 | -46.48125 | 2024-12-03 05:08:00 | AQUA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 06265ccf-dd78-335f-a759-201e7d678236 | -5.79516 | -46.4796 | 2024-12-03 05:08:00 | AQUA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 9f0ed13d-9619-3248-a76c-d1faf4da7587 | -5.14295 | -43.23379 | 2024-12-03 05:08:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| d5dcc544-c20a-300a-be4b-c63fb4aa5b45 | -6.97311 | -43.5121 | 2024-12-03 05:08:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 4bada8da-42cd-3e3e-b032-59d0a12edc55 | -3.259 | -53.6388 | 2024-12-03 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0a676a8f-5dd2-3c35-89d0-d5c5e8832391 | -5.801 | -46.4719 | 2024-12-03 05:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 41778218-8daa-3c4f-93e1-c8165e5c742a | 2.7267 | -60.3916 | 2024-12-03 05:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1f06969e-9f74-3a8d-9ed8-899d0bcb08c9 | -5.1181 | -43.1964 | 2024-12-03 05:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7dfbe359-ee1a-39c9-b9cd-114a4667bd29 | -3.2775 | -53.6181 | 2024-12-03 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 383eee40-805e-3175-9cb5-10b69bf6eb38 | -5.8195 | -46.4929 | 2024-12-03 05:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 0c3d96a7-6108-3707-84ac-eafa8104cd25 | -3.347 | -46.0486 | 2024-12-03 05:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 4dd2515d-d313-353f-862c-a8dc3b600b19 | -5.8197 | -46.4706 | 2024-12-03 05:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 0f940c59-8494-3648-9749-f1df0d640ee5 | -3.3285 | -46.0494 | 2024-12-03 05:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 40540993-743e-3f0a-ac99-a268446ad908 | -1.0735 | -53.4562 | 2024-12-03 05:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 3a805eaa-dc40-36fb-aa07-472cee5b71ce | -3.259 | -53.659 | 2024-12-03 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 7e8f8432-962a-33ef-86ff-2a497fd4dc32 | -5.118 | -43.2198 | 2024-12-03 05:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| ace62165-ea76-3ff3-97dd-8e82784feeb3 | -5.8009 | -46.4941 | 2024-12-03 05:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 6556a9c1-f423-3f83-b2c8-8ffcebded416 | -1.0919 | -53.4561 | 2024-12-03 05:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 7aa201a8-24fc-30a0-8639-8fccd4517a0e | -3.076 | -53.3808 | 2024-12-03 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 590503cf-66c4-38ab-8fcf-69e7d5b7ff56 | -3.2774 | -53.6383 | 2024-12-03 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 7d124431-909b-319f-be2e-769abddcb713 | -3.2591 | -53.6186 | 2024-12-03 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2b7d8bab-a15c-3926-920d-439b71487032 | -3.2958 | -53.658 | 2024-12-03 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 2e64565f-1837-3cf5-977f-8a81c57f0cf5 | -3.076 | -53.3808 | 2024-12-03 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 106040a1-4992-312e-9432-83b17594044e | -5.801 | -46.4719 | 2024-12-03 05:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 47eac8ce-de75-3e81-974d-643077aee1a3 | -3.259 | -53.6388 | 2024-12-03 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 099b7aff-e23a-353a-a917-b26ad1a61187 | -12.7149 | -58.2032 | 2024-12-03 05:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 6484b354-ef79-3dcb-a53f-945ce73aeb6e | -5.8195 | -46.4929 | 2024-12-03 05:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a2e729fb-9ba4-3271-a299-dda5f1aede36 | -3.347 | -46.0486 | 2024-12-03 05:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 4efee926-b4f8-38a0-b7fb-4b387962e452 | -3.259 | -53.659 | 2024-12-03 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 11581b99-4caf-3c8b-946e-1e93371b7cfb | -5.8009 | -46.4941 | 2024-12-03 05:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 1615fbb5-597f-3815-aa17-e042307e05ca | -5.8197 | -46.4706 | 2024-12-03 05:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 5bc05dbb-1916-3fba-be51-9389789f45e1 | -3.2591 | -53.6186 | 2024-12-03 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 856c9d1f-9480-3646-a789-dd6e6be195a3 | -1.0919 | -53.4561 | 2024-12-03 05:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 2796eb30-dd76-3480-9538-62cd610caf6b | -3.2958 | -53.658 | 2024-12-03 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 30a5ac4c-0146-3ae2-8a6d-fed334486e58 | -1.0735 | -53.4562 | 2024-12-03 05:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| a25f957a-661e-3580-96dd-8cf51d7ad130 | 2.7267 | -60.3916 | 2024-12-03 05:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 4d7af23b-091d-303f-a54b-3484dc5b878c | -3.2774 | -53.6383 | 2024-12-03 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| f153b441-d78d-3bfd-86d5-92ad57795f30 | -3.3472 | -46.0264 | 2024-12-03 05:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| f1348ae9-4b7a-3793-97aa-ee64a70f1f67 | -3.2775 | -53.6181 | 2024-12-03 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 0964699f-3ac0-3fca-ab2c-ecd5d3bad528 | -0.91513 | -53.10617 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94fb1a24-776a-3c79-9084-53ec948b7830 | -1.36672 | -47.68752 | 2024-12-03 05:22:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3f02d82-8771-3fbd-9c1a-3bfcdd8430fd | 1.10976 | -56.02732 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef71452c-8225-3b71-b00a-f4f194ef129d | -4.04228 | -54.22807 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fce29919-18a7-3ce1-ad1d-71a916eb606e | 1.11269 | -56.03252 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1f8238d-1400-3bf0-8899-85a9e7784612 | -0.72547 | -51.69414 | 2024-12-03 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f4f3786-1825-35eb-aced-e1ebf664bd37 | -4.04488 | -54.22735 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2d93893-e618-3657-8100-977482f93e60 | 1.10342 | -55.98615 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25ec2129-4f83-309e-8723-eb92f544db0d | -3.79595 | -58.97719 | 2024-12-03 05:22:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ababac9-c064-3be9-8998-d5845af407d8 | 4.09753 | -61.19825 | 2024-12-03 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| acfb6ead-a355-38f7-a29b-adf2295141a7 | 1.1104 | -56.03143 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1febc61-bd99-369c-ae32-c7b16bc3c02b | 1.11854 | -55.97687 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e960b3d5-51f3-37af-8542-81f8c94ef669 | 0.90672 | -59.44933 | 2024-12-03 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 366fb689-e6db-33dc-bc1a-d02023463893 | -1.08592 | -53.46018 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 9412166a-c32c-31b8-b327-c7811fb0532a | -3.54954 | -54.59208 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6efe57f-727f-337c-a784-a5e3ea3fabbd | 1.12148 | -55.97219 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f03a28d-323e-3823-9889-7e59dd5fddd6 | -4.03997 | -54.23089 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d080b013-d7f3-382f-8502-f9aedc4d76de | 4.09815 | -61.20224 | 2024-12-03 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6f64b3bf-75e6-3668-9329-b43dec5d679f | -3.58666 | -53.04553 | 2024-12-03 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c374d413-34a8-3b7e-a037-cdfde0f10dff | -3.55011 | -54.58832 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e943abdd-9f7b-337c-9eb8-99bf7b91b61f | -1.73549 | -47.05902 | 2024-12-03 05:22:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d3b2e389-1944-3fc0-8d73-b285eeb8fb41 | -3.41696 | -59.75329 | 2024-12-03 05:22:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efd5c293-74e5-39ad-9613-2b9513c6c44b | 1.09096 | -56.00083 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d77a8654-f221-377b-824a-b20f569d2d77 | -4.17497 | -57.53936 | 2024-12-03 05:22:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cef4d8a8-a74c-304d-a94f-1de8fb76200d | -1.08159 | -53.45941 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| a777aec6-5480-3113-b9be-0283a012c977 | -4.18135 | -51.18107 | 2024-12-03 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e55577a-0154-3594-bb4a-e47eb89e60ac | 4.06548 | -60.67949 | 2024-12-03 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb363d25-441b-3de2-984e-a709928abd88 | 1.11335 | -56.02674 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08790eee-5ab5-371e-9f95-f13a13132de8 | -1.80305 | -46.65748 | 2024-12-03 05:22:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5ce47405-710f-3125-82e0-2f81ca418578 | -3.79315 | -58.97313 | 2024-12-03 05:22:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9f38474-0df1-3eb2-95d9-2b84f2e6b840 | 2.73276 | -60.38733 | 2024-12-03 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 22f78f09-f179-3e3a-a2ee-aef3462f2512 | -0.975 | -53.0952 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91862ea5-3183-3645-933f-c899be10d5f7 | -3.42585 | -54.60977 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73719c7e-a12a-3836-90c0-84ad9a76bba6 | -2.94667 | -58.40472 | 2024-12-03 05:22:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5548624-11c1-3025-92ac-e8b434c7ca48 | -3.46908 | -54.64589 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84a89908-2e95-34ce-b1e4-1559deee9d3d | -3.46813 | -53.88961 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d223ec9a-0fac-3c20-ad38-4c823faa93c5 | -4.48104 | -61.08596 | 2024-12-03 05:22:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93ef5362-f3aa-3dde-aefb-e1701ab79b31 | -0.61303 | -51.692 | 2024-12-03 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b34baf7-72c3-35d2-a63c-14abf304c1b8 | 2.42285 | -60.65088 | 2024-12-03 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3cd0269-f7a1-361e-92b0-5067251d27a2 | -3.86076 | -52.27461 | 2024-12-03 05:22:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ea450760-835e-3f86-b028-cbb9e693e669 | -3.69954 | -54.40319 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d230d67-ab7d-3585-a31c-9ff379b1ed96 | -3.86568 | -52.2753 | 2024-12-03 05:22:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 714fc442-8fb1-3abf-92e2-e79bacfecba2 | -3.61785 | -54.57423 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8024364-af7e-3bd0-9e99-be36e243c9f2 | -1.07482 | -53.44562 | 2024-12-03 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef14751c-fc4d-34ff-8059-1e1751603b89 | -1.34844 | -51.38315 | 2024-12-03 05:22:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa21291c-75ad-3f85-980a-b19ce3c52012 | -3.41061 | -63.49546 | 2024-12-03 05:22:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5ea8790-af5d-39e8-a0b9-e81e48df88c6 | -3.50307 | -53.83499 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ef5c90f-d51b-3743-84a0-9dd4c2f9d52a | -3.55427 | -54.58906 | 2024-12-03 05:22:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02ec090f-d378-344a-8b5d-8738bfae2bca | -3.498 | -53.80857 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9002681a-539c-39f6-b808-1a1cd444331d | -3.43516 | -54.11409 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ce468b5-a493-3fa8-86a6-571e88da2487 | 1.11398 | -56.03086 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 081cdc38-1cd9-3474-b065-7dc035c64282 | 1.13624 | -59.54692 | 2024-12-03 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d507efbf-b58a-392c-a9dd-042330df0f2d | -3.58597 | -53.05026 | 2024-12-03 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa625888-273f-341f-93b6-74033b4c5d81 | -3.50185 | -53.78252 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5668983f-d589-3a8d-b32d-629aeaf23f33 | -3.49806 | -53.83852 | 2024-12-03 05:22:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README56.md)
