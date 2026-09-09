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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12b0f06b-7f69-38eb-b2ae-9e5fa0050198 | -10.6999 | -46.0153 | 2026-09-09 16:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 7d42e693-cb0a-3045-9a00-9ef210681459 | -10.7003 | -45.9925 | 2026-09-09 16:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 321.5 |
| 75a06ec4-fe5e-39c3-87ef-19327ed750ba | -2.0934 | -49.5359 | 2026-09-09 16:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 76d114fb-2ecf-30d6-a016-392888854c2b | -10.701 | -45.9471 | 2026-09-09 16:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 9b5b8373-2fcc-3d5c-b8b8-916cd5176d8b | -12.5198 | -62.6679 | 2026-09-09 16:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 27ac7aeb-7b58-30b5-969f-9d51aa9a0bfc | -12.4642 | -62.5366 | 2026-09-09 16:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 659b2dc9-8112-3563-a769-0a83c2b034ae | -10.6995 | -46.038 | 2026-09-09 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 0486dbd1-5b51-38d6-ac18-c4f620d7da91 | -10.7395 | -45.9194 | 2026-09-09 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.4 |
| f3543d95-4d60-31ac-92ac-58e61a7cc1ab | -12.4831 | -62.5354 | 2026-09-09 17:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 5d76c61b-5cce-3b40-a2d9-9c11b6fa5793 | -10.6999 | -46.0153 | 2026-09-09 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 1d21f30f-d71e-3886-a51a-f75e284c64fb | -10.7387 | -45.9649 | 2026-09-09 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 07d92376-bd98-3e57-bae3-2300d905a611 | -10.7578 | -45.9624 | 2026-09-09 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 96652d3e-5290-3369-90c2-6bb99c24f7c1 | -10.7391 | -45.9422 | 2026-09-09 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.7 |
| e380e1bc-611a-3626-8442-a0e37ee4f960 | -10.7006 | -45.9698 | 2026-09-09 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 12a0ea1e-fe1a-3fac-baf1-6f947553ce0e | -10.7391 | -45.9422 | 2026-09-09 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 0b0279bb-1678-3b93-b6e6-ae7ab90b9ab0 | -2.0585 | -56.4284 | 2026-09-09 17:10:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a3b6f156-9596-3536-9fa5-95e5712069ea | -10.7006 | -45.9698 | 2026-09-09 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 322.4 |
| 9d15570b-d3d3-3a37-a141-4820eca0a4f3 | -12.4831 | -62.5354 | 2026-09-09 17:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| fdd6b686-2c62-3e63-a0c1-d2a064dc4475 | -10.701 | -45.9471 | 2026-09-09 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.1 |
| b9333890-19a5-3555-9b29-a76fbc8cdc57 | -10.7003 | -45.9925 | 2026-09-09 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 281.9 |
| 7c5226ed-9b18-3591-a7af-2ee634c996cb | -1.4944 | -54.2563 | 2026-09-09 17:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| d06685d3-0959-3d11-b537-7abe3dec9d74 | -10.69 | -46.01 | 2026-09-09 17:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 175a9a62-1a4d-3e19-8c94-248d39f5a7bc | -10.26 | -45.29 | 2026-09-09 17:15:00 | MSG-03 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 37c0d1ef-5452-3314-b12f-1f2f0a9e6265 | -4.98 | -36.9 | 2026-09-09 17:15:00 | MSG-03 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| c8a3c9d4-4b98-3371-a121-ed3910cfc106 | -10.43 | -42.76 | 2026-09-09 17:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5ab0a6e2-4b36-309b-8cb6-531972d45767 | -8.6881 | -62.4382 | 2026-09-09 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 0714f813-98a8-36cd-87c2-40705ab43eea | -10.6995 | -46.038 | 2026-09-09 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 29129abc-dd3f-32ce-98ab-ed67c9fcb20e | -12.5198 | -62.6679 | 2026-09-09 17:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 193.5 |
| 23a9be63-55b2-393b-a0ae-a1bb13d98f5c | -10.6999 | -46.0153 | 2026-09-09 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 8c1ed423-c2bd-33f7-ae8a-070de7a08860 | -2.0585 | -56.4284 | 2026-09-09 17:20:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 12775c96-0700-338d-9457-2486929fd60d | -2.0586 | -56.4088 | 2026-09-09 17:20:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9d026575-a15f-3653-b435-9a593c2977f2 | -10.7006 | -45.9698 | 2026-09-09 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 499.5 |
| f0f003c3-b898-37f4-9b01-284c78e26564 | -10.7387 | -45.9649 | 2026-09-09 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 2813da30-bb28-3ebd-a2a4-73110a424f8c | -1.4944 | -54.2563 | 2026-09-09 17:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 62b3b251-be6b-307a-b38d-c4708a5733d0 | -10.7003 | -45.9925 | 2026-09-09 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 334.5 |
| 5831a6c7-d66c-3f6d-bec2-ce2a286b43c1 | -10.701 | -45.9471 | 2026-09-09 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 3193dee8-075b-361c-9e18-44b34d70cddc | -10.7395 | -45.9194 | 2026-09-09 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.9 |
| d00eecf2-28bb-3945-a720-9c487c5dec60 | -10.7006 | -45.9698 | 2026-09-09 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.9 |
| ee6b23da-3c49-339a-90d4-f4a9500f5e94 | -12.5198 | -62.6679 | 2026-09-09 17:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 42f2999e-9de1-3163-bf43-9b43c7fc0a47 | -2.1179 | -54.3874 | 2026-09-09 17:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| ce60e5f9-e169-3d78-bd16-0cda9359bfd9 | -8.7066 | -62.4374 | 2026-09-09 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.4 |
| a06860e9-0cad-3f41-956a-46c40a6b7a12 | -2.0585 | -56.4284 | 2026-09-09 17:30:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c06f4c0e-a030-3614-9231-4fc887330e85 | -10.7391 | -45.9422 | 2026-09-09 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 654.0 |
| c3af165f-93c9-3aba-a9d2-5778d77de933 | -10.7003 | -45.9925 | 2026-09-09 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 288.2 |
| 9f244b8a-114b-3c54-b07d-df33eb8f6310 | -9.7127 | -43.4899 | 2026-09-09 17:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 41c6cb10-3043-3f9a-b60d-146e521577b3 | -2.4653 | -54.8802 | 2026-09-09 17:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d7e8883e-a9ca-343f-bcd7-052dc676b198 | -9.0245 | -65.3994 | 2026-09-09 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 42bd5613-bd46-3c32-8512-aadfee031053 | -6.1176 | -59.9261 | 2026-09-09 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 61cc048d-1a9e-39ec-a085-f15af4c9b215 | -10.7578 | -45.9624 | 2026-09-09 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 290.7 |
| d360e9e4-94bd-37df-b4d4-0874722889d3 | -10.7387 | -45.9649 | 2026-09-09 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 267.9 |
| 630df232-5d7d-393b-91de-d5a4a9eaddf4 | -6.099 | -59.965 | 2026-09-09 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 193.9 |
| df1982d3-a4de-3ed6-860c-4d80cba88cae | -8.6881 | -62.4382 | 2026-09-09 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 1f762352-2683-321f-8689-2f06ae70b8d8 | -6.7832 | -59.4401 | 2026-09-09 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 7f7dd89f-4354-3f28-82f0-2f629598d6a2 | -10.7391 | -45.9422 | 2026-09-09 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 53e3e7a3-3f97-3f7a-b827-480d091f6bd4 | -9.7127 | -43.4899 | 2026-09-09 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 319.5 |
| 0e7733b0-1229-366c-bd97-fd6f988c7133 | -8.688 | -62.4572 | 2026-09-09 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 40a28871-2a95-35e7-a42e-1b9ae1c3f846 | -9.7138 | -43.4192 | 2026-09-09 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 161.5 |
| 17935c07-d29e-3684-b5e0-99aefbf8ce99 | -9.7134 | -43.4428 | 2026-09-09 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| a1d2a233-6f35-3b38-9a8f-c91687613116 | -2.4653 | -54.9001 | 2026-09-09 17:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5455512f-20b2-3c3a-8707-ebb0ae6ca574 | -10.6816 | -45.9723 | 2026-09-09 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 4e4470a6-2fb8-396d-b65e-5786940e0cee | -2.0585 | -56.4284 | 2026-09-09 17:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e848e62e-a1dd-3561-ae8d-b29979913983 | -12.4831 | -62.5354 | 2026-09-09 17:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 0d5032a6-d23a-3155-ad39-f5e6ef9e6e34 | -10.7003 | -45.9925 | 2026-09-09 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 8f8c0e65-dc71-34d7-bbfd-a93332070a40 | -6.8387 | -59.4186 | 2026-09-09 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 2fd3539d-f2d6-36cb-b694-8d11153bd919 | -9.7131 | -43.4664 | 2026-09-09 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| f0b17c7e-adc5-3072-aa33-2d1f060a7f2f | -10.2563 | -45.2062 | 2026-09-09 17:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 130f4729-fd48-3312-ba71-d969db808b2e | -8.9598 | -44.4204 | 2026-09-09 17:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 91d88c5e-5f71-3866-bc84-b25a0ad79de3 | -8.7066 | -62.4374 | 2026-09-09 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 47cb46c7-c6da-3048-9cef-14c2d665b50b | -1.1991 | -55.7304 | 2026-09-09 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ee01e630-4aa0-3745-a1f9-efdbdcff53f1 | -6.6357 | -59.4459 | 2026-09-09 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 380117e2-2047-3aed-888e-756161aee011 | -10.2559 | -45.2292 | 2026-09-09 17:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 349.9 |
| e79e9b50-3c7b-3e98-8342-8682c9b6588f | -12.5198 | -62.6679 | 2026-09-09 17:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 118.0 |
| c65602b4-187e-3039-8d07-7b045ad07258 | -8.3904 | -62.6774 | 2026-09-09 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |


