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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a872d0a5-b0df-3643-88d8-9fb4eac5d35d | -3.32156 | -53.85681 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ad352ba5-8f3d-34b7-8088-7301050d1a1a | -3.58798 | -54.32068 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b022a34-34e1-3ca9-b911-1f33a4ef0921 | -3.21752 | -54.30733 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f2279979-2363-321d-bd46-b727b8aaf1eb | -4.14911 | -54.03766 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 59006ca6-f90b-3a39-8b23-5d8854f5400e | -7.24229 | -45.25846 | 2026-10-06 00:18:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| da0023a8-c4e3-3356-be2b-9fb89c0059a1 | -2.99789 | -54.11667 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 4ed5558c-2bce-3235-939e-0b3676174bac | -8.76929 | -62.87172 | 2026-10-06 00:18:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 28.7 |
| b70627eb-5cba-332f-90e5-cb368f1e410e | -3.0225 | -53.88961 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 022e4c9b-173a-358f-8a59-58405ae19528 | -4.11926 | -54.42448 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0940b287-0a3e-3b8c-8cdc-695fb53d7f4b | -5.6737 | -49.21036 | 2026-10-06 00:18:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| ef422ade-360d-34b0-bdf2-5f84e746f5b3 | -2.955 | -54.14663 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| e29ed622-e15f-3a3d-89bd-fc449e44eea7 | -2.94859 | -54.16555 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| bbb0b5eb-bf90-3f57-be59-024c1ee31db4 | -3.80583 | -51.04084 | 2026-10-06 00:18:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 33cec8b4-7f16-359a-a9b7-523843c9d698 | -3.32511 | -50.05989 | 2026-10-06 00:18:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 4be5898b-f899-344a-b7e1-627913bcadfc | -2.99667 | -54.10782 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 970b76a3-4270-33f5-9a31-e7bf607e36dd | -6.23325 | -51.82366 | 2026-10-06 00:18:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cd33e3fc-ae19-318a-abcd-466df04095fb | -3.38201 | -58.21284 | 2026-10-06 00:18:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| c8863596-e0ba-394c-93a6-5ce2fdd4c841 | -3.09848 | -54.17731 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c2362b9c-7eb6-3d3f-a32d-4ae2e7582af6 | -3.04508 | -54.26295 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f6d2a725-3b51-39bf-afb0-5d6abee05a2a | -3.05028 | -54.23533 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| feb23261-49ad-330a-9dc5-c8b5289a0bc5 | -4.56848 | -54.94791 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e7eca580-496e-3707-82aa-34466da4560a | -3.51185 | -54.63244 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 91c9d2c5-2a2e-30f2-a1dc-211477d20e9c | -3.52187 | -54.63998 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7a424ba3-3b00-3801-a043-fba773cfb9a6 | -3.84494 | -50.318 | 2026-10-06 00:18:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5eacbbd2-a427-3baf-99cd-b6b9e6dc6793 | -6.31508 | -54.78891 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 26f84836-f4d6-3614-86f9-f4d77835cd6f | -3.67434 | -55.95982 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dc3d73cb-9fd0-39d7-8c48-b46e585c14ce | -2.78244 | -54.36268 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| e90ef259-6d06-3ead-9e2c-d0a9d95324d7 | -3.04664 | -54.20887 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6ca617eb-c2d3-3938-93a0-abf26d1f87c7 | -5.39305 | -54.45361 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 247e610e-080a-3343-94fd-433511ad3014 | -3.74596 | -49.38923 | 2026-10-06 00:18:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 8113ea45-231b-3227-b125-982e4fb79eba | -2.77541 | -57.66245 | 2026-10-06 00:18:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4ff9161e-042f-3249-bbd1-8b6fa0e61128 | -3.65845 | -55.50552 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 60dfd173-5352-3f1f-bd10-8cde10cee588 | -3.0732 | -54.18984 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 861c4485-bd50-365f-9580-fadd5c54ad86 | -2.88181 | -54.13887 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| a3f0324a-88aa-3367-8680-29747d943f6f | -2.9881 | -54.04582 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| bebb8da3-f66e-30ed-af37-2c29c350a6c0 | -3.06831 | -54.15452 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| aca1ff1d-3484-396e-abed-3387cc6590e1 | -3.2749 | -54.18531 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 872a9797-fab2-3388-a811-f1103994a824 | -4.36508 | -47.77571 | 2026-10-06 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| e99e8cab-b26a-3779-a819-88a9f2708bd9 | -3.49422 | -53.44398 | 2026-10-06 00:18:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 63dca3de-2a96-3b47-b85f-05d2dda4a0ac | -3.94461 | -55.84752 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c14ccf53-a4b5-308f-865a-f4b963daa9b4 | -6.3163 | -54.79784 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5e0ce607-0a01-3a89-876e-9ef4c063ecc7 | -2.99759 | -54.17973 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0619d8ae-e3de-3ad4-a0de-8807c7be0d38 | -3.69038 | -59.6456 | 2026-10-06 00:18:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ca2181a6-9f65-31a7-97d7-652905778f8d | -3.27125 | -50.3968 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 3ae69d50-d37f-34ef-9c7a-b16f25b90e3a | -3.02374 | -53.89853 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 141.6 |
| ee34143d-f48f-3fd2-bdd3-51e2188ccebf | -3.09085 | -53.71898 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 649d431f-e242-33ed-bbf3-63b3af901301 | -3.67498 | -54.54374 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 97e98236-7b94-3dab-a992-bec346cd1565 | -5.97232 | -55.38617 | 2026-10-06 00:18:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 23daf7eb-ae84-3eae-8ba5-3cb098bbd6b4 | -2.87174 | -54.13126 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 29e10be8-b077-395e-abd6-2581ccc2e5af | -2.89828 | -54.12755 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 34bc0a1c-e916-32a1-8d5d-214b93602573 | -3.14681 | -53.72944 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cef74c52-f5c0-3756-a810-32e556c4fade | -3.63394 | -55.32627 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a92962a5-e023-305f-b54f-63996d40bf7e | -2.78825 | -57.68309 | 2026-10-06 00:18:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 169.5 |
| ee301b66-c129-3323-834f-ff1ab229912e | -3.06032 | -54.24288 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 5edb3d50-24cd-337f-9d9b-b3ef5302d6ab | -2.88453 | -54.09338 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f2d30c6f-cc85-38e0-acbc-a5a4daff2edd | -3.46025 | -54.60125 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c6734887-9af4-3ac9-a103-6ecff7b8d0d9 | -8.70743 | -45.23758 | 2026-10-06 00:18:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 17d64a40-e317-311a-8caf-cdb14abb699b | -3.50823 | -54.60612 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a87e7f99-28dc-3588-822f-684ab9a6fd11 | -8.6883 | -45.22006 | 2026-10-06 00:18:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 4e59206c-da0b-3b6a-bf52-cd1166412e26 | -3.49182 | -54.61736 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a5106c61-cdba-3e44-9ea7-50171ee220b3 | -3.53638 | -58.59482 | 2026-10-06 00:18:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a07c4348-9847-3a06-a3b8-c05cc442d375 | -3.61384 | -55.51172 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2d02dceb-5e17-3d80-9c48-3528819de69d | -7.44962 | -46.84434 | 2026-10-06 00:18:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8f57fdc6-a38c-3bd8-9ce6-47d8a65db167 | -2.97013 | -54.11153 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 30877bbe-1206-384c-a2b1-a3967d8621a3 | -3.71777 | -51.14363 | 2026-10-06 00:18:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 77fa3b0c-8377-36c1-b8cb-417d38403866 | -2.78521 | -57.66111 | 2026-10-06 00:18:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 04dca60e-4158-3e0d-aff8-e757e6df8899 | -3.10726 | -53.77157 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| d6b4950f-b6f9-31cc-b184-8dcf996ab545 | -2.95622 | -54.15547 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| d9ae4978-d159-34b9-8816-770e159b1be2 | -7.37999 | -46.22257 | 2026-10-06 00:18:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 96ca68ca-3372-3378-a354-35e601f0f018 | -3.09976 | -53.71773 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| ba4c892d-d1dc-3d71-809f-e16f9000d101 | -3.14556 | -53.72046 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 72d3a833-0f32-3d30-add0-0b8d72589370 | -3.59006 | -53.47044 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| cce6abcf-6777-3819-aa12-b5b4a2b3f27d | -3.23077 | -53.86641 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3a051008-018c-3c93-8108-592dddbb8fa3 | -4.33883 | -50.40263 | 2026-10-06 00:18:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| bdb356ad-41a2-3029-a18b-1afe81a00f7f | -2.95743 | -54.16431 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 0f6b3973-e343-372d-833d-9c0efc7a32d6 | -3.1265 | -53.71398 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b6a82615-1aa0-39b7-94ef-62d96cadfc1f | -3.05947 | -54.15576 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f884a8bd-9cc6-31f6-9039-6b003136b472 | -2.94738 | -54.15672 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| c7e86acc-ea6a-3848-b8e6-3a91ac3148ae | -2.78123 | -54.3539 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 88ab2925-d003-3481-ac75-b65341f3128d | -3.10227 | -53.7357 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 655ef8a5-4ed9-330a-a1d0-94997b78d844 | -3.57959 | -55.4039 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7ad86465-ed49-39b1-a44a-3e7f2171e7c5 | -3.05443 | -54.39612 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 504b0e70-7d12-33f6-8a55-1a1a9f0661b5 | -8.70732 | -45.24422 | 2026-10-06 00:18:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 9e2474d2-89a5-3929-b63d-004278597dd6 | -2.95014 | -54.11125 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 2a7ec2ea-0f75-3639-9b60-2a3210a0f994 | -3.03504 | -54.25541 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f682da91-73ee-3a7c-bd08-d426caa0a12e | -3.08539 | -54.27796 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b880ebde-46ad-3faa-a47d-fc61dfd179be | -3.50063 | -54.61612 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9dd34b5a-097a-3acc-92bf-708a70d4335c | -4.77689 | -50.82045 | 2026-10-06 00:18:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ba3099c9-e01a-3a44-8dbe-8c9b3916419c | -3.09056 | -54.25031 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e576d811-8bd0-36a0-ae86-e445876a117c | -2.98142 | -54.12797 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 9f52fb20-f066-3452-8bf2-a4bcebad09a5 | -3.68339 | -55.95856 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 26eb49bf-9cc4-3f1d-a536-ddd287003f6c | -4.35472 | -54.86353 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 720b75ee-b25f-35a0-8433-ba0359908963 | -2.89706 | -54.11871 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 02cffa83-6977-3027-be15-ba1138e5c9bc | -4.35206 | -47.77773 | 2026-10-06 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| dbbb2bf8-3595-39b3-85e5-27c0a79e8c48 | -2.94892 | -54.1024 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| abfcd59c-9cf4-338c-8912-74e2a5ce3f29 | -3.08174 | -54.25154 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 595.3 |
| 6c1dbc0c-f2b3-3202-a94d-11c9f4853e1a | -3.69118 | -55.94799 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 991bc130-9699-38f6-98bf-b0c842ca0ba5 | -6.16433 | -55.37597 | 2026-10-06 00:18:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 63d78697-9c81-304f-83d2-171eae5674f1 | -4.91361 | -55.86219 | 2026-10-06 00:18:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 486559cd-dc47-36e4-b287-0bef6b14b09a | -2.94616 | -54.14788 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |


[Clique aqui para ver as próximas entradas](README4.md)
