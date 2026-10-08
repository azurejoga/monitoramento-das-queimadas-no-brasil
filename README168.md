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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3ae73e4-857f-30f5-abb7-d3ed3cdf36e9 | -1.28556 | -55.41861 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f77004d3-9976-34ec-95ca-cd2b6e23e6eb | -3.58098 | -54.66953 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47d85bd3-d30b-31fb-80a0-f31af1a6ce10 | -2.98048 | -54.10651 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a3d451d-0854-30cd-91d8-49c241cf2676 | -2.80073 | -54.07983 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ccc9943-b2f9-3551-a7f5-c2c53ee2a019 | -3.5718 | -54.66047 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee5b232c-bed7-31fe-ac1c-d66f7005810f | -6.50793 | -55.3829 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22983ec2-0de2-3bd3-94a1-08b85999e3ff | -3.16155 | -54.72034 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf71469a-4d62-3841-a2bf-623747fc3221 | -3.5804 | -54.67326 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 443f7cf8-b741-358f-8900-5be6005e6f67 | -8.53865 | -66.97668 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0475ddaa-911c-316c-a341-9bb0c8c2f200 | -2.47854 | -56.11047 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c29bdbb-ca2b-33bc-98e3-33f6f46e8571 | -3.21482 | -53.9659 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92a4d5a5-d18b-32e6-91e6-16215ddaedd9 | -2.15417 | -59.22344 | 2026-10-08 05:23:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 491f168b-6332-3050-ba8e-50ca5245eaae | -1.74446 | -55.02548 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4a58c9f-cfd6-3dc1-8e17-66126f4ca235 | -3.26635 | -54.00525 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d613e99-79a5-385a-b158-9fab14d32775 | -2.76802 | -54.08267 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ce45652-7012-3707-b737-1118adfce88b | -2.98873 | -57.20247 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b54fb8e0-f289-3591-a905-6ec8e1bd98d5 | -13.80732 | -52.80054 | 2026-10-08 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a32bc773-36e9-3a70-8ff9-959c5690baed | -3.11566 | -54.16184 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c7a106e3-1d33-353c-96c0-d9637a2a0885 | -3.70964 | -58.54506 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee278570-754b-3625-8d30-4d4403927d54 | -5.99741 | -53.49903 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d7994e5-f185-3775-8c35-ee944f5ded58 | -2.30085 | -58.09917 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaca2ed0-6913-391c-9873-4a95f9e3bcef | -2.58239 | -56.15846 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3229dbe9-158d-34d1-bfe9-d4d0b0092189 | -3.26865 | -54.01366 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44367e4d-bf9d-3273-a3e1-e1000caca380 | -2.58016 | -56.15103 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff842d54-dcde-3505-a6d6-112ded06ef6c | -3.67792 | -54.50352 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e84d2c3-1844-36dd-a20e-a5c4f0135825 | -3.04582 | -53.9169 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 811a61c9-bd90-348c-950f-d13e473d58ea | -3.17409 | -58.6419 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dff121ff-cc2a-3e99-9232-8538865d0ca1 | -3.43311 | -58.59781 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f246677b-85b2-38b9-a03e-13f6c876e952 | -3.08551 | -54.28688 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e5fbe84-9210-342c-9140-2e34133a380b | -4.13575 | -53.99779 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e544b5c7-5b3a-32b3-b06f-a62d2bd9b1a7 | -3.63151 | -55.45546 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62bba90d-d80d-3183-8e3a-14a9e26bd096 | -3.70487 | -58.29549 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 565352bb-662a-3425-b442-0683604eaa19 | -3.2754 | -54.06279 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af86a8ea-3fa5-3ae3-8abf-1dde53706ed0 | -3.08807 | -53.94758 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 870f1687-f0be-3d9d-90ca-0844683f28b9 | -2.65111 | -56.53799 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef6a08da-14ee-34c3-8cfc-9b1e2152d7ea | -3.55992 | -59.46644 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 47cfef93-88a0-32ee-acce-7adef5253978 | -9.22715 | -67.26599 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4e215d02-2ca2-3607-a8ba-f329238dc93b | -3.8525 | -51.93353 | 2026-10-08 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 39ef5542-0db8-3981-8ad3-0f7edf4c7449 | -3.17843 | -54.61284 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3129d79-75fc-309e-b58c-847947c660fd | -3.96515 | -56.11974 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3059613f-8d3c-3b2e-bd08-770d05b60361 | -4.14194 | -54.92148 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82329592-fb1e-363d-8ec1-ddebfb79ac8b | -3.29423 | -54.05769 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c29abd0-9442-3195-91fe-dbb0e3aab217 | -10.23347 | -58.21542 | 2026-10-08 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9dc2a69-d3f2-3a4a-8560-bd9a8a08d314 | -3.59893 | -61.62909 | 2026-10-08 05:23:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c2e3c82-05f7-33cc-a969-e9fe5fd28827 | -3.65373 | -54.06169 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d91b41fc-0c04-378f-af06-1e1564ba5761 | -3.23343 | -57.87728 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5be57b73-207f-3346-a3a7-d03c62376c87 | -2.79723 | -54.07928 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b9c14fb-a91a-3771-8d11-06fceec3094d | -5.11003 | -47.11922 | 2026-10-08 05:23:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2dd2ba4-7c50-3f14-bf8f-634efdac1dea | -3.47065 | -59.57771 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6ada631-c745-3dc7-8ed8-b3329e30ac79 | -3.3207 | -58.22818 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1889e31f-2518-314b-8095-4e6dd117442c | -8.84574 | -66.80373 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9122b7fc-9654-3486-bfe7-d39ff797671f | -5.69849 | -53.49399 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7031c55d-6f35-30a0-835b-ce3aae677a6b | -4.11653 | -59.87354 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c863fd3-8244-3420-b2be-a3327fed5ec4 | -3.6564 | -55.3203 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4642f10-eeb9-3279-83dc-f266a7d603b7 | -3.14853 | -51.62349 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e828034-7aca-3372-9750-cb91902a3ad8 | -3.29626 | -54.02189 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2223b48-f1c9-3b86-86f9-751cb1ae16bb | -13.17147 | -54.31767 | 2026-10-08 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26de2aae-7f81-3da7-aace-96f5e54d2c2b | -2.86678 | -54.21096 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fff24d1-05d1-3e76-a976-61bd8a21fc27 | -6.51137 | -55.38345 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e68a1ab2-a667-321f-a3d7-8f0290854aff | -6.52647 | -55.26287 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 850731e1-c1ab-3e71-a768-b03d5d5f7d87 | -5.72741 | -45.15774 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 67222f8f-01e5-368d-af23-a81f79e3dd13 | -10.81256 | -56.50045 | 2026-10-08 05:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7ac2929d-eb19-3312-bb3d-cff19fa2932f | -3.99153 | -56.25574 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07d85325-fc6f-3431-8787-dbcb0fadc896 | -7.20677 | -55.10199 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6a7af0e-0a73-3c95-89ce-fe05a473a65a | -3.01612 | -54.10807 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 571d743b-376d-37c9-b197-5ea0b3a2bde2 | -3.69207 | -60.54698 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34eb001f-7712-36f5-8f57-20f1c477ac8c | -4.57272 | -54.95649 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a06e1fb3-2507-3eb3-a0e9-3466481bdd10 | -2.49295 | -56.10564 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da8f671f-5858-3244-8d73-8b8b4fd1b6e6 | -3.03546 | -54.09919 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 376d69ab-c5fd-390c-96e7-02cc4d8eae9c | -6.92707 | -43.66358 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9ff1456d-d7d6-3eb4-9cfe-9e0ad1333ed4 | -3.07332 | -53.94939 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f1465c9b-ebdc-3912-b38b-c973e72061fb | -3.30127 | -54.05878 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 79ef9ead-b10c-30c8-924c-164d8d619d47 | -6.14764 | -47.92741 | 2026-10-08 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 711ed8a4-0e8a-3376-bd30-257206127eff | -3.57122 | -54.66418 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad153fd4-0525-3529-a421-ac2a4013b0f9 | -6.19914 | -52.78721 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 364ae988-f62a-3d8b-8edc-b3efa9db2313 | -3.02686 | -54.06215 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9beb083a-859d-3a97-8c2c-a10fec8ff9fd | -2.78031 | -56.4908 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d80d63ba-b8cb-3b49-91b5-e0e8ae4b72f5 | -8.52707 | -67.00925 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d982104b-56cc-319b-afd4-acabd0490b9b | -3.17043 | -54.08716 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d40c568-9666-32f7-aa98-4958de7f1ae5 | -11.79197 | -46.7768 | 2026-10-08 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c635da5-5d31-3e8e-83d2-9b767ab96431 | -3.48503 | -59.58001 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b8e4fe1-4ad2-3065-a6ac-a9e5dbe1d69a | -3.70616 | -55.96172 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1bb47ae-7032-385c-9128-6bc1a819110a | -3.52331 | -54.66116 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cd2f8a1-5cdf-3190-b2a6-42ab64e657a8 | -10.73318 | -58.91767 | 2026-10-08 05:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca4da4a2-24a8-33f0-abd6-e0924dbd0d5a | -3.97237 | -56.1173 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 444e451f-0f66-3857-b040-03f1ccc545c5 | -3.05864 | -59.26725 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2003d215-d763-318f-85d3-76aec3a1ed2b | -4.06559 | -59.84397 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 009bd487-ee40-32ee-92b4-7eaa1483f7a3 | -3.71539 | -59.3345 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc1ca11d-8575-3c77-b648-e7f9e48a980a | -3.31406 | -54.04355 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 83d6794c-0698-3794-bd2d-5d604fd0bed1 | -4.28853 | -60.95855 | 2026-10-08 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d3be0c9-a2d9-3452-8788-d8aa4b74d652 | -3.2941 | -61.01448 | 2026-10-08 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c2f1aeb-e034-3499-ac68-bfecfd5743e1 | -3.15226 | -54.08829 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ed87d4b-7b54-368f-a553-508ffc41c519 | -3.18036 | -53.83871 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8f40231-5fb3-3a8d-b558-b3453a6d15c9 | -10.90007 | -57.08563 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4832fa37-60bf-3163-b136-c4ad77c8c0cf | -5.0505 | -49.76506 | 2026-10-08 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0631a099-e435-3541-a171-ca8541d48f87 | -3.11947 | -53.79432 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 26719a57-c30d-3994-b723-d5c87afe281f | -6.73037 | -55.11065 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5e83bf94-bf8b-3750-a77d-27fda591ce11 | -3.3021 | -54.66945 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b91a8c2d-6eab-3b6f-ae32-ae0408538c62 | -4.76688 | -55.67502 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a5a9bb9-de52-3b83-b1e8-dccf078ea9c7 | -13.8041 | -52.79157 | 2026-10-08 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README169.md)
