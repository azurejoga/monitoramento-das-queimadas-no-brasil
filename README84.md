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
| 60bda1c2-85b7-3227-81a7-6931603a5dbb | -13.3199 | -51.62 | 2026-09-16 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 6a131fe1-241a-3374-860f-6f621d6853da | -1.861 | -54.4315 | 2026-09-16 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7ce4467a-18f7-3914-8311-9c505cdcd8eb | -9.7877 | -46.1045 | 2026-09-16 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| fe6d9f9e-f9c7-3c74-9b14-10b797eef345 | -6.2916 | -55.2895 | 2026-09-16 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| afa70a08-736a-3ee1-8e96-52258be91751 | 0.1747 | -51.4599 | 2026-09-16 15:30:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 6987a646-f9e7-3c14-827e-0fd5d398cbfa | -7.7808 | -66.9208 | 2026-09-16 15:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 14652103-27b3-3d0b-be30-71fa822d7406 | -15.3408 | -52.9704 | 2026-09-16 15:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| f0d4ca5d-d781-3b74-a256-466cc873c103 | -8.5431 | -44.4902 | 2026-09-16 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 7f6caca5-8a9b-3136-99e3-96b4a6656ca6 | -11.417 | -51.416 | 2026-09-16 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e56ff96d-362a-372c-a961-46c679004a1d | -3.4279 | -57.9816 | 2026-09-16 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 0164bd6f-cfd0-3bc6-8944-34108e16067e | -6.0993 | -59.9076 | 2026-09-16 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 3315b45a-01dd-331e-a94d-5ccc8ffcbbb0 | -8.5497 | -64.0477 | 2026-09-16 15:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 2c46ecf0-f310-3abc-9338-da2831807be3 | -3.4279 | -57.9816 | 2026-09-16 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 2526d8c6-656d-3981-b89b-070f3da5d6a1 | -7.0058 | -59.2382 | 2026-09-16 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 76812e77-369e-3c06-b32e-0cbfcc5fcec8 | 4.2789 | -60.9316 | 2026-09-16 15:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 93c09939-24c4-3eff-8ae3-70c18a9d5cbb | -6.2731 | -55.2904 | 2026-09-16 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 514650b3-8afc-31c1-84b5-ac2c766cced5 | -6.8226 | -58.9947 | 2026-09-16 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d1f3ab5b-1d9f-3442-8868-bd590dfbca58 | -9.3567 | -50.1796 | 2026-09-16 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 1194d772-c101-37e8-b0c9-51b02d72bc27 | 0.1747 | -51.4805 | 2026-09-16 15:40:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 9ac59eb5-7d0b-345e-aa89-743eb756ec12 | -13.3391 | -51.6176 | 2026-09-16 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| b34c4775-d47f-3017-8db8-544c9e780161 | -2.7331 | -57.6271 | 2026-09-16 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a5a57cb1-4687-3ea1-a8d1-f2b7faa6d5c7 | -13.7002 | -51.8274 | 2026-09-16 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| ec5f5116-318c-3979-be55-dd399c21177e | -8.396 | -47.2121 | 2026-09-16 15:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 340.0 |
| ae62ff1b-329c-3df2-82df-c64916e05499 | -13.4009 | -51.3542 | 2026-09-16 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.1 |
| c1bc3e30-ae48-3eba-b499-f05221d79922 | -9.7877 | -46.1045 | 2026-09-16 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| a17b7b77-c0ad-3500-a3ae-f539d4cc6b1b | -13.3387 | -51.6389 | 2026-09-16 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 85429db4-59c7-3545-aec2-4c4e654573f7 | -12.101 | -57.1983 | 2026-09-16 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 29e07a6d-e332-3660-8e25-7d7c004efcae | -9.4078 | -60.3205 | 2026-09-16 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 4ab24869-3e87-3e75-aca2-d053717d2499 | -12.12 | -57.1967 | 2026-09-16 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 73e5c7e8-c9a2-39b4-8746-9836d492117c | -10.7013 | -54.1868 | 2026-09-16 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 157b897c-daca-3dc1-b6f9-d6dcf36292e9 | -3.1816 | -61.1045 | 2026-09-16 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 64a57b68-3870-374e-ad69-d23c138f27f7 | -14.2796 | -51.7097 | 2026-09-16 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 2d53d060-e364-319e-952a-a691283cc4bb | -13.5841 | -51.8845 | 2026-09-16 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9586b4fd-aaa6-3708-bcc3-d6bc3078058b | -2.7149 | -57.608 | 2026-09-16 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| d3168823-aecb-3275-b171-f24a2ba095b7 | -11.2693 | -54.0129 | 2026-09-16 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 59b63e9a-f7d7-327a-a256-2c25520e34c1 | -9.3577 | -50.0943 | 2026-09-16 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 55657dca-1338-319b-b3ae-dc583a99f4c7 | -10.2513 | -57.6952 | 2026-09-16 15:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 0cd598be-26c5-3923-a66e-e875739e0ab4 | -8.9239 | -63.3371 | 2026-09-16 15:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 318ba3b3-a8b5-320e-817e-ab7be8daf4cf | -2.7149 | -57.5886 | 2026-09-16 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 17aa3620-c6a9-3edd-a511-1a6222dfcbe5 | -3.1661 | -53.9235 | 2026-09-16 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 1219788a-2eaf-3c0d-87b6-15e742e6d74c | -2.6602 | -57.5119 | 2026-09-16 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d1675c56-2222-3b06-aa56-8df461a37b95 | -13.5131 | -51.5319 | 2026-09-16 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 9471619d-6511-3124-8157-3fc803b36815 | -9.3755 | -50.1779 | 2026-09-16 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 99896aaa-b549-3bb4-8024-1eba221d6c52 | -3.3183 | -57.8677 | 2026-09-16 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 43bbf80e-786f-3eba-81a7-4f580e134077 | -9.8099 | -45.8759 | 2026-09-16 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| bcdbc24e-6bee-3b23-8e4c-e12b46fd279b | -3.2752 | -54.2622 | 2026-09-16 15:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 81da77d5-4b91-3103-bfb1-9ad43191a9c8 | -9.4137 | -50.1317 | 2026-09-16 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 5795013e-10fc-3223-ad46-a0acf838ed64 | -9.2073 | -65.9536 | 2026-09-16 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| f8216337-457e-3515-a4f5-734780d5ce7f | -8.6493 | -66.5839 | 2026-09-16 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| fe2dd742-9e19-3ee2-b8f8-10476f00bd2d | -13.5652 | -51.8656 | 2026-09-16 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| ad67a519-358f-3f8a-b13d-2afff20c1ecf | -6.1609 | -52.7496 | 2026-09-16 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 78c9ae9c-e244-3aba-9359-f8630702af02 | -10.3955 | -58.2962 | 2026-09-16 15:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a98b5461-78b7-3d82-b8c7-6a93f538e9dd | -10.9105 | -54.025 | 2026-09-16 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8a2cb61f-342e-3b84-a607-4870847abdd5 | -9.3575 | -50.1156 | 2026-09-16 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 4dc6123f-388e-3dfa-a7ed-8202b0d58060 | -6.583 | -58.9658 | 2026-09-16 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 77e13bd2-f904-35d3-86c0-7ed87345a3ef | -9.7979 | -60.4734 | 2026-09-16 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a5e84a54-3156-37da-a600-57d5ad193ce8 | -6.2732 | -55.2704 | 2026-09-16 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 1f33901d-7f73-38e3-832e-021c20790106 | -6.1046 | -55.6367 | 2026-09-16 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 81576118-7a9c-32d3-a9a0-5a91707d39b1 | -1.8426 | -54.4317 | 2026-09-16 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 3555706f-120c-353b-b887-a3b33b2c94d0 | -1.6206 | -55.5679 | 2026-09-16 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| eae267a7-d518-3b80-ab63-216f74fd9019 | -11.2002 | -55.0398 | 2026-09-16 15:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 1bd4740f-be5d-3848-b3ce-139af4e1efb2 | -2.6968 | -57.5307 | 2026-09-16 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4446d395-1a9e-3fba-9fff-bb1d9ad58e00 | -13.5844 | -51.8632 | 2026-09-16 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b8b42cae-2e16-3ccb-885e-a392e4e91427 | -15.5786 | -53.8031 | 2026-09-16 15:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f6977ad9-9085-3b52-816d-8938296f4522 | -8.4108 | -54.7476 | 2026-09-16 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 9e24d533-ccee-392b-8636-7d0413dd8377 | 4.1316 | -61.2378 | 2026-09-16 15:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 540fcbce-697a-3058-b564-48685b316d35 | -9.2072 | -65.9723 | 2026-09-16 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| fd1e1db9-bec1-32b2-a8fc-401b20a9ec17 | -8.6188 | -44.4819 | 2026-09-16 15:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 78c10828-6f0c-3a8e-8113-eb7b61a67827 | -12.6636 | -54.6782 | 2026-09-16 15:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 5c02f056-5831-3cfd-9237-7b1329c14e10 | -12.6821 | -54.7174 | 2026-09-16 15:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 744e790f-6cda-3f57-898c-50376cfe50a0 | -3.68 | -54.1706 | 2026-09-16 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| bdb44af7-fc7e-38de-86f3-31e40d99be36 | -1.861 | -54.4115 | 2026-09-16 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 00841f40-adc1-347a-ba5f-e76529b4e027 | -3.4278 | -58.0009 | 2026-09-16 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e1b0646f-e232-3b32-9336-2d26f823630e | -10.3953 | -58.3159 | 2026-09-16 15:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 124.0 |
| bd364cd2-446b-3fde-ac45-e4eaf8205d8e | -14.2016 | -51.7627 | 2026-09-16 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| fc0f7904-a601-3d2c-a2c8-6a126d5eda04 | -9.1337 | -65.844 | 2026-09-16 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| d5e20b97-9673-3240-94ac-bf1a7b3e2d3b | -9.7793 | -60.4744 | 2026-09-16 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 5bf3d84d-90d0-3f4e-891b-c9b92aa83a99 | -1.861 | -54.4315 | 2026-09-16 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 154cda6b-3b6f-35a3-8f79-69c313f6acec | -11.9906 | -52.4695 | 2026-09-16 15:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 2c4db431-5e53-3c85-ba91-ee3c4993080b | -7.5608 | -62.33 | 2026-09-16 15:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8ac1646a-bc63-3c5d-90c6-af7283d2dc76 | -9.0962 | -65.9384 | 2026-09-16 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| fd0f0832-88fc-341d-8433-f064dd7b168e | -7.0428 | -59.2173 | 2026-09-16 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| fe02e005-9186-375d-a04f-1f3bae517ac6 | -8.8456 | -45.8939 | 2026-09-16 15:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 134.9 |
| f563314f-273f-3008-b8a9-15a810fde118 | -9.7608 | -60.4561 | 2026-09-16 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 01625bfa-acca-32a2-bc5d-dd672473b1d9 | -13.3199 | -51.62 | 2026-09-16 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 3dcbb8f1-3ed1-3acf-b1eb-f0a4bc40c903 | -3.2568 | -54.2627 | 2026-09-16 15:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 8504f764-e5be-364b-8f51-630409a8357f | -6.9872 | -59.2582 | 2026-09-16 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 4cf4a081-3ce0-3d40-9f9a-a5dae0b1d19c | -8.8585 | -44.9149 | 2026-09-16 15:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 236.5 |
| d534ea33-bd79-3e15-ab94-203ff1d3460b | -13.681 | -51.8298 | 2026-09-16 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 177281cf-9cb2-3e7a-acfe-cb3f36ae1df3 | -8.5431 | -44.4902 | 2026-09-16 15:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 195.6 |
| d6577712-ffd7-3aee-9b61-b1f490db1d1e | -9.006 | -65.4 | 2026-09-16 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 429ef390-04d9-3fea-81e6-3bff2103b159 | -12.6826 | -54.6763 | 2026-09-16 15:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 53db4257-6b08-3b23-9d44-ce98090f75d8 | -9.7322 | -64.9067 | 2026-09-16 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 289.9 |
| 39e7e96e-adc0-37e1-8389-d7681ccddc0f | -9.4325 | -50.1299 | 2026-09-16 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a1fc9c17-90b6-303e-ac54-49773c10335f | -6.1362 | -59.8871 | 2026-09-16 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| b0debdeb-c4f9-37c8-83b9-81c22336c20c | -15.3408 | -52.9704 | 2026-09-16 15:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 541189c4-b428-334b-a24c-1505e5231281 | -10.5535 | -57.4567 | 2026-09-16 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4ff9aefe-5d9e-3a52-ab9a-5efcf285828e | -8.6311 | -66.5287 | 2026-09-16 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e00c2003-0663-39f1-a43c-b56c61a72c35 | -6.0993 | -59.9076 | 2026-09-16 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5e61ee1c-2884-357b-a6a6-995ea216120b | -1.2268 | -49.1899 | 2026-09-16 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |


[Clique aqui para ver as próximas entradas](README85.md)
