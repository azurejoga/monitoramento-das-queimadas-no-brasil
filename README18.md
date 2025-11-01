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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cc3ba34-0e28-3dc6-a22e-a66e45968fb4 | -4.29931 | -41.44111 | 2025-11-01 04:38:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bf7d9076-e206-38fe-9846-9c5c7bc75003 | -3.06866 | -51.24687 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 193cc2b4-141f-3b77-bf6b-b7193c51173d | -3.47523 | -53.49765 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec2e1397-4e48-3730-9af3-4d7dd8db7674 | -5.1461 | -49.86818 | 2025-11-01 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b53e41f6-da07-3721-b59f-cd72767f25c4 | -1.85525 | -54.55158 | 2025-11-01 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 91850af5-244e-35fb-b648-ceb610bf9739 | -2.21085 | -46.18523 | 2025-11-01 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a3681f0-68fb-3fb7-93aa-2b7358e3b144 | -6.57938 | -48.73536 | 2025-11-01 04:38:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bfa368c-fe35-3b5e-8673-aee407dd10a2 | -3.47064 | -50.93867 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9684db7-fdd7-39fb-b340-697e63252029 | -4.21974 | -49.78593 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3611f2bb-baed-3135-bbd2-e6bae3a42dd1 | -7.34651 | -47.65298 | 2025-11-01 04:38:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a530591e-286c-3a48-b234-4bda6dfe324c | -5.12403 | -43.39105 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7e30fe8d-8a98-35a9-b4a1-bbbe66032330 | -4.77953 | -46.50291 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebd1f965-2ea3-38c8-aede-ee94d69dafdb | -5.38737 | -45.54472 | 2025-11-01 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01bb6698-0800-3c11-b110-6fc7da70b6ea | -7.34988 | -46.21615 | 2025-11-01 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dea9c6fa-c4ee-3221-a3cd-f9645c4d7722 | -5.59371 | -45.03752 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| edbbcede-f9cf-3f1c-a3b7-67b240ab821a | -4.05324 | -47.50057 | 2025-11-01 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e7fc813-e5a8-3ebb-88fe-3c506597fefe | -4.56038 | -48.48242 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e00744f5-9e3e-321b-acf3-cf947f66db6c | -5.09177 | -47.71104 | 2025-11-01 04:38:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 611012a7-7cf0-3da7-a379-046d10cc3375 | -3.23326 | -50.57857 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b6b47f1-d172-3cd4-a40f-de7c2d28d5f0 | -2.79504 | -50.28745 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 683700b1-fcaa-3b22-a384-0ae324bf1194 | -3.64035 | -52.09607 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b1affe7-2d75-3afa-b274-2a81da8d6b18 | -8.86049 | -49.88132 | 2025-11-01 04:38:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d2ec15c5-1dd5-3d0a-8946-1500339ed9ee | -5.71087 | -46.50604 | 2025-11-01 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c88f1b6-c609-34a9-bd96-91873759e47b | -4.39705 | -47.71616 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc4a9ef1-2935-3763-a6b6-cab187a5fdc0 | -3.1133 | -45.22961 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55908271-27ec-3817-b3e8-9022003ab565 | -4.91617 | -45.59069 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 324317e0-6093-39dc-8e81-dfff26017195 | -9.27268 | -48.22232 | 2025-11-01 04:38:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad49f76c-701e-3212-9848-577a26c33a56 | -5.72405 | -44.53259 | 2025-11-01 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d16e007-b500-32cf-accd-7b399a706860 | -9.26929 | -48.22178 | 2025-11-01 04:38:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a951a95-3276-3723-be91-76600506124f | -8.15115 | -45.44236 | 2025-11-01 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32fa03d7-6f98-3273-818e-ac88e244c321 | -3.74843 | -51.26521 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 663be922-6582-39ac-9338-3405f87b2992 | -8.8277 | -49.71972 | 2025-11-01 04:38:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 633ae9bc-776b-33d3-8cca-333edf2559b0 | -4.53159 | -46.3996 | 2025-11-01 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fc116a5-0c5f-39a1-9761-8a46403beb4e | -2.89342 | -40.49089 | 2025-11-01 04:38:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e8c0fe55-14cd-3ed4-9257-dbaeb3d4a9af | -6.55863 | -52.80017 | 2025-11-01 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a74076a5-cb80-361a-b840-10e739ab2ada | -5.11566 | -43.38985 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1487400-4f73-3db3-b874-619378809649 | -3.03867 | -50.34429 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08124e72-37c5-36e8-b8cb-1150d1f7f364 | -7.36212 | -47.77959 | 2025-11-01 04:38:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e12bd25c-61e7-3a68-906b-e988110b6e0d | -7.07225 | -47.01011 | 2025-11-01 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 447c80c1-9cef-3de5-8d86-0e063a5dee73 | -5.39933 | -48.25154 | 2025-11-01 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b861e47-a112-3563-a615-4dce1711579e | -2.87147 | -51.39287 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2bb138f-b15d-33d4-86d5-deb4723a5adf | -3.22888 | -50.65044 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dc4cf8d-dfbd-37db-ac4f-f4264cceb059 | -4.79886 | -46.4701 | 2025-11-01 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21960836-1050-3ddb-b113-b962eb46bee5 | -2.65549 | -48.50241 | 2025-11-01 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 5f671f8c-08be-3f82-9639-92a1b5b952bc | -2.05037 | -52.07363 | 2025-11-01 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa2adfe2-3209-3680-b8dc-7087de379918 | -4.55742 | -46.68806 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fcbae92-39ba-3919-910d-f794e8a334d4 | -8.85773 | -49.87732 | 2025-11-01 04:38:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9e7b673c-1bd3-3b3d-ba18-79d1ab8d8c05 | -4.82639 | -45.79218 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8676d998-4ee8-38b2-a34d-8e529d62e537 | -3.46718 | -50.93814 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20d7bb8e-f196-30a3-8265-f38c4f272117 | -4.80684 | -48.71501 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c6ad472c-a7a0-34c0-9123-e141f737fc4a | -5.75007 | -46.65873 | 2025-11-01 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f087b802-820e-31c9-83d5-4673ff1310fc | -5.92657 | -48.40529 | 2025-11-01 04:38:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf4d20cb-ce25-3832-a720-d414a3b2e6ea | -6.73722 | -45.9556 | 2025-11-01 04:38:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa70353a-8851-3608-8317-41dd2a2f9848 | -4.68575 | -48.26836 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 109a564c-2ef0-3204-a309-beb08a136104 | -4.64633 | -47.9526 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e58c7298-d928-3874-9e1f-b4049e80131e | -9.02956 | -47.46051 | 2025-11-01 04:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 28952cf1-1783-3c88-a5ed-c6cea48d14f8 | -3.46851 | -47.62991 | 2025-11-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6645de64-bccb-3de6-8bb3-4cb7c61ab63e | -5.96155 | -44.72009 | 2025-11-01 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27baeda8-a2a9-3241-9a4f-d5ae432c5e78 | -4.55431 | -48.47795 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82bd24e2-d8d8-3701-8262-2106b5afe382 | -5.61989 | -46.81029 | 2025-11-01 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 374f39ac-e911-3038-a451-394eb2cf5c97 | -3.21283 | -45.75814 | 2025-11-01 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8626e98a-9ed1-316a-91c0-dca264443511 | -5.48495 | -43.0867 | 2025-11-01 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5b62b76-f8d5-3e20-b83e-64b4a932b449 | -4.56143 | -46.68481 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d10335e1-9763-3935-8280-9b169916d6f7 | -6.20384 | -43.70681 | 2025-11-01 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdd284c1-9f13-37cc-9280-5687a9b16d96 | -3.52878 | -47.54949 | 2025-11-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f653ade2-3ec5-3e69-b1a5-18f863475c9a | -3.49001 | -52.35418 | 2025-11-01 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 943fb38f-31b9-3f86-b90e-3258e650af65 | -4.68409 | -45.66303 | 2025-11-01 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9798f651-75f6-3c83-b96c-6b394a7bd116 | -4.54706 | -45.7996 | 2025-11-01 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61c97ea4-d576-3513-9f4b-e2e87252befb | -3.06804 | -51.2508 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a9a33b55-cc7f-3a61-a609-2e84ff16b9a5 | -4.76167 | -45.4243 | 2025-11-01 04:38:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c78b538-61ed-306f-aec1-f9b65e04b466 | -3.58581 | -50.26204 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1a26750-798e-3a43-a454-696795ae4780 | -3.53212 | -47.55 | 2025-11-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69bbf12b-09c4-3f13-af79-4ad57187404f | -4.40156 | -48.21328 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5332615c-9c3f-36ca-b80e-3c8699b6c8c1 | -6.99604 | -46.53095 | 2025-11-01 04:38:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27ff953e-9060-3b2c-8794-4871f755defe | -3.07157 | -51.25135 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b26311d-7add-3abe-bf76-efb9a14be65e | -3.48188 | -50.07942 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26384880-5466-300d-afb5-09061eeac0a0 | -4.6741 | -46.52702 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7e9f2389-218a-3cf8-b4e4-6a4e4ae7e942 | -5.19418 | -44.91141 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 325b14e4-b392-3c4a-8e36-bb6784ea4930 | -3.41655 | -49.99987 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 11c921dd-d5a7-3ded-a65b-de08b627fdb0 | -3.45665 | -51.54692 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93711474-bab6-3c7e-bd43-6bdfa7cd2a3b | -6.13259 | -45.94296 | 2025-11-01 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c1f9a5f-7cb0-366f-91cf-ce6db8bf0a21 | -2.89257 | -40.49644 | 2025-11-01 04:38:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e3fbc3f1-2fca-3305-89d1-8dba14f62795 | -4.77317 | -46.49795 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ceeec3b-c001-3344-8733-d493522125e5 | -3.56598 | -45.16127 | 2025-11-01 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 398fee61-7610-3e46-9c9c-2edc094809df | -6.32371 | -43.62375 | 2025-11-01 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cffed90c-0a13-36b0-83f1-2dd6071c59ae | -4.60832 | -44.42455 | 2025-11-01 04:38:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 798cb3bc-47f3-3e28-a599-573448475ce0 | -5.25917 | -44.31116 | 2025-11-01 04:38:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5ac98c8-651a-3780-bf72-e4d7f0ddd232 | -4.87381 | -45.72241 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3fcfa6a-e666-3d56-ab36-dafd680128eb | -7.36398 | -47.00034 | 2025-11-01 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0591f77-1917-3c4f-a18f-9c8abb4c7aca | -3.75789 | -42.42947 | 2025-11-01 04:38:00 | NOAA-21 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7a495dd9-c264-3e0e-bb96-c3449ab46488 | -8.70943 | -41.58582 | 2025-11-01 04:38:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9dfa864b-fb14-3ef9-8be5-1ec12f94d64b | -3.5751 | -50.26407 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee1a6d84-5d60-32c8-aae0-0d2f57341203 | -4.91546 | -45.09401 | 2025-11-01 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9684eee3-6f17-3c38-b46b-abd67de850bf | -4.80439 | -45.73118 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ee75b45-16a4-3c01-a22d-d18ddf616cd3 | -5.07037 | -45.11586 | 2025-11-01 04:38:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ec96693-f68f-3edd-a5ae-5d8eb2ce7f65 | -3.5395 | -50.17291 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea2c0a4a-b3f0-37d5-aa3c-31d1babb8e05 | -4.9985 | -48.48739 | 2025-11-01 04:38:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d84b922f-5253-3a26-b29b-ecbf3ae8d15e | -5.48984 | -43.08328 | 2025-11-01 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19a4a48b-d260-3399-9abb-24a6795399eb | -2.06907 | -46.351 | 2025-11-01 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d93fdc4-59b6-3365-b89f-41b389838a4e | -5.8328 | -44.33995 | 2025-11-01 04:38:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README19.md)
