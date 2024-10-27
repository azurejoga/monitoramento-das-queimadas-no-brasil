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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fff31d1a-ba40-3284-a489-bf25025fbddd | -0.98308 | -53.69799 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 44c62971-09f0-3a18-8944-691869c54015 | -0.98255 | -53.70129 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 79e7fb72-4100-3837-8339-2b5cb11c2774 | -0.98204 | -53.70449 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 8d1ae781-dbd9-3775-a98a-5c5d7310f601 | -0.98156 | -53.70742 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 95f5c03d-f0a9-375b-944d-85cc1b506dbc | -0.9811 | -53.7103 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d05d79d2-889c-3ec5-9d92-0e3ca16d12a2 | -0.98063 | -53.7132 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 04d1c288-f777-3ff4-9f9a-a616c86fb733 | -0.98016 | -53.71609 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b0da3e9-2707-3ea7-84f5-c1b51d4e3274 | -0.97895 | -53.69085 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a526fab9-212e-3f91-913f-39f48f888524 | -0.97846 | -53.69384 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30f8c7cb-e34f-32ce-848e-66199d77ed75 | -0.97796 | -53.69694 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c05063b-c3e1-3a1a-92d9-2d15ca73839d | -0.97743 | -53.7002 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7bd96ae7-3164-35d6-8273-1a79b07a483e | -0.97692 | -53.7034 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 061db1e0-6c36-3cd7-ab97-3f20cf9ae223 | -0.97645 | -53.70627 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89f4a38b-6c10-3f71-aa64-1744efe49ebe | -0.97601 | -53.70901 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86d7c0b8-842b-3832-9c66-53ea8358f2b3 | -0.97557 | -53.71173 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af4cc840-65c1-36d3-9af8-b9affb346c2f | -0.9728 | -53.69616 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6863acaf-77a3-3693-89fe-9076e8880c83 | -0.97231 | -53.69917 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 135df06d-0a4d-362d-a44e-64f8e85566d0 | -0.97183 | -53.70211 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24e2f199-869e-3489-a721-2bc0aee8a1fd | -0.97138 | -53.70491 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a06715fe-6aaa-3eb5-8cd9-05c4965b132f | -0.87695 | -53.68914 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51791e50-e5c9-32e3-a7b4-78f0900c924d | -3.07593 | -54.17095 | 2024-10-27 04:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9fcd37e5-de1d-3229-8563-49dba31be0cb | -3.07543 | -54.17395 | 2024-10-27 04:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1175a876-f72e-3848-ac25-2a3722d4ddb0 | -2.77745 | -54.73946 | 2024-10-27 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 66e43a43-c356-3b83-b1c9-1571df76b94f | -2.63998 | -54.29903 | 2024-10-27 04:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fee57b52-8d8b-3cc2-a033-4c1f32c06baf | -2.5665 | -54.0257 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1593fb7-377f-3f48-a76e-5eaa1f73adff | -2.56187 | -54.02176 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea80ec91-ceeb-335e-8b65-09e44bfe6011 | -2.54383 | -54.00309 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06b75517-eba8-33e7-99e5-f220e6c8668d | -2.53915 | -53.99953 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81068af8-3330-32b2-8459-191f474109d6 | -2.53864 | -54.00261 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68aad074-c77a-35ba-8890-eeadb4d45aed | -2.22197 | -54.49213 | 2024-10-27 04:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8dbc6c32-8a30-38e1-9fa3-9833ab73ef74 | -2.22021 | -54.49102 | 2024-10-27 04:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3eb45040-01b9-34b0-b010-d5be814b6d82 | -1.59989 | -55.70539 | 2024-10-27 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 317939bb-8733-3711-959a-d27e8bab3d9c | -1.59936 | -55.70462 | 2024-10-27 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4cf9fc4-f0e1-3942-837a-5be372bfa36a | -1.59921 | -55.70966 | 2024-10-27 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bbdcadc-ee01-3909-a557-91ffc88fb3ac | -1.59865 | -55.70891 | 2024-10-27 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5741303-fde5-3544-afed-dedae12d7cb2 | -1.3709 | -55.86288 | 2024-10-27 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73ea2b6a-04e8-3850-a18d-47a36180e821 | -1.37019 | -55.86722 | 2024-10-27 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f93ee001-60c1-3d80-a66e-7291ad8cb7a2 | -1.3399 | -55.88089 | 2024-10-27 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 077ca6a8-3e4d-3ae7-9ef0-56cd92142873 | -1.33769 | -55.87975 | 2024-10-27 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b5bccd5-3d09-3ec1-ad52-f94106685996 | -1.33396 | -55.87997 | 2024-10-27 04:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e53565d7-260c-3118-94c7-145568100913 | -4.41782 | -55.92646 | 2024-10-27 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 537f70dd-9915-3ccc-b64e-62422622db48 | -4.41716 | -55.93032 | 2024-10-27 04:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2d21347-f8c1-34ae-b79b-29c1e28cc22a | -12.23638 | -40.97818 | 2024-10-27 04:25:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5a35844c-8ca9-3c66-ad23-335f62667624 | -14.11825 | -41.67785 | 2024-10-27 04:25:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2457be39-47c1-39b8-a568-4ab8c6511344 | -8.90316 | -41.44359 | 2024-10-27 04:25:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 312c9d9a-7fe1-3181-a2e0-ba766c273218 | -8.672 | -41.03921 | 2024-10-27 04:25:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f696559c-63f6-30b5-b20a-9b1baab1216e | -8.67158 | -41.04065 | 2024-10-27 04:25:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 215cb221-19cd-373e-ab75-83b3738f7395 | -8.35226 | -42.2607 | 2024-10-27 04:25:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4538c61d-2a44-399e-bd87-35851cd60465 | -8.35154 | -42.26561 | 2024-10-27 04:25:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d163cae8-e2d1-3686-bb91-04db07652666 | -8.34837 | -42.26013 | 2024-10-27 04:25:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dd565866-547f-35d3-ada3-631066ec0bfb | -8.34766 | -42.26504 | 2024-10-27 04:25:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f72b45b4-2580-3b8c-97d3-8c99136a50ab | -8.29491 | -40.96044 | 2024-10-27 04:25:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| fdceffef-ec59-3e7a-991e-261299cd9479 | -10.16289 | -42.4475 | 2024-10-27 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6dbc3e54-feff-3f22-bcdc-3f5c65b262fc | -12.21491 | -42.78135 | 2024-10-27 04:25:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bb3a6b4f-4191-313d-9ad3-7535d5b349e2 | -12.2142 | -42.78654 | 2024-10-27 04:25:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2eb69ba7-b187-35de-9cb6-b7f946ae06cd | -13.71456 | -42.91446 | 2024-10-27 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 180970bd-8caf-3ed1-b8ce-0279dc552d55 | -13.45516 | -43.02948 | 2024-10-27 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1086f55d-81ec-3011-ac92-61da9c5b9e9d | -13.45216 | -43.03269 | 2024-10-27 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 208345d9-1df8-31c0-8bcd-221e7b1e85af | -13.06899 | -42.13349 | 2024-10-27 04:25:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c5ce8a75-afd7-36f9-99bc-0487c04b7bff | -13.06852 | -42.13697 | 2024-10-27 04:25:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7b71a528-3f30-306c-b768-6d647fcd61c0 | -14.27748 | -43.04063 | 2024-10-27 04:25:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 94654494-2ccc-3692-a25c-f637fb7e86e9 | -14.27725 | -43.2494 | 2024-10-27 04:25:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bedba4dd-6f68-35f1-9a32-7b05b88ad38a | -14.27653 | -43.25457 | 2024-10-27 04:25:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7ea64d92-b902-388b-92fb-43da0c060e7f | -14.2397 | -43.07859 | 2024-10-27 04:25:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cc88c29b-cdcf-39fe-a76c-155488a4198f | -14.23923 | -43.08214 | 2024-10-27 04:25:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f036e89-ef91-3e4f-905b-e935acc4f3ad | -13.82739 | -43.23561 | 2024-10-27 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4bbaef21-8a5d-3d38-9ed6-11b9ecfb2189 | -13.76587 | -43.16161 | 2024-10-27 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e2f7fc02-64ef-3159-bea9-f7fb45bc997c | -13.76477 | -43.16362 | 2024-10-27 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ab78fcad-6df2-39fc-b58a-b6ad035c7931 | -15.20065 | -43.53578 | 2024-10-27 04:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b6b7b3c5-bd8e-39a8-8dba-bee972fba9e9 | -15.19671 | -43.53522 | 2024-10-27 04:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36d50962-0778-3f4a-9df5-4c36b41fc725 | -9.04989 | -42.87867 | 2024-10-27 04:25:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b90d5034-7ba2-3084-a292-62d3d2d0526a | -8.71857 | -44.02284 | 2024-10-27 04:25:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f417479-e714-33e5-ac11-d9371b46d076 | -9.96546 | -44.16352 | 2024-10-27 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| addec6d5-d22b-3b28-b35b-b1da53757d10 | -10.81462 | -43.47516 | 2024-10-27 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d8575d2-a631-3e66-8a5d-6e9f6e456f5e | -10.81297 | -43.4771 | 2024-10-27 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 371520d2-7324-31e1-8914-b56756831fd7 | -10.80484 | -43.48052 | 2024-10-27 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b24e098-264d-3e32-b59a-c5daef33c0d7 | -10.80279 | -43.47802 | 2024-10-27 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b46068f7-ba5b-3f2f-bf32-4aa3d3015fdb | -10.74618 | -44.38202 | 2024-10-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ec1722d-282c-364a-ac7b-36876413cedd | -10.74262 | -44.38149 | 2024-10-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec3d8289-bf0f-34fd-93bb-0563979fc9f6 | -10.60639 | -44.27481 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf624a6-67b4-3137-9094-d471ebde272d | -10.60283 | -44.27426 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7376928d-3182-37cf-8ff7-eb8bd24a232e | -10.60222 | -44.27842 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56031ad0-c629-3113-957d-5eb698ce694e | -10.59926 | -44.2737 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a25d5283-5ae8-3223-bdb8-109adaa74f1e | -10.59866 | -44.27788 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8a54678c-2fe2-32e2-a503-b22de15868fd | -10.59805 | -44.28202 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1950b2c6-dde0-3b68-9de1-20736339cf65 | -10.5957 | -44.27314 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ad9fe631-4282-392c-b5d7-6293faa6f566 | -10.59509 | -44.27732 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c15332d4-b1bb-3920-a7fe-e1b77907a178 | -10.59449 | -44.28148 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b953c36c-3304-34d1-b36b-480cc16aec56 | -10.59153 | -44.27676 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62098c3a-b809-3ac9-8fdf-7a554e35001c | -10.5774 | -44.27985 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 654fd1b8-8a48-3763-9428-48a8c1fdc2a3 | -10.57446 | -44.27518 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14968269-bf86-3e58-b1d1-be017a656cce | -10.57383 | -44.27934 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa7ba414-aba1-3129-b0b7-18192cc59585 | -10.57089 | -44.27466 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7378d89d-656f-3500-9186-edf470112c73 | -10.57026 | -44.27882 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d01502fc-a3d4-3763-971f-96cff2f7c7c6 | -10.56965 | -44.28293 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc9048c0-4bd6-37db-9677-237a67ebb48f | -10.56732 | -44.27412 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3c3074f-9846-36cc-bc87-57627e901ce6 | -10.5667 | -44.27827 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5a42428-aa2e-3b06-ad6d-6ae4da1a7e7e | -10.56608 | -44.28239 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72112c59-2f19-3fff-9afd-8a30132c8549 | -10.56376 | -44.27358 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d6c1469-b70a-3f8f-82ec-f2cc56749cd5 | -10.56314 | -44.27773 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README53.md)
