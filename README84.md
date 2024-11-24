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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c86cdf9-f90c-3124-a989-45515cd8beb6 | -2.70548 | -46.28986 | 2024-11-24 05:40:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| ae423b9d-f766-36de-836a-db3f3c67ad8e | -2.37696 | -49.84973 | 2024-11-24 05:40:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f59a0e47-2e32-36a1-91ab-f58bf4149cad | -2.69754 | -46.28317 | 2024-11-24 05:40:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| d421bffe-4a59-33ec-ae7d-44d356110fde | -1.60707 | -46.87476 | 2024-11-24 05:40:00 | AQUA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d2246237-c7c9-37ec-b8ee-ef69f0488c83 | -2.20301 | -48.90677 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7f45f4e6-722b-3dd0-9c46-ab1fce16bc3e | -2.63147 | -51.89265 | 2024-11-24 05:40:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8128302e-4366-32c8-8eea-9d1f7b27bdeb | -2.20783 | -49.86646 | 2024-11-24 05:40:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0989cd69-1200-348d-b9f5-d592e0278918 | -1.21786 | -53.68571 | 2024-11-24 05:40:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 70957172-a7cc-3d15-a090-fda4ee7e6f61 | -0.97806 | -51.71008 | 2024-11-24 05:40:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 32dd8fc3-3f1b-3a81-867e-b57f492cdf39 | -2.86227 | -45.83269 | 2024-11-24 05:40:00 | AQUA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 67d1878c-96da-335b-9d67-90963ee22ba2 | -2.70722 | -46.27778 | 2024-11-24 05:40:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| bd4569d6-1ece-3c0b-9b73-e09f545e2b65 | -2.46725 | -47.07564 | 2024-11-24 05:40:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 656269ed-7b5f-3c44-80d4-fe2c9759a37d | -1.51064 | -54.1746 | 2024-11-24 05:40:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1ac4c18a-b821-3dda-aad3-98956fae65ee | -2.74617 | -48.67177 | 2024-11-24 05:40:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a6ce879c-520e-31fa-988b-4483107eb864 | -1.76894 | -52.70695 | 2024-11-24 05:40:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8e81d2e6-3f98-3416-acc1-692d76235ddc | -2.09826 | -50.35466 | 2024-11-24 05:40:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bc708819-fbaf-3f06-b253-8bf77ffa1fc3 | -2.14273 | -50.90933 | 2024-11-24 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fa211b9a-4939-3826-a525-1eab42fcfe7f | -1.73586 | -52.72489 | 2024-11-24 05:40:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 35153ff3-0a13-375e-9838-4b9469b0565a | -2.29006 | -49.1955 | 2024-11-24 05:40:00 | AQUA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 356bfa40-b74b-3bfe-ba36-8ca71cfa33f1 | -3.09682 | -45.78436 | 2024-11-24 05:40:00 | AQUA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bf2a9479-468c-3e3a-b742-55e05665d4c0 | 0.0129 | -51.1887 | 2024-11-24 05:40:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 19.8 |
| a4f71bf1-e637-393f-bd42-12f3197f40d0 | -2.21905 | -46.39582 | 2024-11-24 05:40:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bc1e6693-a9c4-3df6-ac25-6f4aa24cb07d | -0.94243 | -51.64795 | 2024-11-24 05:40:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c00293b7-9a5a-3a03-81c5-7019efa1fb78 | -2.03193 | -49.0038 | 2024-11-24 05:40:00 | AQUA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 96a76d18-10bc-3d95-a34a-a51c99d64063 | -2.19605 | -50.67669 | 2024-11-24 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e281ca7d-8e19-318e-be9d-9486b448cc87 | -2.15062 | -50.615 | 2024-11-24 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9cd2205c-7d48-30da-9298-3a7d431fbda7 | -0.28358 | -51.60992 | 2024-11-24 05:40:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 31d19a52-9f88-32fb-9c30-7c223626caa3 | -1.50841 | -54.1889 | 2024-11-24 05:40:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| ed96cb1b-beff-3f7b-b662-58d4e284e550 | -2.31949 | -53.85894 | 2024-11-24 05:40:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| a6a7a7a1-9cd7-3f7c-9449-03872add2544 | -1.59396 | -52.57814 | 2024-11-24 05:40:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 156771aa-8dec-3dca-b3f9-0497ff7769f0 | -0.91431 | -51.64382 | 2024-11-24 05:40:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c4917a1d-43f0-3d17-9b09-19ed815b3228 | -2.86413 | -45.81966 | 2024-11-24 05:40:00 | AQUA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a69d9186-d8ac-3536-a0f6-3308c519212e | -2.17025 | -53.77136 | 2024-11-24 05:40:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b0137d59-cc61-34d5-bf6d-edb9a37a3dff | -2.70116 | -48.6594 | 2024-11-24 05:40:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a9482d86-30b3-32b3-acf3-c5a2f8761701 | -1.60551 | -46.88548 | 2024-11-24 05:40:00 | AQUA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 35ca5d39-bd6a-327a-b893-59a4a6238d35 | -1.76724 | -52.7181 | 2024-11-24 05:40:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| aa38b95b-579b-3a4a-9afb-7a3c41f3b33a | -1.11072 | -53.3945 | 2024-11-24 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0360d462-3b6f-3000-989f-a81203434dd7 | -2.20167 | -48.91573 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d3fcc8cf-cf86-3f1b-abf2-fb8759494505 | -2.53611 | -47.35996 | 2024-11-24 05:40:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a20c8593-d4ff-35b4-91e3-fda674cc2673 | -1.22398 | -53.68063 | 2024-11-24 05:40:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d2df0b33-950e-398e-8156-1014d37e558b | -2.69696 | -46.2763 | 2024-11-24 05:40:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a20ff723-4415-3321-ae38-a69e374c5f55 | -2.74753 | -48.66263 | 2024-11-24 05:40:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e06dce92-ae88-31d9-b6e9-d3f2f0ca96c3 | -0.57172 | -51.72282 | 2024-11-24 05:40:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9b6b4b02-0459-3687-87f3-5be08f2650e0 | -2.15596 | -50.45388 | 2024-11-24 05:40:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 877a5792-c59c-3ef5-84cf-ae9042f59775 | -2.40269 | -49.0551 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f2408977-cb1d-3232-99fe-7137ca0006f6 | -2.45339 | -49.08065 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b0f639ff-fe35-321e-a73a-533013203c62 | -2.73394 | -49.1214 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b3124e1d-bc15-36e5-88b5-591f53e6f900 | -2.57865 | -51.87888 | 2024-11-24 05:40:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| aedc4e1f-218b-3901-b064-4f0f3fb72a88 | -2.43428 | -49.08698 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b82352df-5623-3b71-acd2-13cfd8eff5c8 | -1.43914 | -53.39853 | 2024-11-24 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 97eabbcf-ab56-39fb-835f-d4397c0574f6 | -1.61729 | -53.29832 | 2024-11-24 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 99327c1b-8cbe-35fb-be6e-558a535a0dac | -1.40671 | -54.46685 | 2024-11-24 05:40:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d89e2ae1-e868-3f5f-bfc0-38b266860bd9 | -1.44782 | -53.39279 | 2024-11-24 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 6e0f2518-6642-3306-b30d-0bb54e9e14e8 | -1.94544 | -49.52332 | 2024-11-24 05:40:00 | AQUA_M-M | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d8ead087-0e85-3877-9bd7-7af41fb1761a | -2.31123 | -50.58932 | 2024-11-24 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 771c15f7-aa36-3a8d-b99e-9ce428a9f91b | -2.73355 | -46.09391 | 2024-11-24 05:40:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 00eb198e-5e9a-35f2-988e-d1c727387873 | -0.28509 | -51.59984 | 2024-11-24 05:40:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 01a8a4c6-d88f-3424-8b46-daf82fbb9e6d | -2.41252 | -49.1111 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a31bd6e8-5601-3b2a-a87e-62cbfae94711 | -1.26918 | -52.68702 | 2024-11-24 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6aa10207-a3d2-3933-bba6-5cdd4b428f03 | -2.74535 | -49.11138 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f1a56269-3e5c-3d24-95a4-1d1c2bf408a5 | -1.44955 | -53.40018 | 2024-11-24 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 35ee0121-4cb4-35d9-a374-e853a90403f9 | -2.45206 | -49.08955 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| cdc2e260-d95a-3568-8d6c-c8f2f676f00f | -2.44317 | -49.08826 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 28e7467c-a1f9-38ac-acc3-a57db1a20f78 | -3.44671 | -45.68003 | 2024-11-24 05:40:00 | AQUA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8dba9823-cf00-3b9c-8f89-66dfd95c649e | -2.64383 | -46.85799 | 2024-11-24 05:40:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b5fb4c93-57f8-3b20-aa49-b59686f05383 | -2.14135 | -50.91845 | 2024-11-24 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 00ef4125-509e-3beb-b29a-95af9a9948e0 | -2.4445 | -49.07936 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 1f7c95c1-1356-3cd9-be3e-b41fea0b28a1 | -2.36995 | -50.38631 | 2024-11-24 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 27a087aa-e474-3bfe-90e1-c1506a03c859 | -2.19842 | -50.53971 | 2024-11-24 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9956e8fa-e299-326d-8d18-3fb2354f07ca | -2.37827 | -49.84096 | 2024-11-24 05:40:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b1a0c020-b5cc-324a-b604-e2325a49b688 | -2.2118 | -48.41655 | 2024-11-24 05:40:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d5e73a3d-00ef-3b11-9a2e-08c61418b236 | -2.39379 | -49.05381 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2c26a7f7-8e2f-3398-89b8-2d6ba4112b41 | -2.28875 | -49.20435 | 2024-11-24 05:40:00 | AQUA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 95b22688-beb2-3a28-89b2-f43a8c71119a | -2.44184 | -49.09716 | 2024-11-24 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e666388b-7aa6-3bf5-a225-12f875f568cb | -1.86136 | -48.16463 | 2024-11-24 05:40:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 99070b0e-c002-3b13-b6cb-39c63f0631cb | -3.52423 | -53.51133 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8672c976-cf79-34bf-8ad1-ebb34af11186 | -4.1571 | -54.58315 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83f5968f-962d-3a18-8e4e-ebcafb84692a | -3.18606 | -54.76918 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 690d13c2-2dbb-3630-b894-845206e451e2 | -3.26426 | -53.82852 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d8ec12a-6210-393b-a564-45810299e538 | -3.57736 | -54.52333 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35c5dc8d-6202-3b49-b0c0-9039edaab37d | -3.25423 | -54.21578 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b30b543-8a0c-3ca2-ac96-a3ac9f0fb3de | -3.24025 | -54.23011 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38323368-aedc-3051-9992-a2fa521cdc5d | -3.51094 | -53.80914 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27d259db-6de5-3830-bb2c-f0497ed9a044 | -3.2257 | -53.92643 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9854507b-8b21-3130-8874-f1d820c67dbc | -3.51353 | -53.81152 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3763535-e4ed-39e8-8003-9745afcebe6b | -3.25363 | -54.21973 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c168ed3-bf6d-353f-97f7-f382d05bb6b8 | -3.2454 | -54.23509 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14c31568-846a-3397-858a-7e9f564368d4 | -3.2391 | -54.24075 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88887ee5-9f5c-3985-aeb3-8f6eb8d4f861 | -3.24487 | -54.24166 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb519c4f-3a84-35d6-962c-009a1094f112 | -4.08883 | -54.75886 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c39627c-7c20-3068-9ba7-b6d8b9945b88 | -3.80428 | -51.34515 | 2024-11-24 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4a34423-4364-342a-878c-43883842420b | -3.50303 | -53.82141 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c747e814-04da-3989-9aea-fa124bc20a5d | -3.17372 | -54.32119 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42e9f164-b61b-3963-b6b6-9198fea80c9f | -3.27086 | -53.82489 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85feb921-b654-3aca-8381-bdf85e880903 | -3.17826 | -54.3302 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35ed95a9-c454-3c18-ad7a-233c51dee967 | -3.28069 | -53.84032 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4884993-7d57-343d-9a05-e0ae50d3ea67 | -3.24996 | -54.24395 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 341cd21f-585b-37ab-a5c7-49230c5b67d7 | -3.25237 | -54.23051 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63891fa9-efab-3b96-bca4-28c5d4349835 | -3.18047 | -54.76841 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da91d521-54c8-3162-9312-8818a97df5cd | -3.82287 | -52.41677 | 2024-11-24 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README85.md)
