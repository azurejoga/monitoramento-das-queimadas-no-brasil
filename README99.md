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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e1473de-cc87-34a7-8d20-e2b50d806ef3 | -9.80005 | -53.59113 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c22e56d-65b2-3902-b435-1c1f80b6cf02 | -9.7967 | -53.59061 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 526e3349-ab9a-39cd-ae11-717ada2b2d99 | -9.79614 | -53.5942 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41a657e7-608c-332e-9015-09dda5ea2b35 | -9.79279 | -53.59369 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87dec276-2bd7-3363-8deb-3e02c692fbb8 | -9.78943 | -53.59317 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eeafcfbb-5004-36a4-896f-c81efa75fd90 | -9.78888 | -53.59676 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56e806d2-bb40-34d5-855a-7d0ab57cb0e6 | -9.75406 | -53.73457 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca7b0f09-9a5a-3bc2-a8c4-0ada26bd3b1f | -9.67119 | -54.25032 | 2024-09-26 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd72a1a0-fe07-30d1-a419-2cd8158c2037 | -9.66842 | -54.24631 | 2024-09-26 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93d58dc6-761b-3349-97f5-894d7dec6d9a | -9.66788 | -54.2498 | 2024-09-26 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59bc084e-2fc9-3210-9b47-c3d6ebf53851 | -9.66511 | -54.24578 | 2024-09-26 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca585033-3c33-3beb-a8ce-69b358b8e634 | -9.6618 | -54.24526 | 2024-09-26 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0625a512-2b64-3ce5-8843-903609ef0984 | -9.66126 | -54.24876 | 2024-09-26 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf7811a2-a3e1-33de-9c8c-b71d75b8b0ec | -9.59249 | -54.2524 | 2024-09-26 04:57:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00640efd-2e56-38f6-a324-ab72e863c564 | -9.81789 | -53.56441 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f89245db-071c-348b-b821-dd9bbafe93d1 | -9.81734 | -53.56802 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3546c1fb-6641-387a-bed9-ca46e47343f1 | -9.81679 | -53.57163 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7278ba8c-2250-361a-b4de-be774f737f42 | -9.81398 | -53.56751 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f527414a-c4c5-3f5e-9dd9-b1dc13af8c8e | -9.81343 | -53.57111 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a1fae6d7-b642-35a7-a1f3-130b9fa54f0a | -9.81063 | -53.56699 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 604880ec-5e3e-3ace-b906-22419a8c1749 | -9.81007 | -53.57059 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 895d4a81-4802-38bc-9502-5e8b363dd03d | -9.80952 | -53.57419 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2da41348-5166-3feb-8e9c-6f1e8fa18121 | -9.80897 | -53.57779 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66650f00-e108-3ccb-b27b-3b3600236247 | -9.80782 | -53.56287 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 02e40a50-19ed-3939-94ae-f10452d9ea8d | -9.80727 | -53.56647 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22c36316-edf6-3730-abde-36af482e9384 | -9.80672 | -53.57008 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 026ed751-0c72-33bc-90ec-6bb758ddbcd1 | -9.80616 | -53.57367 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e3894de-9f77-3298-afb2-f2b97e91729e | -9.80561 | -53.57727 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97f78627-4fed-303d-ba6c-c4d884bc6108 | -9.80446 | -53.56235 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c49f0b3-6273-33d2-a49e-4c41ebd833e0 | -9.80391 | -53.56595 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f39d9338-50b8-3814-a1ea-41c729fb8b08 | -9.80336 | -53.56956 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b23a2ebc-8ebf-311b-96fc-ad7e99ac29cd | -9.80281 | -53.57315 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e7b8384-e7ac-3149-a0f9-a78848f570c7 | -9.80225 | -53.57675 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f65cdb7-0d56-3e0b-b064-e79fd5b0bdae | -9.80111 | -53.56182 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d741dfb-a712-38b5-b0c2-ed4743fcd605 | -9.80056 | -53.56542 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 675e6e0c-8ee6-3e8d-aa81-6ce50fb44aa0 | -9.8 | -53.56903 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c96aea7-ce62-331d-8469-013e730040c4 | -9.79945 | -53.57263 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b159318-6a68-3c8e-88e7-e7d282bd61ee | -9.7989 | -53.57622 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfa88c1b-1a0f-39a2-a519-eabe63d41d93 | -9.7972 | -53.5649 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7df47b19-fa54-3efe-8202-9c11310509d6 | -9.78487 | -53.55561 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91b3fd3f-9557-3de2-8efa-01f5d6eecc3b | -9.78151 | -53.55508 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 373931dc-557d-33b3-8a03-7dfb3a73049a | -9.66954 | -53.53065 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8980055-f4f3-377a-806b-120e28b3ba22 | -9.66899 | -53.53426 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6509ed2e-37d0-3a17-b388-5d9c95887aaa | -9.66789 | -53.54148 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5f1598d-828b-3015-9f58-3c8d67859775 | -9.66734 | -53.54509 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c58e2ed-89e4-3722-a1e8-0b64223dd145 | -9.66618 | -53.53012 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b225956e-907a-3c57-9a94-71981fbbac39 | -9.66563 | -53.53374 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ea65e79-df50-37ec-a9fd-aefcd4eb782e | -2.14641 | -53.64937 | 2024-09-26 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 245d7808-8661-3d73-a99b-16ce1b78bc19 | -3.64021 | -54.04058 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9a28aec-ab56-3628-839f-050fda074428 | -3.45801 | -53.81409 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ef9612e-c582-34d1-9b1a-006ad78c89f9 | -3.4262 | -54.19086 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ccfe20f2-f1cb-3396-8bd5-105e8f3564fc | -3.35817 | -53.77743 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 47cee916-54fa-3562-b50e-2fd913dfa1e6 | -3.35763 | -53.78087 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22467751-4105-3e69-bd9a-05b095eac139 | -3.35487 | -53.77692 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efad825c-cfe3-3e6b-b7aa-c18751bcc820 | -3.35433 | -53.78036 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b8b9d29f-1751-3f6b-894d-34246a405fc2 | -3.35379 | -53.7838 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a32be34-9f22-340d-b602-bc94cbe5c2fc | -3.35157 | -53.77641 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53f8ec0d-9cba-3879-a4d0-4a7c0deea739 | -3.35103 | -53.77985 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 561752f4-44db-3bab-802b-e2fce8d11cb7 | -3.35049 | -53.78329 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ede5ff1e-e8b2-3191-b8db-c1489c39c884 | -3.34773 | -53.77934 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cf29b73-e52b-3fae-999c-2c80fd75a677 | -3.34719 | -53.78278 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d80337b0-862a-31d9-89b7-e9681465d098 | -3.34665 | -53.78622 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 93dcf63f-ea4a-330f-b937-11353df3adf7 | -3.32878 | -54.14003 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b161742b-615a-3cfa-a780-07a7a1c6e573 | -3.32823 | -54.14348 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2726cdfa-0f80-3939-9492-07bba87614cd | -3.32768 | -54.14695 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b614508-d703-3326-baa1-fc9cde21bc90 | -3.32546 | -54.13953 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d427023-163a-3bb8-827b-7fed573baefc | -3.32492 | -54.14298 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c56deef7-a3c5-34dd-ab5f-a76c1aba1c68 | -3.2665 | -54.10196 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15ad2a05-ca8a-380a-9e93-b977ad1ae2fb | -3.24046 | -54.50463 | 2024-09-26 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6903e605-e2b6-375e-8116-fa545bce9346 | -2.95342 | -53.70948 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd9aca66-b3af-34b8-bc9d-3ca67c35d445 | -2.95288 | -53.71291 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e67f930d-1be0-3bac-b790-6af443876018 | -2.95012 | -53.70897 | 2024-09-26 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f5d1020-9485-37cf-858b-fa5190016ff4 | -2.8748 | -54.16744 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6cad72a-42d0-3ded-b18a-a5ab70fd950f | -2.87426 | -54.1709 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9237f682-1940-3763-b9d3-8b27fc5b2bee | -2.65632 | -54.62585 | 2024-09-26 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 040cb490-8d37-3c1f-92c4-c2821e3f6b28 | -2.65353 | -54.62179 | 2024-09-26 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bed50cb-03e8-3045-af30-8ae7a8215b4e | -2.65297 | -54.62533 | 2024-09-26 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f831eeb-06a6-391d-82fe-be92d67403ee | -2.56292 | -53.96547 | 2024-09-26 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55488fda-87b5-34a7-8168-038fb34bc4a5 | -2.55664 | -54.61054 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76c16efd-aea2-324a-afdc-830c5440bd7f | -2.55328 | -54.61004 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52b4e93f-9b6b-332e-8199-602475429bb4 | -2.47618 | -54.56124 | 2024-09-26 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04ff92ce-8e61-3bd9-9399-0446f525d8f2 | -4.18239 | -54.42426 | 2024-09-26 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b38733b2-48f8-389b-8764-1274982e0cde | -4.00803 | -54.08463 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 145ebf1b-a029-3e67-93d5-e7c4daca8931 | -4.00748 | -54.08807 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89782a89-6e0f-3b0f-ad73-48c45d4b518d | -4.00472 | -54.08411 | 2024-09-26 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f413e03-c750-307a-9646-197ebf92086d | -3.86565 | -54.38161 | 2024-09-26 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7f8c3d3-dd25-39bc-8090-e45bb1f62778 | -3.82374 | -54.12948 | 2024-09-26 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f55d07a9-3c3e-3b10-abc0-246e52b8c39c | -3.77444 | -54.35605 | 2024-09-26 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06d4e16b-ae4e-3ca0-844e-76ef3b10d954 | -7.66386 | -55.28746 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e598e8f-967c-3c03-9d09-8a2abc657a3e | -7.65778 | -55.28291 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 549788a4-07ba-3b8e-9e15-889ac1a561eb | -7.65666 | -55.28992 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34ab2c3a-d6d6-3875-acfe-1fe29199843e | -7.65334 | -55.28939 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1652017-72f2-35e2-990e-e8b2f1695cc3 | -7.62457 | -55.27765 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a89332a4-f942-3e09-8a57-834b6b63a8e0 | -7.62274 | -56.16091 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 314fd404-50c2-3031-babb-3caa7ad64b52 | -7.62215 | -56.16458 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b18e8ca-2232-38ef-b362-15622c8f7554 | -7.61875 | -56.16404 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 355654c4-49eb-3e6e-9039-5a5ec2f7e4b0 | -7.61596 | -56.15981 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70d2016c-f2ef-3c4d-a230-c05069c2eca6 | -7.61557 | -55.35537 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 846479cd-7dff-3b6c-b1a5-6f36b8b0ff3e | -7.61237 | -55.2901 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e7b8aca-bf92-356d-9837-a83359f95529 | -7.61225 | -55.35484 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README100.md)
