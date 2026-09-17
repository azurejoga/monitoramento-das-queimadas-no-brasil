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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2d56480-0495-385a-9cc2-dbb648a02490 | 1.95641 | -50.97629 | 2026-09-17 05:33:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80210705-b084-36cc-85b3-a584134711b8 | -3.32559 | -57.8573 | 2026-09-17 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d177906e-c863-37f7-acf6-8ff0322388b2 | -3.4563 | -59.25504 | 2026-09-17 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91bf3a0c-ec41-3e1c-be5c-1f99cb1210eb | -3.54317 | -53.99312 | 2026-09-17 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70c84c2d-39bf-3485-ad18-a8a7803d5db8 | 2.20206 | -50.88383 | 2026-09-17 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24fd9a86-4255-3681-a1d3-e2c549785a82 | -3.47385 | -54.68992 | 2026-09-17 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4b82979-ba88-3524-9518-427be74dd012 | -3.53994 | -59.068 | 2026-09-17 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f305c98d-79af-3cb3-93b8-0799b9608c48 | -3.42486 | -58.23339 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28499c3a-dc71-3981-9116-897bbc99200d | 2.20753 | -50.88294 | 2026-09-17 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 495c7b33-a2c3-3e04-9d07-c80a349b76f0 | -3.47169 | -54.70436 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e2aca4a-48fa-33bf-9dac-68c740f3fb41 | -2.46746 | -54.68237 | 2026-09-17 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| baa8ff17-9b75-33a8-baf3-dbd87f73ada5 | -3.48164 | -54.70081 | 2026-09-17 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9c7c6f9-e60c-30fa-b317-90539e9e4a32 | -1.60903 | -55.56659 | 2026-09-17 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37edab0f-703a-3eec-89be-abd146437886 | -3.4451 | -58.41626 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 940ba47c-2e1c-38f0-8b9d-8522d13eecd5 | -4.24126 | -54.88401 | 2026-09-17 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ea777cc-fbf5-3e21-a2c8-dbdbcc87fbd5 | -2.63884 | -54.69334 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d5a316b-a66c-305f-a604-b8360eee2c61 | -3.13408 | -59.02518 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f8c5cfe-9e5b-3486-be8d-3473abba1f79 | -3.81148 | -55.88903 | 2026-09-17 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ff004d7-500b-3172-86f8-4ccb26fdd79a | -2.9618 | -50.32806 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 02305564-e1b9-385b-b0a5-16f283eaa489 | -1.74285 | -55.25492 | 2026-09-17 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa08f10b-ef54-3a7e-ab65-e69c6c2496b8 | 2.31936 | -60.91819 | 2026-09-17 05:33:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2804dbc2-edbc-36d7-ac8f-f8b8ae2645eb | -3.48381 | -54.68637 | 2026-09-17 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92ca9f99-78ce-3dae-8267-4390be62a803 | -3.02434 | -51.33826 | 2026-09-17 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3e4730d-31b7-3af4-a8cd-63c9472d7eb3 | -2.09771 | -52.05776 | 2026-09-17 05:33:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50484612-d406-301f-aac6-cd2514bda6be | 0.90888 | -59.62632 | 2026-09-17 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b999ea4f-18a5-315a-9458-ac9b859ee5ae | -1.60845 | -55.5704 | 2026-09-17 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 222ca2ee-eee1-3e54-a1d6-54c7c81dea01 | -3.64301 | -58.5637 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a57cb08-99c7-3cce-bed3-9e3a63407e19 | -3.33499 | -59.82867 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95077fee-ffa2-3bda-a8ba-150e8d9bff1a | -3.26838 | -54.25869 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca976428-b5cc-3c4f-9c68-e6173662bc28 | -3.17839 | -48.58508 | 2026-09-17 05:33:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef16fc87-7169-3369-a79c-c8eca2a6f8ec | -2.09824 | -52.05437 | 2026-09-17 05:33:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38bfeed7-5ae8-399e-a09c-9c0a4e6806bf | -4.10565 | -56.34715 | 2026-09-17 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58f37826-c977-3804-9c56-47806a9563d3 | -3.58708 | -58.53529 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 424d19fb-26a1-356f-8cf1-641e9edcac50 | 0.91138 | -59.62598 | 2026-09-17 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3157cc54-a0e4-3fa0-babc-70ae856db478 | -2.46692 | -54.67987 | 2026-09-17 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3240d0cb-a808-34df-88f7-be0a4fafaa54 | -3.44407 | -50.66965 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a7ff60d-35fd-307c-9b22-d9d772d3bfce | 2.21359 | -50.88558 | 2026-09-17 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| addce2ad-4dcf-3b8d-b868-086f67fb13e1 | -3.48021 | -54.7103 | 2026-09-17 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a957cd61-028f-3c21-aaa2-ec36fc2b559e | -3.02378 | -51.34204 | 2026-09-17 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c45c819d-d204-3521-bac4-8c6f546f0867 | 2.71405 | -60.29858 | 2026-09-17 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fff14f6-d026-3bcd-ae86-e01095565a61 | -2.89888 | -54.18237 | 2026-09-17 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a13eb134-891a-3f06-8a31-8a5f01519981 | -1.79295 | -52.17992 | 2026-09-17 05:33:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 08e7c62d-5157-3b37-9d7a-d3f1712f9ca9 | -2.82206 | -51.33966 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b73338a3-3e4d-3a70-85fa-c6c01f05d10b | -3.35315 | -59.84653 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff78c181-78bb-3ad5-b396-83f13f20f115 | -3.4575 | -59.24734 | 2026-09-17 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3629ee5-5285-334a-b72f-6ee6ec281574 | -3.48339 | -54.7204 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c779be4c-7804-3eb7-a5ec-2120cb2d2771 | -3.47847 | -54.69054 | 2026-09-17 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0c63693-6b22-3201-9c74-c7b51c8f9fb9 | 2.20605 | -50.88012 | 2026-09-17 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54a65783-edf8-33df-9a3e-cc7c40bf7e4f | -3.31674 | -57.8651 | 2026-09-17 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e48663a5-982c-32d1-bf17-19dffd8fe96f | -3.33632 | -56.95063 | 2026-09-17 05:33:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b324c33-3239-32f9-bd19-a7313bff79c2 | -3.35257 | -59.8502 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c71d7c33-78f0-3b8d-a747-fde70ca51bf3 | -2.96936 | -50.31942 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b1ca5f4-579d-3090-b372-ffe803f4d30e | -3.488 | -54.72107 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 87833c1e-125a-320a-97b5-30591d209082 | -3.13117 | -59.02074 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0f1f32c-09d4-3043-b539-f98eb7a73abf | -3.3384 | -59.8292 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d2c2d50-b59a-3f6a-b549-408cfbd37df0 | -2.10311 | -52.0586 | 2026-09-17 05:33:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff57b2b7-4e25-3f42-8307-047abbe0bed8 | -1.79245 | -52.18323 | 2026-09-17 05:33:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 47e23064-96bf-3720-b718-a205ecb02b3d | -3.50513 | -53.21096 | 2026-09-17 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| add437ba-e999-3035-adad-6f2e7e80791d | -3.13468 | -59.02128 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 291b8184-19ec-3829-a320-8f150b0a0171 | -3.42725 | -58.19424 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0d0db70-0b24-3949-a6b7-25cf169125c2 | -3.45393 | -59.53458 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d3e0bcc-9ab6-3603-bf4e-46591d0becdd | -3.59809 | -59.06483 | 2026-09-17 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c14c7d84-8fcc-3619-91d6-be2526c2a260 | 2.21266 | -50.8863 | 2026-09-17 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edd47901-c23f-3e4f-9e98-eebc932e0f3d | -2.90834 | -54.18381 | 2026-09-17 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ef8feb8-6afe-36b8-a592-43d548c8badc | -1.14841 | -54.17001 | 2026-09-17 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e36bb567-88ea-3c5b-9d76-c68aba61ce09 | 2.20146 | -50.8803 | 2026-09-17 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a24760fb-e97b-3e51-a73c-e66f3bc0efc8 | -3.73446 | -55.94431 | 2026-09-17 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb2a5629-5103-39dd-b797-03b2b1ac5f0c | -3.28183 | -57.91889 | 2026-09-17 05:33:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 471f1e71-8577-3e8f-bb05-ceee7f5c2934 | -3.26211 | -54.26795 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26fd61dc-cf2a-3472-bde3-76b518c5ba80 | -3.33158 | -59.82812 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f81c89a4-6814-3542-bbea-bdf88692747c | -1.14382 | -54.16922 | 2026-09-17 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e2512ed-2c35-3bf6-9d0f-0f9ce8edaae7 | -3.47879 | -54.71973 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 83370e83-85f1-36c7-b8d2-75f1f4b94faa | -1.14833 | -54.16798 | 2026-09-17 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d5ad221c-6b30-344a-8ce0-0352a4f87de0 | -3.47702 | -54.70018 | 2026-09-17 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bcfa9cd0-938f-3ea0-a5aa-6ad88252612f | -2.90984 | -54.17383 | 2026-09-17 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 222c9616-3d11-38e1-acc7-7605b8cb1472 | -3.45195 | -59.53101 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6108157d-2792-316c-b446-1864d8891022 | -3.34916 | -59.84967 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dabebb17-56a9-3cfd-9f24-158690a3329b | -2.0914 | -56.42579 | 2026-09-17 05:33:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ead6d38f-fd5e-34d8-bedf-8029c5c0b8e3 | 0.78679 | -59.20195 | 2026-09-17 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e44971cc-ad2f-374f-953b-05bbe51b1852 | 0.78622 | -59.19836 | 2026-09-17 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92a37463-97cf-32b2-961e-304408357df1 | -3.44583 | -57.9786 | 2026-09-17 05:33:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9e416a4d-9653-31e9-b289-7289f547f7df | -2.63955 | -54.68871 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f93b4106-56ad-3892-a134-b1ab0a1fb209 | -3.38821 | -50.45231 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8746c00-2e39-37cf-a0e3-964f38450556 | -3.4795 | -54.71501 | 2026-09-17 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f77a5de9-688a-375c-877c-43f832475907 | -3.43024 | -58.19909 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98fc0be6-27e0-396b-9532-d9328da04ae9 | -3.64365 | -58.55956 | 2026-09-17 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb30dc7c-307a-3e34-9b2d-a12e2d17d4ef | 0.91194 | -59.6295 | 2026-09-17 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b2c8401-ebc1-3104-abda-4158d3309816 | -3.37361 | -52.79985 | 2026-09-17 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 700bb856-72ff-3d75-824a-2c4d06cb4751 | -4.42093 | -55.50773 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faf863a1-6a2e-3ee3-8c92-6b8495bb054d | -3.71234 | -60.63286 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a4afe13d-807c-3f95-81d8-8013c5ea9dd0 | -5.90249 | -59.93634 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e7f238c-e7bc-3e9e-9093-b718600ee97a | -9.59513 | -60.5148 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b44a494e-dae8-3880-92aa-6840517d4e61 | -8.00216 | -61.3758 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3361f98e-ef68-368b-9058-0830a19b3c28 | -3.69729 | -60.61969 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc3cb273-7aac-3f4b-8853-9f7a00075c86 | -5.91232 | -59.9418 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4270383e-cffe-33e9-bf73-e85c1cede38b | -9.17493 | -58.3039 | 2026-09-17 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ebcb616-66fd-317f-b72f-0ce66f063be8 | -8.75318 | -66.57076 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2062176-30b5-3a09-b165-48dab2776a7b | -6.79695 | -58.79212 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 852760bc-3b8c-3c00-bd76-475b81a0c3e2 | -6.37054 | -58.28864 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff0f14af-50fa-316f-b322-cc29d96fe819 | -9.69756 | -58.1808 | 2026-09-17 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README74.md)
