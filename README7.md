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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daa42f4f-fdab-3513-898e-cd7410fefc90 | -12.5155 | -63.2911 | 2024-10-19 01:18:30 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 969ef516-5564-3749-a512-2d9cef7f47df | -12.5176 | -63.301498 | 2024-10-19 01:18:30 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 50c104a5-6fd5-3709-8952-486db1ffd55b | -12.5036 | -63.282799 | 2024-10-19 01:18:30 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 83863db6-8701-3b03-951f-214a76b0597e | -12.5057 | -63.293098 | 2024-10-19 01:18:30 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| da5e52aa-8043-36be-a7e8-4312ffad3da2 | -12.5078 | -63.303501 | 2024-10-19 01:18:30 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 775393e7-10c4-34d6-953f-e7a4cf5c2973 | -12.4917 | -63.274502 | 2024-10-19 01:18:30 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 31d024b2-b4df-314f-82fa-848bb5eb1018 | -12.4938 | -63.284901 | 2024-10-19 01:18:30 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2c0f196a-de9b-3710-9766-2be0565de835 | -12.4959 | -63.2952 | 2024-10-19 01:18:30 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8017ae0a-af9a-3054-802b-f52cb2b358b3 | -10.1441 | -54.9016 | 2024-10-19 01:18:38 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b26879d9-cd28-397b-bd5b-b0b3e3f920b2 | -9.0346 | -67.429298 | 2024-10-19 01:19:41 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09caf171-a09c-39ba-b13d-0d950d681aad | -9.0249 | -67.431297 | 2024-10-19 01:19:41 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bdf44406-bc8f-313f-b701-d86c907ea68c | -4.3869 | -50.527599 | 2024-10-19 01:19:54 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28c1e406-9644-3289-a1c1-d5a170d3cb35 | -4.3922 | -50.5495 | 2024-10-19 01:19:54 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a0dbfce-104d-3c69-ba02-bab5a36fd336 | -14.88638 | -50.74955 | 2024-10-19 01:20:00 | TERRA_M-M | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 65815426-a7cd-35eb-b8ca-9783559340c0 | -16.82314 | -53.94774 | 2024-10-19 01:20:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| fd1b51aa-4a52-3724-85c9-047594236c4d | -16.82186 | -53.93825 | 2024-10-19 01:20:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f5604670-df55-3cb8-8e21-8e3ce789c39d | -16.81413 | -53.94903 | 2024-10-19 01:20:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dc1bb111-77f4-34ce-a14c-e926465d69f9 | -14.38151 | -54.53576 | 2024-10-19 01:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1ece89a9-f87e-3b84-a626-4d603b269288 | -14.38024 | -54.52629 | 2024-10-19 01:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a67ddbd-9fb0-3911-b5ef-bf6c8588be89 | -14.0428 | -53.87605 | 2024-10-19 01:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 04eb5d67-4782-3743-a9c5-db39a2d8b30a | -4.1511 | -51.245899 | 2024-10-19 01:20:01 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae74c17f-64a2-3f97-b3f9-278a063e8390 | -3.7012 | -51.119099 | 2024-10-19 01:20:08 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 295f3ad6-7f17-3ae5-b868-f9418ddafee3 | -3.6865 | -51.1008 | 2024-10-19 01:20:08 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19407804-1429-3989-a559-eb3bdf9471bd | -3.6915 | -51.121399 | 2024-10-19 01:20:08 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be53a1bc-8bf7-3299-9df7-c6c7a633cf3c | -3.4099 | -50.203899 | 2024-10-19 01:20:09 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a7602d6-8685-3ef3-a5e4-0d5bd912936b | -3.4157 | -50.227798 | 2024-10-19 01:20:09 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac9b89e0-923e-3771-9c7c-e041373d805b | -3.4003 | -50.2062 | 2024-10-19 01:20:09 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c54aa6e-ffae-3c4b-b1d9-7a384ea78151 | -3.4061 | -50.230099 | 2024-10-19 01:20:09 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3d74acd-ba6e-3365-8e83-032540c5b7e1 | -3.0721 | -51.224899 | 2024-10-19 01:20:19 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c582e69f-881f-36c1-94fa-bbcf0d79b933 | -3.0624 | -51.2272 | 2024-10-19 01:20:19 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6788985d-d2a0-3fed-8ad7-de346fc613a0 | -2.9691 | -51.049702 | 2024-10-19 01:20:20 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9498918-3358-3b6e-bf23-0badcc80e3fc | -3.296 | -52.862202 | 2024-10-19 01:20:21 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f766a088-4c96-3e94-b9a8-e42fa057a12a | -2.8158 | -51.307098 | 2024-10-19 01:20:23 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8271678c-01ab-357b-97c0-47e5f7a4dc50 | -2.8206 | -51.327702 | 2024-10-19 01:20:23 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14295504-67c9-3b3e-bd9a-ed829b310fa2 | -2.7819 | -51.380001 | 2024-10-19 01:20:24 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a85709ff-54f4-33e9-b32e-7e6464c2bfc9 | -2.7964 | -51.355099 | 2024-10-19 01:20:24 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a84fef1-9db6-3c0e-ac3c-7aecab24e5f6 | -2.7771 | -51.3596 | 2024-10-19 01:20:24 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbe76f61-a6de-377b-8546-120876a547e1 | -3.4039 | -54.152699 | 2024-10-19 01:20:24 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c520ccd-5a0e-3fc6-acb6-dcf9cd72f161 | -3.4136 | -54.150398 | 2024-10-19 01:20:24 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1479d98c-40a7-36a1-90a0-bbd1faebbecf | -3.4234 | -54.148201 | 2024-10-19 01:20:24 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24b228d4-76d3-3f83-9665-fdf40840a88b | -3.4204 | -54.135399 | 2024-10-19 01:20:24 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 630086e7-a5dd-38ae-95d5-7e8dd51d941e | -3.4174 | -54.122501 | 2024-10-19 01:20:24 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff0bbcb-93a5-3fdf-b341-90b67f1f4fbe | -2.7722 | -51.382301 | 2024-10-19 01:20:24 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14a929e2-7330-39f9-ac97-6868c5a0e42d | -2.7674 | -51.3619 | 2024-10-19 01:20:24 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de2ee529-2bf8-3de2-b69d-001ac3b2a2a2 | -2.9326 | -52.930199 | 2024-10-19 01:20:27 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dd4e88b-b6e3-30f0-a52e-a728e21b3620 | -2.9289 | -52.914398 | 2024-10-19 01:20:27 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8905396-ed63-3f4c-9a69-a5bed51bbef3 | -2.9423 | -52.928001 | 2024-10-19 01:20:27 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fca703a9-6fcd-3f5e-acf5-a2c977535fb7 | -2.9386 | -52.912201 | 2024-10-19 01:20:27 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9a55cc0-9935-3cf0-9ce2-4f8c13f22ef5 | -2.9349 | -52.896301 | 2024-10-19 01:20:27 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 457dd00d-3e81-3c2a-a7ea-5389a6963bcd | -2.9566 | -52.857601 | 2024-10-19 01:20:27 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3efdc027-9905-3a8f-a277-424567411636 | -2.9528 | -52.841599 | 2024-10-19 01:20:27 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6777154d-15a7-3f52-b1bf-c98a67c47b71 | -2.9663 | -52.855301 | 2024-10-19 01:20:27 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96537800-af23-3685-9100-fe3f94e56311 | -4.7016 | -60.799801 | 2024-10-19 01:20:28 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f822daa-cd77-30a7-b838-a9f2ecc11568 | -4.6924 | -60.758598 | 2024-10-19 01:20:28 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bbe2e379-1f25-3115-a0b3-52a1b78740de | -2.4882 | -51.8242 | 2024-10-19 01:20:30 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd1c4d5f-af02-3ef5-8363-4391a892fb38 | -2.8341 | -53.340698 | 2024-10-19 01:20:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 699cff0c-c885-3b8e-b4c0-a77d3b83a6f1 | -2.8306 | -53.325802 | 2024-10-19 01:20:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e64e643f-e74d-321e-9e3b-43a0363333f3 | -4.2624 | -59.992699 | 2024-10-19 01:20:32 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af924e3f-34ab-3fb3-8114-95a77467637c | -4.2608 | -59.985802 | 2024-10-19 01:20:32 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64c34290-2d19-31f7-a736-f61375383c30 | -4.5038 | -61.111698 | 2024-10-19 01:20:32 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35ee0f3d-f336-38be-8bd2-659d07fd6e63 | -2.7811 | -53.992599 | 2024-10-19 01:20:34 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ad97936-ae54-3cb3-b040-acdfe90788e3 | -3.983 | -60.398899 | 2024-10-19 01:20:38 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f27d9d9-ed15-3ac3-b618-ab44615c2e53 | -3.9814 | -60.392101 | 2024-10-19 01:20:38 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 090c06af-ede9-37f5-839c-a62212289ddb | -3.9929 | -60.396702 | 2024-10-19 01:20:38 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67882cf9-319d-382b-93f8-5ba134f8d021 | -2.3092 | -54.3913 | 2024-10-19 01:20:43 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9187f1ca-7e10-34f1-8813-142a2b601134 | -2.3062 | -54.378502 | 2024-10-19 01:20:43 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be2b716c-207d-3fec-a552-ca37b1e0ba6a | -3.0505 | -59.192402 | 2024-10-19 01:20:49 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1c2a815-4744-33c9-8e15-c52ab41d1e32 | -3.0489 | -59.185299 | 2024-10-19 01:20:49 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88300b03-f064-3688-9ac6-a6422c79cd81 | -3.0457 | -61.681999 | 2024-10-19 01:20:58 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f5a5cba-f19c-3d4c-b8b3-34d9360b0b5c | -3.0441 | -61.674999 | 2024-10-19 01:20:58 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89c9fe28-e09b-3b99-a7dc-2a177152e6fb | -3.0426 | -61.667999 | 2024-10-19 01:20:58 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e30f4c9-69c3-3bd2-958f-0b332250ab44 | 1.0036 | -59.4417 | 2024-10-19 01:21:55 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 345ed46f-9a59-3105-936c-8f897f9d0291 | 1.0053 | -59.434299 | 2024-10-19 01:21:55 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 089837c0-5809-3780-9c17-4530beb0232b | -7.68808 | -47.31353 | 2024-10-19 01:22:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| dd2861e4-5094-371c-94a8-fa5469f57175 | -7.67801 | -47.33936 | 2024-10-19 01:22:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 98994f83-be73-3d63-9351-31d700375e29 | -7.67425 | -47.31578 | 2024-10-19 01:22:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 90cf401e-c3fe-366c-b69d-618af3c71dea | -6.61773 | -47.38292 | 2024-10-19 01:22:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 9a4dad76-0f30-30c3-a020-49c578d43119 | -6.61339 | -47.39014 | 2024-10-19 01:22:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 4732d48c-4d80-36ff-bbf1-76c48b70c2bd | -6.44968 | -49.93513 | 2024-10-19 01:22:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 66939f66-edaa-36cf-b096-0f70055af56a | -6.44738 | -49.91973 | 2024-10-19 01:22:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| cbcdcc37-e942-30a4-b917-6dad86fc3264 | -5.35641 | -47.74953 | 2024-10-19 01:22:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ea02addf-4ddd-3eaf-a11b-6e11ff4e44ba | -4.75833 | -45.83358 | 2024-10-19 01:22:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| e3cb157a-a289-38d2-b7ca-6c35fde7abc8 | -4.74825 | -45.82821 | 2024-10-19 01:22:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 6d513fda-a782-30a6-ab54-a97356b89865 | -4.70951 | -45.8428 | 2024-10-19 01:22:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 295.6 |
| 130c6f1b-ffd2-39f2-bac2-ba004680249e | -4.69308 | -45.84484 | 2024-10-19 01:22:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 186.6 |
| e13544b8-9584-3655-aaed-5a3b4140217b | -12.44253 | -54.4244 | 2024-10-19 01:22:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d99ddb0e-ef10-3335-8996-b16074e3fc46 | -11.36124 | -55.20383 | 2024-10-19 01:22:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e419b438-d2e8-34dc-9f54-b4ed0b72ff18 | -10.96235 | -54.37669 | 2024-10-19 01:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc300fb0-d6ca-308d-8b27-6a5ab75cb8e3 | -10.67549 | -54.90282 | 2024-10-19 01:22:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| b9a36fec-5750-3c6c-a1cd-710bfd0af483 | -10.67424 | -54.89373 | 2024-10-19 01:22:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 73ad8d20-99c3-3239-a0fd-1bf9acb95191 | -10.47952 | -55.0826 | 2024-10-19 01:22:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0a282b31-89ce-30b2-9bbc-a9921f6ba835 | -10.16091 | -54.90498 | 2024-10-19 01:22:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| e815fd02-1c67-3bd2-baee-ad2d7f5721d6 | -10.15967 | -54.89592 | 2024-10-19 01:22:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| de5cf41e-45c3-3fe1-b41f-c5cc98d775bd | -10.02639 | -54.33616 | 2024-10-19 01:22:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 68164c85-a885-3834-8f4c-5c73e48a4d51 | 2.1502 | -60.846298 | 2024-10-19 01:22:19 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b73c464a-db04-3308-9e33-c8b2e14ea4c6 | 5.0724 | -60.118698 | 2024-10-19 01:23:04 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| afe07c69-d11f-3be3-96d6-e8c51d6b8b11 | 5.0741 | -60.111198 | 2024-10-19 01:23:04 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae50007-1303-3abc-a318-372a1e4ef22d | 5.0626 | -60.1166 | 2024-10-19 01:23:04 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1164fa4a-700e-30b8-8bb2-787eb31a057d | 1.00646 | -52.21623 | 2024-10-19 01:24:00 | TERRA_M-M | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 856d2e6f-b204-3000-81d2-547507bf71a3 | 0.99474 | -59.44394 | 2024-10-19 01:24:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 16.8 |


[Clique aqui para ver as próximas entradas](README8.md)
