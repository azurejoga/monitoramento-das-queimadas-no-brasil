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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdc21b4e-395a-3d7a-a548-3ba472ab926e | -1.12622 | -53.44788 | 2024-10-17 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71c25855-c4a8-38b5-a1df-37c71926e487 | -1.12567 | -53.4514 | 2024-10-17 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e21ae2e4-7b0c-3e37-b95b-823ef853e866 | -1.11951 | -53.70829 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 33f3bb40-8d9b-364e-b5ec-43c58164f2ea | -1.05 | -53.37067 | 2024-10-17 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a1d6957-d792-3093-a1fd-dc6a71d569a3 | -1.04075 | -53.51672 | 2024-10-17 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2c45d4b-160c-3809-a00e-99b2fcba13ad | -1.02389 | -53.73218 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0568cbd0-63bf-3ede-9bac-1c9343da280c | -2.94993 | -54.14622 | 2024-10-17 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 840fa6a0-1293-3c67-9e7f-76e8696e3ec8 | -2.94553 | -54.15267 | 2024-10-17 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1f15a9cf-0ddc-3418-83cc-b5d8fa4a1769 | -2.94499 | -54.15615 | 2024-10-17 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6fe08f7c-28b6-3ff5-9f6e-6eb670428054 | -2.87646 | -54.18106 | 2024-10-17 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f320906-a575-34c6-b138-9c5b04b64a4d | -2.87315 | -54.18055 | 2024-10-17 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 408c0b39-b296-375c-a5e0-3a0c1762b20c | -2.82306 | -54.15153 | 2024-10-17 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34a92129-8ecc-3eee-ab39-dd0840457699 | -2.79887 | -54.19747 | 2024-10-17 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53e47d62-6850-3864-bec2-434d8277fee4 | -2.78845 | -54.02504 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beb07788-1c43-37bd-974e-6f212a6e3dd2 | -2.78791 | -54.02853 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98ac0c74-1da2-323f-bf7e-00e61c91ed4b | -2.56928 | -54.01218 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7729aa9a-437f-3597-b3a8-60e417b86639 | -2.56596 | -54.01167 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fabd6935-a356-38e3-a6a5-0810c4736f59 | -2.51762 | -54.10372 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aad2e574-63fa-3d71-8727-e5524bdb92dc | -2.38933 | -53.7263 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c85cd87-41cf-3a08-b853-75ba963e6471 | -1.28755 | -55.52121 | 2024-10-17 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0199cbd-2c45-3d34-ac44-2f18dcf11ef6 | -1.28423 | -55.5207 | 2024-10-17 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4692d0f-0b18-3500-ba98-c244ec8d1b89 | -6.27566 | -56.52495 | 2024-10-17 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f526548b-4dcd-33d6-a889-722703bc982b | -6.3453 | -58.18495 | 2024-10-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31b827ed-6df1-3656-8c4b-fe5ebf4714db | -6.34434 | -58.16898 | 2024-10-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14e87af0-125b-3e64-95cd-99ce1b1861a8 | -6.34086 | -58.16841 | 2024-10-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9d7b80a-a76c-35e8-af57-d0978b0e3089 | -6.34023 | -58.17228 | 2024-10-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74b5ab28-1676-34f3-9643-01089aede750 | -5.85353 | -57.53173 | 2024-10-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57d29426-2de8-3f6f-b269-12c245b3151b | 1.30398 | -60.41276 | 2024-10-17 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 336672dc-35bf-3425-8bfc-c93fd1f0b424 | 1.30383 | -60.41299 | 2024-10-17 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ea1754a-d7f8-39f8-8e4a-4183742f337c | 1.2972 | -60.42702 | 2024-10-17 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c785c181-ded1-3787-b120-83c01baf6943 | 0.68435 | -59.64156 | 2024-10-17 05:04:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59b06ae0-d27c-35fb-ad02-c61636b4bd1e | -3.92 | -42.39 | 2024-10-17 05:05:04 | MSG-03 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7b394e74-7bed-3ef9-bfd0-e2cf110ae7f0 | -2.9674 | -47.9931 | 2024-10-17 05:05:22 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 385119aa-8ac0-3630-b4f6-199ef498a3c2 | -3.5086 | -51.1122 | 2024-10-17 05:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6dcb1aa2-90b4-3b56-a542-91a074821664 | -3.7007 | -45.9223 | 2024-10-17 05:05:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 1f6e871d-8a44-3e07-a440-891ef98d088f | -3.7009 | -45.9 | 2024-10-17 05:05:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| f0f4a939-3ee7-3ad2-b035-b6947dcc5b29 | -3.7574 | -45.7634 | 2024-10-17 05:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 674e9c34-9e2c-3650-8881-103989277bd5 | -3.7575 | -45.741 | 2024-10-17 05:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 4b4403c9-13d3-3c57-aeed-017f0f1e5424 | -3.7761 | -45.7402 | 2024-10-17 05:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| fd822f4d-d303-3ed8-9a0f-1761f9fdade6 | -3.9078 | -42.4256 | 2024-10-17 05:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 52.5 |
| c2a50728-9cbd-361c-b855-03161c63bb63 | -3.908 | -42.402 | 2024-10-17 05:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 141.4 |
| b5c4b5e0-c0a5-369c-ba03-42f5057094cb | -3.9081 | -42.3784 | 2024-10-17 05:05:28 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 50.0 |
| cbb15a3a-61b2-3f4a-88e2-2bce8849b763 | -3.9265 | -42.4246 | 2024-10-17 05:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 60665ad4-2b7b-3ade-8ea6-3b16fc7fc084 | -3.9267 | -42.401 | 2024-10-17 05:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 197.6 |
| be21574d-2f5c-3d09-a2d0-e7df62ed9590 | -3.9268 | -42.3773 | 2024-10-17 05:05:28 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| cdf1ed0e-2ec7-3d4c-bddc-49238bcf1281 | -5.9788 | -45.3621 | 2024-10-17 05:05:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 96ecfb10-ba1b-36b0-97e8-89ca7e6348e2 | -9.1552 | -61.9047 | 2024-10-17 05:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| bd2cac86-98c0-39fb-be33-1a5cfe1c796e | -8.45709 | -66.96416 | 2024-10-17 05:06:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a73ec02d-f9e8-3389-8249-b75dc2468c09 | -8.45285 | -66.95451 | 2024-10-17 05:06:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f802afc9-eb18-3594-afb0-8b740df66f3f | -8.45205 | -66.95879 | 2024-10-17 05:06:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d5a8eba-c11e-3096-ab2d-9f0eb5e441a2 | -8.45125 | -66.96306 | 2024-10-17 05:06:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6057c74-e180-340d-971a-2d83785b7fff | -9.19089 | -66.07593 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2395e97f-f7eb-3bdf-909d-88c7dd800c80 | -9.19021 | -66.07953 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23647f8e-5c31-39f7-9812-1e4780c03dd3 | -9.18998 | -66.07552 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b042aeb-c960-34d6-b914-7f4592744b0d | -9.18932 | -66.07914 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1c23a71-39f8-31c0-a0c3-b6b356c49c84 | -9.18804 | -66.08613 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f74b1ee-22c7-363a-b16e-51d6026b3aca | -9.1874 | -66.08968 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f04d6e1b-ca43-307e-939c-1cfaf9f16aec | -10.29826 | -67.53349 | 2024-10-17 05:06:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbd08858-424d-3c45-9473-ce8ee6b690cb | -10.09962 | -67.34843 | 2024-10-17 05:06:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4abde55-d661-3968-9f56-ea5351f5e333 | -10.09883 | -67.22758 | 2024-10-17 05:06:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9744be0c-1e33-33f8-abd9-7a11aa3943a7 | -10.09309 | -67.2263 | 2024-10-17 05:06:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0810994-8938-3606-90f7-1ad002b29c92 | -9.81648 | -67.26155 | 2024-10-17 05:06:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3b4dba5-02dc-3a8a-8c0a-eb5ed753b47a | -9.68003 | -67.37961 | 2024-10-17 05:06:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 600df970-f49b-3ed7-b67d-1c5f2273f2e2 | -9.66948 | -66.83254 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 879d2f53-61d1-3455-823d-85093033d688 | -9.66382 | -66.83141 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccaf20fe-6036-33ee-98ed-8d98071db2ec | -9.57397 | -66.64108 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23152343-a341-3759-8263-3ab8d7e34e8c | -9.56834 | -66.64008 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b9864b7-4269-3270-bfee-a2cc8c2160a8 | -9.55855 | -66.72264 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14958bac-2f4c-309b-9c6e-ec5e46804d29 | -9.55781 | -66.72652 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90735548-379b-3fb9-b2f3-8e53dea97fbc | -9.55707 | -66.73042 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3608ed53-2efe-3ee4-9cb3-55a8333d90d7 | -9.55363 | -66.7177 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7b0e6aa-1358-3554-9ff6-db7a1c3b9737 | -9.5529 | -66.72158 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 129ac347-7e39-36d4-8caa-dafd23eeb409 | -9.49765 | -67.10673 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53c67d69-022f-395f-9c97-9f5be7e79ed8 | -9.49687 | -67.11081 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d567452-1799-3d54-bb9f-e7a1bdfc5b69 | -9.47527 | -67.09826 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e21d70f-d4eb-3e15-b5f9-31573e3c9524 | -9.47184 | -67.08485 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de13cc3b-90e3-3e44-a1f8-653b30eed686 | -9.47105 | -67.08897 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5bb3d17-1a2b-3db3-bd53-f775abeddb6c | -9.46947 | -67.09718 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e58dee0e-7857-3d79-9008-05982ec8f8ef | -9.46492 | -67.15234 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13ef4dd7-7691-36a7-af99-2acd91884302 | -9.46366 | -67.09621 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb05d8fd-70ea-3f03-ac81-62646f3d403e | -9.45829 | -67.15555 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e152df4b-23f2-32dc-a49c-63720a15a3db | -9.4541 | -67.14597 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 572678c1-74e1-3235-baaf-90227d5b4f7d | -9.44891 | -67.14409 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58f1a2c0-9c57-3a88-89d2-01b60200ff05 | -9.44828 | -67.14494 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d03d8969-c0dd-3fbd-bee2-0e80f22cd3d7 | -9.44812 | -67.14833 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15919333-0a78-3e5b-8313-c4a9175c3669 | -9.44746 | -67.14919 | 2024-10-17 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 502fd8ee-6757-32c7-a465-9dc90f54078f | -9.41731 | -67.8249 | 2024-10-17 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7f47418-51c9-3aa7-ab16-1e324115ff84 | -9.76901 | -68.81159 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 28b88c57-99a6-30ea-811b-bce634fc048e | -9.76874 | -68.80645 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0ee29af-80c7-3506-b240-0110302db905 | -9.76769 | -68.81188 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 844bf148-af8f-3b35-8ec6-d5e1c809e4d2 | -9.68527 | -68.59262 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f1a7dad-b3d7-3622-9c6a-d6cb67c345cf | -9.68421 | -68.59792 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c082c2c-1aca-319a-a460-7334ccd02a91 | -9.68308 | -68.57074 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9894e645-f757-351d-bb1f-4ad3e980fa89 | -9.68295 | -68.59029 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da2169c5-6adf-3899-89c4-c48d610c2c69 | -9.68192 | -68.59563 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00f845d1-85bd-3e54-9e45-f8666eeaa6e5 | -9.68062 | -68.5684 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dc016cec-2198-3f0b-905b-508bf807dfb5 | -9.67964 | -68.57349 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8282e685-f736-3787-914f-907573ccf738 | -9.67895 | -68.59136 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37d3243c-77e4-3b5d-b5f2-c31df1701837 | -9.67677 | -68.56949 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0418957b-6326-3375-8b9f-159b6ac6de9e | -9.67263 | -68.59016 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README44.md)
