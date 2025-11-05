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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce9a9101-f786-32bd-8376-78302501a0d3 | -19.37355 | -44.54377 | 2025-11-05 04:16:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0adaec04-cc64-33d0-996f-b78d273ae1d1 | -17.98454 | -43.43771 | 2025-11-05 04:16:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66cffa48-484b-342c-a2e6-f886530ef753 | -20.04637 | -44.43887 | 2025-11-05 04:16:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 68e18041-48b5-36de-9dc2-db63ca4966ca | -23.54104 | -47.3856 | 2025-11-05 04:18:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ea4a7b5e-9e61-3dff-a484-8bf4d740fbfb | -5.0399 | -43.6205 | 2025-11-05 04:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| a49c48e6-c2a9-3824-bd22-279c90c75400 | -4.4259 | -48.9465 | 2025-11-05 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5737a59f-f370-3924-80d0-c251e313397b | -4.4632 | -43.2386 | 2025-11-05 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 3bfcc5da-98e5-3336-9cbe-3b3270b4581d | -4.4073 | -48.9474 | 2025-11-05 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 2f071953-73eb-3c5e-9f0e-90dac41810a4 | -5.4553 | -45.3988 | 2025-11-05 04:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| da7ebd01-b5b7-3783-9a09-5bfbd3312370 | -2.6509 | -48.4985 | 2025-11-05 04:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 6a5e41d5-90ea-391c-b75f-3c01e7dcdee3 | -4.7668 | -42.6572 | 2025-11-05 04:20:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| ddef896c-dc7a-32fd-8e08-dcaa98b1ba8a | -4.4633 | -43.2152 | 2025-11-05 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0816f39c-35ce-36ea-aaae-d1c57d33c5ca | -2.6508 | -48.52 | 2025-11-05 04:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| b18cf3fd-b38e-3a6a-9d68-1728d45e4b97 | -31.84465 | -53.05433 | 2025-11-05 04:21:00 | NOAA-20 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 261b8501-edab-32a6-b568-78d52cb12b0b | -5.0399 | -43.6205 | 2025-11-05 04:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| c5689b6f-ff57-378b-a428-e8bbdb41b372 | -4.4259 | -48.9465 | 2025-11-05 04:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 9429571d-a2e3-3d45-be99-adffa71aa5a1 | -2.6509 | -48.4985 | 2025-11-05 04:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| d370503a-c5fe-3f10-83be-95e4fca3f10e | -2.6508 | -48.52 | 2025-11-05 04:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 511845e8-a831-347b-95c5-59bceb6e1f3d | -4.4632 | -43.2386 | 2025-11-05 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 6c89fd56-dd9a-306b-9adc-ddf7719e11af | -4.4633 | -43.2152 | 2025-11-05 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| df5f0a7d-9c0c-301a-8409-92c8d0494b18 | -4.4073 | -48.9474 | 2025-11-05 04:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 6c7a263b-594e-3cb0-9058-45bdeda024b5 | -2.6508 | -48.52 | 2025-11-05 04:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| a8177a3c-45a1-3cf0-8520-1c473f93feeb | -4.4073 | -48.9474 | 2025-11-05 04:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 67865496-4610-3767-8a48-686175df801f | -4.4633 | -43.2152 | 2025-11-05 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 6994b96b-72b7-3703-a6fc-d24d7e8d9841 | -3.3748 | -44.2417 | 2025-11-05 04:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 956e8ccc-af33-3f68-bd98-51d928fed8d7 | -4.4259 | -48.9465 | 2025-11-05 04:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| c488a138-9e70-3d12-9356-0222273c0e73 | -2.6509 | -48.4985 | 2025-11-05 04:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| ecb13e56-512e-33cd-ad1c-c7bf39ce895a | -5.0399 | -43.6205 | 2025-11-05 04:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 60eb8dd4-17de-3dfa-afb8-9589ebe6cdce | -5.4553 | -45.3988 | 2025-11-05 04:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 0dfd64bc-ed2b-3abb-bfd4-2f44c244d7fd | -5.0399 | -43.6205 | 2025-11-05 04:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 0624f050-5dbb-3cb8-9a0e-47fcfe45920c | -4.4073 | -48.9474 | 2025-11-05 04:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| d842fdd1-c70c-36a4-b47b-b87ded221eac | -4.4259 | -48.9465 | 2025-11-05 04:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 5cf28a38-103f-3d0b-9767-1645091bff85 | -4.4633 | -43.2152 | 2025-11-05 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 0726b503-5eae-37a6-87fa-74abc436616c | -2.6508 | -48.52 | 2025-11-05 04:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| c922a955-6000-38a4-bc6a-26a3f2a47dca | -5.4553 | -45.3988 | 2025-11-05 04:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 467d5710-932f-3f27-b1aa-e6e09849039a | 3.36445 | -51.29271 | 2025-11-05 04:59:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fc490ed-1426-31ee-9918-bab846eb0097 | 3.36102 | -51.29325 | 2025-11-05 04:59:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 916a9692-46da-3219-b287-78c9b721797e | 4.01765 | -60.82398 | 2025-11-05 04:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 903c673b-1c7a-3b63-845b-e5acca95308a | 3.40218 | -51.28674 | 2025-11-05 04:59:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1bccaf5-61e4-3495-bd59-a17e2462c933 | 3.40502 | -51.28246 | 2025-11-05 04:59:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52d9d163-9267-3618-823f-13b8e7468d5b | 3.40159 | -51.28301 | 2025-11-05 04:59:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6826e336-6640-3478-a37b-9aaea8745e7f | 4.86621 | -60.2568 | 2025-11-05 04:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 444a47a4-1ac1-3410-93cf-fea7b6088d4c | 4.87632 | -60.26082 | 2025-11-05 04:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df22175d-cd53-3873-9f6b-64b6e3ae3319 | 4.86159 | -60.25779 | 2025-11-05 04:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b9fae2f4-1bae-3ee7-91ed-7c2046063e12 | 4.87545 | -60.2549 | 2025-11-05 04:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51ccf15c-6dce-37c7-8fc7-f742e0d746e7 | 4.0169 | -60.81894 | 2025-11-05 04:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 91ef77b1-2fe4-3cd8-ac80-310ac97e6e83 | 4.86476 | -60.24686 | 2025-11-05 04:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e449eee-b751-3462-93a0-5ba2a7a30d5b | 3.29676 | -51.35248 | 2025-11-05 04:59:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 887ce4a4-c29f-36ca-9e32-eb337bf72283 | 4.85696 | -60.25872 | 2025-11-05 04:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21f158aa-d0f8-3d03-836f-963595ce4031 | 3.89854 | -59.6414 | 2025-11-05 04:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e60c25ac-d6d1-3dff-92cf-9f8c8174d65c | 3.36788 | -51.29216 | 2025-11-05 04:59:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 418a8350-bdbc-3700-a8d6-3f5246de5e1e | 4.8602 | -60.24818 | 2025-11-05 04:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b9e63f6-d1f8-36a8-80f4-6d437357f5a5 | -2.6508 | -48.52 | 2025-11-05 05:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ff7f9c2c-5c04-3786-8c0c-18e0c91e2554 | -4.4633 | -43.2152 | 2025-11-05 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 0afff37e-ebd3-309b-811e-bc591bdcc698 | -4.4632 | -43.2386 | 2025-11-05 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| e2a416d9-0fef-331d-bfc6-dd02a479a43b | -4.4073 | -48.9474 | 2025-11-05 05:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 4e436486-dc8a-3884-a654-e965b53395cc | -3.4091 | -44.44588 | 2025-11-05 05:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4e15a7a8-d977-3966-84e2-a293dfca67e2 | -1.29256 | -49.15273 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 03cba19e-7d34-39dc-8399-b7169a42053c | -3.24406 | -48.88 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a06ce67-56a2-3a5e-8e86-24caf79e84ef | -4.04662 | -54.4543 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20ca7c1d-5b2b-3fbb-b3c2-71c2a7053a45 | -3.64828 | -44.43621 | 2025-11-05 05:01:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbb38456-e812-36f6-ab74-f306ae0a180a | -3.8845 | -49.11412 | 2025-11-05 05:01:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b07d8ad-a9fa-316c-8bae-a8b15ce761c9 | -3.96387 | -43.78658 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| dd8f05ee-3062-328e-b948-7e7343a9b555 | -2.38514 | -48.20253 | 2025-11-05 05:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4802ddf-35dc-3753-aef7-4139e8ae528f | -2.75702 | -47.75625 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a044e9e3-4687-3dfa-94c4-5d22147f5191 | -3.47896 | -43.6267 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58000ee0-15b2-3458-9e89-5374aa97219b | -3.32433 | -53.8497 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f05ad8b-5a5b-31c3-a276-16d245c71e32 | -2.48655 | -55.72353 | 2025-11-05 05:01:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa111264-82c9-3fb1-b220-a801bc5d2a9c | -2.44949 | -49.015 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 850f02c9-f054-34e1-889a-0e4a34a7ce52 | -4.47273 | -43.22921 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f3028703-bd74-3e7c-ab4f-c1c3b1527e4e | -2.98142 | -48.70171 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01d420db-b210-3360-8ea1-e2ac51b188af | -4.41894 | -48.94429 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 7bd486b8-be10-35c3-be22-02e2347a867f | -2.79467 | -50.30967 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ace18b26-50c2-37cf-b416-6e21177a1c30 | -4.10734 | -48.02058 | 2025-11-05 05:01:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 12ba54d6-3ca9-3e4b-8d40-9cdc030bd8ed | 3.14849 | -60.72128 | 2025-11-05 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de1e6e9c-f708-3aa9-80d0-3c32ed17f87c | -2.93308 | -51.3106 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dff48834-e9c2-395d-abe2-19872f5ed2cc | -3.42668 | -49.16681 | 2025-11-05 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91d03b54-9c8f-3073-85af-e9e0b3f772be | -3.31767 | -53.84867 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c068807-5c9f-3ff2-97f1-94f30bfb50b4 | -4.11363 | -43.878 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9ba11f5-2baf-36cf-a601-028a687047c5 | -3.81326 | -51.2879 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c993353d-2851-3609-af24-ddb469df957a | -3.31543 | -53.84114 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 975aa217-f8f4-39e0-94ce-3a8ade7ee6e2 | -4.09871 | -47.2855 | 2025-11-05 05:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 252fe8c9-b471-3c5f-bdc4-5af0e3570101 | -4.30103 | -43.79423 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b16455b6-96fa-3924-a735-13c55ba2faf7 | -6.41543 | -43.07301 | 2025-11-05 05:01:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 573d894a-3d8b-3abd-b7fc-e9913dfac707 | -4.97293 | -49.59631 | 2025-11-05 05:01:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af325cce-7b26-3bc7-afe0-e46c2b488768 | -2.65014 | -48.51018 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| c5bb6448-f931-3fc7-b513-794826c5558d | -2.10627 | -47.34065 | 2025-11-05 05:01:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44cbeae6-0974-3bd2-a9f2-19c9654ce01e | -3.11285 | -51.03322 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 679ac976-b5ad-3612-bbc5-e3cb046d8d7b | -3.43347 | -51.51545 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d9e750e-ef86-34f4-a5ff-532048627705 | -2.83617 | -49.41237 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0629b980-45e7-339a-b1e8-e2b7bfc12234 | -3.24572 | -50.79239 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31af0f0a-76d3-3020-a6a8-3ce6821fbe6f | -2.65888 | -48.5115 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b886f689-2eb6-3b14-a037-081cbbd02a96 | -5.43008 | -44.66272 | 2025-11-05 05:01:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 350c6523-173d-3b8b-a416-336262911001 | -3.91113 | -54.71199 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5566a290-eaab-30eb-b5e2-8493c42a557e | -2.7929 | -50.3129 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bf267c46-dcb9-35d9-beb1-dd9a9fc150ec | -3.36545 | -51.66916 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e789e12-c788-3399-b043-af9cb1c48d12 | -6.37363 | -42.41171 | 2025-11-05 05:01:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 3c80978c-a931-340b-80da-7f1a8f330544 | -4.39563 | -49.76142 | 2025-11-05 05:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8254cca7-b9b3-38ab-a9f7-469b7b7f31dd | -5.48087 | -43.58031 | 2025-11-05 05:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| d30e1673-9e68-3ef1-893c-d9c34b61dfeb | 0.09455 | -51.08601 | 2025-11-05 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
