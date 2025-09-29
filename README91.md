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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed1bd14c-b455-3648-9ba1-c1fad3aa55eb | -9.1102 | -45.8653 | 2025-09-29 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 16f0c80a-301f-305d-93b4-3fbbd93bdc36 | -14.5331 | -48.4491 | 2025-09-29 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 176.9 |
| e8a04ef8-ed44-35bb-8281-69642bed8460 | -9.4458 | -47.5923 | 2025-09-29 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 7a4c2518-9304-36b2-ac91-4076a98f4310 | -6.4131 | -43.0724 | 2025-09-29 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 70142fd9-69fc-32c9-a8ed-653a9df0abca | -7.8163 | -47.0003 | 2025-09-29 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 000ec71a-b2fb-3bd9-9c70-d5a733f5232a | -7.2813 | -42.8269 | 2025-09-29 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| f7af1323-bef3-32f1-8cb4-7002b219a06f | -7.9626 | -47.3405 | 2025-09-29 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 91ca0644-6223-3924-a6d3-afd5f9e4f800 | -7.281 | -42.8505 | 2025-09-29 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 51dbf4c1-6414-3fc0-af7e-24e5f1ef52a1 | -8.8948 | -45.0253 | 2025-09-29 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| c085de83-7be2-317d-8e41-5a4e35675e54 | -9.4194 | -54.697 | 2025-09-29 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| f2d7c629-8cf6-306d-ba2e-596f540a4250 | -6.0609 | -42.608 | 2025-09-29 13:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 794f00dd-97ba-3052-86c0-e6b405437d29 | -7.2216 | -44.7601 | 2025-09-29 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 23e782b9-10dc-3b0a-a86b-b7c8a8fe6024 | -6.4319 | -43.0707 | 2025-09-29 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 0f05f043-b1b2-37b4-accd-6a372403b615 | -14.5331 | -48.4491 | 2025-09-29 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 1ac58db2-a00a-32d5-8f20-9cfd1313d964 | -11.8482 | -51.7916 | 2025-09-29 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| c9029036-f656-3685-adc8-f74254155ce8 | -7.4488 | -46.299 | 2025-09-29 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 36b888ec-9278-3e0b-90fe-ba69d444e1a5 | -7.2214 | -44.783 | 2025-09-29 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| ffe9c7f1-154b-3ce1-8de7-368a1a3b9612 | -12.9732 | -45.2051 | 2025-09-29 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| f0d62591-3040-3f12-b954-664a88cb2d53 | -9.9959 | -43.6172 | 2025-09-29 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| a553db60-ecc3-35a1-9a19-6b04c7fa0181 | -13.2346 | -50.9691 | 2025-09-29 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 8112d1dd-0048-3d69-a76a-5c7800c47473 | -9.4007 | -54.6984 | 2025-09-29 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 09c8a58c-6acb-3002-85c4-49c7cd9d0f7c | -17.7144 | -46.6865 | 2025-09-29 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 142.0 |
| da4a1287-7abf-3408-a553-c87251c20287 | -6.0811 | -42.4644 | 2025-09-29 13:20:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| fe79158b-0e2e-3376-a25a-5efdcbd70834 | -7.8163 | -47.0003 | 2025-09-29 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 7755816f-40e5-370b-bb79-b94d4a13a2bc | -8.2662 | -45.5018 | 2025-09-29 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| bed73843-5cb3-3802-96ca-78e310fc3a72 | -6.9692 | -43.7927 | 2025-09-29 13:20:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 54a96b5c-b980-3a07-ae27-a19c7f0df08f | -12.9543 | -45.185 | 2025-09-29 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 0efb239b-5158-3687-99fd-1101af4e9104 | -9.7674 | -46.1971 | 2025-09-29 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| c157baa3-c7e7-3be2-9920-2b5442aeb4c0 | -7.3653 | -42.1058 | 2025-09-29 13:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 300.9 |
| a9d62b55-dfd0-317e-bd70-28b17a4b4594 | -11.3638 | -45.057 | 2025-09-29 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 249.5 |
| 64f9665b-f13f-3469-930d-8b1e7abcc523 | -8.2854 | -45.4772 | 2025-09-29 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| e1914225-b4c1-3b54-a14b-681a1951240e | -7.2999 | -42.8486 | 2025-09-29 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| ad1cf9db-7d92-3c50-a6dc-9c9452dbab87 | -12.863 | -46.9582 | 2025-09-29 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 712158f8-fa41-39f3-83ab-fb26e7a16709 | -11.4405 | -45.0461 | 2025-09-29 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7eecda2f-3029-3298-9f34-97dc5b0d0f83 | -13.1816 | -50.6969 | 2025-09-29 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 236.8 |
| acca9bfb-be9d-3de9-a88e-d870bf29e769 | -7.3464 | -42.1078 | 2025-09-29 13:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 187.7 |
| fc18a670-2dfa-3e46-a07c-d321efee6239 | -7.365 | -42.1298 | 2025-09-29 13:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 153.2 |
| b7b1890e-397a-351b-98c9-2b2bfb838106 | -7.5089 | -44.297 | 2025-09-29 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| eb85b6ac-d595-35c8-8a9d-b56d7481b9db | -11.4409 | -45.0229 | 2025-09-29 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 8bae11c6-8a18-3201-b65f-f5e84d59bda4 | -13.011 | -49.4423 | 2025-09-29 13:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 77d9dbf5-2476-3c11-8aa4-e5a933c7338b | -15.219 | -50.1071 | 2025-09-29 13:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ed690f87-6779-3a49-90da-e36a7b49aa10 | -6.4317 | -43.0942 | 2025-09-29 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 40fcdee0-0c81-34b5-8c4b-482c39fd9295 | -11.3443 | -45.0828 | 2025-09-29 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 23cea04d-5b5c-3a35-9e75-cb085491b49f | -8.2848 | -45.5225 | 2025-09-29 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 19c851a2-6ea2-3242-84b3-56bb23ec86dc | -13.2008 | -50.6945 | 2025-09-29 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 213965fc-e886-31ee-ad89-de5bd93533b3 | -6.4131 | -43.0724 | 2025-09-29 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6929d5f7-b99d-3627-bdc7-1a07d4fd1583 | -9.4455 | -47.6144 | 2025-09-29 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 73dc5fb6-8482-3004-b431-8b68bcb2b890 | -7.9628 | -47.3184 | 2025-09-29 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 94782dbc-f6bb-392c-be0e-f44f995f1cb9 | -11.3447 | -45.0597 | 2025-09-29 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 926a2f4b-dadf-3430-9861-88640aed5461 | -7.2405 | -44.7584 | 2025-09-29 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a0d4de30-6c31-3f93-8761-2fe1a805bd62 | -10.6239 | -48.5386 | 2025-09-29 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| fa0d0f0d-b8d0-3be7-a075-93258d9eff29 | -13.2005 | -50.716 | 2025-09-29 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 3bfc761d-e8b5-3bea-8844-c59cc6e7c3d5 | -9.9768 | -43.6197 | 2025-09-29 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 2ee4a8fb-09b8-3ce3-90e2-0b898e81e297 | -7.4676 | -46.2974 | 2025-09-29 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 175.0 |
| fb37cb25-e529-3f44-8359-de222b105df0 | -13.3796 | -48.1577 | 2025-09-29 13:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 127.9 |
| c65bf8c2-a0fa-3f8d-bee7-c7743d22d10e | -9.9872 | -45.4228 | 2025-09-29 13:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| d8d03b4b-ebb9-3250-8d66-c3f4c624b68f | -6.0609 | -42.608 | 2025-09-29 13:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| c3bb639d-1d52-304b-9387-b57dca37ce7f | -7.281 | -42.8505 | 2025-09-29 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| d3c9bf62-0a0f-33ef-b784-c4d4fdae5692 | -6.7482 | -43.3704 | 2025-09-29 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 59.8 |
| 108e9ebe-dd6f-3ce2-bdb4-2c4a67c4a4d3 | -7.8165 | -46.9781 | 2025-09-29 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 96738465-7360-3f6b-8ef4-b43f7526bb41 | -17.4055 | -47.1199 | 2025-09-29 13:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 2e588c50-9325-3106-8183-f1bd38289462 | -8.0034 | -47.0497 | 2025-09-29 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| d9a6c264-62be-333c-b1ad-1a65923372fb | -7.8566 | -46.7527 | 2025-09-29 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 5e5dfc42-ed65-3e16-805e-fffd251d5a5f | -8.2665 | -45.4791 | 2025-09-29 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b8caf530-59ef-3068-b35c-e23b649f45c5 | -7.9008 | -44.5805 | 2025-09-29 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 053db3bd-070e-3387-a67d-0ca6c06f351d | -8.1614 | -46.3899 | 2025-09-29 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 61f2a13a-2093-380f-ad7e-a3db5fff887e | -7.2813 | -42.8269 | 2025-09-29 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 7316d870-4d31-305a-b0ed-5cb0f94f2989 | -15.6127 | -46.2465 | 2025-09-29 13:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 150.8 |
| ad84d0e1-0a8e-314b-a5a5-84bc71b23353 | -9.4194 | -54.697 | 2025-09-29 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 142d8489-88e1-3059-b52b-9ff37d895287 | -14.6049 | -45.0161 | 2025-09-29 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 5707ea59-e35e-3e20-bae7-de483f1d15d3 | -14.5345 | -48.3821 | 2025-09-29 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 2e3265cd-92bb-36ab-aea9-6a6d716904e5 | -7.3001 | -42.825 | 2025-09-29 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 1d28034a-8dd8-3e63-908a-be96a70a7ad0 | -10.3257 | -48.2001 | 2025-09-29 13:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 03fda297-b617-351c-845b-c3802ed3b5f1 | -7.8378 | -46.7544 | 2025-09-29 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 8416dbe9-702b-3b49-bdcf-005ed88164c8 | -6.5232 | -45.1843 | 2025-09-29 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 90ba6455-95ff-3586-8766-b529aa27aa02 | -12.9547 | -45.1618 | 2025-09-29 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| c13e5212-30e0-3829-80b6-7e40995a3682 | -10.0062 | -45.4204 | 2025-09-29 13:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 4645f05e-2da6-377c-8d75-b9f856b1ffdc | -15.219 | -50.1071 | 2025-09-29 13:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| d85b02e9-a1d6-3f6c-b1c8-e8365b1ef3f4 | -13.2346 | -50.9691 | 2025-09-29 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| d8885c83-b05f-30a1-b4cc-be97824051b7 | -7.3464 | -42.1078 | 2025-09-29 13:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 141.7 |
| a642c80c-5c48-30a0-b99f-506fc881b45d | -14.6942 | -48.1557 | 2025-09-29 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 7e32c267-e1f2-3a76-bbae-f9a4bf68df66 | -14.8902 | -51.0678 | 2025-09-29 13:30:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 97abe97f-62f6-3557-8c05-9a0cace0f918 | -9.7264 | -47.7827 | 2025-09-29 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 6c92f708-164f-3499-90cb-5d201e5e2eec | -13.3796 | -48.1577 | 2025-09-29 13:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 3e1f1d72-6ad9-3aff-a37a-1e8ae78ac765 | -6.7482 | -43.3704 | 2025-09-29 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 5e75e6f9-5bce-3039-94e6-18deb60f4baf | -11.3638 | -45.057 | 2025-09-29 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 282.9 |
| 0746fcc5-7f36-3f74-aa9d-78c760e562d6 | -13.1816 | -50.6969 | 2025-09-29 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 203.2 |
| 7e15ddbc-ff5a-38b1-8f80-256934959724 | -6.0609 | -42.608 | 2025-09-29 13:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| 3cca15d9-0893-3e69-a344-3efebeca9fd0 | -8.2665 | -45.4791 | 2025-09-29 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 785de6c6-8b7e-322e-af3b-15fb299955ea | -8.5224 | -44.6305 | 2025-09-29 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 81856b2c-f787-389a-81cd-2e9afdc421bf | -9.8852 | -45.9122 | 2025-09-29 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7a71fae7-bc89-352b-88b9-4070816427c8 | -15.2194 | -50.0851 | 2025-09-29 13:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 61aa1cd0-b704-3c49-9048-7b1eebb88b68 | -8.8948 | -45.0253 | 2025-09-29 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 030d1561-544d-3e78-9037-364338e48dd4 | -7.4676 | -46.2974 | 2025-09-29 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 712fd548-6285-37a8-9844-5efc947c77e5 | -6.4131 | -43.0724 | 2025-09-29 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 620b5c93-abed-3206-b1ac-84a37b44cb62 | -8.2662 | -45.5018 | 2025-09-29 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 73d19005-84a1-3273-a734-73ce4b1ece40 | -9.3705 | -47.5781 | 2025-09-29 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| e5425a82-e80f-3bf4-a5aa-02f140ce18b5 | -10.3257 | -48.2001 | 2025-09-29 13:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 181.0 |
| dddbe05e-052b-34ae-8636-23fff29684da | -17.7344 | -46.6823 | 2025-09-29 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 128.9 |
| bc4e82dc-3d1f-39fb-a47d-a096c8b9c0eb | -7.8163 | -47.0003 | 2025-09-29 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 158.2 |


[Clique aqui para ver as próximas entradas](README92.md)
