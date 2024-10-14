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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a1bf8d8-f621-3469-a385-84d438aa43a1 | -2.86086 | -52.4674 | 2024-10-14 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25e31f54-473d-3711-9171-241f53080b22 | -2.66457 | -53.34612 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d34e7ab-77d1-3a3f-a5e1-990f28fa657e | -2.6639 | -53.35034 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f439a172-aff1-34f3-ad8d-959c2efafe2a | -2.66025 | -53.34976 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 089e2085-6d47-3023-b1dd-9c6f15a6f282 | -2.65978 | -52.52896 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1807eeb-6591-3b87-b752-5caf721610ad | -2.6566 | -53.34918 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7de80ff8-1276-3c48-91eb-89fd83d8564e | -2.65593 | -53.3534 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7241ec8-43b6-31f4-a8dd-dc921bd1d6e8 | -2.25896 | -53.48033 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e703534b-df17-3ead-b099-77485310a676 | -2.25827 | -53.48465 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45c63dc4-00c6-354f-becc-648e78093573 | -2.25457 | -53.48405 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 402d6e0e-355d-3d39-a6ff-0e045e544dae | -4.36594 | -53.66757 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a47f3449-a60f-3cbd-a5c7-1a7007be3469 | -4.36231 | -53.66698 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a359057a-527c-3f7e-adf5-934383d79a2a | -4.1753 | -53.53194 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b839749d-871d-37f4-9c77-b48afbfad73c | -4.17462 | -53.53609 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09892636-0879-3c63-a3a6-3b8490db9087 | -4.10097 | -53.73772 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a365b746-11cd-3bf5-9fa0-03f93f20b68b | -4.09867 | -53.72857 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 048c924e-29b6-327b-9eb2-78d0a01092e8 | -4.09799 | -53.73284 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca619732-9a61-3a90-830c-c841f427464e | -3.96357 | -53.75713 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fd35376-428d-3013-8bc8-8cc1bf455639 | -3.95387 | -53.44823 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01c5e2e2-076c-383e-a492-07f308d6aef4 | -3.87045 | -52.28787 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 388df0b0-f992-3775-a72d-90053a6e0f8f | -3.86985 | -52.29159 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f1b06a6-818e-3141-8596-59776d28b0eb | -3.86641 | -52.29105 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81d545e8-05dd-373e-823d-3139e3318c19 | -3.77759 | -52.39285 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30135ad6-d160-33df-b09a-7914e883f805 | -6.17941 | -53.37152 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bdf593d-6cca-378f-82b4-9bd557e2b593 | -6.02698 | -52.75615 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce6dd139-6ca5-381c-9910-a6fd5e35b714 | -6.02354 | -52.7556 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebb7a844-22a3-3413-8de6-01dfffadcbd0 | -5.99852 | -53.35215 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faea8982-5032-34c4-99de-aef4cac636e6 | -5.995 | -53.35159 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f525f7d6-41a8-33f0-9616-c3b868f3d4fa | -5.91592 | -53.30345 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcce848c-6ec3-3c71-bc86-96c6d7c4c00d | -5.91303 | -53.29902 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15b4df25-7f0b-38b1-9fa0-10156a3ab954 | -5.72028 | -53.6913 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d79eb33-348c-3824-9b2a-82fffc4739f8 | -8.64209 | -53.65279 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9eb75a6-3cec-3ecf-aa42-a652fc58d3b8 | -8.63924 | -53.64835 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88d588ee-ddc4-3e1c-9a35-7f89f48b9831 | -8.63862 | -53.65218 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19255729-37f0-300a-aab2-dba937f48029 | -8.63577 | -53.64776 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b862bb37-7762-3708-8630-36ba80ef75c9 | -1.6987 | -54.87247 | 2024-10-14 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 518f23dd-7b3b-3e98-add6-232125ac042a | -1.69465 | -54.87182 | 2024-10-14 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd98db2e-b7cc-3ecc-9936-06273c48215d | -1.69213 | -53.81284 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad3f2509-7247-30f3-ad67-5beeadfe3b1a | -1.59739 | -53.34646 | 2024-10-14 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b9f2a1e-4dbc-3604-8b76-911303d9c4d4 | -1.59669 | -53.35081 | 2024-10-14 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c30cda00-9197-3e06-aa43-51cc5f18fa06 | -1.42232 | -53.47056 | 2024-10-14 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 412ec54a-eb33-3cce-b04a-427cbf44dd91 | -1.23234 | -54.11546 | 2024-10-14 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2850b4f-c6de-31f0-b827-c61f344328ce | -1.14675 | -54.10097 | 2024-10-14 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3be645f4-73c7-3228-827e-1966966c0387 | -1.14665 | -54.10275 | 2024-10-14 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36ed2632-e856-3d6e-a00a-37b0b0e7efc7 | -1.146 | -54.10579 | 2024-10-14 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4c59eec-d4d0-3c83-a3aa-dae47d6fb0ef | -1.14286 | -54.10034 | 2024-10-14 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bd36c94-4fda-3c7d-a6b0-09cd308414e4 | -1.14277 | -54.10212 | 2024-10-14 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f85aff96-df34-338e-a4cc-0267feeade82 | -3.36481 | -54.56895 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 730fd7de-450c-3fee-9118-dcea4329b4ea | -3.3573 | -54.71331 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b56cc241-1fcd-33f9-8c88-e10d53c947be | -3.29968 | -53.85205 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fa7af02-fd36-35ea-971b-d94e35553bc8 | -3.29897 | -53.85648 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 163e4642-91bc-38ba-8ed5-43fd1e6531bf | -3.29667 | -53.84705 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aad70b1d-bc3d-3a78-a960-f09b17a68628 | -3.29596 | -53.85147 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 419783ae-da72-32f4-a0e6-0987882b8769 | -3.29294 | -53.84646 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6859742-984f-365c-8043-41e8f3383e57 | -3.27027 | -54.18117 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e429d216-b02f-3066-9ab2-ee62d848f90f | -3.26647 | -54.18054 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1183fdd9-4aa9-3432-bf7d-dd337a48d878 | -3.25831 | -54.20725 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77845fb1-e483-39bc-ae69-0814fa84a186 | -3.25598 | -54.19744 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c237076-6461-3574-aeb6-23dd4f0b4d67 | -3.25524 | -54.20203 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35232e59-297d-3e68-8efe-b35ed10f0ff4 | -3.25292 | -54.19221 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfee398d-e87e-3c7e-9c28-a99eadc696a5 | -3.21751 | -54.85797 | 2024-10-14 04:44:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a2fe380-804d-3caf-b3df-8f8e4cd9150b | -3.16757 | -54.77546 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f484bc9-87a3-3c6f-a47b-07ff4e0445a9 | -3.11649 | -53.74103 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5513013a-d32c-373d-a73c-4b2bda5784b4 | -3.0855 | -54.24371 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d032c87-6409-342e-b6aa-ecad5821a768 | -3.08244 | -54.23845 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d540a73-ed9b-3166-9899-93b998736226 | -3.08168 | -54.2431 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f0b9b8a-ba7a-31d1-aa0e-57f62dfbd015 | -3.08092 | -54.24776 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f660c88-0980-3de4-a7d1-1dff4ed2151b | -3.07862 | -54.23783 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 841d150a-15f0-37c2-b53e-b47549860197 | -3.07786 | -54.24249 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59b8ee13-01b9-3f11-b2d0-4fd9be51402f | -3.07709 | -54.24718 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2a8486a-cc51-31c0-8e6e-0c27bfb4ffa3 | -3.0748 | -54.23721 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da910a9c-7511-3402-bbd5-059f820f5478 | -3.07404 | -54.2419 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f8ba621-f5d5-3e5e-aa03-97992fdfdc68 | -3.07326 | -54.24661 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3df4e408-3c96-3acb-994b-cc1e6fadfdee | -3.07238 | -54.23956 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34dbe59f-5575-35ec-b670-55d143e9eee3 | -3.07163 | -54.24429 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3cd70e7-4ee6-30e9-819d-05b40cb4191e | -2.99958 | -53.91554 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52c3e993-bccc-3919-8d77-c58be15fb8e0 | -2.9966 | -54.17513 | 2024-10-14 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f1c40a8-96cd-3eef-9679-da817c72cd3d | -2.99358 | -54.90602 | 2024-10-14 04:44:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a42167e4-cf49-3e75-a659-7905300c55c7 | -2.99275 | -54.91114 | 2024-10-14 04:44:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a58a8a73-acb8-33d2-90fd-d807c4b6fdf0 | -2.96334 | -54.65186 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 00c73d91-0698-3619-8291-a3a14cdd65c5 | -2.96255 | -54.6568 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ce122697-a0c3-300e-a445-fec0803f53c5 | -2.87599 | -53.96672 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28562547-7983-38e3-b59a-33459460ff18 | -2.8412 | -54.48879 | 2024-10-14 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc373c69-7fcd-3fb7-a0b3-c2723acec1c2 | -2.81012 | -54.08754 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5619175-3a01-3f15-9b77-b62d93890250 | -2.80707 | -54.08234 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a79ab50-0cb6-3b74-990e-04df9d7cdadf | -2.80632 | -54.08694 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b47f1d17-985e-3520-a7d8-03fc4f385cb8 | -2.80327 | -54.08174 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccfa836b-adf3-3ac4-891c-43d925d70862 | -2.65404 | -54.31039 | 2024-10-14 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 48481863-9eaf-3b60-9354-141db6a80e65 | -2.57184 | -54.0071 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5738f831-a666-3b01-98a2-f8d6acb9e11a | -2.57108 | -54.01171 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 25412d98-13bb-3810-9069-3ea5be5a9718 | -2.5683 | -54.0088 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f11166c3-4426-38ff-930d-60da042ab3ff | -2.33328 | -54.59005 | 2024-10-14 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6cf979a8-4e91-36ab-9a4e-d1075f1efb66 | -2.28472 | -53.79983 | 2024-10-14 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8f0c613-c2f7-31b4-b9a1-13851ded61d5 | -3.67031 | -54.06832 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 721acc24-a272-3a15-8e29-ec00fb36ad4d | -3.66958 | -54.07282 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d2f7729-d9a7-30e5-a3ab-43b9d293921c | -3.62162 | -54.13015 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db053133-0c75-3d55-a4c0-e42ac85437c7 | -3.62127 | -54.13225 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d05b344e-e442-30ba-80b9-c38f860edc9e | -3.61824 | -54.12701 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5823983e-9f2b-358d-90dd-64f902a459c1 | -3.61785 | -54.12952 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd98d521-3e32-3698-a3d8-693aed265b4a | -3.61751 | -54.13161 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README87.md)
