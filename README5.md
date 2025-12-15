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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf194550-d5e6-3b0e-8c8f-216cace6140f | -6.5631 | -51.1126 | 2025-12-15 04:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a2ebfbba-02c2-3011-a0d7-6d140f275f80 | 0.05477 | -51.11325 | 2025-12-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c440e73c-fd1f-306a-8e41-764951414e26 | -2.58375 | -45.14009 | 2025-12-15 04:42:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6096923b-7601-346d-8756-3782e236d503 | -2.75802 | -42.63585 | 2025-12-15 04:42:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b21948f8-6b53-3358-a0e6-ab660dccfdcd | 1.12671 | -51.05169 | 2025-12-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e04a569-314a-31cf-ba13-3d495dcd0edd | -3.77328 | -47.1609 | 2025-12-15 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62e0eaf2-95fd-39ac-aadf-0e29923eaaa3 | -3.70493 | -47.15031 | 2025-12-15 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c95b2e1-7eb9-35af-8dd0-747546cf1df6 | -2.22853 | -45.65387 | 2025-12-15 04:42:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cbd96074-72c4-3c71-8cf4-e43a640708f8 | -2.24754 | -45.78913 | 2025-12-15 04:42:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db98182f-7e74-3541-8628-74d70e0a55c7 | -2.0315 | -46.31517 | 2025-12-15 04:42:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9057c580-e9bb-34ac-acab-8fefedd047d8 | -2.94315 | -49.1344 | 2025-12-15 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b20ce031-9727-309e-8534-d93971f7c824 | -2.63527 | -47.29236 | 2025-12-15 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c243499-bfdb-3b6e-9f38-f2dbf379da71 | -3.71858 | -44.50182 | 2025-12-15 04:42:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87121e2e-e037-3644-ae40-39d8b227a309 | -2.83532 | -46.73178 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d953bb2-79b6-37c9-959e-80f6c114c857 | -2.43511 | -47.05544 | 2025-12-15 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e2ae767-11ee-3a06-9832-73b9e28b6788 | -1.55619 | -47.07174 | 2025-12-15 04:42:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5ad867f-626a-38ab-ad4d-f7cfcfc6d7e2 | -2.7574 | -42.63999 | 2025-12-15 04:42:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 441a5f30-6843-303e-9aaa-0e5adcc4e739 | 0.0682 | -51.17451 | 2025-12-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f469b9a4-cb19-313e-943e-b37e2fbae31d | -2.93982 | -49.13387 | 2025-12-15 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d53069ff-b789-30d8-96e5-931e5eff9073 | -3.30652 | -42.53724 | 2025-12-15 04:42:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1b55d94-48c4-343e-805f-baf52f8edc87 | -2.22494 | -45.65332 | 2025-12-15 04:42:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae27b697-d913-3478-9c47-3a61bd1f9723 | -2.16772 | -45.92743 | 2025-12-15 04:42:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6fac8ec-ce08-3748-b52a-40d60853598d | -3.01954 | -45.33717 | 2025-12-15 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6841a0ef-b004-3427-8828-8ec438687864 | -3.79939 | -47.05917 | 2025-12-15 04:42:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a916d500-8306-3f5b-be60-100a792e4f66 | -2.39769 | -45.76841 | 2025-12-15 04:42:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4489ae84-5f8f-3edc-8ba7-d729b57e2814 | -3.71469 | -44.50118 | 2025-12-15 04:42:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d476c6e-fca8-3e86-99dc-6014f1ee7402 | -4.80788 | -38.98166 | 2025-12-15 04:42:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d78d155b-cdc0-32f4-9f34-107f21e1658e | -2.83877 | -46.73231 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 456997f4-9c55-3e7a-8213-1bfac180da38 | -3.05723 | -52.8333 | 2025-12-15 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ef5f238-461f-314a-9136-2a13563de839 | -3.20648 | -46.83298 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0203517d-56ca-34b3-b119-dcd2957d0360 | -3.71736 | -39.62526 | 2025-12-15 04:42:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c45a77f0-d3a9-39f9-8841-31bfae56dc9d | -3.06029 | -52.83857 | 2025-12-15 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 353ced20-f89b-36e6-8009-354492b40eb4 | -2.43568 | -47.0518 | 2025-12-15 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1460700-4bea-30c2-b07a-5a32b2b7a1d8 | -4.03895 | -41.91169 | 2025-12-15 04:42:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c13c5de-7d38-38ca-8b9c-6df91322f352 | -2.34549 | -48.42253 | 2025-12-15 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93fe54ad-ef83-3614-9406-b7ff67ab03ec | -2.6347 | -47.29595 | 2025-12-15 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fabaa58a-b2f1-3dfd-9cdf-2546b495a193 | -3.14577 | -48.15403 | 2025-12-15 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7143476c-675c-3d98-bbfb-edc8f46de012 | -3.79883 | -47.06285 | 2025-12-15 04:42:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2b925c1-b8a4-3308-ab51-14d56a07f1a1 | -2.69936 | -49.11763 | 2025-12-15 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b70d0df-06f5-3e8d-9b8d-031172777913 | -2.46052 | -52.22329 | 2025-12-15 04:42:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 444fe86a-8a36-3fc8-b965-86b078d98ed1 | -1.90755 | -46.5925 | 2025-12-15 04:42:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d36f4616-609a-3aef-98c6-2876e1225a93 | -3.14632 | -48.15055 | 2025-12-15 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8ffbc13-e33a-3d2b-95b4-6900e27a3e8e | -3.06104 | -52.83391 | 2025-12-15 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82877d08-e0e3-3f34-b25d-8d0f5bb13cfd | -2.9426 | -49.13785 | 2025-12-15 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c20738df-586d-3b43-ba21-e183115ddf9a | -2.58488 | -45.14215 | 2025-12-15 04:42:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7219793f-e0c3-3538-ba8e-6ad95fbf3e89 | -2.63133 | -47.29542 | 2025-12-15 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| caeb33b4-7b40-3fef-83b4-0e515a8ddd04 | -1.30957 | -49.29828 | 2025-12-15 04:42:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fca3b4e0-e785-3f26-acd4-32dbe2296513 | -2.70268 | -49.11814 | 2025-12-15 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4966d02-f86b-30dd-8003-555c594bcd99 | -2.22557 | -45.64925 | 2025-12-15 04:42:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 40c02b22-24fc-3ab9-a498-1b09ab09febd | -2.83935 | -46.72858 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6b2a7b10-6e6a-31c4-a6f3-0463da939331 | -2.39412 | -45.76786 | 2025-12-15 04:42:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33cbb96f-d5ea-3280-84a5-6939c91eccc2 | -2.41021 | -45.68732 | 2025-12-15 04:42:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd96ef47-cb77-3770-ba45-e54af0b3e697 | -3.20706 | -46.82925 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a9c8a32-c423-3fa9-9d28-2029ef411f48 | -1.31292 | -49.2988 | 2025-12-15 04:42:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07bb93fe-29f8-3d68-8dca-1b299a62c956 | -3.9648 | -41.53229 | 2025-12-15 04:42:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0849f42-eae3-3e81-b529-d1f4f931c347 | -4.04082 | -41.91369 | 2025-12-15 04:42:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8e440aea-fdc1-3581-8181-67ce0a8eeabe | -2.93928 | -49.13733 | 2025-12-15 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ca7f437-a56f-354b-8cb1-e41e750c09b0 | -3.30211 | -42.53657 | 2025-12-15 04:42:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a61e7557-92bf-356e-be10-fbf768afc6f6 | -2.28587 | -53.70472 | 2025-12-15 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93fab746-0eb5-33c3-af3b-decaf1ad6445 | -2.35364 | -45.61739 | 2025-12-15 04:42:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 371b3a9c-6cb3-373f-8455-b1a511c4b448 | -2.35483 | -45.68023 | 2025-12-15 04:42:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b65cfd8b-87ad-30f5-9958-098476a569d4 | -1.88286 | -47.92172 | 2025-12-15 04:42:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1139508-19b7-35b6-94a7-11ab40b4c97c | -2.63808 | -47.29647 | 2025-12-15 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eda52d37-3d8f-302d-83d4-8db4d53ace7c | -1.32468 | -52.38945 | 2025-12-15 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01a57093-d7bc-3f54-90f4-8c98f75db154 | -2.50383 | -48.03975 | 2025-12-15 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 528d582a-84d0-3168-b9f2-0a04c51915c5 | -2.83591 | -46.72806 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4a3c79d0-69db-3f55-a373-18f36f68a2ff | -1.5373 | -45.85521 | 2025-12-15 04:42:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c1a175b-175d-3a08-8edf-a8e2406abe6b | -2.41415 | -48.28465 | 2025-12-15 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 28c08f2b-37f6-3bc0-ba0c-7bf53433b431 | -3.14244 | -48.15351 | 2025-12-15 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 140bba85-51ba-39b8-8136-9a0e862ad2bf | -3.72248 | -44.50242 | 2025-12-15 04:42:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcff71e4-a504-3f1b-ba49-9cc9c956bf69 | -3.98289 | -46.9803 | 2025-12-15 04:42:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22dbe2de-e8af-3274-83c3-9f38c4f59a1b | -2.22431 | -45.65737 | 2025-12-15 04:42:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e844ff4a-4ae7-3fbb-beee-749e18e74392 | -2.16711 | -45.93138 | 2025-12-15 04:42:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 106ea7a0-859c-3bb5-a26c-6e06db846f26 | -3.96557 | -41.52723 | 2025-12-15 04:42:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a8804aaa-2560-35ec-8ad0-a4ec4a6fa768 | -3.30134 | -42.5343 | 2025-12-15 04:42:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 95e559f2-69eb-3849-9f44-7fea8ce721ab | -3.96383 | -40.9301 | 2025-12-15 04:42:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e74c1020-4add-3b1f-9130-fb131009f9ce | -2.83188 | -46.73125 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 844ae418-27f0-3f2f-afdd-fd510e9b6e59 | -3.14189 | -48.15698 | 2025-12-15 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aef47c1b-5f53-3548-b273-f7b79828e45d | -2.83246 | -46.72753 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e60a9676-e2f5-3a4e-8ead-5dce63c7df34 | -3.20362 | -46.82871 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e963135e-94a6-32d9-b567-d915083ba6c3 | -2.69829 | -45.16964 | 2025-12-15 04:42:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77df40ad-74e2-346a-ba0e-60095ab18958 | -2.41155 | -48.28441 | 2025-12-15 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc8ad2b2-1855-3d6d-98aa-d2bbc5384e1d | -2.63865 | -47.29288 | 2025-12-15 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6733a89d-d0cd-3c45-8bc5-d9b468f1b6fb | -2.35546 | -45.67616 | 2025-12-15 04:42:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc95542f-395f-387b-8148-7ad6aed22179 | -3.20247 | -46.83617 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1195e34-bc7e-37b7-bc15-4d8d6eafdfe8 | -3.02322 | -45.33775 | 2025-12-15 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 408044fb-c1fe-3b67-bc64-b4cc913ad77a | -3.0641 | -52.8392 | 2025-12-15 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef75319a-82f3-30e3-abb4-7fc9e74b9705 | -3.05417 | -52.82803 | 2025-12-15 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 387242d9-134b-3041-8174-973206c7ec80 | -3.2042 | -46.82498 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee80338e-6bac-3a43-bf6f-078c399c0a6a | -2.23275 | -45.65034 | 2025-12-15 04:42:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3003f41-bf31-3b2e-a4d5-770f6013e2d6 | -2.28531 | -53.70826 | 2025-12-15 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7eb09901-8fd0-3804-8d32-955c60cf09c7 | -2.39707 | -45.77245 | 2025-12-15 04:42:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1979961b-6efc-3cd3-8276-1cb3dfce2f7f | -2.76175 | -42.64065 | 2025-12-15 04:42:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fea28df-c08f-3357-928c-a11adf4b3082 | -2.85162 | -46.82943 | 2025-12-15 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef00ed69-810d-3b53-98d3-515be7418d72 | -2.58309 | -45.14444 | 2025-12-15 04:42:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eac6d804-c2c2-3229-9b46-f930c6bf414d | -3.01888 | -45.34147 | 2025-12-15 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57053911-bb23-3414-a941-a2ebd3dba955 | -3.1491 | -48.15455 | 2025-12-15 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 640e8a82-fb03-36a9-918e-3e9f5758d278 | -3.12492 | -41.77294 | 2025-12-15 04:42:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f510a907-7878-37d8-ab61-a97ce3f64974 | -2.69763 | -45.174 | 2025-12-15 04:42:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8328e89-7d0d-369a-8a85-d717149880e4 | -3.98231 | -46.98401 | 2025-12-15 04:42:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README6.md)
