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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8129f17f-b75b-304a-9667-0beb1db3773a | -5.70323 | -44.78803 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c8cb5e21-f3ff-316a-96d4-ca6f8a76fd74 | -5.7025 | -44.79241 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e0ff7a5-4831-317b-b4ff-2fa237952b74 | -5.58458 | -44.87652 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a01bce44-75c6-3d93-8926-9ebd58998762 | -5.58009 | -44.87571 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0d7b533-b519-3943-9c1a-b539ca6ce43a | -5.48051 | -44.85092 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc2742f0-097a-3a31-934f-c980fb11e97c | -5.33086 | -44.84745 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f07c71b0-0584-3ce2-8cdc-16039bb64826 | -5.32635 | -44.84668 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fd2bb5f-d118-314b-9fe8-c87680874140 | -5.24027 | -44.79703 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| e7c373a3-fea0-3e76-b12a-8d4ef62f3f77 | -5.23577 | -44.7963 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb6b0bd8-1656-300c-8985-4550a104e89d | -5.23125 | -44.79567 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14f4ebbf-2607-3cc4-b43a-16af08c2cb2a | -5.23048 | -44.80024 | 2024-10-10 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b278c1a2-c74a-3128-a3ae-943186153c5f | -6.43029 | -43.78641 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6b699e7-d70f-3ca7-9a82-50f9c55db886 | -6.52048 | -44.00199 | 2024-10-10 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6b149ad-8e91-3071-86b1-29d2294209e2 | -6.50739 | -44.33992 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c094b036-189f-3a06-8932-b021c0341a50 | -6.50669 | -44.34407 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8fe689f3-bab3-3fcb-83b6-0b6d9ea58ea2 | -6.50651 | -44.16613 | 2024-10-10 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d98ce68d-c897-3ae8-827f-05b19fdcbdc8 | -6.50015 | -44.15266 | 2024-10-10 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40879926-cf06-397b-9d88-5bd1d9fa14ad | -6.47061 | -44.01767 | 2024-10-10 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41c9c980-7f8e-32af-ace3-4bb53846f8d9 | -6.45433 | -44.16625 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56c7dcac-7675-3b9c-92d9-a7995ebff8aa | -6.44262 | -44.26218 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e49f154c-ea48-34bc-8a37-bd3a10eeab0c | -6.43835 | -44.26157 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c34c4429-c44d-3095-9991-a93531dcb1da | -6.43765 | -44.26575 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a14d8b8b-a3ab-3b16-8400-cbda6fd96442 | -6.42679 | -44.43586 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed5da625-1218-3077-8aa3-8b7a7c39acb6 | -6.42324 | -44.4306 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fa0b59d-45df-3530-b54d-fcdef7a26727 | -6.42252 | -44.43489 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 559638e2-fb5e-355e-9cdf-4528ef827bad | -7.6328 | -45.26986 | 2024-10-10 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d0bba24b-d438-342d-ac44-6ba6c8b185d2 | -7.63204 | -45.2742 | 2024-10-10 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 6a00123a-8ce8-3001-acf3-a6528de4d601 | -7.62832 | -45.26918 | 2024-10-10 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| aebea783-03c2-32d8-915e-95f53ae89379 | -7.61416 | -44.85697 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f676028b-165f-3264-888e-c771054d8652 | -7.61344 | -44.86114 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e27ea9cf-aa4a-3822-a43e-d16c1d95d2b9 | -7.61055 | -44.85199 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bb263ef-f0e5-33bf-8366-bc3a97959641 | -7.60982 | -44.85617 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcfc89e9-8f27-3c58-911b-9e64281c8588 | -7.30926 | -44.97083 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7eb6e9af-4d4b-34a4-9f8f-7d735ecb2b85 | -7.30854 | -44.97506 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c137cd5c-c1ba-3e29-94cd-f10016efd0bd | -7.30782 | -44.97933 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 77d4c68b-0ef8-3dcc-bc2e-e80c9d250b60 | -7.30488 | -44.96999 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f03828e8-22e1-36ea-9a29-a22c8ef64964 | -7.30416 | -44.97423 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7b6e8a62-5638-3b32-8f0b-7a2df3523c4f | -7.30343 | -44.9785 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c0d58fe2-1a3f-3eb1-a30a-66b0eab92438 | -7.29903 | -44.97771 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f23d037c-2991-332c-8f5d-8d6fab2b098b | -7.29828 | -44.98214 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2173436a-ae6f-3ef8-95a6-41b8a1224da2 | -7.19838 | -45.03871 | 2024-10-10 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e60e476-f64f-37df-bda5-432a2fee3260 | -6.93601 | -44.19794 | 2024-10-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac19da52-d1c3-3443-bfa4-43ff85bf4bce | -6.93219 | -44.06166 | 2024-10-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89bac904-2c51-36df-ae82-a2b56f6c05e5 | -6.92864 | -44.05726 | 2024-10-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a30468eb-58f7-303e-8aef-23f4fd5a2202 | -6.92801 | -44.06105 | 2024-10-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17454b73-a6b7-36ab-9e8d-ebca48484eab | -6.65051 | -43.87144 | 2024-10-10 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ab025c8-5f1e-3a99-8e57-dbbc9a9ede36 | -6.64901 | -43.87069 | 2024-10-10 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62723165-4935-318c-8fe5-b4a4563c3542 | -6.64508 | -43.80173 | 2024-10-10 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89eda931-d995-3324-8281-934954ad5f54 | -6.64098 | -43.80094 | 2024-10-10 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1cafce4-6544-3ead-9b93-2622ba734e63 | -6.62255 | -43.75957 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f2e850f-441a-383e-904d-82f6ea1e9367 | -6.61845 | -43.75885 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 734e741b-b221-3939-9c10-8aa155e7de10 | -6.60714 | -43.77592 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| beb88870-740d-3e2e-a2a3-cce6e8397c1b | -7.11489 | -44.70439 | 2024-10-10 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e359d652-f9d6-37b5-b43f-bdfe80eedd21 | -7.0932 | -44.67489 | 2024-10-10 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f8d5827-ceda-365b-b5d6-f9c1513d74fc | -7.08886 | -44.67421 | 2024-10-10 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b23e560-a0a4-3131-b4a6-c6b8224710ac | -7.08815 | -44.67832 | 2024-10-10 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ecbd255-f6ce-34aa-8b1a-23502c9ebb98 | -7.04884 | -44.80188 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90c4cff1-ec1d-31e6-a87d-cddfe4ec3016 | -6.9439 | -44.61572 | 2024-10-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e116f57-8bbe-3547-adbc-36ead594a80e | -6.94236 | -44.84176 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 509d866c-3b0f-3667-b33f-09a7cee427f9 | -6.94029 | -44.6107 | 2024-10-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41ce1291-5fc4-3c08-838b-ee417ee2207b | -6.93959 | -44.61488 | 2024-10-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4804d526-3d15-3491-a142-b98161caf33e | -6.93797 | -44.84101 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13c492e0-9ce4-3bfc-8d72-104e3aa9df6b | -6.92138 | -44.56504 | 2024-10-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16efa33a-009e-31ba-beb6-fe912392f43b | -6.92067 | -44.56919 | 2024-10-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5fc58bc9-50ae-3db5-a433-dc2ce0ac402c | -6.81188 | -44.46652 | 2024-10-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 200b966b-48eb-3afb-8955-91f1c2f6d479 | -6.81118 | -44.47064 | 2024-10-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01861e5c-b9d0-3141-b160-54de3474942b | -6.73087 | -44.56489 | 2024-10-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7eaa45f1-c74c-3a29-b28b-47530469d481 | -6.52797 | -44.56956 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1550cec-a6b0-3d84-bdcd-522ac23b6a9a | -6.52685 | -44.56647 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b33415b4-55e5-3187-9640-6d3bfa79282e | -6.52615 | -44.57064 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 856b06d4-5d91-3b1b-8f2b-3c844628dd14 | -6.52182 | -44.56991 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7906089-62dc-357a-a4f3-2cc1e1fe8b1e | -6.51166 | -44.34068 | 2024-10-10 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a48d63ac-b0e6-3de3-abf9-67c4a42ef503 | -6.50679 | -44.69114 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 126d70a6-ad4d-375f-881f-ac8caf91af59 | -6.50587 | -44.69257 | 2024-10-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d51d0eb-6007-3d1f-8005-22c841c0e349 | -7.2144 | -44.14335 | 2024-10-10 03:55:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6a46a64-db05-3392-9eb1-a793065aba69 | -7.20854 | -44.0019 | 2024-10-10 03:55:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b134378-aabc-3268-958c-4bdfdeaa5bf5 | -7.2079 | -44.00566 | 2024-10-10 03:55:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46df3a5a-675d-36e0-87f1-1d02c6887684 | -7.20764 | -43.81263 | 2024-10-10 03:55:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 508e5bde-85c5-3206-b0bb-675df4428b23 | -7.20723 | -43.8126 | 2024-10-10 03:55:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb807ab6-5083-365c-b07a-9217a4d32aa2 | -7.20703 | -43.81632 | 2024-10-10 03:55:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 074d226b-7b2b-3ded-b683-cc2b725e1980 | -7.20659 | -43.81628 | 2024-10-10 03:55:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6d3fe02-1d41-3dd5-b6db-ddaf20618298 | -7.20441 | -44.00122 | 2024-10-10 03:55:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cd41644-78e7-32a2-aefb-cf5ea05bf5a1 | -7.17202 | -44.06584 | 2024-10-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f4f9c8c-19e7-359f-a637-9bf03064d604 | -7.17138 | -44.06954 | 2024-10-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e0163b6-d7f6-3b8a-8df0-81d4ea5ad922 | -8.24834 | -44.85882 | 2024-10-10 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b47c801-5c35-353d-b260-b27f8564eb4e | -8.24764 | -44.86284 | 2024-10-10 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5cd16bfb-5013-3ea5-b8cc-83960d6c01e7 | -8.24404 | -44.85813 | 2024-10-10 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c745ec2d-cfe9-3ff3-91aa-9c1c1d0003e7 | -8.21185 | -44.39354 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b82bd0e4-561a-3fb6-85aa-f0558c967120 | -8.13394 | -44.46462 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f0c59bdf-af2f-3560-92ff-f611c3196a5e | -8.13041 | -44.46005 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e64dd82-932e-3d5f-a56d-99550c6b2f53 | -8.12975 | -44.46391 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6644a55-d1f3-37f3-bbc7-f06aeaad4c98 | -8.06126 | -44.78565 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 404ab916-0d1e-3814-baa4-865bbe00b0dd | -8.00271 | -44.36954 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f40d17ab-cbb6-38f8-afd4-177b24d0bde6 | -8.00204 | -44.37342 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3ec86676-de28-3a67-8548-30f9037cbbfe | -8.00136 | -44.37729 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dc2c9430-f1ba-3604-9660-f4da4479c748 | -8.00069 | -44.38116 | 2024-10-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 324c816b-3a36-3937-8c28-23c8bd04b130 | -8.36199 | -44.13197 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03f5f6c6-edcd-303b-89b5-e1dc8fc95afa | -8.35982 | -44.12027 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 373ce315-4867-3210-93b5-b1df2bef82de | -8.35854 | -44.12761 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b02ca18f-9e82-36c4-98e3-cb2497a140fb | -8.35573 | -44.11958 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README46.md)
