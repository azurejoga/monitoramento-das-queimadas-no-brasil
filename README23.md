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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1bac683-238f-3645-8738-202581422583 | -1.08416 | -54.11296 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92effc78-9489-3342-ba84-b0da480c09b5 | -3.12769 | -53.74827 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 56721a8d-4549-34fc-95ec-7fc79cd93dbc | 1.79854 | -55.58481 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bcda2bc6-6bc8-3529-8b3a-b40be147d43f | -2.28991 | -47.88377 | 2026-10-03 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a37394ed-8b3a-3dfb-b938-88ec3117271a | -2.92673 | -50.42491 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8728d0d-dcb0-38ae-87b3-ca2f40f4257a | -2.89836 | -54.07908 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87fe6173-9117-3b8c-9319-f0669a1c18a8 | -4.06146 | -51.09042 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 187d0035-20df-34a8-a1be-82184e6d518e | -2.98014 | -53.26889 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64769588-02a3-39d4-a7e0-1117af3a093d | -1.14585 | -54.15816 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21815101-44da-37d8-b984-72a4f05fe31f | -3.18733 | -54.09982 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e5bcb33-4281-3d4f-9052-b8d7dd7d4765 | 0.98719 | -50.01268 | 2026-10-03 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdda4502-eb00-3293-b00e-2a8c008008a8 | -4.27824 | -47.02 | 2026-10-03 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d2f9572-686f-3ed4-9093-2ba4ef3bb276 | -3.01585 | -53.89399 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70421f1f-f2ef-3764-86d6-bf7c18830953 | -1.7664 | -55.02971 | 2026-10-03 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6f21739-984a-3acd-a73b-1b65ecc33201 | -4.9084 | -45.70997 | 2026-10-03 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e2eabb6-08ce-31e4-a374-3785085e8715 | -2.93217 | -54.15245 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cff4938-65d9-36cf-835c-116289b1c008 | -4.98439 | -44.88468 | 2026-10-03 04:38:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de712d8a-e7bd-3b84-9937-3a261a961f65 | -3.0759 | -51.27944 | 2026-10-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c759b455-18cb-3fe5-a564-b7c98129f2b4 | -3.12215 | -48.67718 | 2026-10-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d7a5ed4-a62e-3c06-8a35-d6fcc9f35653 | -3.1144 | -50.28859 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3409603-c6a6-3403-8054-ac6ee85842df | -2.71751 | -54.5043 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2266bd55-5d5d-305d-ad5b-e5b535fd264d | 1.74249 | -50.80105 | 2026-10-03 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d2baf12-ff56-39b8-9b1f-a84f85470f19 | -3.12086 | -53.74016 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b8b44539-516e-302c-921f-f1ac61a0bd33 | -2.89205 | -45.40416 | 2026-10-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c417dea1-ed8f-34cd-909d-eaa796f358ce | -3.02043 | -53.89114 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6de294c-d3cd-3178-aee8-5bc773bcbe09 | -1.64415 | -55.14677 | 2026-10-03 04:38:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 433866fa-59a6-3c8e-9a78-bcbb3b87baa8 | -4.73485 | -43.26646 | 2026-10-03 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 16f14220-2057-3f1a-984f-338ee1a645ee | -3.03015 | -48.4167 | 2026-10-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01bdb6d5-2f71-3d7d-b1da-9a1a757e01c0 | -4.35407 | -43.83006 | 2026-10-03 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 023e52d8-4fdd-3c37-abf9-00aa80c00015 | -3.13166 | -53.74889 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 883baf84-be84-3f04-a4aa-2cabbdc2a531 | -3.87745 | -51.89283 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec96f06e-2613-3e38-9c88-d5f5ffed91c3 | -3.13222 | -53.74547 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ee81ef0-8134-3eef-b23c-147e612fe8b4 | -3.13961 | -53.75015 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 309d2876-efc0-3f10-b733-eead7f8a6cd7 | 0.62193 | -54.40928 | 2026-10-03 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c491281-5088-3d7c-8986-9fca50173123 | -3.08098 | -54.40062 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3206460e-d694-33be-b7d2-db7d898035ed | -2.91409 | -54.0853 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c79fb252-a824-31f2-9122-e7571202593c | -2.96207 | -51.51217 | 2026-10-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 706e337f-5b84-3d18-939f-4401514f84bd | -3.29363 | -53.84866 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d7d735c-6034-3d1c-aca4-4fa8f426529d | -2.984 | -53.26953 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 246f1927-5677-3b3c-b6a1-1d273248bdc6 | -3.12253 | -53.7299 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 05449ba6-d955-3d16-8176-22ca5d6ba9c4 | 0.60139 | -51.56059 | 2026-10-03 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47476213-6ea0-3dd3-8224-4815b12b4050 | -3.88099 | -51.89338 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a4d5094-0a1c-3cae-8b88-aa2fef569033 | -3.01131 | -41.14256 | 2026-10-03 04:38:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 8ca1e185-7e4a-3529-a7b6-38c9ff2e4f0a | -1.08012 | -54.10512 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7dce3f4f-6685-334b-9b4a-7deaf3632f30 | -1.99354 | -49.65075 | 2026-10-03 04:38:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db49929a-1c6d-3247-a2a8-2d95224ab12a | -3.12483 | -53.74079 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aef18d0c-93fa-30bb-83ba-6ecb5c9f976b | -3.27931 | -53.83585 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 052a269d-d04e-366c-9884-26dce0de2941 | -3.41156 | -52.83363 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f12c1253-2bed-3bd1-8b99-a61e1795636b | -2.48575 | -56.09622 | 2026-10-03 04:38:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a658297b-7e72-3ea8-882d-6b0387587860 | -2.1757 | -49.7692 | 2026-10-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f89cf551-cf87-3a8a-b871-16bec771d2d2 | -2.96678 | -54.09451 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7487616f-bc20-3ead-958f-ab181851332c | -2.04954 | -56.86514 | 2026-10-03 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57a06a9e-6868-3982-a819-3511c2763ad4 | -1.08791 | -54.11034 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1a18ec1-2cab-399b-b4ad-e69286527ea6 | -3.10552 | -50.28725 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ff0522c-9511-3c34-bb29-6c978b4470ff | -3.29527 | -53.83828 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0db5a4a-c502-3245-8202-3a0e3e1c6c33 | -2.87117 | -50.3275 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9205f03-5ee6-3138-8a45-4f403761506d | -3.15816 | -48.73261 | 2026-10-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e05cc9a-a91b-3b7f-a056-34b51edb8686 | -3.40134 | -54.06867 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d0c2514-858d-36bf-af3d-e57e806e10fc | -3.10825 | -50.28399 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9129f68-3e89-355f-b3ec-abe64fb4671f | -3.10542 | -50.30182 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5708d782-9f0f-33dd-b15b-f3dc8c6fa041 | -4.04837 | -51.08452 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec3748db-71fc-36ec-8fe5-8d9c30cb3f12 | -1.26869 | -54.55761 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff18b0e7-13d2-3be8-9395-5afab32b2850 | -3.14072 | -53.74331 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dc0e855-506a-3c02-a0a5-421dcc932a70 | -3.00606 | -53.87813 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f1a40e4-816f-319e-a5d2-da699ce12b60 | -3.01698 | -53.887 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 811e7313-52c4-38cc-a6d2-c3387aebc4c0 | -1.27667 | -54.56303 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32572822-3d73-3be1-bc04-50c96e1a60e6 | -2.88103 | -51.02837 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1077798-4ebb-3477-aa63-0f54ddbdc4d8 | -2.93097 | -54.15974 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7916730b-79f1-3e46-b2d7-8775e4405bff | -2.97027 | -54.09877 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a63c87f-9aed-33fc-95fc-833bcdf1c6e4 | -0.24582 | -48.48992 | 2026-10-03 04:38:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a825c02-ab4c-3861-8eda-62947dbb287d | -2.95856 | -51.51162 | 2026-10-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b054ac8-532f-3bbb-8dfb-d45a396d9e20 | -3.12713 | -53.75169 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4b026ae5-dd44-3ebd-9d32-63459847e906 | -1.63968 | -55.14609 | 2026-10-03 04:38:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ffb5b42-3c7c-3436-b88c-ec465ad50c5c | -3.07304 | -51.27506 | 2026-10-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04d7f26c-0a2b-3d8b-885e-b0119aeef020 | -2.88849 | -54.11467 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85786b5c-ff93-3b8c-ae29-9a565f507c3f | -2.97549 | -53.27312 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3dab7189-fdf3-3bf4-9ab9-f13785d38209 | -4.73426 | -43.27056 | 2026-10-03 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 160006e0-9776-37d9-b58a-391e6f66d48d | -3.28494 | -53.82613 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c30c2f62-aa51-3b2b-9dfe-d8ed3d638f18 | -1.53774 | -47.51352 | 2026-10-03 04:38:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1143c812-0ff1-33b4-906a-81b493f667a4 | -1.08478 | -54.10912 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3beadad-e8b3-3f9d-9e72-2dfee41a610c | -3.2862 | -53.84397 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a9f37a5-d885-3f81-92b5-5ccedcad24bd | 1.73892 | -50.80159 | 2026-10-03 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d43deddc-371e-358a-964e-e1dd6d4fbc3e | -2.90594 | -54.084 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61355c44-ebdb-3e98-a990-5468c2fcc091 | -2.89023 | -54.12993 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42154f5e-5566-3771-90af-eb64fdc48d67 | -2.82384 | -50.49733 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7fe710e-8d93-3004-a710-513398ca4d01 | -2.33809 | -51.94547 | 2026-10-03 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2bf9e61-c90a-3325-b131-60d6cedfddc2 | -1.03832 | -49.20929 | 2026-10-03 04:38:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b642515-d66a-3db7-9353-b10b76f2071d | -3.02 | -54.23389 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6a6ca6b-3c92-31ef-9412-d2f3103d4ebc | -3.88035 | -51.89738 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73acbb33-919b-31ec-a2c5-0c7c86bc4dec | -2.96619 | -54.09813 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1eb9d79f-5e59-3261-ad14-6f31a115e3b1 | -3.17054 | -54.10054 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f596440c-df18-3e20-9cf7-b8c52e0d89de | -2.9656 | -54.10175 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f5bc54a-21a2-3152-9467-89f080125605 | -3.28549 | -53.82268 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7125f9d3-f657-3097-9b28-c96dace4125e | -3.12824 | -53.74485 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe2e93dc-afe7-3943-94cd-546ebb10f325 | -3.10599 | -50.29824 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71a81855-44df-3b07-bb5c-9ea2845dcb25 | -4.06082 | -51.11683 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17bf38e2-d7ff-30ba-8c26-b4d04a159352 | -3.05575 | -54.16415 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9a777ae-882c-3dac-b87d-988f498555e3 | -3.29473 | -53.84174 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bb5c53b-cc73-3832-8488-de29479e5b4c | -3.28093 | -53.82561 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62e1dd08-ccd9-39fe-8635-ed0effea83fc | -2.97403 | -53.2578 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README24.md)
