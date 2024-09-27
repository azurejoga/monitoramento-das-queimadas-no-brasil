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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe731412-e8ce-348e-8ce2-7c1146d6bb09 | -10.49853 | -51.15282 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42b033e1-2e6d-304c-bd2a-0f9433495d7c | -10.49797 | -51.15633 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9de395fd-6450-3b74-bf9c-fbc9e4c719b3 | -10.49595 | -51.23203 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 753250a6-da97-31ad-8935-e3ef086545fd | -10.49465 | -51.15581 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6212ba99-49da-3b81-a77e-d37038c0288b | -10.49409 | -51.15934 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76bf91b8-7226-3be8-991b-eae75d548d4f | -10.49321 | -51.22791 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db8f5b86-2552-363b-859c-cc3eae72245a | -10.49296 | -51.16642 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d891c4b8-6f20-362e-b768-e65d8b3ab3ef | -10.49263 | -51.23148 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fecc69e0-4d58-3d40-8a99-c0c63f80bbed | -10.49124 | -51.19867 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e882887-edfa-3848-a1a6-723f3ad3b876 | -10.49076 | -51.15882 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f20b85a-aa44-3677-99ba-5d5c2a53374d | -10.49069 | -51.20215 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e68536c-e47a-3f73-a7da-d49df16a277e | -10.4902 | -51.16236 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e42bdc9-5154-3025-ba54-fe2c106bc387 | -10.49008 | -51.22745 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74615654-55ac-30f0-a212-ccbec66455f9 | -10.48964 | -51.1659 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c77d8197-7c79-34e0-93b9-b8ecdd84fbd0 | -10.48951 | -51.23101 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c0808f8-ba9c-3989-87d9-a0eb3c44c6a3 | -10.48846 | -51.21616 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73fcf3d2-464c-356c-90a5-4f2ac68eef9c | -10.48789 | -51.21972 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 365cc54b-83a0-30c9-b553-9ef075248c75 | -10.48732 | -51.2233 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14436750-6efa-38b6-a1c5-daf7425ff699 | -10.48681 | -51.20506 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b13df263-73e8-3ef0-9eb0-99b19c2179a1 | -10.48626 | -51.20856 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9684dd8-784d-389a-8724-c8b3bc377602 | -10.4857 | -51.21207 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11cefbcb-923f-364f-9773-fa368c08ffc9 | -10.48519 | -51.17247 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cef201bb-d657-364a-8bb2-242a95192b13 | -10.48463 | -51.17599 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4329557-5ea6-3a34-9504-625ae464738e | -10.48405 | -51.20103 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 314c5445-ebe3-31cd-9db1-2a198f77d46a | -10.48351 | -51.18301 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76e361eb-d079-3629-922d-ef17ae96837c | -10.48296 | -51.18651 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eead0200-248c-3395-8d2c-af94c180e0da | -10.48019 | -51.18247 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bf6abc2-bb0d-3763-bc13-01f807d087c2 | -10.47964 | -51.18594 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86362dc5-b8cc-31b4-8951-97d3931f87d6 | -10.47853 | -51.19292 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5af4ef0c-199f-3676-b83e-40e5d37e8fc1 | -10.47797 | -51.1964 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 645c1806-37bd-3cac-8232-a80f2b786bc4 | -10.47687 | -51.18194 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4d079b03-91e9-3590-b1ee-fe22a8697e2b | -10.47631 | -51.18542 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc2dba17-17c5-3ec1-a14a-ee57cbd0344a | -10.47576 | -51.18892 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 389e227a-254b-30c3-8dbc-1bc10abc3f77 | -10.4752 | -51.1924 | 2024-09-27 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ada111ba-2ca0-35ef-80b3-76423fe2b5d4 | -11.13116 | -50.83473 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f0106c9d-5ee2-312d-9f03-334a49e36701 | -11.12841 | -50.8307 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0646f8d-cc4a-3e50-ac2d-d3b0ac4ce722 | -11.12787 | -50.81267 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86e34a75-2a9a-3755-a587-4316207ac902 | -11.12785 | -50.8342 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d0a2a3f2-a2d9-33a3-85b7-1d59b3d29e96 | -11.12732 | -50.81617 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d776c32-d908-3c16-92d1-ddcb83f0b0ea | -11.1251 | -50.83016 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef1713a4-8fda-355f-a698-4f0ccf6ea51b | -11.12455 | -50.83366 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dae712a-9720-3376-a35c-ac60a836ac76 | -11.65166 | -51.71039 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1f5786f-7fc0-3e20-9619-26bee40ccc09 | -11.35422 | -51.54844 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20f6c6b0-128d-33da-9c89-9d2344f896d9 | -11.34422 | -51.54681 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4037e2f-93c0-3590-8548-33a031d4f699 | -11.34365 | -51.55037 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a32dba6-d7d5-3d36-ad57-ceea4072f59d | -11.34089 | -51.54626 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81b99c98-93d3-3812-8e62-1e0fba756a46 | -11.13396 | -51.32966 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55b4d2d3-23c2-347c-9ab2-71057da673a4 | -11.06169 | -51.44174 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90f5c910-635e-3737-b887-fd039c4d86f3 | -11.0536 | -51.38573 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74b5bb62-913f-32f4-9f47-42b9af85b0af | -11.05303 | -51.38928 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0b2e36d-37cf-3de0-bc14-b73a84b574ba | -11.05246 | -51.39283 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77aebe63-bc18-35f8-98f3-55b6af95c867 | -11.05189 | -51.39638 | 2024-09-27 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3de4e926-4100-3faa-95bf-523f8f7307e0 | -11.04457 | -51.4207 | 2024-09-27 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5729ec9-c63c-3c99-b196-32313ee74f2c | -11.04068 | -51.42372 | 2024-09-27 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6daa99fe-416f-3ecd-9c06-ed86ad220028 | -12.61556 | -52.21923 | 2024-09-27 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1844f877-5f0d-3256-9013-d57e4e6e64ae | -12.71915 | -51.95425 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d77c56ba-e38d-3ca4-8c87-45a0352255b0 | -12.71857 | -51.95785 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6f9f1b9-ccc0-3f48-820d-8dd095562018 | -12.71697 | -51.94651 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed1954ac-f33b-320b-89f5-324b11d40cd4 | -12.71421 | -51.94238 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e261cc3e-dba0-3588-a72b-afde16121f09 | -12.71407 | -51.9645 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2afe7f0-f443-3d05-b951-4e243e2b51c4 | -12.71349 | -51.96811 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e5571aa-c158-3147-b2cc-1b93a3223f07 | -12.70957 | -51.97117 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66e234fe-1bfa-3749-9ccd-e2aebc41004f | -12.7087 | -51.93411 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42b620e7-c570-3584-904a-8533a59dbe55 | -12.70594 | -51.92998 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c4bba0c-b600-33b4-9a11-413183bfd189 | -12.70231 | -51.97367 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd8826bf-41e1-3ef3-84f2-5c444081c88f | -12.90179 | -51.28021 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01b47268-a2b5-3e3c-b414-d73028cb6022 | -12.87901 | -51.20774 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34ca1888-ec99-3fde-89c1-1f3bda9aba4a | -12.87246 | -51.16339 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3100fc5a-cc80-3d04-b3d6-455a50235e7f | -12.8719 | -51.16692 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7475a4a-1227-30d5-9568-ec1ff4faee7c | -12.86916 | -51.16286 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba2cfdc5-5bea-3175-90d0-cf294d773a78 | -12.86397 | -51.30293 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be4a2eaf-b819-305e-a3db-5235d01c4416 | -12.851 | -51.14904 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb8bb7a9-4a38-3066-b6e6-4bf6a23e6e8a | -12.83142 | -51.31568 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dc83aec-5ee3-391d-b9a3-2a7f9e6b9e7f | -12.83086 | -51.31921 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afb0bf1b-31df-31fa-bbaf-1ceeb2d04029 | -12.8301 | -51.13118 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58e5cf9a-8a53-3ac0-9c92-03e5df48e16b | -12.79998 | -51.32138 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a0dfc76-57a8-33f7-924b-708701528945 | -12.75333 | -51.33495 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed917bd9-185a-3589-90ac-786861647121 | -12.75277 | -51.33849 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53fd2c10-85b6-3a88-9d38-39edc0d6c0f5 | -12.75002 | -51.33441 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8d7b6bc-6559-3852-8f61-29e5a3f497ef | -12.74946 | -51.33794 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66733f7d-eda0-3cec-952c-b67d29dfee06 | -13.17427 | -51.21329 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e718ea3-90fa-344f-954d-53710ca4cdf1 | -13.17313 | -51.24196 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77e05546-df50-33a0-aa06-981cccd8b6bb | -13.17096 | -51.21275 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ab0fd4f-5543-3828-8048-4f5d98a92d23 | -6.34025 | -51.71494 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dda3b1a-d93a-3f69-99e7-1f337dd61c4a | -5.79123 | -52.28193 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a1eeff0-597b-3d31-a7f7-ce9c22cb6836 | -5.78766 | -52.28137 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 286b1fa5-7d3a-38e4-b25a-29a6a9f96e39 | -5.71178 | -52.35018 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 389eabd4-725f-335f-9313-27e9815be52b | -5.69857 | -51.57548 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b75908af-a505-324b-aaf8-2c7d84035771 | -7.79716 | -52.40612 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b45231d-d9eb-3a58-b7aa-98568145e544 | -7.7963 | -52.40696 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14702e7d-90e7-3ee0-ba51-2e9e02a1818b | -7.79364 | -52.40554 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de17622b-2795-33a3-a947-a5051373efc7 | -7.79278 | -52.40644 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f898283-3c9a-370b-a002-8121129a0c0a | -6.96485 | -51.65366 | 2024-09-27 04:40:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6a9890d-9b1d-372a-a5b2-155f947c45e1 | -6.59768 | -52.30223 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a0572ce4-d445-39c1-a84d-3bf77216d4dd | -8.25107 | -52.55984 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5dd99465-32e1-33d1-aced-b8495b24ab29 | -8.17936 | -53.15239 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ead6d495-ffab-38fd-b48a-ce755a67e651 | -8.17572 | -53.15182 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c524eb6-afb4-3355-a25c-278caac1f900 | -8.17552 | -52.79634 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e5598a2-8b1a-313a-b279-21abf3ac342c | -8.17209 | -53.15126 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2fd446e-b16a-3f71-8d5c-8ed695b7cfca | -8.17129 | -52.79973 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README95.md)
