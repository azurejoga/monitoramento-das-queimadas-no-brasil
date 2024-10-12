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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da1abdb5-664b-3474-beef-1c1ace837d7e | -16.98784 | -57.48503 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 00e1115c-2a7c-3ae5-b2ed-ed85f621fb5a | -16.98276 | -57.44667 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 52426a2d-a846-3d95-a903-61fadf8378d5 | -16.97373 | -57.448 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 50bd6824-bdb0-327c-bb01-3f3754cc67db | -16.97247 | -57.43843 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 054e3959-e381-30de-b390-88e85ef6ad27 | -16.75956 | -57.56635 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 84b1c446-d6f1-3118-ba2b-3c483df7dfac | -16.69789 | -57.44861 | 2024-10-12 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3137ea8b-9c41-3d69-baf5-4176507a2c8f | -18.66913 | -57.33578 | 2024-10-12 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b11dd0ad-ca41-39f5-a699-12b940c62f4a | -15.97853 | -59.0997 | 2024-10-12 01:34:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 1f1bd6a7-9c0b-308e-8e5a-94804e8cdc8d | -15.65785 | -59.36328 | 2024-10-12 01:34:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 194d7f33-896f-3240-ae4b-9bd8c024c917 | -15.62555 | -59.44137 | 2024-10-12 01:34:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 133419b2-9b46-3858-a8c5-b20968d4fc44 | -15.6241 | -59.42998 | 2024-10-12 01:34:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4e9df809-4863-3919-b63b-1beabc93203d | -15.62272 | -59.41914 | 2024-10-12 01:34:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cde2c6bc-616b-333c-b559-0fc735ce1238 | -12.30139 | -59.1679 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f5e2aee7-dad2-3b64-835b-8036dcda7897 | -12.26958 | -59.21278 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6f6d641e-8016-34ad-8ee7-752450b8dbb1 | -12.10382 | -58.7275 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 943f84bf-7384-3bbd-b4d5-90bc154dfbd6 | -11.89346 | -59.00952 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e101e860-0ef1-38e8-93a6-a568923f4743 | -11.8843 | -59.01084 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2c70e840-1978-3f75-a823-87d6a1cbd17b | -11.88301 | -59.00116 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 7120d35a-6c9d-3099-b017-10bc3902af91 | -11.88171 | -58.99144 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a2909fb3-88a3-393a-9eb7-0eb65f3617c2 | -11.87384 | -59.00236 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a88e6e52-b1c5-379e-ba2d-b585dd58a85f | -11.8711 | -59.05204 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 83b6c120-83ff-39ab-b216-f5b53dbe417a | -11.85975 | -58.89671 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7d6dbe9a-84af-3221-b77f-a82eca099936 | -11.84295 | -58.84042 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f1e70995-bad8-31bb-bc0d-e103fc0dfb57 | -11.83513 | -58.85125 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| cc170148-d398-3802-8d0a-2dee996bdfc4 | -11.83385 | -58.84167 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 2a809db9-7039-3ffc-b49d-c23a89f6d8fb | -11.82602 | -58.85248 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 99dcb0b5-4442-3a73-9563-7d630bb057dd | -11.82475 | -58.84294 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| acd7538c-b0a1-3f08-adef-7e067a0ffacc | -11.71938 | -59.29556 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c59900a-7900-319c-858d-35daed1cd720 | -11.71806 | -59.28561 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 422e1eb2-e879-36b9-aa3f-8a6ad4888b57 | -11.71676 | -59.27574 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d9d1dc21-50c1-38a4-954f-415075e059bf | -11.66294 | -59.89781 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fae83718-d5f8-334e-ad59-f5fd4820cf3b | -11.58324 | -59.99055 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1149321e-5bf6-39da-bba3-5dfe25501088 | -11.57366 | -59.99195 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d36ed811-7eb8-3324-9407-49943a306dec | -11.57227 | -59.98138 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d4c80b33-d9c0-3945-8245-155f4a77ed5a | -11.48605 | -58.99319 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c224fa9e-ee48-3863-aef2-0b618d72cfb7 | -11.38526 | -59.19666 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c0f0ef16-c5eb-35bd-a714-cbff264d9a86 | -11.37607 | -59.19799 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc52e12e-6c97-3404-ab77-718bad590e4c | -12.96156 | -60.06642 | 2024-10-12 01:34:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2df88be5-7173-31c7-9b02-c26ffb6731b7 | -12.96012 | -60.05532 | 2024-10-12 01:34:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 22343f64-db32-38ec-9fc5-3c9a9ab31a82 | -12.67527 | -59.8339 | 2024-10-12 01:34:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 184fb60e-f3d0-3cac-9c42-f71cb547c355 | -12.67385 | -59.82314 | 2024-10-12 01:34:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 44945d2e-0a65-37fc-a429-c1f028eb98a4 | -12.34581 | -59.16579 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b2f621bf-ff71-3ced-9517-688d8f384e96 | -12.34451 | -59.15584 | 2024-10-12 01:34:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3fec7049-d67c-3a9c-9bf5-b89aeeeb4867 | -12.33661 | -59.87577 | 2024-10-12 01:34:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e9888000-be3d-386c-82ae-0ded372f77c5 | -12.324 | -59.26616 | 2024-10-12 01:34:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cc5688b5-6498-3e14-86f0-96a7cb9a2768 | -13.74519 | -60.12838 | 2024-10-12 01:34:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f3816424-b12f-344c-aa7a-12de2d3b5bd2 | -15.63126 | -59.9705 | 2024-10-12 01:34:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 83bc7c5d-ab25-3bc9-ab3d-0d1880b1ed20 | -15.62268 | -59.98396 | 2024-10-12 01:34:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 91b97aa7-aa33-33f7-87de-8eca5254b3bf | -15.62115 | -59.97187 | 2024-10-12 01:34:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 19c8ff3b-de92-38ce-a249-66acea851b8a | -11.54228 | -60.30048 | 2024-10-12 01:34:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d9e3e6e3-1920-3292-b46b-457535dba02d | -11.54081 | -60.28938 | 2024-10-12 01:34:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4896980e-4143-34bc-800e-b45c87a620ac | -13.72719 | -60.63926 | 2024-10-12 01:34:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 30.9 |
| aabb717c-438b-3783-861f-57f4eea363be | -13.35403 | -60.58649 | 2024-10-12 01:34:00 | TERRA_M-M | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 9bb1159f-37ba-319c-b8b7-b08f1b534d30 | -13.35243 | -60.57362 | 2024-10-12 01:34:00 | TERRA_M-M | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 6811c644-ac0e-3bb6-b522-3a6864edd0ff | -11.80466 | -63.00349 | 2024-10-12 01:34:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2a98157d-8b10-316b-b88a-ae9f7d05707e | -12.99073 | -62.48448 | 2024-10-12 01:34:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 2e41a05e-e9b9-39fb-887a-392201ad717e | -12.94773 | -62.52381 | 2024-10-12 01:34:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| e6b0f93b-f07e-3305-89ba-0b710202210a | -12.94771 | -62.62604 | 2024-10-12 01:34:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| eed0d79c-a3f9-3ad7-beca-796efec7556d | -12.93006 | -62.73787 | 2024-10-12 01:34:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| df7d2145-123f-349c-aae0-e986294b069f | -12.90539 | -62.53485 | 2024-10-12 01:34:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 4ad93103-96dc-363b-9506-e7a9060a9a5a | -12.75939 | -62.27984 | 2024-10-12 01:34:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ca7cc34f-4c29-3d52-b43f-22d4e813537c | -12.73262 | -62.25122 | 2024-10-12 01:34:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 28.6 |
| e30e189a-3025-3834-8003-b9831dbc9166 | -12.73074 | -62.23547 | 2024-10-12 01:34:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9a302b19-bd71-31b1-8827-2e3cbbc16fad | -12.47062 | -63.0214 | 2024-10-12 01:34:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 40d09a87-4912-3af4-bb47-c832b16bd3ca | -12.46851 | -63.00354 | 2024-10-12 01:34:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.7 |
| b6d6d781-715c-3e24-895e-a9be6f0578f0 | -1.6061 | -53.3492 | 2024-10-12 01:35:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b6951f4a-c779-3501-a5af-f842613e5f1b | -2.77 | -51.3829 | 2024-10-12 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 42d47432-7d66-322a-a0f5-5b1684a737b0 | -2.7701 | -51.3622 | 2024-10-12 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 9006a5d3-4a77-3fc7-923d-6583d7f73462 | -2.7884 | -51.3825 | 2024-10-12 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 944074e1-9118-3214-b6cf-7b7ff36fac33 | -2.7885 | -51.3618 | 2024-10-12 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 9892fbe4-0a8f-3c18-9d8f-90494d311792 | -2.7983 | -54.0129 | 2024-10-12 01:35:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 6b118dd9-1d98-33f4-b3ce-3c15b612dff8 | -2.8611 | -51.6699 | 2024-10-12 01:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| beff73f6-3b63-32fd-ac57-a4e458c538bc | -3.0311 | -50.5642 | 2024-10-12 01:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 2a020bb5-b7e9-3edf-91a1-efbaddcd9dfc | -3.161 | -50.3718 | 2024-10-12 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 60560499-e7f0-397f-80f7-329f87fda128 | -3.1611 | -50.3508 | 2024-10-12 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 7a254502-0c00-3bf6-a221-df609efca034 | -3.2136 | -46.7843 | 2024-10-12 01:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ae37fb99-1a22-3c96-8b69-f194acd84f8b | -3.1427 | -50.3514 | 2024-10-12 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 837ad061-bb3c-3fbd-9024-0d1590942f49 | -3.69 | -47.9451 | 2024-10-12 01:35:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2e76a426-8e00-30c9-8d35-e2be8b19e386 | -3.6901 | -47.9234 | 2024-10-12 01:35:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 166.8 |
| 5f649dfb-1839-3b2a-863d-7dafc18b3bc5 | -3.6903 | -47.9018 | 2024-10-12 01:35:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 933ca60d-d390-37d6-9e22-231209d6e0e7 | -3.6978 | -50.1225 | 2024-10-12 01:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 09072128-c8c4-3059-916c-492a5f8fe08f | -3.7086 | -47.9444 | 2024-10-12 01:35:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 85c06618-862a-3ab5-8f2e-2b50d7b2eb15 | -3.7087 | -47.9227 | 2024-10-12 01:35:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| b607f1c0-0b53-341f-ab60-c644f98133c6 | -3.7163 | -50.1219 | 2024-10-12 01:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| ba040eb8-0253-3d68-b6a4-8cfed667d831 | -3.9394 | -46.445 | 2024-10-12 01:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 45.1 |
| b6c978f0-7974-3f57-9f6c-3c3895dc9903 | -3.9396 | -46.4229 | 2024-10-12 01:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 34929e16-a17a-32a2-bd0c-c8da2df13563 | -4.7188 | -60.7882 | 2024-10-12 01:35:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f0b26543-cca9-382a-af03-c6385d09a32e | -4.7371 | -60.7877 | 2024-10-12 01:35:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| cfa804a2-2eac-3d3e-bd1b-4b75b1f5b98c | -4.8116 | -56.1639 | 2024-10-12 01:35:34 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 3350dbbd-ade1-3cf1-90ae-e9f8e1305c07 | -6.0603 | -44.629 | 2024-10-12 01:35:40 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 677be639-c3c4-36bc-8744-f59ff6c31b2e | -6.0791 | -44.6276 | 2024-10-12 01:35:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| e2d3351c-e64e-3e71-b84d-ec389eaf311c | -6.7285 | -59.3267 | 2024-10-12 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 30905f94-a265-3ec8-9394-1b6692bf6f2c | -6.7469 | -59.3452 | 2024-10-12 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 13c85644-40a1-3fd0-8a97-f3dc558d3f65 | -6.747 | -59.3259 | 2024-10-12 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 221.0 |
| 66b14ab0-e792-3fa5-909e-31654c0c2a74 | -6.8776 | -59.0697 | 2024-10-12 01:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b78eb949-fcbe-3e96-889b-fe3fc4ce7ef0 | -7.8715 | -54.7016 | 2024-10-12 01:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 149.0 |
| e7aeb39b-e29b-3f4f-9f18-be3500b09347 | -7.8717 | -54.6814 | 2024-10-12 01:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 4611359e-25a3-35bb-8791-6b5373080104 | -7.8529 | -54.7027 | 2024-10-12 01:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| dbbe2c64-1f23-3fd1-b9b4-c048432b52ca | -7.8713 | -54.7217 | 2024-10-12 01:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 2836e085-c3ed-3675-9dda-da3bc0444e9b | -8.4231 | -55.4704 | 2024-10-12 01:35:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |


[Clique aqui para ver as próximas entradas](README23.md)
