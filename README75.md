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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09836b5b-2e04-3def-85d4-3c1fa49eca97 | 1.95894 | -60.5668 | 2026-09-22 05:21:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba22f356-b098-39ab-90fe-da0d3d144c2d | 4.03741 | -59.65799 | 2026-09-22 05:21:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acd65dd5-c65b-3ebf-b0b3-d4a1c9ff4731 | 1.90713 | -60.58218 | 2026-09-22 05:21:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09217481-49ce-3198-a793-611cf2ecbabd | 1.99242 | -50.87234 | 2026-09-22 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d47bbf54-e4cb-3941-92a8-476069b29014 | -0.93166 | -47.55208 | 2026-09-22 05:21:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddb68402-2aeb-3b9a-b9bb-10992c57898d | 1.98142 | -50.87925 | 2026-09-22 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1b1c2ff-a532-36ee-a128-3aca614c6367 | 1.77452 | -60.23825 | 2026-09-22 05:21:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cd597188-1f5e-3d1d-bb4e-8e34a63a4f2a | 1.07611 | -60.6783 | 2026-09-22 05:21:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9025a28-c955-3d8e-a889-e1e6ded1d547 | 3.24643 | -60.23505 | 2026-09-22 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47b14cd8-1dc9-3b20-9673-6b44a5647c1d | 3.24697 | -60.23861 | 2026-09-22 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf887bdf-b3c4-3fe1-8cd2-8fda0d2849f7 | -0.93762 | -47.55303 | 2026-09-22 05:21:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54df28cd-70db-3950-a051-0e6f2203467c | 1.08015 | -60.67763 | 2026-09-22 05:21:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31ee66fa-791e-3b17-b94e-3d61d9ae77c8 | -0.93683 | -47.55286 | 2026-09-22 05:21:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53eb4da5-25dd-398d-a79a-ef87704f3a4b | 1.55198 | -55.86331 | 2026-09-22 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06e76148-707e-3353-9e5b-d8ef095fd459 | 4.59076 | -60.72235 | 2026-09-22 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6959db8-28f3-354e-91c5-5c41fcf688b1 | 1.9595 | -60.57036 | 2026-09-22 05:21:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a38c707b-36f2-3700-b413-7e74f0536f9c | 4.03265 | -59.65327 | 2026-09-22 05:21:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60649e21-a469-3bc9-b6d6-9d4cd7446ae5 | 2.09856 | -60.21316 | 2026-09-22 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c314c6ef-a784-3f7d-9770-4162fdf36746 | 2.43921 | -60.93321 | 2026-09-22 05:21:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7bca33a5-141e-3452-a749-759d0c44c51f | 4.2599 | -60.64742 | 2026-09-22 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 612f7258-23a7-30e5-b38a-7fcfd001e7c5 | 3.25103 | -60.23799 | 2026-09-22 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97ea7bdb-e05c-33d8-9c94-3cb373094549 | 2.09777 | -60.20813 | 2026-09-22 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 459b4530-13ed-3674-8e38-35ff943cb0d6 | 1.54324 | -55.78688 | 2026-09-22 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6155106-c676-3b07-93f7-f747fb2904b2 | 2.4398 | -60.93705 | 2026-09-22 05:21:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 268b0f6a-ad9e-3b7b-894a-4c611496c899 | 4.25548 | -60.64375 | 2026-09-22 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 77a1b319-3790-3e90-83ad-20f6c4445f6d | 1.81606 | -56.08082 | 2026-09-22 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1ac9d96c-b8ae-3c1c-bdc0-a827d204572d | 1.55033 | -55.85295 | 2026-09-22 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6080d980-18ae-3dff-9fde-6e92eb0b6849 | -0.93245 | -47.55224 | 2026-09-22 05:21:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 921ece35-9654-3118-a6da-00f4d76eb0a1 | 1.08071 | -60.68116 | 2026-09-22 05:21:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1f33da7-863c-32b9-b477-0e899f3794b6 | 2.3163 | -60.92032 | 2026-09-22 05:21:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4a59f24-9c43-32bd-9904-c7a6803f5282 | -3.98114 | -55.4721 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7592e0fe-041e-3c36-be9e-904734955fca | -6.91573 | -59.62899 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57d143c8-c133-30de-b2cc-31e5791a67a2 | -3.3649 | -50.46141 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b88cc8e-b295-398b-a079-a09e6a1245d3 | -5.20185 | -56.07585 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b86970ef-1fe7-3237-a713-1cf19e4803a7 | -5.91749 | -55.69812 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06e09f43-f123-386e-9417-f1c589bb93a5 | -6.58065 | -58.99915 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ef11461-77f9-38cb-994a-4e3f7adf6e48 | -7.58368 | -57.69334 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afa8d631-8135-35a3-9b7b-46a5a5528475 | -6.11775 | -57.74514 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57c3f769-a6ae-3e26-b298-98f1f3352df4 | -4.53034 | -54.97665 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e921bb27-ff76-35d8-b314-b9dd76542307 | -5.30662 | -56.00889 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d6cdcbb-0156-395c-9f70-37d703616ddb | -2.66462 | -54.96431 | 2026-09-22 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67b8d6a9-c8d8-3803-b8a1-0562061e4bc9 | -5.97845 | -57.76953 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 405f992c-a568-3ad3-949a-393cc633b184 | -6.91057 | -59.84398 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8aa4a4ff-9627-34bd-9870-575c186d4a81 | -2.90999 | -54.18789 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c57572a5-75e1-3a44-b6a4-419605c94725 | -6.35644 | -58.28672 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07ae7005-3ec0-334d-a407-937b48f57124 | -6.15422 | -57.72591 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa641944-7932-3663-9f4f-f176b7046618 | -1.02408 | -53.73288 | 2026-09-22 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74b98814-bcd0-33d5-a90f-0b12082cbe35 | -3.92755 | -56.05085 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94bbbd58-95ad-3ced-a612-a8d326f7ad3c | -2.78476 | -59.95985 | 2026-09-22 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b7172d9-4589-3ee6-b2b7-c490d04e6e79 | -5.99189 | -44.71991 | 2026-09-22 05:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa15502e-ce6c-3f8e-85a5-a8967f582c2c | -6.86744 | -59.90549 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dabefc70-d6dd-3d94-9536-169191b76747 | -13.86874 | -48.57491 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 795df0b8-ce8a-395b-8541-6cfe75e7e32a | -1.21004 | -54.01381 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5428fb1-db43-3408-bece-88c2c20417f3 | -4.26177 | -55.44089 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43868cc6-0c97-3c44-a633-ca03be57bec7 | -6.31128 | -57.74006 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1271edd5-65b1-3fd7-9c5b-0b2f9351b98f | -8.31612 | -44.74403 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 730c2161-1856-3f58-b6da-77a0837e75a1 | -6.14471 | -55.69514 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fa3136d-7b76-3494-ad2f-5aa79d33ea5d | -3.44876 | -50.61763 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a87beecb-9acc-344b-89a3-6c773c3858ac | -6.16144 | -57.72349 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99de1668-9ba6-35d2-94c6-787942547e5b | -6.00027 | -55.68049 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e756e6f4-89df-3ce8-bce7-86b5f8de4f89 | -1.91472 | -58.26136 | 2026-09-22 05:23:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7138407-d5c6-35c7-97b1-3e9bad857766 | -7.40292 | -44.80859 | 2026-09-22 05:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75b19359-b957-3ead-8496-30c1944bbb4e | -3.45968 | -60.26733 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 755a3c74-1a39-3ef1-9eb1-72016e0a0f27 | -2.4454 | -57.86554 | 2026-09-22 05:23:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2becd52d-46fb-3411-b203-d90fafda92d4 | -6.31017 | -57.74702 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78adc4d7-dc70-3cd4-adc7-8fd1dbdf3f97 | -4.45339 | -55.44178 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 96ded868-58a1-359e-a87d-f737d4b44acc | -3.06478 | -61.28615 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8213e968-7b11-3b39-9646-0c3074c33ebf | -2.65405 | -59.68539 | 2026-09-22 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dff25c0f-b0bd-3faa-bcc8-82a042be9463 | -5.90194 | -51.77786 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dd148e81-2771-37fc-af24-ee9d1110c1bb | -6.31113 | -60.00088 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 986fb005-e3fa-3f8f-912f-90daeac4c187 | -6.91796 | -59.63724 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd2ac60a-cb16-3e36-8ff7-d3ecc0ee08a0 | -6.43739 | -59.97525 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfc60ffa-29b0-36ff-9803-4285472f1e26 | -3.44938 | -50.61359 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b288441-4685-36c2-9358-99a238f57da5 | -8.78482 | -44.29994 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f7b553ed-593f-35a8-bf40-ecab6d09491e | -6.31626 | -59.96915 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cd3d87e-e3b8-3d61-9e77-cde511d363be | -6.35249 | -55.74934 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 506c4897-cedf-3b82-8961-6a46dfa86a30 | -5.45539 | -60.14999 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f6ce7bd-fe9f-36a1-9b5b-c58ba1678168 | -2.92232 | -54.17798 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 653a0d8e-3232-3451-9ee9-68d185705fe0 | -6.73198 | -55.07578 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f12fb55-b1f3-342d-bbaf-e1e8d2ab33c6 | -7.54489 | -47.32318 | 2026-09-22 05:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dac9fff7-c859-3c32-98be-4418af036672 | -13.52175 | -51.51624 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 6140371c-fdcb-389f-8ebc-5eab8f0d2bb7 | -3.3124 | -57.85876 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84aaac57-7d40-3f86-86be-24bc9662af61 | -6.09167 | -57.69459 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eb37e4ef-fc6b-310e-be61-6bd153ec78a0 | -12.86737 | -50.94223 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| edfa7f61-a75c-3c6d-a6f8-4edc9cf956a6 | -6.67054 | -47.37708 | 2026-09-22 05:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd5ae3f2-2caf-3027-b742-33e76567bdac | -3.54477 | -60.5791 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9237f9d8-35a0-33e2-b781-ece2825aae2c | -12.8527 | -54.04771 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5268fc5d-8417-3b9b-87b4-9467ecfb6043 | -11.70216 | -50.99925 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d84608be-6ed8-3160-98d0-45e990611f56 | -4.34176 | -55.64499 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d746dfc6-629e-3866-84b4-90b24e43f10c | -10.90798 | -53.96646 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 862c3c59-e744-321c-b465-e3342c5d1c4b | -6.67633 | -50.94087 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 531642ec-6b0e-360c-9fd9-14369145f6dd | -2.93889 | -50.4919 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d49003c5-5b87-3953-bb33-386a2ac52dc6 | -5.81997 | -52.11629 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45690d67-226e-3bda-8076-3a7825d03355 | -6.42293 | -59.97721 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f46a663-30df-33b1-aea7-5bf57b1a42ef | -3.51958 | -52.74274 | 2026-09-22 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 559bb825-d816-360b-a7d7-52149cae9e66 | -12.87786 | -50.93805 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e262d30f-8e67-33ac-9ece-df00c0be856a | -9.1891 | -65.85674 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 993784ee-caff-3158-8ac2-9d00f0b0576c | -9.05905 | -48.77775 | 2026-09-22 05:23:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5122de8-3cff-30f7-85f5-233ce79a5760 | -6.75365 | -59.11698 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55385416-31f5-3d3b-8d77-cf40b8e492d4 | -6.71238 | -59.00512 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README76.md)
