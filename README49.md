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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3106630e-7d80-3529-b17e-b5de36ce5641 | 1.9133 | -55.7616 | 2026-10-03 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6dc1be74-abed-34d4-8212-8aced4d632c7 | 1.9316 | -55.8008 | 2026-10-03 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 9279ea8c-458d-3f80-a2c7-e2ca9ea05418 | -1.1712 | -49.3181 | 2026-10-03 15:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| cdd37fa7-5060-338a-a527-500b3ef21250 | -1.1163 | -49.0423 | 2026-10-03 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 0629f08b-9311-3f27-9ebe-a1d6a34aad9e | -1.0423 | -49.1921 | 2026-10-03 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 4385773a-10d2-3a71-9453-61034b41ac99 | -1.1897 | -49.3179 | 2026-10-03 15:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| fa08947d-c4b2-35c6-b94f-11e48bd10266 | 1.9793 | -50.84 | 2026-10-03 15:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 73.1 |
| bb6e991a-1c21-3919-ab2d-96ca6ff3c70f | -1.2082 | -49.2752 | 2026-10-03 15:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ad77ac97-96f2-330b-b533-c358460d2b31 | 1.9977 | -50.8397 | 2026-10-03 15:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 64.9 |
| a9b00ed0-b12b-321b-a57c-cb2dd9aa754a | 1.7583 | -50.8232 | 2026-10-03 15:10:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 80b98240-a656-3902-8289-4b32dd581f44 | -12.1967 | -57.1103 | 2026-10-03 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 246a5dca-5d27-38f6-8c27-78ecc9c1ecac | 1.9317 | -55.7416 | 2026-10-03 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| daebc62d-8119-3924-8ecc-80893a3d7ba7 | -2.0007 | -49.6647 | 2026-10-03 15:10:00 | GOES-19 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ea4f35bc-e787-3d68-8ea2-e2aecf0dabdd | 1.8037 | -55.6249 | 2026-10-03 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 78e2b700-ad87-3749-8128-441e80c297ff | 1.8037 | -55.6051 | 2026-10-03 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 0945b40e-b971-3bf7-a1ac-de9005cff5c3 | 1.7399 | -50.8026 | 2026-10-03 15:10:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 095a713d-d9f5-3cb9-aaab-695bde3bd5f5 | -1.0423 | -49.2134 | 2026-10-03 15:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 6de80b5e-545f-3640-9a5e-f110cd947e17 | -9.9175 | -65.0313 | 2026-10-03 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.6 |
| d9b756f0-6001-34e1-bf1a-c20c416bc577 | 1.7041 | -60.8399 | 2026-10-03 15:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 9e1fbb89-8284-3033-8961-3035b237ec8d | -1.1713 | -49.2969 | 2026-10-03 15:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0152223a-25df-3c5b-a6e4-ef4c5af65036 | 1.7399 | -50.8235 | 2026-10-03 15:10:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 54e47642-b668-3131-8c2c-1187ca04a509 | 1.95 | -55.7611 | 2026-10-03 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 88e81691-c260-3bd3-a569-7a5fa1818263 | -9.0584 | -66.1073 | 2026-10-03 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 924ce03a-3ad8-32ae-97ad-ddabe5ae7d7d | -9.0231 | -65.7169 | 2026-10-03 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| a94bf32f-1516-3e40-bbbc-ec6dda1e9048 | -9.0046 | -65.6988 | 2026-10-03 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 64a1404d-cef6-3ca5-b9b6-664322aa26f8 | 1.9608 | -50.882 | 2026-10-03 15:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 168cb2b6-ca9b-31da-86a3-110df852bbda | -4.7197 | -56.1473 | 2026-10-03 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 275053de-4f24-3e17-9458-ee5f79408d2c | -8.6665 | -66.936 | 2026-10-03 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 4d126437-4106-37ce-b044-133d0d8c5edb | -9.0232 | -65.6982 | 2026-10-03 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 72dc3a2c-eb03-3099-9426-1695242abafb | 1.8038 | -55.5656 | 2026-10-03 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d8e1413a-fa68-327e-b738-106ea91d1ee2 | 1.9424 | -50.8616 | 2026-10-03 15:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 613c4e5b-a24d-319e-86b2-3dfe136a9932 | 1.9132 | -55.8011 | 2026-10-03 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 5dc999b7-2097-3510-befb-bbf67f8f9fe5 | 1.9424 | -50.8824 | 2026-10-03 15:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 8c9d1be4-4b2e-3919-9366-35518e32cfb9 | 1.7854 | -55.6054 | 2026-10-03 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f50f8539-c6f9-3515-ae06-d8f2123195a2 | 3.4341 | -51.2808 | 2026-10-03 15:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 5a1eb338-d2c2-3e58-82e2-61f3ed9535fd | 1.8037 | -55.5854 | 2026-10-03 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 372940fc-028a-313c-aede-6077a93b8bae | -2.82 | -54.09 | 2026-10-03 15:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d22908db-e0ef-3c17-b691-8743093c31a9 | -1.1529 | -49.2334 | 2026-10-03 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 70382925-baf1-3652-ae1b-34d4c9cdf22c | -0.4889 | -49.1327 | 2026-10-03 15:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 18eecdcc-1a35-3bc5-b221-e2aa06f5258a | 1.9132 | -55.8208 | 2026-10-03 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 4db06a20-ae28-3464-8fbe-b84340ed34ab | 1.9608 | -50.8612 | 2026-10-03 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 21d7c782-8e58-3d63-8dd5-4d84b27d043c | -9.0584 | -66.1073 | 2026-10-03 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| afd90856-8034-34e0-b5a9-6e6167aa0200 | -12.1777 | -57.1119 | 2026-10-03 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| d542140c-8621-3035-a5f0-7e986dc213a3 | 1.7399 | -50.8235 | 2026-10-03 15:20:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 85902d51-f9c7-3b22-ab35-c5704552fa23 | 1.895 | -55.7816 | 2026-10-03 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4d9764c6-62f2-3c8e-9493-4a4ec2c4294e | 1.9424 | -50.8616 | 2026-10-03 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 9af64244-55b9-3c69-9b85-7ceb67ce64c8 | -1.1901 | -49.084 | 2026-10-03 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 802bdb60-1d33-3815-9361-172089fad347 | -9.0045 | -65.7174 | 2026-10-03 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| d87daee3-cbdb-3e02-bb94-e27630886154 | -9.8989 | -65.032 | 2026-10-03 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d00168ae-237b-344f-9b53-76de24d99946 | 1.8692 | -50.6753 | 2026-10-03 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 44a14d95-abc4-36d7-a27b-74f0b387401d | 1.1323 | -50.7277 | 2026-10-03 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f2b60df4-e855-3c6a-8350-b9f22ce731fb | -9.9175 | -65.0313 | 2026-10-03 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 162.1 |
| fd7e9e14-c3e0-369b-b7ee-cfad657755de | -9.9174 | -65.0501 | 2026-10-03 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 0cce627b-8bcc-3011-98d8-a06ca5192c75 | 1.9424 | -50.8824 | 2026-10-03 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 268cff09-6f2b-38f0-a431-7f197abb2be4 | -12.1775 | -57.1319 | 2026-10-03 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f8a1499a-9320-3500-b5fe-76b5b0d2cb3a | 1.4268 | -50.7866 | 2026-10-03 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3a3c07ed-9596-3e08-a720-325116f76cc2 | -1.0423 | -49.1921 | 2026-10-03 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 9798d3f3-4f6b-3434-b672-db252123648a | -9.0046 | -65.6988 | 2026-10-03 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 3cbc615e-f76c-332e-81b2-43db073536ca | 1.9316 | -55.7811 | 2026-10-03 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 326dd905-6792-3fbd-ad9c-552c9add6dac | -12.1967 | -57.1103 | 2026-10-03 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| aa2e29d4-d5d6-3c59-a2fd-02fbbde3123f | -8.6665 | -66.936 | 2026-10-03 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 980e9153-13f0-324e-a7a7-927df7f867cd | 1.7041 | -60.8399 | 2026-10-03 15:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d880bd03-9cae-3979-8067-3e92e542024a | -12.1385 | -63.1688 | 2026-10-03 15:30:00 | GOES-19 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1d7afcf3-9a8e-3ff5-a101-21a594a68258 | 1.9317 | -55.7416 | 2026-10-03 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| c5b2d4db-0638-3ea4-babd-352772c0759d | -9.9174 | -65.0501 | 2026-10-03 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 5ea4e997-cb05-3bd0-9147-c65dcd37eda9 | 1.9317 | -55.7219 | 2026-10-03 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 223a24b3-b979-39fb-9398-532c4d97ba28 | 1.8037 | -55.5854 | 2026-10-03 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1bef0fdd-95fd-3864-a351-0282ceee594a | -9.9175 | -65.0313 | 2026-10-03 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 191.0 |
| 24ce81cd-cfd3-3944-bb3c-1b52847358ce | -12.1777 | -57.1119 | 2026-10-03 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 8478e1ce-c95b-3781-9af5-dd685b20dfcb | 1.8036 | -55.6447 | 2026-10-03 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9f206bf2-f2e7-3b0f-addf-d6cf8ed70f75 | 1.7853 | -55.6251 | 2026-10-03 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a3906bda-dba8-32aa-bb57-f69f75c73d89 | 1.7583 | -50.8232 | 2026-10-03 15:30:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 85abe775-1235-3d34-b509-d16331d1ab2c | 1.95 | -55.7414 | 2026-10-03 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e93d8b42-41d4-3ad8-9fa7-971a9f1ccf30 | -9.8989 | -65.032 | 2026-10-03 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 90a3aa21-b1e6-3b1d-ba11-274432acaade | -12.1773 | -57.1519 | 2026-10-03 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| cb955450-6736-3e37-9167-85d006416970 | -9.0231 | -65.7169 | 2026-10-03 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| c8263cee-cbde-3570-9e56-e7502b4c4e05 | -9.0046 | -65.6988 | 2026-10-03 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 207.3 |
| 3ca9fa09-014a-3882-9dd3-b593d8a8f715 | 1.9316 | -55.7811 | 2026-10-03 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 47b3056f-1bdf-38f2-900c-2728b9c17670 | -12.1967 | -57.1103 | 2026-10-03 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 667a33a5-978a-3819-892d-581c5cf6f941 | 1.7399 | -50.8026 | 2026-10-03 15:30:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 27442e1e-cef8-36c8-b522-cd277812ffcf | -8.6665 | -66.936 | 2026-10-03 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| f3567caf-9945-3f24-9fd1-fbc4d1da0fe5 | 1.7041 | -60.8399 | 2026-10-03 15:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.4 |
| d87f7716-6fb8-3dde-b9ab-cbf0827fcc44 | 1.8037 | -55.6249 | 2026-10-03 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 59913d7d-d8d3-35f3-b2bb-e183e621bcc5 | 1.9133 | -55.7813 | 2026-10-03 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f0983ade-310f-398c-af74-681190ec22f9 | 1.6476 | -50.9082 | 2026-10-03 15:30:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a70162bc-4fd1-3dea-adb4-65500760550c | 2.0138 | -61.0826 | 2026-10-03 15:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 76.7 |
| c39ac262-1cf4-37a9-9acf-544064231b81 | -2.5493 | -57.9986 | 2026-10-03 15:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| ecd64fb6-dcb9-35c6-85bc-0d25d9abb898 | -9.0045 | -65.7174 | 2026-10-03 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 24ff61e0-2661-3c27-8af7-be5b8286fef1 | 1.8038 | -55.5656 | 2026-10-03 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 0c444cb0-2472-3950-a09e-06f4aa839a69 | -9.0615 | -65.4169 | 2026-10-03 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 83cce9a7-45eb-366a-a37a-0fe1508c806e | -12.1383 | -63.1879 | 2026-10-03 15:30:00 | GOES-19 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 32451cd6-6d83-3df3-b42b-a60ec157977c | 1.8319 | -50.8427 | 2026-10-03 15:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7ad1831b-1fdc-33b8-8bd7-330e49f9d2dc | -1.0911 | -54.1202 | 2026-10-03 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| bae17398-bf74-3b9d-9044-a6eb24b89bae | -9.1173 | -65.3777 | 2026-10-03 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 80c3f81f-1fef-3586-862f-83948c00b642 | -9.7499 | -65.075 | 2026-10-03 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 95dfabda-8b07-3c5c-926e-1b7fed5e10c4 | -9.9175 | -65.0313 | 2026-10-03 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 216.5 |
| 2bf5fca8-b40a-3620-b8af-d4f1bc63c5f7 | -9.3764 | -65.4813 | 2026-10-03 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 6a1388d6-71ee-3384-9aaa-4090e8bedc28 | -8.8705 | -66.7822 | 2026-10-03 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 6b5180c3-7f7b-31dd-b560-edaeb9cd5a25 | -9.4565 | -64.3344 | 2026-10-03 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 2cd0ca86-8620-3e05-90ac-368da25e7045 | 1.7399 | -50.8026 | 2026-10-03 15:40:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 64.7 |


[Clique aqui para ver as próximas entradas](README50.md)
