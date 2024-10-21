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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 141608c3-cdba-3498-838e-ff7c8d94686a | -1.19371 | -53.64006 | 2024-10-21 01:07:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 84e42741-498d-32a6-a8eb-a3a2bfb38c08 | -1.19236 | -53.63034 | 2024-10-21 01:07:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 057757f7-6b3a-3f19-aa13-a5455fd06089 | -1.191 | -53.62056 | 2024-10-21 01:07:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 2715ef0b-0ce1-3b51-b21d-854b0c1c6759 | -1.18305 | -53.63173 | 2024-10-21 01:07:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d236af12-588a-3ef2-af4f-6b6ab8f7af0a | -1.18167 | -53.62175 | 2024-10-21 01:07:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 44e3f76f-cb90-35af-a6c8-4ed680acad7a | -0.60078 | -52.15933 | 2024-10-21 01:07:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e52a77ea-ea05-3fed-9b62-150c9a9603d5 | -0.21293 | -49.9085 | 2024-10-21 01:07:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9e4ddfb3-755e-3670-9450-953f5985f3fa | -0.1824 | -51.54443 | 2024-10-21 01:07:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b2ae1470-df5a-3faa-9423-efc4fa5f0220 | 2.91563 | -51.00222 | 2024-10-21 01:07:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0ef84f06-e29f-32da-bbe1-f75636947040 | 2.10683 | -50.65606 | 2024-10-21 01:07:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ec2915fd-c2df-3365-bb09-1fcf0121f8ff | 2.09771 | -50.65479 | 2024-10-21 01:07:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8433b21c-d793-3273-9e82-691325a4c965 | 1.82647 | -50.48231 | 2024-10-21 01:07:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 03f851b6-f9b1-3f93-b653-bd9ae4053828 | 1.82515 | -50.49181 | 2024-10-21 01:07:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 31804749-7266-3674-87c8-2aac87e45d3b | 1.01424 | -51.15453 | 2024-10-21 01:07:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9f17683f-a72f-3c5b-9dee-8ebcb608c48a | 1.01299 | -51.16349 | 2024-10-21 01:07:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 38.7 |
| b297246d-3a9e-3411-a38c-c90930f1c149 | 1.01174 | -51.17245 | 2024-10-21 01:07:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 22.0 |
| a369878b-5747-3d92-9331-571073388236 | 1.0105 | -51.1814 | 2024-10-21 01:07:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 47c5c94a-a4b0-397e-ad4e-236200cb7b35 | 1.00554 | -52.21742 | 2024-10-21 01:07:00 | TERRA_M-M | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d356411-c3cd-342d-b7ef-b0f7fb3a4c5d | 1.00409 | -51.16224 | 2024-10-21 01:07:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c17b06dc-049a-319c-89eb-3f305e672bc3 | 1.0028 | -51.1656 | 2024-10-21 01:15:00 | GOES-16 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b9fc288c-cb49-3107-931b-818ba0a48632 | -1.2018 | -53.6366 | 2024-10-21 01:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 88f3254b-4b84-3bba-8006-f2518c008083 | -1.2018 | -53.6164 | 2024-10-21 01:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| eaa97383-7f9e-3003-90f3-e0637d1a62a9 | -1.1834 | -53.6368 | 2024-10-21 01:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| feed616d-a041-30bb-9453-059889d667d6 | -1.1835 | -53.6166 | 2024-10-21 01:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 3d22f0fe-1fd3-36d9-9d15-14675a52681c | -2.2199 | -50.4594 | 2024-10-21 01:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 844d1662-698c-3503-9a7d-27afac39daad | -2.2671 | -47.0775 | 2024-10-21 01:15:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 0f57cbc9-e30e-3338-9a46-21a10460e73f | -2.2856 | -47.077 | 2024-10-21 01:15:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 17952a6a-7819-3587-986c-e8d364f0f1ff | -2.464 | -49.1024 | 2024-10-21 01:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 9d34b576-372d-32d1-9813-fa0a766a126f | -2.4824 | -49.1233 | 2024-10-21 01:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a78943b9-d9bf-31ae-b8e8-634915ecaff7 | -2.4824 | -49.102 | 2024-10-21 01:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| f5f0d9ec-9a77-360d-9cc4-d926e017917c | -2.8668 | -45.4631 | 2024-10-21 01:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 2f9c1548-b482-3ba9-a10c-8b1f8df001d3 | -2.8555 | -53.3459 | 2024-10-21 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 25ea2f4c-691d-370b-93e5-64210a18818d | -2.8556 | -53.3256 | 2024-10-21 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| eba84f94-2bce-3ca3-b2a5-adee6ccc26eb | -2.905 | -45.2143 | 2024-10-21 01:15:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 122.0 |
| bd63bd7c-02da-3d6b-921b-5e5f67236b54 | -2.9051 | -45.1918 | 2024-10-21 01:15:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 6a95bfa8-0451-3eaa-8aba-fddf39fb4873 | -2.7773 | -49.3067 | 2024-10-21 01:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 374aea13-f55e-3bc6-b08c-c2a90395782e | -2.7885 | -51.3618 | 2024-10-21 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 3e54fe57-1dcb-37e9-a6eb-a767f4c18eb9 | -2.8069 | -51.3613 | 2024-10-21 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| cdc45b49-51d9-32d8-82ec-dfa90b926a52 | -2.8482 | -45.4637 | 2024-10-21 01:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c2faf558-7ae5-3a5b-8444-0fc693a25838 | -2.9853 | -53.0384 | 2024-10-21 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e623974e-cc59-3860-bd45-51940fbe5087 | -3.0036 | -53.0583 | 2024-10-21 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| db927464-48ff-34ee-bd17-fde2cf64edd3 | -3.0037 | -53.038 | 2024-10-21 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 1ed5ae66-42c0-35b1-8fdb-c18f05704518 | -3.0176 | -54.3489 | 2024-10-21 01:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 9986deb4-47a0-39fd-bb42-48f781c19f0c | -3.0581 | -53.2395 | 2024-10-21 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 9870401c-83b1-364a-af9a-be594e45e04a | -2.9674 | -47.9931 | 2024-10-21 01:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 49e22d51-bb98-3856-9780-c14ea6d479e0 | -2.9852 | -53.0587 | 2024-10-21 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| c56d7854-115a-308c-b8b5-0e55a5fe7801 | -3.0765 | -53.239 | 2024-10-21 01:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 98cb8450-210d-3b60-8659-c05a85789216 | -3.1138 | -53.1163 | 2024-10-21 01:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 543a9c59-3a4e-309c-a797-a2861463789b | -3.1962 | -50.8099 | 2024-10-21 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| f37204da-569f-3e63-8311-a0cc97945e1c | -3.2146 | -50.8093 | 2024-10-21 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 3b3aa5e4-4369-3c79-9136-8392a72f80b5 | -3.2147 | -50.7884 | 2024-10-21 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 9eab736c-5e99-3b3b-9410-cc042f1fc7f6 | -3.7752 | -53.4012 | 2024-10-21 01:15:28 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 361bcccd-79e4-3c47-9aa3-d1da3fe8871e | -5.6894 | -46.435 | 2024-10-21 01:15:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 167.9 |
| ce9ec9ec-5e8d-3c26-a66a-3fa2a26adcea | -5.6896 | -46.4128 | 2024-10-21 01:15:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 0046599c-029b-3dab-9940-43e0654173e7 | -5.7081 | -46.4338 | 2024-10-21 01:15:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 04617a62-5904-3cb8-a0b9-b95e5a531727 | -9.3718 | -66.4891 | 2024-10-21 01:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 257ffdfb-1239-39ff-a283-1b85f0d3aa45 | -12.4778 | -63.1885 | 2024-10-21 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 1be95378-d12f-3df1-bbce-aeffbecae6a6 | -12.5147 | -63.3014 | 2024-10-21 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 693bf0b4-d696-3079-aa87-53533dd068b9 | -12.5168 | -63.0329 | 2024-10-21 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 06deb11e-5f76-3883-964d-26307f851fe0 | -12.5357 | -63.0319 | 2024-10-21 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| cf481a38-bb35-3084-b8cb-3c03702f3d2a | -17.7262 | -57.4545 | 2024-10-21 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 224.4 |
| 826d7097-19bc-3373-b565-1debf82e16ff | -17.7848 | -57.4885 | 2024-10-21 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| dcf73568-1273-3153-afcb-73f4dfe89de2 | -17.6871 | -57.4387 | 2024-10-21 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 533440a1-de1b-3ae4-b634-655d8d46dd79 | -17.6875 | -57.4181 | 2024-10-21 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.8 |
| f652a1fd-d793-3afe-bf14-701cc149d0df | -17.7065 | -57.4569 | 2024-10-21 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.5 |
| 988adc1e-1d35-33d1-899a-82da5bd1f506 | -17.7259 | -57.4751 | 2024-10-21 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.6 |
| d5e64c77-beb0-3251-b4d1-3c10c312b976 | -18.263 | -56.1021 | 2024-10-21 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.3 |
| e84512e8-2e4d-342a-a641-ec1074a4f2d4 | -18.2828 | -56.0994 | 2024-10-21 01:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 147.6 |
| 15e7b817-07b0-3de4-81c2-84b9a80c5cde | -18.2832 | -56.0785 | 2024-10-21 01:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.2 |
| ac4d5cdc-ef1f-36b9-ac57-3ff545a39d5f | 1.0028 | -51.1656 | 2024-10-21 01:25:00 | GOES-16 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 82.5 |
| bf457b51-357a-3848-9f8d-0f8d574e4813 | -1.1834 | -53.6368 | 2024-10-21 01:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ad4f25cc-d045-3bcc-9a15-16e3d9d2f393 | -1.1835 | -53.6166 | 2024-10-21 01:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 04b1ad5c-3681-3251-9da9-dc4524771d85 | -1.2018 | -53.6366 | 2024-10-21 01:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| b2866a46-34ef-3da9-ab44-335a81476bbc | -2.2671 | -47.0775 | 2024-10-21 01:25:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| b0cdae9b-de90-3383-9fc5-cd6299e91b27 | -2.2856 | -47.077 | 2024-10-21 01:25:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| b7cc6726-7a75-310f-a534-2da287f8197c | -2.464 | -49.1024 | 2024-10-21 01:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b48cc23d-f3d7-3eaf-b5a2-f357e3d2cd65 | -2.4824 | -49.1233 | 2024-10-21 01:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 5e78a696-2121-31dc-b664-19890cb2c898 | -2.4824 | -49.102 | 2024-10-21 01:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 5215ff87-8ba4-363e-aca8-a98084e0007e | -2.7773 | -49.3067 | 2024-10-21 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 52b05911-4dc5-36eb-8e23-9df95c3faaef | -2.7774 | -49.2854 | 2024-10-21 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f97ded9b-1ddc-3fd8-9832-02e10ac8e2a4 | -2.7885 | -51.3618 | 2024-10-21 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| d678c897-2807-3df3-96ce-677671538d52 | -2.8069 | -51.3613 | 2024-10-21 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| d7d35e8e-d0f2-35b2-bc57-93d2fd4e923b | -2.8482 | -45.4637 | 2024-10-21 01:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 745fbe46-9dae-3be8-a1fc-529bc1c9cf03 | -2.8372 | -53.3261 | 2024-10-21 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 890a7feb-a917-3039-b936-188da76dfdc9 | -2.8668 | -45.4631 | 2024-10-21 01:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 02369cdd-2695-365d-9871-b2068640fa72 | -2.8556 | -53.3256 | 2024-10-21 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 7ce4db51-11f0-367e-82c3-dfb325185c84 | -2.905 | -45.2143 | 2024-10-21 01:25:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 66601926-4a6c-394e-acde-831da79a72c3 | -2.9051 | -45.1918 | 2024-10-21 01:25:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 96da21de-8599-3847-a914-f241e103a86d | -3.0036 | -53.0583 | 2024-10-21 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 42d15ce3-9db4-31fd-a141-5d190914f36b | -3.0037 | -53.038 | 2024-10-21 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 79afaadb-3dbc-31b4-a654-c8a598ce027e | -3.0581 | -53.2395 | 2024-10-21 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a65b14ad-8cac-3976-af8c-8c17e92b388c | -3.0765 | -53.239 | 2024-10-21 01:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 57ac1a07-c831-3818-bef8-30d2f8a45f1c | -3.1138 | -53.1163 | 2024-10-21 01:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 43491477-c865-3b84-99e7-1f3fbc1221a6 | -3.2146 | -50.8093 | 2024-10-21 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 36614df9-696b-3574-a8d4-9e37c028db3c | -3.2147 | -50.7884 | 2024-10-21 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 47d90bec-eb99-3e5a-b08e-3a5e76dfd58f | -3.2585 | -53.78 | 2024-10-21 01:25:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 18e3f1c7-73e0-37a3-a8a5-81329c872f51 | -3.7752 | -53.4012 | 2024-10-21 01:25:28 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 01257a41-2d05-3c8e-b2af-25fcfe8e40f5 | -4.8924 | -45.8386 | 2024-10-21 01:25:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 27f97f61-232a-3a21-8398-0ea99e0813ac | -5.6707 | -46.4363 | 2024-10-21 01:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 4a030e98-ad8c-354a-bb93-80b5c6952dd7 | -5.6894 | -46.435 | 2024-10-21 01:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |


[Clique aqui para ver as próximas entradas](README15.md)
