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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfbe3cfe-a671-3d53-89b8-a07f902f69e5 | 2.26862 | -60.25669 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6076f213-9ca2-34f5-9986-fcac1de0e8b2 | 2.10303 | -61.81992 | 2025-03-04 05:14:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| baf3c707-e8e4-338b-91be-a99c3f8f5861 | 2.35919 | -61.05645 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1832ebe-6c09-3a73-a08d-ee2536ce2cdd | 2.34032 | -61.05954 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f12e1258-5f2f-345f-a78a-d44525a84c71 | 2.20928 | -60.54702 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b602c2b1-7845-39f9-9957-0ee76128f939 | 1.75943 | -60.229 | 2025-03-04 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1ede4b3-087d-3572-9ed1-e16ce75e093d | 1.9415 | -60.39285 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 276d78e8-aa9e-3fcf-8bbf-303e2978871d | 3.5363 | -60.11401 | 2025-03-04 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8aefdcf9-c828-319d-8888-4c482779dd64 | 2.34407 | -61.05878 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 470fbd63-ac6d-3586-a35d-545a8acc9b0c | 3.06389 | -60.08631 | 2025-03-04 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3234623-6132-3de6-b3e5-349ec6063761 | 2.3561 | -61.06155 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4880e160-8939-3390-9a36-de69764384d0 | 2.34854 | -61.06268 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88252fdd-87e1-3926-9f53-c7dbc678517b | 1.96503 | -60.61596 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fddad709-9461-380a-9b4d-0488cc7336e3 | 2.35232 | -61.06213 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac155092-0cee-3e69-a10a-2fd8a4734f14 | 2.36367 | -61.06038 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79e171d1-03ad-390d-b4aa-6b07fafe399a | 2.34477 | -61.06332 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb2db80d-dd2c-353d-9ef1-6b0678d9b755 | 2.34715 | -61.05367 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f98498c-3cae-3918-96d9-bad407a7c697 | 2.26672 | -60.25827 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8effe348-108e-3a9c-b300-22241d0e4b84 | 2.36086 | -61.04223 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61bc2a74-35ed-3201-bf43-b6489b279652 | 3.54525 | -60.09968 | 2025-03-04 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a233d10-dad2-31d0-b440-9fda37ef39fe | 1.93856 | -60.39773 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43b8d712-9016-3099-a297-e762e79119bd | 3.67662 | -60.26974 | 2025-03-04 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 472f07fe-7477-37aa-a292-8889e3f95fe9 | 2.35988 | -61.06092 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d68dc72-7de7-3c75-bb80-0b878aaaf2a2 | 2.17022 | -61.83572 | 2025-03-04 05:14:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 022282d1-a8ee-352e-8379-c0b3fcb54e97 | 3.50235 | -60.18434 | 2025-03-04 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a51af71c-8a0f-3aa8-9021-046053559ab8 | 1.1223 | -60.51899 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66a4d60b-b47e-3201-866a-68ef8a44106a | 0.9654 | -60.52768 | 2025-03-04 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59c9db23-1e76-3074-b53b-5499adc00274 | 0.9239 | -60.33197 | 2025-03-04 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38bccb0c-e29f-35a0-a412-cc2f398a3ce6 | 1.13187 | -60.50898 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d32370e1-af63-3c0e-9bdf-512ca796e01f | 0.67525 | -60.56901 | 2025-03-04 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 355fcc2e-9932-398f-befe-8be0609da490 | 1.12464 | -60.51009 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a6ff0805-9f0f-3b93-9874-fae3ee8b6082 | 1.01091 | -60.57324 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c64ce851-5bb3-361a-b93c-52af52ec3b4d | 1.13612 | -60.5126 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fa449f15-41b4-3e03-bf9a-5ad44be52298 | 1.08584 | -60.67396 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d3f72ee0-39ee-3fa9-b3cc-fda30e44c8bb | 1.12167 | -60.51481 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e0b8e19-94d3-3447-a99d-7733373ee30d | 1.13484 | -60.50427 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2603a021-57b8-3d36-929f-9fcfb9d60d2c | 1.12825 | -60.50954 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e43f791f-6f30-310f-9b5c-25a056648996 | 1.13315 | -60.51733 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c6036677-18e8-3af5-b8cd-1f2d2afebf67 | 0.74772 | -60.59738 | 2025-03-04 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1ed1a77-fe3d-34c0-ba70-8e58b3f83d9d | 1.13548 | -60.50843 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 922a0720-d8d2-3572-a5f8-d08f28d0dedf | 1.12528 | -60.51425 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 36992373-0f22-3dd0-b02f-278bb5d03415 | 1.08155 | -60.67028 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d53b6a0c-cff5-3625-9769-630170d87260 | 1.13123 | -60.50481 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 369d6c5d-1440-3032-af7b-1245f6deec8b | 0.97305 | -60.45868 | 2025-03-04 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fbc3aa5-e184-351f-a275-81920770fadb | 1.13251 | -60.51315 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| dd75d19a-66d7-39a5-a64c-fbfa883ed205 | 0.64856 | -60.65834 | 2025-03-04 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a922cc3-15bb-34cf-9dc6-ff0ae504a283 | 1.13973 | -60.51205 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c63f6e75-fec4-3f7d-aafd-bb28d1d92489 | 1.12889 | -60.51371 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 992fbdde-ec34-3b08-91ab-43ce70102ca2 | 0.96179 | -60.52821 | 2025-03-04 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f1c4a68-1faa-3179-b6c8-937ce9a6868b | 1.12592 | -60.51843 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 97730e5c-3830-3eb9-8252-0f3239f59000 | 0.67886 | -60.56847 | 2025-03-04 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae0d0774-eb85-30dc-8adf-60e9e13ee7c7 | 1.08519 | -60.66972 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d68a2e14-21a5-34b7-86bc-19f5090042f0 | 1.12103 | -60.51064 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b74a35d-7f42-3738-83ff-d3a1cc3d710b | 0.83584 | -60.55959 | 2025-03-04 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39762405-795a-3eb7-8069-c1087e0bc14c | 1.00643 | -60.57689 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ae85c5b-d02a-3711-8c05-d29981f6f564 | 1.01005 | -60.57634 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1d7f866-2698-317f-9fd4-1adfe8633efe | 1.0865 | -60.6782 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a166a2a5-1df9-3b57-a4d3-2e6ea72db0f9 | 1.0822 | -60.67452 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 07e2097d-a054-3c3e-bd35-754d2022fa25 | 1.12953 | -60.51788 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.6 |
| a248eea8-5503-378d-84d4-7006c4d268ef | 1.33175 | -60.71305 | 2025-03-04 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1da1ccd-246f-31e6-8314-95fe3cba5be7 | -20.92033 | -56.54425 | 2025-03-04 05:20:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 745a7156-c1dc-3455-9b96-58912a9d9bf9 | -19.98779 | -57.23983 | 2025-03-04 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abd5a2c4-6b0f-3194-bf59-2312314d658c | -21.63299 | -48.68169 | 2025-03-04 05:20:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6afafd7-0fcb-3ac3-9acc-6f0f5c9d651f | -21.63901 | -48.68212 | 2025-03-04 05:20:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64be731d-d1f1-36d8-a051-e429a766b83d | -20.92451 | -56.54475 | 2025-03-04 05:20:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40377fad-5cf5-3c27-b5be-a9fc8ba0208a | -21.63217 | -48.68106 | 2025-03-04 05:20:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5ba5f67-de18-3125-9fdc-eafc27cadab7 | -21.63983 | -48.68275 | 2025-03-04 05:20:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4dcc91d-ce51-393e-960d-e56ee95d5255 | -26.25881 | -52.81874 | 2025-03-04 05:22:00 | NOAA-21 | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 49a649f8-27f0-3d23-9607-9ed660ed9462 | -21.45002 | -53.85022 | 2025-03-04 05:22:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2e659e2-36ac-3dac-a7d2-361991e0f5ea | 2.35815 | -61.04883 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 81a62b84-250c-355e-8a52-81e62344586d | 2.35118 | -61.04986 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f8cd942d-7cba-360d-8845-0b0d22bcec30 | 1.9389 | -60.34613 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f3580f5-7317-3655-b563-b1dfe3da6508 | 2.34197 | -61.05918 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f0284e3e-a2c3-3e74-ac5e-bbb050560174 | 2.36102 | -61.04445 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 40503b1c-3459-39c6-b85f-b7738ac97aef | 4.25391 | -60.51285 | 2025-03-04 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 360667fd-ecb1-36d1-89b2-a652b14a79fd | 1.85608 | -60.29377 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06b89252-fa3e-3c4d-b2d0-ab5f1471920c | 2.34421 | -61.05091 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ca770fbe-970e-333a-8a65-1934c7f214bd | 1.12238 | -60.51473 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4dabeefa-c53a-39c8-bc1e-5ed7ba45ce32 | 2.35366 | -61.06533 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b22e8e2c-0303-31d9-820a-316c93b6e403 | 2.39453 | -60.23346 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 112f5782-cc8e-32e2-8614-05c2d45a524b | 1.13387 | -60.51718 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ae6b199a-f48f-3a06-b484-27b679c7b8d0 | 2.36001 | -61.06042 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6756ba6-8c13-3d58-ac93-d798d74209b7 | 2.35405 | -61.04554 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0fa6de1b-151e-31d8-b89d-28cae2cfd2d0 | 2.36348 | -61.05986 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2739fa3b-7316-3a6a-8b89-65dad0380cab | 2.16874 | -61.83389 | 2025-03-04 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9ce1deb-893a-35f8-8ae8-2fe7cef16789 | 2.35938 | -61.05654 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bc5438a-394e-397d-a1f7-c53bc75c87f0 | 3.53703 | -60.11657 | 2025-03-04 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e0b286c-ba35-327e-9fad-68a8803e7146 | 1.33006 | -60.71473 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16e39952-d431-3e54-8965-d326deb85f4f | 2.3604 | -61.0406 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f69125e8-ad4f-31e6-905d-a9ecec0cec9f | 2.34485 | -61.05486 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd48fdf4-78c8-3ad1-97f6-1f3378425e89 | 3.42675 | -60.71344 | 2025-03-04 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 743f47e2-900f-3e10-ae5c-e33510d92250 | 2.34609 | -61.06257 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a960372e-5447-3d8b-9da1-04b8af13ed74 | 1.12303 | -60.51888 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e10fc5e-dd13-3ba9-84fd-5cf368448efa | 2.0994 | -61.81471 | 2025-03-04 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 62328e9a-01b4-371f-8045-3d28cc5ad9d1 | 2.35528 | -61.05318 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4fb818c8-5ed7-3a49-8916-09da70188f71 | 2.0003 | -61.1406 | 2025-03-04 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fe0d5b5-7606-3a63-9546-ade4a935d3c4 | 1.63379 | -60.2317 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4670a227-de02-3770-982a-0f8a925f2ef6 | 3.22192 | -60.98782 | 2025-03-04 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9e14c5ea-1147-33b0-b1ed-fcd357af0389 | 2.41468 | -61.20267 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cbf0f1d-b90e-34ab-9976-13beba2f2eb6 | 1.14045 | -60.51191 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
