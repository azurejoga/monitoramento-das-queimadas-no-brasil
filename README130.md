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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ec05806-e5a7-3451-8ce1-87cc7844d5e8 | -17.16103 | -57.39883 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| c3f06160-a6c7-3565-baa5-39b29da6d4ea | -17.1603 | -57.37545 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 48f6108f-2de0-31ea-b4d4-b3b1fa2be394 | -17.16013 | -57.37864 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d46bf594-5884-35ff-9f47-a16a8e47b127 | -17.16012 | -57.40364 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 2cd33c39-f161-3ef9-83b3-cf20479b08b0 | -17.16012 | -57.40038 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| ebd6afa4-7f95-36b2-8933-5d9b3b06d67f | -17.15936 | -57.38024 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e1dd5e8d-082e-3ba4-a3d7-fbf74f06bd86 | -17.15922 | -57.38344 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2da0b3fc-b50b-343e-8738-985be2f16031 | -17.15917 | -57.40518 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2b5ba4e5-6142-3e40-8a47-be9f7865b5e3 | -17.15841 | -57.38504 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 322677f0-c72f-35a5-a7c0-4b68a95ff1b5 | -17.15832 | -57.36329 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 80407a96-f005-33cb-9e54-2630e0681afd | -17.15765 | -57.36494 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 9b968887-2ea1-38f8-b4be-775e90d5ba7e | -17.15741 | -57.36808 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 78bf07e7-af46-38cc-a5fd-1a1899ce392b | -17.1574 | -57.39305 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2fb5986f-52a6-376b-a61d-eceaf09b3cff | -17.15671 | -57.36972 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b37634c9-045a-31ec-b5b4-70b9599da850 | -17.15652 | -57.39463 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 87993147-36f5-3cf7-b245-a999b5463685 | -17.1565 | -57.37288 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 30cf6e9a-0901-3a85-b266-e5455c31da47 | -17.15649 | -57.39787 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 4fa27892-aa03-3977-baa6-66cbc1c21039 | -17.15576 | -57.37451 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 700e69ee-775f-32af-8f6b-f7b610d640ec | -17.15559 | -57.37767 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8aa7e2cd-427a-3329-98e2-ad2f7c01d351 | -17.15557 | -57.40269 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 3224b625-0333-31ca-9fe3-7927d074e026 | -17.15557 | -57.39943 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| f46eeaec-6fbf-3c82-93b1-beb3e3919e34 | -17.15482 | -57.37929 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5738734a-4334-3843-a6c9-dd02d8bb0876 | -17.15468 | -57.38248 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ae00a80b-2064-315e-85ae-5547026e5ea8 | -17.15463 | -57.40423 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| bcf01853-d9c6-3a8d-a912-766915c6437d | -17.15288 | -57.36713 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ecefaa5d-cb6a-349a-8146-556242a51312 | -17.15286 | -57.39209 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c0df37b3-1730-3df4-a0ca-32d7cfa268b9 | -17.15217 | -57.36877 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 5958f9fc-e029-38f9-b12d-4fc388c4c9dc | -17.15198 | -57.39367 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 27757a1d-226f-3a03-81fc-af591b621aea | -17.15194 | -57.39689 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 34d6f63d-d11a-3af9-8f5c-f8c1d0c30a50 | -17.15105 | -57.37672 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 262f1a89-74e9-351d-ac28-5c2a12697047 | -17.15103 | -57.40171 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 2d475968-0b0b-3b08-8404-816f861b8af6 | -17.15103 | -57.39846 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| da51c612-2ab9-3eec-8b96-6a6cf726a444 | -17.14831 | -57.39112 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 6e9113a6-a9ba-3154-afeb-1eb8d8185878 | -17.14743 | -57.39272 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 2e7a7a0e-95fa-3e86-acbf-0544d09f167e | -17.1474 | -57.39592 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 3f30646d-f566-31dd-98bc-1e3575ca0928 | -17.14648 | -57.40075 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| dacca72a-0d6e-322b-a68a-688629efb335 | -17.14648 | -57.39751 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| e295fe11-b12f-36cb-98dd-730d478cecee | -17.14556 | -57.40557 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| e2b4c1f0-2fa3-3e9e-9ae0-1973f75c7e41 | -17.14553 | -57.40232 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 18c4b515-a4b8-3ea7-a9f7-c4baa616c214 | -17.14285 | -57.39495 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 4fdea0dc-3594-30a8-a94c-611bcfd3858f | -17.14194 | -57.39978 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 1a9242fa-55a0-37f4-87fe-848572f75a38 | -17.14102 | -57.40461 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 219f8fb6-dcb8-315b-b210-619e3eee3f21 | -17.13923 | -57.38919 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 54b72b65-1e51-318d-9cc4-239e8806a79c | -17.13831 | -57.39399 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1a874c20-420c-371c-8f59-6513d0ca9f00 | -17.13739 | -57.3988 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 061bcc94-1305-3c70-8893-fe19593b1bee | -17.13647 | -57.40363 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 77f587c2-c047-3370-b316-0b05848568eb | -16.80585 | -57.3819 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 60f0a2dc-fc0b-30b6-bca9-c3d9ac9c22e8 | -16.80128 | -57.38093 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5776297a-95ac-3d35-9dbe-612ae9a814de | -16.79578 | -57.38482 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f5bdc8a5-0d74-3a15-94df-a206828d99e4 | -16.79028 | -57.38872 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 76c617c3-0696-3782-8ad1-fcf8acf1d777 | -16.78664 | -57.38288 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 6262f879-fbdd-3ca9-8149-1706d71e9d0c | -16.78301 | -57.37708 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 81b35aad-ffbe-3b50-abad-e8c201fe0aaf | -16.67787 | -57.28789 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9471524c-02b4-3134-a229-a2121cf6d104 | -16.66384 | -57.16585 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4938be8d-f054-3a21-81b4-39de2661fa6a | -16.66285 | -57.16813 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fe506f17-417c-3e2f-b833-36455348678c | -16.65402 | -57.313 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 76e94d02-ce5c-3321-8465-4d8bde95a733 | -16.65197 | -57.15109 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 36ec0f1b-3866-37ad-98e7-136470a7707a | -16.63217 | -57.30338 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5fa2891d-3b1d-354b-bd53-4ef76ac68e14 | -16.85559 | -56.71739 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e45f4d40-db8f-3e5e-a88b-c10616213f06 | -17.12373 | -56.75368 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 31e88ca9-3d71-300e-9090-82f8d2d190cb | -17.1202 | -56.74838 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 96395ab5-f02e-3983-8846-224f7aefb4ff | -17.11937 | -56.75276 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 487b8b40-b2f9-3583-a26e-69d7677eb7a6 | -17.11622 | -56.79324 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7b5173a8-9528-3ed4-900e-a704713ad977 | -17.11352 | -56.78352 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 816dfaa4-54ea-36d3-a9a5-0053d51d6174 | -17.11269 | -56.78793 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c076a9b7-aac8-34d0-bec8-d5fdc75fe471 | -17.11185 | -56.79232 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d8838789-7989-3f26-978f-c4c10275b9dc | -17.11083 | -56.7738 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 99ebd748-ee4f-35a6-a336-7b30cb65e782 | -17.10999 | -56.7782 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a98bc3ef-f78d-3211-bcb8-ec3ddc2f780e | -17.10915 | -56.7826 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ac0b7785-9370-3a2f-b53a-105f73972e41 | -17.10831 | -56.78701 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ad1e6854-6f05-3815-8b9a-e09ec611a468 | -17.10748 | -56.7914 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c375eb02-aba1-36b3-9284-7bba966c7e46 | -17.10562 | -56.77729 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f11c9a90-2c15-33c5-baae-e78a8aa5541e | -17.10478 | -56.78168 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 28fbbd17-6895-3b44-978e-4e3752a8e5bf | -17.10394 | -56.78609 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 1409f067-4721-3567-901f-1fae2d367fda | -17.1031 | -56.79049 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 2c8c833c-9e5c-34bb-9f78-1a311a927db1 | -17.10041 | -56.78077 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 616909ae-59c9-3ddb-b207-e5731d188886 | -17.09957 | -56.78517 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 037eb883-67af-3222-be52-c20f5bae1d9e | -17.09873 | -56.78957 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b44cd6ad-5582-3dc8-8511-0ad0760b1e60 | -17.0952 | -56.78425 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f7724d58-6fc8-3fac-b567-3f6daeabab26 | -17.09435 | -56.78866 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a66ad659-73ed-31c9-b638-505b83abe4c3 | -17.09167 | -56.77895 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1f314b0e-75b1-3764-9734-b2e1853f8855 | -17.09082 | -56.78335 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d135448c-4acd-3ca2-b38d-789676c1a148 | -17.08998 | -56.78775 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2b8fc4fe-d459-363f-ada3-0bbf76730e48 | -17.08729 | -56.77805 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 281e4981-1895-3642-b19a-fcf1a845b86d | -17.08645 | -56.78244 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0b74db21-1e58-3af9-9724-2a9c25f5ca02 | -17.07855 | -56.77622 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 153ad0e2-5d56-3e18-97aa-de361111b82c | -17.0777 | -56.78062 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 718235c6-4a78-36da-ad19-269f531a452b | -17.07685 | -56.78503 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b31c52a4-9252-31ec-80e7-71e8e71075f1 | -17.07601 | -56.78944 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 74a39b39-578e-384e-aaff-03ccbe1592ba | -17.07516 | -56.79385 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0350f98b-3ca7-33a0-9e62-6959d6d083f1 | -17.06993 | -56.79735 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cbd3d5bc-4651-3ab7-9542-91dff615bdfb | -17.06555 | -56.79644 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1b61c07f-f433-325b-b7cc-1fc526335d36 | -17.06469 | -56.80086 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 99e81937-ccc7-3edf-81f7-b53deb79ea69 | -17.06172 | -56.79823 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f01094ba-4c65-3b77-9fb3-6b7ffb57baf2 | -17.06117 | -56.79552 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4fc38bbe-14f4-3328-9b69-28c92dc47cf9 | -17.06032 | -56.79993 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7033d6c3-6b02-3351-9655-5c305f49e863 | -17.05734 | -56.79728 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e7ff390e-0bfe-3cf8-b764-85bf349b29fe | -17.05679 | -56.7946 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d202b99e-ae16-351c-bc32-f7b579ddc073 | -17.05296 | -56.79636 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f3bc3a9d-6231-3735-aedb-7517f94dd702 | -17.05242 | -56.79369 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README131.md)
