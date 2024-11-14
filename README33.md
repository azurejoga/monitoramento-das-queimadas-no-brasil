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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d76793a-67ee-3bd5-8c3c-9db74245d5c5 | -0.90557 | -51.72446 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3d9c972-aca0-30af-94ae-2b39e067fbb8 | -2.1065 | -50.84805 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73450521-a690-3b59-afe7-addfaa6f0163 | -2.88999 | -50.41862 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5a1feb9-ffb0-355a-907b-64980410b34c | -1.38813 | -51.56168 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94435d6f-ff26-3c5b-bcfa-2e6496b48be2 | -4.05398 | -48.32179 | 2024-11-14 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c240c08f-b0ea-3ec9-9127-2841840a29f3 | -3.772 | -41.59608 | 2024-11-14 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6051e0a4-449b-378e-a291-4f2c685d7a55 | -1.40102 | -51.13402 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75ed431f-a6f3-3b70-b1d1-95baf592c7ac | -3.88948 | -46.0906 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ad36eb2c-e0e6-33ec-a7d7-1da104011a95 | -5.35614 | -43.54251 | 2024-11-14 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c75d1dfd-a130-3343-8bcd-873d0e18a56f | -3.40388 | -50.30392 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5be6026b-6b5e-37c6-a447-c8df66389fd3 | -3.95236 | -46.4115 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ec9b49ac-cb70-352a-8fc7-108eb2ef4554 | -4.33115 | -48.6172 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5b82db9-812d-336d-8530-fb234f65ff15 | -4.0764 | -49.13784 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d8f8cc6-0945-39fd-b8b0-69630a9ab929 | -2.1059 | -50.85181 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 745c1565-1597-3d4f-972f-84a2cfaf2ec2 | -1.96254 | -52.10674 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a3e8cad-6877-36c0-941b-7433acbd9206 | -2.66286 | -46.83142 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b87fb33-123b-38b6-b55b-9e34d2ff9bc6 | -2.27046 | -48.44035 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ce7c49d-caaa-326b-8f81-9604536d2edc | -3.04829 | -48.00907 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7af923ec-fa54-331f-87da-4071719ef2fb | -4.27026 | -48.19818 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a90c7a15-2515-3ea5-b75f-66129e974288 | -2.1881 | -46.63533 | 2024-11-14 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea4e8284-7891-32aa-a747-966eb380d4ed | -2.68844 | -51.70735 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77df779e-6b73-3393-a45b-932f8dffcf29 | -3.43745 | -50.3091 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89b29ab2-5b13-350f-90a5-932156d2a12d | -2.64803 | -45.80303 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| da413bc1-1f87-35dd-a0dc-e8938d06c938 | -0.80499 | -51.48461 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0de0ebd9-94a3-3f37-9b0a-5705bcad2dc1 | -1.63868 | -53.27585 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c077fa8-8c43-3cb9-8fa5-46e8b68b71a0 | -4.04895 | -48.31029 | 2024-11-14 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52594688-ad87-3e3d-9249-226184a34eba | -2.37865 | -48.53101 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe4fde6d-c005-3658-a26b-28ec669e184d | -2.00479 | -46.30235 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24063be0-e235-3da3-914f-1e04c96abdf4 | -2.6379 | -46.17284 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c8a2281-3f1f-3bb3-b75e-2318fad8d96b | -1.61712 | -52.23069 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 151a5669-4c02-39c7-92a7-0f1a317e1301 | -1.36956 | -52.25384 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9ef787c-7f72-3cf7-b409-5672165ac50e | -1.71073 | -47.04683 | 2024-11-14 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca934bf0-fab5-3b00-9f6f-aec550645611 | -1.67012 | -52.56253 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c76dda2d-3fcf-37a9-aa22-b76e1e1f4af3 | -3.05547 | -50.33364 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a392073-e6b7-30d4-8f77-deb63563bfbb | -3.23745 | -50.66897 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4be413fc-1b9f-3f23-992a-0b4868622150 | -2.87034 | -47.84171 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8e7a4a7-aa0e-3c35-95eb-2514a6cc3b2f | -3.41787 | -50.36811 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4c95c3f-360d-3530-a070-19a617855942 | -2.95032 | -48.02628 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d341ab0f-23dc-38fc-be26-5eb25b9b2243 | -4.59424 | -47.0686 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9a4115e-810e-3a12-a634-35a43817a2de | -3.60562 | -48.90955 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa8a82ae-77eb-3d42-a2f8-11b669b4c2e1 | -2.37267 | -48.54766 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1d159d4-eefe-3e33-be4d-73418b37c6a5 | -1.38327 | -51.56928 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2727b6f7-4ee1-39ea-8bab-baa2fffafb74 | -3.05423 | -45.53148 | 2024-11-14 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25309e27-aaff-31dd-9a97-78b3f071b2cd | -2.24224 | -51.43216 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 46fb9aea-c802-3065-9738-d19ba6ef5059 | -3.16236 | -50.58684 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eae71495-ed2a-345a-a503-a93d1536932c | -2.17564 | -48.54522 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59acfc7d-3306-395e-b6f8-5a9ff5d51540 | -2.4242 | -48.87228 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57abd3f0-08a6-3794-827b-95e76021823d | -6.96609 | -39.82895 | 2024-11-14 04:40:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b412558f-e4f2-349e-a9d7-493d527ebd5d | -3.11363 | -45.88003 | 2024-11-14 04:40:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3eb7b616-f5f3-32b3-aff2-3b5e43fa9222 | -2.80557 | -46.65784 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13df10ea-644a-3928-84ab-39b36077d333 | -4.10943 | -48.49031 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49295dd9-45ad-3206-ba02-c111d0198a9c | -3.7135 | -50.60903 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 64624a14-f509-3de8-9063-3acaa415d60f | -1.2852 | -52.47084 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c632e878-1f08-33c9-9aab-db4ab97aa554 | -2.66894 | -46.99487 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cdb2d35f-3fc4-32d4-9d56-124b5fd24494 | -1.55367 | -51.22107 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abe53104-08e7-3270-96e7-049b5b458ca5 | -4.22302 | -46.81629 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98a35fa9-aad1-37a2-8862-0b178ee1e051 | -2.31636 | -49.14697 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0395887-7a43-3e93-a970-9c441bd5b104 | -3.4938 | -50.84386 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fea17381-0995-3968-9d3a-3c8391085b45 | -3.16988 | -50.45111 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3b3d245-2ab7-39db-83db-c8aacaaa49de | -3.20985 | -46.48655 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9aedc859-b2ae-3d29-8cb9-48d36712db24 | -4.03066 | -44.67788 | 2024-11-14 04:40:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc75fa55-86dd-37cd-b8d7-b9440b0f4e83 | -3.24578 | -46.53155 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad9c66c4-50fc-398a-86ee-10957b91c103 | -4.30033 | -48.06964 | 2024-11-14 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3cc5047-2c55-33d7-8624-25774d0bd827 | -1.58494 | -47.66443 | 2024-11-14 04:40:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97658874-5383-3ab4-b3dd-7961ec9cdc06 | -3.49494 | -50.83653 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6305e3b-b282-320e-b2ba-db361d350b8c | -1.39195 | -51.10064 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51e269fa-5e67-3822-a0ec-4297a4421ba1 | -4.44444 | -49.59098 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8868ff66-a4ba-3ad6-b303-6f30bce1f19a | -2.65599 | -47.35624 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a0ca745-e6d8-3733-ad2c-6fb5579b97fe | -3.15897 | -50.58632 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 056f983c-1375-3763-882b-2385621ad364 | -3.41394 | -50.37116 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7715dff0-7a0b-3ed8-b75a-c42d08dee6c6 | -1.39236 | -51.12068 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c93a8da-ffbe-3e3e-8b85-17220aa34e65 | -5.07371 | -45.5074 | 2024-11-14 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40bf09c1-ae57-35d2-96bd-af9a1f82f634 | -2.3566 | -48.52059 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b053d94-f007-39af-af61-0d876c1a83c5 | -0.89037 | -51.72645 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5db104cd-a3cd-35fc-9cf0-10117a4b4f28 | -2.69498 | -49.18575 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 766b2382-d151-38e3-97d3-b556ee2f46d2 | -1.68451 | -48.46445 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f61d719-ae4a-3ed1-a10d-41625fdee54b | -1.21692 | -51.74765 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93431d51-81f5-34bf-a6ec-c5568149e687 | -3.32621 | -44.07809 | 2024-11-14 04:40:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3d719d0-f711-3468-ae52-921366ea3fa9 | -2.82054 | -46.65243 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 352c9598-e9ac-33c6-817a-d4f26a00dbd6 | -3.03751 | -50.33818 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d91135dd-b3ae-3862-8729-6b27535fc9cb | -5.07574 | -45.51029 | 2024-11-14 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aaccf36c-d354-3012-a88b-0610bb2dfdd8 | -4.45522 | -45.35946 | 2024-11-14 04:40:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9f14699-ab74-3a76-b2cb-28d6a46103ec | -3.03249 | -48.08867 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 668b90ba-866a-3f14-ad7e-2f9b5c7c5cbf | -3.46822 | -50.3102 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 657c42ad-02fe-39ed-8367-dd9c265ada05 | -4.11606 | -48.49133 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3d0fccb-d424-313b-b458-592c4f0fd27b | -4.59711 | -47.07288 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9487ea48-97d9-368b-a30c-b6d79926b58c | -4.20731 | -48.60513 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfbaee0b-37bf-355a-8fbd-607efdc8108c | -2.62975 | -46.81885 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a34b7e56-5621-3391-8ce0-ca7f00e21321 | -3.02269 | -51.0918 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ae26564-7754-3a21-93b0-8a1260420bec | -2.38232 | -46.49021 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 334cdaa0-9d45-36ec-8332-b4350a412dac | -2.64866 | -45.79897 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7137f134-60fd-37f7-a814-9f2b52e4cdd7 | -6.96398 | -39.83005 | 2024-11-14 04:40:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 759cd485-578a-344d-b349-697bdfc43bb7 | -2.66571 | -46.83566 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8190f73-b2b3-345e-93c4-2fe718ee3f04 | -2.80078 | -51.49977 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d72c4076-2447-3ba2-a025-c9fbae28b3c2 | -2.62576 | -46.82203 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aec7e760-04fa-31f3-ba90-383fd8748de7 | -2.91013 | -49.48392 | 2024-11-14 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6fdf58b-cc71-330d-9497-11f6f8248552 | -5.56283 | -45.3644 | 2024-11-14 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75cfb344-ddd7-37fd-a3b7-839e4e2c6656 | -2.15267 | -48.95256 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92a0901a-d359-3342-a4c7-8043f3722b06 | -2.95581 | -48.01286 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 011a131d-055f-3d2c-8311-adb68bdba44e | -3.3228 | -50.08469 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README34.md)
