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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8aaca71d-6c0d-3e9e-9b7b-0cf6e45c9cbc | -2.40288 | -50.33162 | 2024-10-01 00:50:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 339.5 |
| 61502ef7-3964-3dda-a41c-45019e623bc8 | -2.40129 | -50.32016 | 2024-10-01 00:50:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| e5dedf66-e73a-30d1-af6d-75e8556cef3d | -2.39445 | -50.34449 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0c447fed-8386-3bd7-9c2b-17f552ebe4f1 | -2.39287 | -50.33301 | 2024-10-01 00:50:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 7cde9730-4275-3686-a561-094f7a967383 | -2.39129 | -50.32155 | 2024-10-01 00:50:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9d2b2a5e-3564-335a-896c-e4a0d95dad1a | -1.65228 | -47.0474 | 2024-10-01 00:50:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3020b8de-bfcb-353e-acda-e53e8103913c | -1.65106 | -47.03861 | 2024-10-01 00:50:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 26392ac9-2aa3-39d4-8ab6-4f80feae91ef | -1.41761 | -47.41187 | 2024-10-01 00:50:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f0d91cbf-0043-391c-900f-3c7733ee7e45 | 0.14853 | -51.3993 | 2024-10-01 00:50:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 036ad6e7-c2c1-3c75-b76a-7af8a92877db | -3.81589 | -52.37726 | 2024-10-01 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| ced18782-8d8e-3c04-95f0-85ed903bf0b7 | -3.81363 | -52.35988 | 2024-10-01 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 971281ec-1264-3071-aa3b-4f454d4aa418 | -3.80841 | -52.36631 | 2024-10-01 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 95a75896-2a7b-3b21-8323-9fddcae0ae5f | -3.26635 | -50.66837 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 28933ca3-7dd0-378d-b851-714779266ece | -3.21596 | -50.45165 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4c161ce8-69b8-3746-99b5-9cd7326eb267 | -3.13855 | -48.99364 | 2024-10-01 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0d7e01fe-0ba5-3a5c-9b4f-0c52968ed3ae | -17.577101 | -46.759201 | 2024-10-01 00:50:02 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f0772a3c-d09f-30bb-841a-60324f18f035 | -17.579201 | -46.768002 | 2024-10-01 00:50:02 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ba5123ae-6a88-3054-8d16-b3905f434a99 | -18.600599 | -53.036999 | 2024-10-01 00:50:08 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bd064a52-328c-3432-96f6-4c1f7533dcf3 | -18.602301 | -53.045502 | 2024-10-01 00:50:08 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 969b4b5a-4f40-375e-991f-cff64924f4f2 | -18.590799 | -53.0392 | 2024-10-01 00:50:08 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3be3aad8-0a35-3c9b-9aba-a1ebeec0c14b | -18.592501 | -53.047699 | 2024-10-01 00:50:08 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3c028d8d-fda9-3a22-87b8-aa2d97d7bed5 | -18.580999 | -53.041302 | 2024-10-01 00:50:08 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c2430b2d-9c77-352d-b600-e47d1e78861d | -18.582701 | -53.049801 | 2024-10-01 00:50:08 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 84e40313-31e0-3c9f-a04d-7a0f788a058e | -18.8641 | -54.467701 | 2024-10-01 00:50:08 | METOP-B | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 780a9f5f-ad71-3149-8232-15262c71da6f | -18.8661 | -54.477699 | 2024-10-01 00:50:08 | METOP-B | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8906f775-9a10-326c-b49f-8d88529c83b0 | -18.868 | -54.487701 | 2024-10-01 00:50:08 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a2ca4800-4863-3645-b5de-99bb8b01a525 | -18.8699 | -54.497799 | 2024-10-01 00:50:08 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6a04ddbd-dc01-3b8b-a981-c62b9b8570cc | -18.536501 | -53.175201 | 2024-10-01 00:50:10 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| abd6f766-9dc3-3c79-a1d9-d839524f2b4b | -18.5348 | -53.166698 | 2024-10-01 00:50:10 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5a99c165-0c10-321a-82ea-12661444c972 | -19.1632 | -57.4366 | 2024-10-01 00:50:13 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6c5ee241-83bd-3f7e-b52e-6174d9796f79 | -19.166 | -57.452099 | 2024-10-01 00:50:13 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f1f3c62d-da68-35f7-a0aa-e84ceadf6e77 | -19.1535 | -57.438499 | 2024-10-01 00:50:13 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 801b4430-64c3-344a-86ae-81ab699b51d0 | -19.1562 | -57.453999 | 2024-10-01 00:50:13 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5dc9029a-b7ee-3b60-a905-9773cb108f7a | -19.131201 | -57.426899 | 2024-10-01 00:50:13 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aa7aacb4-2db6-3c48-b112-8d7dd9d10b85 | -19.134001 | -57.442299 | 2024-10-01 00:50:13 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 350459be-cd4d-38bc-a5bc-6cfb799a9751 | -19.1215 | -57.428699 | 2024-10-01 00:50:13 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6d40fdb1-34ef-37b8-b9ff-8a90b7ba7ef2 | -19.1243 | -57.444199 | 2024-10-01 00:50:13 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5be39676-7029-3e51-8cf8-cc0a1ca53d33 | -19.1145 | -57.446098 | 2024-10-01 00:50:13 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0bc74e11-5063-3e21-8780-08708fc77624 | -17.289801 | -49.0825 | 2024-10-01 00:50:16 | METOP-B | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 099c6ecd-5ce6-3e1f-9b03-e84641ffb161 | -18.030001 | -52.648201 | 2024-10-01 00:50:16 | METOP-B | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 331b725d-853f-3767-b84c-bbda52fc4c88 | -18.031601 | -52.6562 | 2024-10-01 00:50:16 | METOP-B | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ddc0d884-3130-33ae-993f-c1a4773c47d5 | -17.709499 | -53.180698 | 2024-10-01 00:50:23 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 03d80aa8-347c-356c-84a3-1f1dd7c5d1e1 | -17.711201 | -53.189098 | 2024-10-01 00:50:23 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e290fc0-73b6-35e7-9076-6272ee0bd620 | -16.5042 | -48.043301 | 2024-10-01 00:50:24 | METOP-B | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 08ff890a-c564-3e6a-b894-bb0d68ccacb2 | -17.6766 | -53.170502 | 2024-10-01 00:50:24 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 199539b5-ddb4-3076-bafa-a2fbf0d37728 | -17.678301 | -53.178799 | 2024-10-01 00:50:24 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 73841750-7848-3a98-8f90-d08e1efc1e35 | -17.6651 | -53.164398 | 2024-10-01 00:50:24 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0e9a0b75-32a2-310f-8ab4-f145b954031d | -17.653601 | -53.1581 | 2024-10-01 00:50:24 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c60e147e-b09d-3aeb-93ca-35ffd250c50b | -16.5023 | -48.035301 | 2024-10-01 00:50:24 | METOP-B | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9bcc2426-8f84-32ff-a3e8-ad4577ec2e07 | -15.2008 | -46.215599 | 2024-10-01 00:50:38 | METOP-B | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5700e1d1-67da-36ea-93a3-c77f70a1c8be | -15.7695 | -48.483101 | 2024-10-01 00:50:38 | METOP-B | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 641ef512-e9cb-30ff-a17a-59c68f52f75b | -16.6297 | -52.566601 | 2024-10-01 00:50:39 | METOP-B | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7da2d6a0-1cd2-330f-a0ec-a2ff74d603b3 | -16.631399 | -52.574299 | 2024-10-01 00:50:39 | METOP-B | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 47bb12b5-4d16-3365-88d6-f75400021388 | -16.6199 | -52.568802 | 2024-10-01 00:50:39 | METOP-B | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9edfd3b4-475d-38f5-9524-a9b499cc0cd7 | -16.621599 | -52.5765 | 2024-10-01 00:50:39 | METOP-B | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aa4bcbae-0002-3370-be37-0c7d8bd2d294 | -17.1833 | -56.1381 | 2024-10-01 00:50:41 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c5907270-c66a-397e-9392-ba4118c684cf | -17.1691 | -56.116402 | 2024-10-01 00:50:41 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fd9dfbef-78d0-3676-8696-ea8758aea0cf | -15.357 | -47.427399 | 2024-10-01 00:50:41 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| beb87b91-4674-33ec-abf1-b6177acb03b7 | -15.3505 | -47.574501 | 2024-10-01 00:50:41 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 85d0735d-4829-32a1-b449-74a14b5d7261 | -17.1856 | -56.150002 | 2024-10-01 00:50:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c65f5fe3-8e89-3dc2-9e26-8aa75c4ac235 | -17.187901 | -56.1618 | 2024-10-01 00:50:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bd72141f-7b6e-39ff-a926-fc65d377b447 | -17.171301 | -56.128201 | 2024-10-01 00:50:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 61d8a1e4-aca6-355e-a860-b668f22f734c | -17.173599 | -56.140099 | 2024-10-01 00:50:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0f68d36-63af-349d-99ba-c0380f38e257 | -17.1759 | -56.152 | 2024-10-01 00:50:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a54b30c-6bee-3730-a88f-1a705a73780e | -17.1782 | -56.163799 | 2024-10-01 00:50:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ab2c25f-83a3-3677-82e0-c45941c6205c | -17.180401 | -56.1758 | 2024-10-01 00:50:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| feb588f2-d32b-3f7d-8340-4d653593ca6a | -17.182699 | -56.187698 | 2024-10-01 00:50:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2eb3cef2-1d63-3cdb-8944-5f2e4dc56223 | -17.184999 | -56.199699 | 2024-10-01 00:50:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6355189-d291-3b2a-8fc8-42b33638ea67 | -15.2774 | -47.484001 | 2024-10-01 00:50:42 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ee404e9d-955e-31ff-a28b-619aeb5faf2e | -15.2795 | -47.492599 | 2024-10-01 00:50:42 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4ba7cc1a-e10f-399b-a301-4691ffa09203 | -17.161501 | -56.130199 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5976ff27-a17e-3138-8341-5180fbfde239 | -17.163799 | -56.142101 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a2cb1813-92e2-3160-806b-e3d3036ee3dd | -17.1661 | -56.1539 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 75576ecd-8f03-3c6b-bbe2-ff18dc370c5b | -17.1684 | -56.165798 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 09792f1e-e8f5-3256-a823-6dcaaad47bcd | -17.170601 | -56.1777 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 329d1b1e-9d02-33d7-9ccf-08f0aeab83aa | -17.172899 | -56.189701 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3dcab035-b63b-38e7-8a13-dbda6e69991e | -17.1752 | -56.201599 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2688e8c-e3e0-3d41-94c0-bfa378353de4 | -17.153999 | -56.1441 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8f340a41-3c31-37e2-91d2-03485ea84819 | -17.1563 | -56.155899 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 279c5d2f-b095-3c34-8777-b7a8f77e9dac | -17.160801 | -56.179699 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f4464549-3d56-327e-a835-6b38ccb9d9cc | -17.163099 | -56.1917 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e1bdace4-ec51-3db2-a217-6b344f9388a6 | -17.1654 | -56.203602 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a0a4adcc-41d1-34f1-9741-e3023b6a1c06 | -17.1443 | -56.146099 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 31fb5d9e-4d45-3029-95fc-b6fef135d0b7 | -17.146601 | -56.157902 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa5f7024-5e36-3494-8881-47be71dcf4bd | -17.148899 | -56.1698 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 39b301ed-552d-3856-91d4-d731c15d18fa | -17.1511 | -56.181702 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 98b4beee-5ccd-3de2-a411-a50099ee68aa | -17.1534 | -56.193699 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c1a6de8-977e-3ac0-a97b-9c76c51a90a9 | -17.155701 | -56.205601 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6ff5445b-9c46-3e6a-9640-f2f763fd55df | -17.134501 | -56.148102 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c1f7a0e3-36c6-356c-8b03-005ac2672c9f | -17.136801 | -56.159901 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db608175-06b2-3796-9ccc-0b700491e8b5 | -17.139099 | -56.171799 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 18f0ecd8-a107-397c-98ae-2010da5dd7e5 | -17.1413 | -56.183701 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 08c9e4df-9fc9-3da5-94aa-4e23f89ec6d8 | -17.1134 | -56.091 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ff6290d7-f09b-3fad-b9cc-2923f4af4524 | -17.1157 | -56.102798 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f3299383-9da9-3423-8f46-aed5036c2abf | -17.117901 | -56.114601 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7848c156-e3e8-3651-9a41-4aa29b49045b | -17.124701 | -56.150002 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 36989e74-dbab-39f6-a4bc-1f9b28ddd708 | -17.127001 | -56.1619 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 497d1073-9d13-337e-b330-2299d7d55c2d | -17.129299 | -56.173801 | 2024-10-01 00:50:42 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 577f5037-a052-34c9-9dc3-f8ae2d397e20 | -17.084101 | -56.097 | 2024-10-01 00:50:43 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1bd848a0-3186-3124-ba58-6c2806e69098 | -17.060101 | -56.077499 | 2024-10-01 00:50:43 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README13.md)
