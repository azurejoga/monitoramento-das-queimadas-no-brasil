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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dc3e0a9-ac8a-3c16-9745-6407431ee895 | 0.45452 | -60.48479 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08062355-b3f4-3a41-a6ca-65036c63c04d | 0.44967 | -60.48923 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f162eb9-129f-3b4f-a768-0fd0a4423383 | 1.6933 | -61.07705 | 2025-11-06 05:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 436af299-5d00-3bf0-9d6e-b5264ce656c1 | -1.64283 | -53.71842 | 2025-11-06 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42e207ef-31ca-3f2f-a8cb-1b5f7a4d0ec1 | 2.12735 | -50.85638 | 2025-11-06 05:12:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd9d2109-3b1c-3a51-9877-8a546bd57018 | 0.44742 | -60.49102 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8becaea3-73ee-3d70-8666-914adc9032d9 | 0.45137 | -60.49039 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffe6b599-a18c-3c4b-8668-a7a15f9eff87 | 3.30402 | -51.35226 | 2025-11-06 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c340d661-619e-397b-9515-890e4e531530 | -1.64574 | -53.72292 | 2025-11-06 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c736ae3d-3a00-3e22-a786-6cfebc8d2b93 | 0.44582 | -60.48101 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d8c0317-c136-35b0-b0c9-c6a41029134f | -1.62575 | -54.71389 | 2025-11-06 05:12:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 520b5dd8-498d-3108-84e1-6095ad752f1e | -1.64989 | -53.71954 | 2025-11-06 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca3d1f2a-9b40-34c7-b5a6-e30295bf46ca | -0.76261 | -48.53508 | 2025-11-06 05:12:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 166bc040-b5f2-3bf7-a228-ec0f4e012c9a | -1.62236 | -54.71334 | 2025-11-06 05:12:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 566eeb66-6810-3746-96b6-e08134f93e73 | -1.33761 | -55.46219 | 2025-11-06 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b79c1d0-f799-3136-ac39-22bf717f5491 | -1.63988 | -54.06196 | 2025-11-06 05:12:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f71a5d5c-41e5-3b96-b007-9042579b96db | -1.9611 | -52.06713 | 2025-11-06 05:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b498244c-fe7a-3594-b51a-b506d1c98f35 | -1.64406 | -53.71058 | 2025-11-06 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de8b362d-480b-39b3-9ffe-d781e6d88186 | -1.97457 | -52.10852 | 2025-11-06 05:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccd01149-d999-3922-a648-cb949b410ca0 | -0.76459 | -48.53406 | 2025-11-06 05:12:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12daaf6c-f737-38d7-b38a-91c24fc20e13 | 0.44347 | -60.49165 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7755ec5c-85d5-37df-b1a6-227fef9532c6 | 0.44815 | -60.47923 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23131fba-cebf-3f36-98f5-11277bcd130f | -1.64636 | -53.71899 | 2025-11-06 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc0839f9-7c21-3484-a4f2-720395153293 | 0.44662 | -60.48602 | 2025-11-06 05:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a93a469f-5dc8-3e48-8475-2a64b01c3f9d | -1.63931 | -53.71785 | 2025-11-06 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 959b28b4-3c30-3c74-9ee7-15e4e7b96084 | -0.36185 | -51.73005 | 2025-11-06 05:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21800712-22ed-3e50-9c1a-6f354df24d10 | -4.46105 | -43.23173 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5dfbb2e2-3fc3-3bb1-9b96-ac15f3037def | -3.81372 | -53.47094 | 2025-11-06 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aeb47b2-43f7-3a47-9673-b910ec901252 | -3.82816 | -49.81337 | 2025-11-06 05:14:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 551b3942-e4f1-3138-b3b3-ae1fbf9734fa | -3.14505 | -50.28778 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 216cfb5d-2479-3488-a081-da2d077d65c0 | -3.86836 | -48.33327 | 2025-11-06 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d61f234-a114-307c-b016-910534ed45b1 | -2.967 | -51.53323 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac0e82c0-d945-3860-8b65-e66cbf083d1d | -2.80697 | -50.27247 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b995921-cc3e-36bb-9948-37218cddbef5 | -3.92934 | -47.70025 | 2025-11-06 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a46e6824-3894-324b-ab6b-539cc15cbd16 | -4.00062 | -55.46776 | 2025-11-06 05:14:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aafe8589-06e1-352b-bf1e-0e2506d67f9e | -3.86484 | -52.60366 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ec5ba63-2d85-3dca-8c09-639c211b32cc | -2.897 | -50.47464 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7db96fb4-52a8-3d44-9e48-241d73c16c6c | -2.9826 | -51.35029 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2ae5ff0-6c1a-3931-b331-b7e6bf8c2a81 | -8.06814 | -54.92464 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a3a036a-e918-37f9-9484-23c3a041f4a0 | -2.1554 | -53.64196 | 2025-11-06 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6d12130-711c-3a0e-829d-c83d3f3291f1 | -6.6206 | -55.01779 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54068f9a-0da9-34de-883f-a2310c0df21b | -4.54211 | -46.44381 | 2025-11-06 05:14:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0916cba2-7225-30d6-8327-c01c62552123 | -3.11365 | -51.03057 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4f6bd3d-588b-31b7-9091-e86d86344aff | -2.46222 | -57.91266 | 2025-11-06 05:14:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ba6b46df-d210-3b50-9678-cad46bf6bb12 | -3.90213 | -55.80954 | 2025-11-06 05:14:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e763598-15bb-324d-b104-a53ec1fe4d2e | -3.9013 | -51.28573 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e9db4e4-a5a5-3cac-be3e-6344c8cbc7fc | -2.98672 | -51.35093 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7c004fb-790b-360f-a8af-de1ff55e5e5f | -3.11684 | -51.20675 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6051974c-293d-38a0-971e-14b47f5f9fa2 | -4.36662 | -50.88967 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f274ced6-16dc-3b4a-824b-64918705ccf6 | -4.43229 | -50.606 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7576bbf-d2f2-326c-b883-7d5d430e8066 | -3.62005 | -43.53397 | 2025-11-06 05:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d798c3d-cf99-3b4e-9d3a-4fce0741e29b | -2.78727 | -50.31322 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 075a2c42-1c53-3c80-a983-e30946f267db | -3.78157 | -51.68058 | 2025-11-06 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bde78886-d800-398c-8d39-4e9da074e351 | -4.14177 | -54.92045 | 2025-11-06 05:14:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cce40aaa-f4be-3b1f-8362-237e683f5714 | -3.60797 | -43.5193 | 2025-11-06 05:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00309d40-98fd-3e0b-ad1b-6bb2e45b1300 | -3.93031 | -47.69362 | 2025-11-06 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 93046349-1a3f-3fd2-8c94-8839d2104b84 | -2.93214 | -51.30941 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ab6cbff-ce5b-3e43-af0c-a8bc2a501f4b | -3.46894 | -43.64959 | 2025-11-06 05:14:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 76cd9f7a-0f00-3073-aa2f-5ca59cbf9ea8 | -3.47581 | -43.65079 | 2025-11-06 05:14:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 15f48cfa-6854-3b8c-b4ac-6b85ea0998a7 | -3.77764 | -51.25167 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d080cbc9-1e32-36d2-af48-15b6a01980fa | -3.83837 | -55.97599 | 2025-11-06 05:14:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63508d61-a2f1-3b25-874a-cc601e4135fc | -3.14883 | -50.29278 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6335c51d-79ec-3aa2-a35f-5d0cb0cca45c | -3.9021 | -51.28482 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ddc2f20-2c31-3de7-82b2-0d184586f1bf | -3.22562 | -50.94243 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87024fc4-9010-36be-a5a9-6f200c02e9b5 | -3.14439 | -50.29212 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5168bbca-626f-303c-84c0-a48e19d29d74 | -3.78211 | -51.67702 | 2025-11-06 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2da02061-a6c5-3b58-aae5-3d51b29afa97 | -3.41536 | -52.76952 | 2025-11-06 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fad52b88-554e-381a-8fd5-314428ea0bf4 | -3.93079 | -47.69027 | 2025-11-06 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f39791da-c1f1-3ca6-8aa5-e191430110b4 | -3.5046 | -51.54337 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 51b4c7bd-16f8-304c-aa2c-12d24df22a9f | -3.22622 | -50.93846 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bc621f5-86c6-3436-82f7-c93edd0f6982 | -3.10795 | -51.20914 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 997f3d5a-2422-3765-bdfa-7ca374d7a142 | -4.49644 | -50.74498 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e837868d-22c6-3bfa-b3a4-45b5c07c0211 | -6.11965 | -57.71033 | 2025-11-06 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75ce0683-3c15-34c1-8e87-e16805fb30c4 | -4.4958 | -50.74921 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fdfdb3a-d2ee-3bf2-be67-a6a339fa91c0 | -4.59384 | -43.34101 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| eae98a90-385f-3ef7-8a0d-a7942ae24cec | -4.57964 | -43.33867 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d87473ad-0113-31b1-811a-3e51a795cbe1 | -3.2547 | -51.20352 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97b2e867-eb1b-35a9-a39b-bdbb4d09f3d1 | -3.48176 | -43.65828 | 2025-11-06 05:14:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| edf84572-ea17-3441-824b-d5fc3a04503f | -3.01903 | -51.19618 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 698c69e1-73f5-3267-9bc7-11fc81b9d87e | -2.79168 | -50.31386 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7181b869-6bd6-3d6e-a98e-d5607bbb03e5 | -3.04289 | -49.51551 | 2025-11-06 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a739c9ab-773f-3f27-ade2-0c17094a5588 | -3.92982 | -47.69696 | 2025-11-06 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ec4ed623-b504-382b-9f9f-2d1e402e7bb0 | -8.11653 | -55.07935 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b783b1ac-0d5b-3ec8-8002-97a653a5fb4b | -3.41915 | -52.77013 | 2025-11-06 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e23d7efa-776f-39c0-90b5-ce30f543ddf1 | -3.46987 | -43.64314 | 2025-11-06 05:14:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5ac42cf3-668c-3da6-a29a-5be203ead84a | -3.82062 | -51.3091 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e5c7c99-679f-3835-8d5f-5bca198085ae | -3.40617 | -50.27333 | 2025-11-06 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 083f34d0-f45c-3caf-8cf8-90cb9de2116a | -3.92397 | -47.69941 | 2025-11-06 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c2c4228f-c1ba-3c83-a179-e851035e65c0 | -3.33153 | -52.09645 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fde1c68a-0aa5-3c56-83cf-527003f16a02 | -2.83626 | -57.64704 | 2025-11-06 05:14:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 360fa04f-18a2-37d2-b94e-ee1738ada9f0 | -3.92493 | -47.69282 | 2025-11-06 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eb4e1ceb-110a-39e1-916b-f3e0167cde42 | -3.33546 | -52.09711 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74912815-fd8d-3ed3-9b69-4333a42849bb | -4.46919 | -43.22568 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84b24b06-9db8-3a98-986f-2a4f03bd5031 | -3.47398 | -43.66339 | 2025-11-06 05:14:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cbb4cf7b-48b3-3b35-a677-48f096aaa220 | -2.89763 | -50.47052 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e67cad02-f8a3-3bf0-9bf4-ec68c6ef31a3 | -3.14949 | -50.28843 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5055f572-419b-3d82-8ead-183d27a3e41d | -2.98278 | -52.82368 | 2025-11-06 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8132a307-95cf-37df-9728-e11161a3c50b | -4.43169 | -50.60398 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 256127a2-4583-3dbd-8db4-a95223f265a4 | -8.12008 | -55.07991 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c45a3afd-ff6b-3be6-ac02-938d31a50179 | -4.87327 | -56.08974 | 2025-11-06 05:14:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README24.md)
