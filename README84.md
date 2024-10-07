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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6c2b45b-2566-31cb-9d5d-bc90a226b2b0 | -14.02182 | -47.28576 | 2024-10-07 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e72d6a40-08db-37bd-8b98-4a5ce18c7f98 | -14.01717 | -47.28568 | 2024-10-07 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e7cd337-6996-3f91-a74d-27b5c810fe04 | -16.48881 | -48.02358 | 2024-10-07 04:53:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 206f7404-fa1b-3bbc-bec3-47dc77f7d1e2 | -15.8629 | -47.37202 | 2024-10-07 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7d6ae97-b529-3ec6-b84e-4f34e26f90a1 | -15.70298 | -47.15475 | 2024-10-07 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec0f1af1-2c64-3428-bf8b-bec853566f10 | -15.69825 | -47.15409 | 2024-10-07 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 676e6c7e-2d19-3273-be65-20fb022aa105 | -15.63822 | -47.7308 | 2024-10-07 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8efc47e7-2a7d-3224-881e-fe7f92dcfbb6 | -15.57018 | -47.85704 | 2024-10-07 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa62d476-3dd2-30e5-8468-719757f2aa60 | -16.53757 | -49.04177 | 2024-10-07 04:53:00 | NOAA-21 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c2e3cc2-45fd-3bbe-9bc8-8fff23b4dc8d | -16.14304 | -48.89257 | 2024-10-07 04:53:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bcf86353-cf7e-3575-8551-15b44434ef1a | -16.14252 | -48.89669 | 2024-10-07 04:53:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ff50c90c-1061-34a0-9b2f-d3d8fdebd23e | -16.13881 | -48.8919 | 2024-10-07 04:53:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6facda82-e9b5-3f89-a1ec-66db2db81dfe | -16.1383 | -48.89599 | 2024-10-07 04:53:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a4addfcb-a512-36e4-aa92-09339bc90213 | -16.13356 | -48.89937 | 2024-10-07 04:53:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17d28d5f-bd44-3e10-bc27-85176bb3e1f9 | -16.10425 | -50.23199 | 2024-10-07 04:53:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7c80bc6-533a-3876-8af2-05d54ff92ccc | -16.10172 | -50.22138 | 2024-10-07 04:53:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a5c8181-0d5a-3d44-b33e-7ee59e04e3e4 | -16.10035 | -50.23156 | 2024-10-07 04:53:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e144315e-ff4b-378b-aaf6-099a6a355cef | -16.09781 | -50.22102 | 2024-10-07 04:53:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fcfb25c-db17-30ce-b2b8-dc925cc147bf | -16.09062 | -50.21548 | 2024-10-07 04:53:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1d70a060-506d-35c3-aabb-385899a9d6cb | -16.08668 | -50.21528 | 2024-10-07 04:53:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4564b3f0-8e10-3630-8c19-f9877904a0cb | -16.08342 | -50.20998 | 2024-10-07 04:53:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bfb6206c-4c1b-3e50-9c8f-5eb4008feecb | -16.08275 | -50.21501 | 2024-10-07 04:53:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b27bf1fe-581d-3472-b6dd-c335a6ea08db | -16.0795 | -50.20965 | 2024-10-07 04:53:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cbb18bb3-2c50-36c4-ac57-588a87233a95 | -16.07502 | -50.21342 | 2024-10-07 04:53:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 17e7d20e-6b24-3569-af65-6259039e60ea | -16.07438 | -50.21823 | 2024-10-07 04:53:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 579584eb-470b-32ad-937e-f37660978f9b | -16.07373 | -50.2231 | 2024-10-07 04:53:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4f5ed2da-50c2-345f-a504-770a95052e05 | -16.0699 | -50.22198 | 2024-10-07 04:53:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 55584122-7322-3109-9959-d89da5696591 | -10.54065 | -49.10917 | 2024-10-07 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 0e6d37a0-35e1-382c-9f7f-48ed9f718b07 | -11.13634 | -49.61953 | 2024-10-07 04:53:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e316d8a-4475-38f4-9ffa-c40790eb1e2f | -16.31544 | -51.27485 | 2024-10-07 04:53:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56d81bd9-23dc-31f0-b439-863dadd9ddb4 | -16.3148 | -51.27937 | 2024-10-07 04:53:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d890271-b4e0-3e84-90cb-9bcd056f0878 | -16.31415 | -51.28402 | 2024-10-07 04:53:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f581ccd1-b445-30ea-a0d9-d70194a30adf | -16.31179 | -51.27419 | 2024-10-07 04:53:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f21f8969-f209-3b1f-9a8a-34d55a8b959f | -16.3105 | -51.28332 | 2024-10-07 04:53:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f53a0bf-88c6-3c2c-a539-ec6c568dd87d | -16.20258 | -50.92693 | 2024-10-07 04:53:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 63f88892-b803-3362-bf4e-59c2e556a705 | -16.182 | -50.93793 | 2024-10-07 04:53:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 178a45aa-6ada-3a3a-9bfa-da90fd49ff53 | -16.18137 | -50.94258 | 2024-10-07 04:53:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daa58883-c1db-38d0-9055-96234bf2fbef | -16.17827 | -50.93733 | 2024-10-07 04:53:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52dac638-6451-3afa-b0fe-f17bb4b17edd | -16.17764 | -50.94197 | 2024-10-07 04:53:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c88388a-3024-3651-b6b1-9744361e74ca | -16.06375 | -50.44382 | 2024-10-07 04:53:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42f99504-9919-3920-9d54-75fffbd0a8d6 | -16.05925 | -50.44811 | 2024-10-07 04:53:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89f69cf9-575a-3066-a687-4df521be67b1 | -16.05541 | -50.44751 | 2024-10-07 04:53:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1643868f-b9e0-3506-a9cf-0c737a946509 | -10.66619 | -51.53592 | 2024-10-07 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e02ae0c4-4aa4-3574-af92-4b785d0d8df0 | -10.65861 | -51.11805 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43a57c3e-2466-3aa5-8f81-00b061c1d720 | -10.65802 | -51.12197 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3faf1d18-a144-3497-b2ff-9133a2951ddb | -10.6557 | -51.11361 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cf86280-3f16-3b1d-bc8e-9689c1f7ad90 | -10.65222 | -51.11308 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0912b09-f949-3b1b-b9f2-1bf5c2668c71 | -10.65164 | -51.117 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18874ceb-73de-38e8-bb29-176807d841ec | -10.56382 | -51.07267 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b217401-92d4-3afa-885b-2c1de47de29b | -10.55684 | -51.07162 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93b94867-c91d-3cab-837f-d8846f942d84 | -10.55394 | -51.06718 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad50002a-63f8-3db8-8947-c46026c9c33e | -10.55045 | -51.06665 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fa5f7c3-9e5a-38b9-aafc-ae7105ccb4e1 | -10.54754 | -51.0622 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88b02e78-b9b8-3e51-a5b4-b33a2ae8dcb1 | -10.53708 | -51.0606 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32523b24-bb5a-3c48-af96-7c2b270f2028 | -10.52254 | -51.0624 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df7779e7-5ac4-3aac-ab6f-8bc1d9a39b9f | -10.49702 | -51.07959 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb948725-0316-3439-89b0-3dd68fb24f0b | -10.49644 | -51.08348 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9c2d394-c00e-3189-a6fd-7002c64847d9 | -10.49408 | -51.09907 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d68e61b6-5cf7-3d62-bbdc-57e2b05a3bae | -10.48825 | -51.1141 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77e5b1c9-0536-3f3d-994d-1584e62af8a1 | -10.48419 | -51.11746 | 2024-10-07 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74c2a39b-5984-3667-ab3b-c2c3ebd3e452 | -11.27787 | -51.35945 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bd3bc73-76ea-3379-bad2-ae6442598fc4 | -11.27497 | -51.35503 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0dff1760-58ee-3a5d-a8a4-e318e520a7d0 | -11.2744 | -51.35891 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6c31f11f-e91a-3529-a1b0-31b84678dc74 | -11.27093 | -51.35838 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5a6fc595-19a6-35b1-ac95-079880cbe823 | -11.24055 | -51.23909 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea7ede62-8166-3d7c-8e57-9504f90be25e | -11.23833 | -51.24152 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9308cb7d-b2ce-32bc-9917-d24a76e4b692 | -11.99066 | -51.91221 | 2024-10-07 04:53:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73229b39-5033-3163-aee5-9d37682c9e1e | -11.98724 | -51.9117 | 2024-10-07 04:53:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce35c583-0e60-3ec5-9372-9fe10f29c16c | -11.98325 | -51.91495 | 2024-10-07 04:53:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78195182-a90c-34d1-bfac-caab9c903b75 | -11.97983 | -51.91444 | 2024-10-07 04:53:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a18f8809-880f-3dba-b646-b0f3763d5eb0 | -11.29808 | -51.39038 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f2a8986-afbf-3dc5-bae9-f855a789d904 | -11.29692 | -51.39813 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 353b30f5-3ebd-3e96-90f2-71bf88289499 | -11.29578 | -51.38208 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1728e9db-68bc-316a-93cd-0748c1cfbf51 | -11.29347 | -51.37378 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f914e0f1-c3a7-31ab-a7f1-e1472eb17e86 | -11.29289 | -51.37766 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 357a5033-8aba-3f12-9ae7-3baec8d65329 | -11.29231 | -51.38154 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ddb1a848-a0fa-3834-add6-8525d3e8be97 | -11.29173 | -51.38543 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8a9206d-9a85-33dd-a65c-060c45360e49 | -11.29059 | -51.36936 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 06104bda-bc75-3b7a-b89a-6fd06677e9f0 | -11.29001 | -51.37325 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 00dd6572-056b-3a18-af98-b7c4bef881ac | -11.28943 | -51.37713 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6aaf6f0-ceae-37cf-8d4f-5c820961fbba | -11.28885 | -51.38101 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65ef9b69-6152-303d-af65-673d1f4a10a0 | -11.28827 | -51.38489 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ea38050-7ffa-342a-b67d-ea2717edd7e7 | -11.28712 | -51.36882 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10620195-9d6d-3cc6-858e-d4011d7cd697 | -11.28654 | -51.37271 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f003f63a-a7cb-3c8a-a366-5edab2e0b0b4 | -11.28596 | -51.37659 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| acc40561-1f63-3d87-bc95-cb714fcca856 | -11.28538 | -51.38047 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a4382660-45d2-3c5e-8e40-9f21d0cc7e63 | -11.27729 | -51.36333 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5706eef9-198f-376b-87f2-3a5846ee6443 | -11.27671 | -51.36722 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33969d2b-dae5-325f-968b-43f1f15e69e6 | -11.27382 | -51.3628 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d571a051-8e24-3ef7-a274-55108d2b9c7d | -11.27324 | -51.36668 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9f3e014-cda2-312d-ac7a-45c3dacdd04a | -11.27267 | -51.37057 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 563896e1-f433-3379-bf0e-1e59eeac54df | -11.27209 | -51.37445 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f491532b-8a53-34f7-b34e-85bb72f0e232 | -11.27035 | -51.36226 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4bbfd787-7229-3cfc-8f2d-e603df5260e4 | -11.26227 | -51.39278 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5e56928-5935-3055-8856-06676594834a | -11.25937 | -51.36454 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cb29420-a8ad-330b-80cc-8e11643707ca | -11.25881 | -51.39224 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5adbfcab-0b37-35dd-9e9a-e8d857c95a8b | -11.25592 | -51.38783 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f72364f-239f-32a6-9809-73d7ce5fd069 | -11.25245 | -51.38729 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6473eda9-3411-34bd-9c99-85387f4fef86 | -11.25243 | -51.36347 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b24144a-800f-359f-95e8-150a83e7d653 | -11.25186 | -51.36736 | 2024-10-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README85.md)
