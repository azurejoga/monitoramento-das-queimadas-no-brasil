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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce7e8a3c-7161-3a57-b5b0-e95767ec6178 | -2.87267 | -51.74666 | 2026-09-03 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b325006d-2c52-3d14-a9de-8692cd4794cc | 2.51732 | -50.85137 | 2026-09-03 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca11817c-75f4-39ab-8ed8-36301963c241 | -3.33839 | -42.80117 | 2026-09-03 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0ce2f8a-8b7d-392e-ade8-a0abcee7ccb9 | -3.24511 | -47.25244 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 521338bf-08df-30a6-9d21-d2f295dc501b | -2.60474 | -48.25154 | 2026-09-03 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f87c2c43-7869-309b-bab6-65bb55783018 | -1.47994 | -55.54607 | 2026-09-03 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56e1d46f-638a-3a48-819d-994f84527969 | -1.0249 | -53.72532 | 2026-09-03 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14699bb7-2e25-385d-941f-ff938f49d3fe | -3.80329 | -49.1106 | 2026-09-03 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59394925-15ae-377c-8781-f226d83cb05c | -4.11323 | -51.02974 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 411898d2-2e38-3373-8b3f-bdbbce656ee5 | -1.79931 | -47.9522 | 2026-09-03 04:55:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3257bebb-84fc-3b9b-8827-1c7b3897d162 | -4.11659 | -51.03025 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e2f1e81-aa13-3219-8c82-a849f059a551 | -2.00575 | -54.15242 | 2026-09-03 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29e2e622-02d1-39f7-8d8d-e2ddf86e968d | -3.80171 | -49.11176 | 2026-09-03 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adc593ec-3483-3839-9cad-2dda1ca93443 | -4.14681 | -51.07847 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebd6f6ea-fcba-3880-9575-67dfc2b16c70 | -4.37896 | -50.76501 | 2026-09-03 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5df1fb38-f9a8-3be7-bf25-f8035e8fe91b | -4.11099 | -51.02211 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd79d69f-8939-3bce-896d-650b0eb72676 | -3.22166 | -48.61276 | 2026-09-03 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df1755a4-efec-3ab3-bac0-cf29f2c4fc7c | -4.18516 | -47.84644 | 2026-09-03 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e5da0fd-5374-3f54-9cd4-9b5c09b336a9 | -3.24459 | -47.25587 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 7f16459b-9f3d-39e2-b62f-9a0834a173ef | -1.01803 | -53.72412 | 2026-09-03 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbc2524e-0941-3546-a691-c93c1de857df | -3.80532 | -49.11229 | 2026-09-03 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1d61647-e6c9-3ec4-b9e0-25ced177e7a9 | -2.55541 | -44.14386 | 2026-09-03 04:55:00 | NOAA-20 | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b886d3ce-2737-3e73-8587-ff642dd54409 | -1.42245 | -54.22506 | 2026-09-03 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18583b57-0256-3197-abf3-72b530d90c5b | -4.02366 | -47.72282 | 2026-09-03 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 915b6818-3cc4-3443-b68d-d60a6e4c457e | -3.62729 | -54.02926 | 2026-09-03 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b90d6a4a-1909-309c-ad14-8934c4032a58 | -1.4795 | -55.54354 | 2026-09-03 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56da4328-447e-3c75-87d8-1c173a9a27a3 | 2.51786 | -50.8548 | 2026-09-03 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f150c7c6-7937-325e-9556-538be0e62ca5 | -2.40708 | -57.89739 | 2026-09-03 04:55:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1fcae46-17f9-3e9d-bd29-9b05906724ed | -4.14345 | -51.07798 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 523b485e-9549-3f2a-a2d8-1082902a5941 | -1.62043 | -55.16829 | 2026-09-03 04:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbe55518-8099-32af-addc-6ac5abb9e553 | -2.26127 | -47.00953 | 2026-09-03 04:55:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0018e35a-beca-347f-ac9c-8bed3c271dd8 | -1.02148 | -53.72466 | 2026-09-03 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d9cc3b1-52b1-3222-9eb8-4d1e0307b2f7 | -2.10936 | -53.51992 | 2026-09-03 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dc55a35-833e-3622-90c9-c6ba2a693c82 | -3.22058 | -48.81157 | 2026-09-03 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1cbd598-233a-395e-baed-b07ac068006a | -3.33245 | -42.80384 | 2026-09-03 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 147f36fc-14bb-33a7-90bc-b20679accbe9 | -3.24061 | -47.25524 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6bfa1120-3094-346e-bde1-c5cff1b2c712 | -3.17352 | -48.13043 | 2026-09-03 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e9c4e66-1aec-3f7f-b871-026fe9c56f88 | -1.48068 | -55.54157 | 2026-09-03 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fba229b1-112a-3736-b142-812deb9e8f0e | -2.92921 | -54.09565 | 2026-09-03 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b952a073-be7a-3542-997a-319a1bf8454a | -1.51195 | -54.95698 | 2026-09-03 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b4f022f-4ee7-3dfa-a4c8-8af2dda7caa6 | -3.92753 | -49.05558 | 2026-09-03 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd1ecbd1-1bc2-3988-b295-cfeaedbf740e | -4.08698 | -51.04375 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d144ce2-1c67-3724-b493-ca25b4f5434c | 0.97946 | -59.38636 | 2026-09-03 04:55:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 381b71ca-15e1-37c8-95c9-85ca13a28e65 | -3.49446 | -53.28531 | 2026-09-03 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0881085b-346c-32da-9904-231349fd85ce | -2.56271 | -50.58976 | 2026-09-03 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1119a32e-3ed2-3d67-a09a-86c7c976f823 | -3.96663 | -48.12968 | 2026-09-03 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3516244d-8650-36ec-8aff-087a9dd9c298 | -3.03406 | -51.00363 | 2026-09-03 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b79f865-8c62-3035-a3fe-8d0e07fda724 | -2.47792 | -49.40708 | 2026-09-03 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21e2492c-9f27-3d52-b374-e064c6a09287 | -4.0234 | -47.72476 | 2026-09-03 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03df6dba-5756-3759-bd8b-ce86c5e98a0e | -3.62657 | -54.59914 | 2026-09-03 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f57a1e6c-b8fb-339c-9459-c4af9e5c77a9 | 0.46742 | -50.91067 | 2026-09-03 04:55:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19caa1bb-f1be-3f6e-8698-21bb7b1dd336 | -1.47752 | -54.81607 | 2026-09-03 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 964d2a43-ea67-319b-bc2b-40083b0c5c67 | -1.71496 | -47.09068 | 2026-09-03 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0c3be30-4954-3fed-ac0d-54dfa3eacab8 | -2.38854 | -47.60476 | 2026-09-03 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98352ccc-2cb0-3e5b-b5f0-43591843688f | -3.24563 | -47.24901 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 566c6430-2f66-3921-ab8c-324111b15cd5 | 0.97902 | -59.38345 | 2026-09-03 04:55:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b0265c0b-7f05-380e-a3ac-21fda2cc8b5b | -2.48143 | -49.4076 | 2026-09-03 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fd5be92-9fa2-36ce-9e14-f74917fdc1b9 | -3.50544 | -46.12215 | 2026-09-03 04:55:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70a24e95-ee55-3c4d-8b8f-ff9ab14a13a7 | -3.6453 | -49.9691 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0fac0fcf-44b2-3cc8-8724-501de932f1ad | 1.6745 | -60.13941 | 2026-09-03 04:55:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4292f94-7f8a-311b-ab8f-5ec3586ae0ac | -4.52322 | -48.74842 | 2026-09-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5eb322ac-b903-33f4-b8fa-244372ca4a36 | -1.14913 | -54.18775 | 2026-09-03 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf60f86c-10e3-35e6-82a1-2c7d15b77068 | -3.18621 | -48.02434 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94f2b38c-a783-3e4d-8ffe-cbeacbb1284e | -2.7885 | -49.52813 | 2026-09-03 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf43bd0d-9fd0-3684-ba97-1f45758dea24 | 1.67501 | -60.14274 | 2026-09-03 04:55:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 81e09f98-aabe-3398-94b6-9b34f27c51a5 | -3.03229 | -48.41335 | 2026-09-03 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f6b99e3-e89a-366a-9bf8-1fe5f9bcc9f1 | -2.47534 | -49.33075 | 2026-09-03 04:55:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df68ac93-b5f5-31a4-aa01-417b093273da | -4.14737 | -51.07495 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6653f927-fc7d-34c8-a92e-177aee75c560 | -1.47392 | -54.81546 | 2026-09-03 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c89eb570-11a8-3cfc-9e15-cf944cff1e00 | -1.01519 | -53.71986 | 2026-09-03 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e0339c4-4090-3187-92e1-b75dfae52cb5 | -1.46672 | -54.8143 | 2026-09-03 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f380ae6-4470-3c15-ae06-d58931c3f708 | -3.81858 | -50.11409 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c1cd7052-20a1-33ac-9197-65c5592e9eee | -4.14893 | -51.07804 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bac9daea-794c-333c-8d2e-8e286848fe81 | -1.65715 | -55.03053 | 2026-09-03 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5aee9b91-6007-3b46-94db-136c1a235aa7 | -3.03599 | -48.4139 | 2026-09-03 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e283fdb6-2a14-3b31-8726-640d88be44e1 | -3.33891 | -42.79773 | 2026-09-03 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1a757c8-6f4f-3e22-b287-f8dbf817d2c5 | 1.91187 | -60.58066 | 2026-09-03 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b74e5054-75fa-3dec-b07e-9050b71ff583 | -3.59426 | -55.37823 | 2026-09-03 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a71eff3e-1ec9-3c81-aa29-f615eb2a31c2 | -3.24875 | -47.91703 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be3a216e-71c1-36c7-8540-0d6161aced3a | -2.705 | -49.50446 | 2026-09-03 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 396af9c9-3bcb-30d8-a67b-2c11c6d9f084 | -1.50831 | -54.95646 | 2026-09-03 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5d8a3e0-67a9-3329-891d-b780da44a1ba | -2.72336 | -49.78831 | 2026-09-03 04:55:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 776f125a-c999-3551-b534-c5e8f7d08420 | -3.67446 | -53.75623 | 2026-09-03 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64217b8b-539f-30f7-9877-ecea04cf708f | 0.79088 | -51.96734 | 2026-09-03 04:55:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 744ecff8-4300-3158-bb12-61fd7aaf889c | -3.23765 | -47.24778 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 098f033f-f36c-348f-9296-e936d0a61353 | -3.03764 | -48.41675 | 2026-09-03 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 575ac201-0833-3a32-8a1b-3d0184662287 | -3.12778 | -48.59091 | 2026-09-03 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cb5fe5b-fe4f-3e92-ac2e-68e76ab72bf1 | -3.48483 | -52.98503 | 2026-09-03 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b0a50c6-453f-3ec5-baa6-074bdafaa7cc | -3.67504 | -53.75261 | 2026-09-03 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 774eb0fe-a6d2-313d-8ebe-86bf781fd9e8 | -1.62111 | -55.16402 | 2026-09-03 04:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fa846f0-017e-342b-942f-fa6b70a94b06 | -2.82974 | -48.65389 | 2026-09-03 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f560c24d-d33b-3405-93e5-baae928e08ba | -3.33193 | -42.80729 | 2026-09-03 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 514e3c3c-5304-3e9b-9693-996505941d45 | -3.24164 | -47.2484 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bcbd9af9-664e-3b37-ad82-b577f22fc0d3 | -3.24112 | -47.25182 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bd61cd96-1027-3b07-ad3c-5f989965d91e | -2.44724 | -50.25875 | 2026-09-03 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b44c0457-78a4-3cca-90a3-9e11fa17df9d | -1.46607 | -54.8184 | 2026-09-03 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c73fd450-c690-343e-87d3-baacd1acefa2 | -1.50765 | -54.96062 | 2026-09-03 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fdbb2646-1ac8-36a7-b9d2-e5f36a71af96 | -4.14948 | -51.07452 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50fee8e4-8957-3cfb-ad1a-6b26c79d366e | -3.44697 | -56.32447 | 2026-09-03 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 915e9705-4950-3c12-8d87-ebb3ae3dcfbf | -4.1753 | -42.43671 | 2026-09-03 04:55:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README33.md)
