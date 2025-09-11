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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 422f76a2-8e5a-3265-90ca-00c4e3674985 | -13.78609 | -46.28542 | 2025-09-11 04:46:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eb98b3f1-0174-3bf3-a704-8dbe464cd343 | -8.89871 | -51.06069 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 844a5ff8-f915-3e79-848d-450ad5e4fcd5 | -11.99584 | -47.59782 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9aceae39-a6cf-3307-a4f0-02f1e1adff1f | -15.83448 | -52.24347 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ac955e4-b25c-3411-bcf3-567ec3cb7b48 | -11.48208 | -43.67662 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e23089a5-b385-381e-8a41-7ae44eeb20a4 | -13.24077 | -51.7737 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 818f9c85-0e8e-3410-8ee6-e8c268d884bd | -11.34064 | -46.4869 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3f876e66-c7e7-30f6-b7b8-90ee0ae000dd | -10.73362 | -46.13518 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8eca8511-ed1e-343d-b39e-dc810a77b733 | -9.80287 | -61.52629 | 2025-09-11 04:46:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0060b357-b825-3fa3-aada-5369239705cf | -11.35059 | -46.50806 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fb847c6e-106d-321c-a45d-b07594739f39 | -11.49652 | -50.38676 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 674924e4-90d5-3404-9abf-190f873a7804 | -12.84603 | -52.94762 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2da901fc-06e3-370d-bdec-812db3f1937b | -12.84102 | -52.95768 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b86c3b9-5995-3e16-a75d-ca1ea5deb2e7 | -15.25198 | -53.76932 | 2025-09-11 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56a7c30e-c827-37a8-a788-aabdac1a47e7 | -14.39843 | -47.31242 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0bac60d0-c5ef-3215-98f2-832759f11c56 | -9.68391 | -46.78018 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a25e247-210a-3acb-91ef-f8966fb296e1 | -12.06623 | -64.17843 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61618c17-e09f-3e66-bfab-3120605070be | -12.97309 | -48.04244 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b099bb9f-6369-3545-979e-da0431993232 | -10.56861 | -51.49762 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19e6bc36-98de-368f-9c88-52f6440737e2 | -11.47698 | -49.263 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb488810-a73d-3276-8f3a-35d9643ffd94 | -9.70082 | -43.5389 | 2025-09-11 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf57b9ea-439a-300b-80ef-54accaaa78ad | -15.89335 | -48.17971 | 2025-09-11 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c7493f0-194d-3c80-88a1-600918b7598c | -9.29215 | -48.42233 | 2025-09-11 04:46:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| def53bb3-0cfe-33ad-a99f-83d22df2d702 | -9.077 | -50.48077 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f24f269f-b621-3426-a4f3-87d90d2445b6 | -11.13795 | -52.04541 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10a10466-334e-3dd1-b15d-4e1557b9e17a | -14.90807 | -55.87621 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d10843d6-9b80-3ded-bfec-272bcf173db9 | -10.00789 | -51.71655 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e6d5f07-6dc1-3520-95ec-84353e4b52c7 | -12.85654 | -52.94574 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9df3b471-fac9-31e9-b1be-b3d4fa99fdea | -12.04635 | -47.61008 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f39e88e-ef03-3ade-8edb-59508127e046 | -9.91983 | -49.87081 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59955668-8291-3d3f-8942-b62d547a7015 | -11.88198 | -58.80968 | 2025-09-11 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f4fa1c8-41c2-355a-bec8-abb2eeb26b1e | -13.85743 | -47.36179 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 375e184f-395d-38e6-ad53-74bf28615d28 | -10.33648 | -54.55027 | 2025-09-11 04:46:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7578b496-5e9b-303c-8a5b-0d56dea14ef4 | -9.97091 | -51.69275 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a39c8cc-35bf-3543-a0ca-b88b1703d855 | -11.48589 | -49.25186 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 039fd24a-7835-3a1c-a5a6-6962bc93aa6f | -10.13198 | -47.89276 | 2025-09-11 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19c6dd04-b1ec-3007-b9eb-3e45d6302a49 | -15.14403 | -52.45385 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a38e2b3-64ef-388b-aae3-a272875ce556 | -11.1682 | -45.28969 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c36be459-8277-318f-9c5d-74143ab0a2f2 | -11.87283 | -58.81343 | 2025-09-11 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6935ae80-8fd7-3334-98c2-1776e6cc38ca | -12.07244 | -50.99158 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c837bb4b-ff11-3bd1-9e82-1c79274ac0e6 | -10.56058 | -43.667 | 2025-09-11 04:46:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 211a2b0f-bbb5-3cb7-a7ab-0961e92ec18e | -12.85587 | -47.96165 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cf5427ba-b59d-3d16-b019-bc88239d96ff | -12.47735 | -53.82542 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0efcb265-af7b-3afb-8012-1f1efbe9b844 | -11.38439 | -43.52557 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae75a1be-a937-379f-ab0f-74b471e4cb2e | -11.60314 | -52.21745 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1066dc6-0c3d-39c2-a38d-de2b510d71df | -15.12433 | -47.03278 | 2025-09-11 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7db6bab1-c9f8-3a67-9fb6-34c840e7a7a9 | -9.08258 | -50.4669 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc3b3dc9-98cd-3fe0-b857-cd818efa37da | -10.16344 | -46.17801 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a09a68eb-1b48-3521-a0cc-747289bbb020 | -9.34099 | -48.93896 | 2025-09-11 04:46:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa95cec4-62b1-3d3e-bd94-e30f2fe37f6b | -11.72698 | -50.62344 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 43b35c70-b7d8-3205-a803-01639b969baf | -12.96301 | -54.75862 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3d89753-6404-3ed3-a379-82956a23ae5e | -11.8812 | -58.81395 | 2025-09-11 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb7c32df-7897-300b-8693-16cdaed368c1 | -12.93237 | -54.79316 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11e29ab1-7ad0-3895-85ec-efc588dcaa59 | -11.46915 | -43.69626 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7718b04e-afc7-3ad4-a04b-e2f1249d0912 | -11.68629 | -46.90731 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0041760-a564-3daa-88af-598114ececd3 | -11.13188 | -52.01928 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8ea67bf-d081-33b3-8f0b-b2027f4d1d4a | -12.93259 | -54.81325 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca99ec30-954d-355c-83cb-7d38865b1f49 | -14.28491 | -54.74417 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 527b4011-4036-341c-be52-b6e427923c63 | -14.13505 | -45.39401 | 2025-09-11 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ad96336-6b77-372c-982a-3f6f26c44133 | -12.0329 | -47.61507 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f7ff12c-a6ab-31d0-9a7d-1a59025ce0b7 | -11.7801 | -50.57106 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2745c5f1-ed91-3954-806f-ccda02065866 | -11.45575 | -43.5997 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a46628d-2514-3d2e-ac40-f73e43e18b13 | -9.79875 | -61.51804 | 2025-09-11 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f50c0a1-a92a-3cd7-8960-15fb73698f7b | -12.40634 | -63.81416 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c56c0c79-38fa-320b-80d8-07bf013491c6 | -11.4774 | -43.63321 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7715d238-38b2-36a4-baf1-2f02a5cba6c6 | -9.72201 | -43.53291 | 2025-09-11 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 407cdffa-2145-32fc-997e-c1bbe68012e9 | -15.10841 | -50.09929 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8eecbc10-4232-30c2-9753-0202c48e6deb | -12.92265 | -54.78749 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38055a84-dd8d-3247-9d72-c3d6564c2a3e | -15.14432 | -48.61383 | 2025-09-11 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f79a12da-9b19-383a-a31f-a515986bb966 | -11.94297 | -46.64529 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93e6f004-6d54-3cb2-9405-52d53b844e8d | -15.1324 | -52.44091 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5fab95e5-8208-393c-a277-d206434631ef | -11.15892 | -52.04161 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0ea5d40-b251-36b2-9f8d-674bf2626edf | -14.89463 | -55.84819 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b006a70f-37da-3f58-8cc9-c1d347be6f01 | -11.44788 | -43.57992 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9342d95a-adde-3521-a407-b31af720365b | -11.19407 | -55.06227 | 2025-09-11 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 973eeec5-19b1-3575-b247-d86789e66430 | -10.67019 | -48.62156 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cd32010-a08e-3567-80cb-5a0d384fba73 | -10.54099 | -51.52208 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e911a24a-839a-317c-875d-0e58c39ecf52 | -10.5631 | -51.51114 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b050305c-32dc-365b-bb08-7456fcfa0f0b | -15.13517 | -52.42298 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b29493d1-56c8-30d9-8be0-94535be97d53 | -12.86041 | -52.94274 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14986e1f-353f-34b0-81d0-927a3e7e4922 | -11.50335 | -50.38782 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e77dcbb-6025-38a9-877e-5b6aff6ca977 | -14.88586 | -55.83958 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a090b209-043b-3f0b-88ed-e88864e02be5 | -10.89499 | -47.7711 | 2025-09-11 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d51e467f-9377-3a2a-9215-e1053a233e51 | -8.89927 | -51.05714 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01c6fe9e-8291-3f33-8c08-4c38d9d653ec | -12.47145 | -47.48792 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 960f8267-85de-39a7-bf72-4cce2b9459c8 | -9.88716 | -51.87965 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0f1cb5a-8a4a-3c5d-b344-4d9519e19389 | -13.65452 | -45.7199 | 2025-09-11 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96881cdd-8962-35e6-abac-882ef3abf3de | -14.37106 | -47.29578 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| af506d7e-fc17-3653-a29f-fd89f9acf9bb | -15.67613 | -47.02411 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 27a3b173-5f20-3ab7-9b24-6db3140e890b | -9.01661 | -49.50536 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 014fc24a-97b6-3816-b357-d3f9438a914a | -11.47935 | -49.24664 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73445810-9b76-37d9-8c3a-63066fbe5912 | -9.29961 | -46.76342 | 2025-09-11 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5774ff1f-9925-3461-8c46-4c74d4cbfcb7 | -11.4656 | -43.60402 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2b70ed3a-bf9e-3ec2-a98e-d1602b7eea3e | -11.15671 | -52.03407 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b927347b-bf6a-3d54-b8e4-b1fd1bff75e4 | -10.64586 | -48.63485 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f13ddefd-cc9f-3a55-b10c-b4b693e96a1e | -12.97411 | -46.72988 | 2025-09-11 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18bac17b-f85a-34d8-9930-cb7db77157c3 | -12.24653 | -46.7553 | 2025-09-11 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b6bdd9b-f5b2-3892-8261-338a4a359ff6 | -10.543 | -49.88989 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74958552-3fe1-3f22-9148-b17ef844922c | -9.09169 | -49.81621 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24612fd9-f9c9-374c-a0e0-2743b908a162 | -15.22753 | -44.04205 | 2025-09-11 04:46:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README103.md)
