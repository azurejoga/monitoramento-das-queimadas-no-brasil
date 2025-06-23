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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94021cfb-c4c0-3329-8255-ae7db93df8dd | -11.18503 | -54.40668 | 2025-06-23 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aeedb450-d684-3697-b975-3bd219f37045 | -12.25188 | -46.68587 | 2025-06-23 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e9a5fdca-76da-3d76-9080-421195d601a9 | -13.36026 | -53.24623 | 2025-06-23 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 37c77597-a741-3aa4-82ce-8c70a2ce12c7 | -10.29179 | -52.5653 | 2025-06-23 04:46:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 696f5eff-4de5-3467-8df9-a3ef0a386137 | -10.89388 | -56.46189 | 2025-06-23 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 383b35d6-3fc8-32b3-a44c-031029736449 | -13.02601 | -42.67376 | 2025-06-23 04:46:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ceb446fc-753f-314e-a566-4cd826179f21 | -10.29567 | -52.56231 | 2025-06-23 04:46:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b44223a6-4c9c-327f-8012-79433352e377 | -12.19869 | -49.62774 | 2025-06-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b214ce8-ba44-3e88-80ce-72e30f34585d | -11.61229 | -58.29864 | 2025-06-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd120c28-7491-3e7b-aa4e-610127bc9f99 | -10.94834 | -48.22647 | 2025-06-23 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2120db4-4abc-3e0d-94fb-0c949cf57ab4 | -17.3911 | -42.6302 | 2025-06-23 04:46:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 65ea5c80-927b-3bdc-81e8-827a766cc57d | -16.98359 | -50.24714 | 2025-06-23 04:46:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdf4e5ab-1861-351e-8687-53e1874cc017 | -11.58404 | -44.64888 | 2025-06-23 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4100be6-56e2-3d4b-902e-e47c481060c6 | -11.18158 | -54.40608 | 2025-06-23 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd2dd7ed-8f9d-381b-b862-1783ab0b0938 | -11.61383 | -58.28063 | 2025-06-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee2faef9-ac0e-32d3-8935-21673f9ca643 | -13.26652 | -46.82333 | 2025-06-23 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 849550c4-9853-3c4e-86b7-af7e381d3ed8 | -12.19928 | -49.6237 | 2025-06-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02451dbc-833e-35d7-a656-2267946dff60 | -10.68086 | -56.55193 | 2025-06-23 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 604316b5-4f1e-3765-abf9-920ca9c17489 | -11.61442 | -58.28639 | 2025-06-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1523cb56-0474-36f8-a11c-6191917e007c | -10.8665 | -53.7576 | 2025-06-23 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf342803-a153-309f-91a0-3b5d90c6cd42 | -10.86589 | -53.7613 | 2025-06-23 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b351afe-0bed-3849-a242-a5f8d90ed0ec | -13.24091 | -49.83303 | 2025-06-23 04:46:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 60f3bb51-f1e4-3004-be36-6f8823837185 | -12.307 | -53.26634 | 2025-06-23 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef9b4e88-2e8f-35c0-ae9d-da6583595f82 | -11.61234 | -58.28881 | 2025-06-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8970b70a-f002-3540-8874-e3c7bee25d73 | -17.39653 | -42.6353 | 2025-06-23 04:46:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 081f1444-4711-3b32-a733-80fbe05adf46 | -13.27071 | -46.82413 | 2025-06-23 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2ba04e5-488a-394f-b4ab-f9de03a7892e | -17.39155 | -42.62584 | 2025-06-23 04:46:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5af237a8-156e-300b-a081-f08c3144b144 | -12.30367 | -53.26579 | 2025-06-23 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c72a246e-ae78-3a59-8de0-389ff575f2b7 | -11.61371 | -58.29049 | 2025-06-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20814a82-5e6c-3447-8e8e-750645c4a7f8 | -16.22105 | -49.97168 | 2025-06-23 04:46:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cf0cc19-2777-38d8-a822-8dc7ad59f9e9 | -11.62238 | -58.28211 | 2025-06-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70701281-ea87-31f6-aff9-1fb247570df4 | -11.57792 | -44.65866 | 2025-06-23 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e9918b76-c2b0-3281-a7ea-a4ae23e1d4ec | -11.5786 | -44.65345 | 2025-06-23 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed883cf6-21df-3f29-9943-f846e5a6a5c7 | -12.19575 | -49.62317 | 2025-06-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0903d5e4-b52c-31d9-a9bd-ae6537a1a396 | -10.5013 | -53.58487 | 2025-06-23 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24872d7c-1292-313a-8190-2c9ee7e82573 | -15.56756 | -47.85375 | 2025-06-23 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce135a6d-9250-376e-9fc7-c576124ee8c3 | -12.43757 | -44.75383 | 2025-06-23 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dcd30d0-ef55-3ca8-9aa2-597fb8ff9a3f | -16.22021 | -49.97338 | 2025-06-23 04:46:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3caf46e4-e3f1-3977-bc5b-d5ab652468b3 | -11.09924 | -46.66644 | 2025-06-23 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0cc8be3-c0c1-3ebf-9e0f-198f531376bc | -13.21393 | -53.26988 | 2025-06-23 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1612042b-a0fe-33c7-aa62-3b699e457cfb | -11.09976 | -46.66267 | 2025-06-23 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffcc3535-acf2-3105-a3bf-507831612ca3 | -11.10439 | -46.65968 | 2025-06-23 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 08099f51-f282-3726-91f0-01fcc1fe99e9 | -11.61308 | -58.28473 | 2025-06-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ac1eb90-74b3-3c12-8ca8-84a718c07293 | -14.28883 | -52.06987 | 2025-06-23 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1ddb74d-8de2-3e8b-abb3-79738fbb0f12 | -13.83042 | -44.45788 | 2025-06-23 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11be1ba0-49cb-3865-b067-77eb7c08e108 | -17.39065 | -42.63454 | 2025-06-23 04:46:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1326cccc-6431-3333-87ac-8b3694b8bf61 | -11.13804 | -53.93995 | 2025-06-23 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1a2d51e6-815f-3d46-a51e-e9c653028a3c | -11.49952 | -48.07883 | 2025-06-23 04:46:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e41c0509-9739-3eb0-951b-ec60108f343f | -12.25072 | -46.68713 | 2025-06-23 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5d2ea86a-0c33-3333-859a-278810a9eb74 | -13.82378 | -49.30924 | 2025-06-23 04:46:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3d1910a-3751-36e3-b4d1-d14de5c23a5a | -13.82345 | -49.31222 | 2025-06-23 04:46:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbc91a4a-161b-3f8d-bfcf-9ab4440ed442 | -11.61514 | -58.28228 | 2025-06-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6883b7f9-d2dc-38b0-8794-f3bd18757a84 | -16.68253 | -43.88299 | 2025-06-23 04:46:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c43f6850-1d06-3e2e-b07a-0d59ae8e1693 | -13.66839 | -43.66518 | 2025-06-23 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84c56215-482e-36cf-8ec2-852a537bd899 | -11.61512 | -58.29773 | 2025-06-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5874d1ae-9dfd-3146-aca2-d28e4cde7165 | -10.57154 | -51.89301 | 2025-06-23 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68286e20-5ef4-3c01-a1fc-050bbf1415f1 | -11.61736 | -58.28546 | 2025-06-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32166c3f-3628-30f7-8a83-b6fece5d8357 | -13.24032 | -49.8371 | 2025-06-23 04:46:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f4d681ba-2166-3d2a-86e6-7566cf23264d | -13.2754 | -46.8212 | 2025-06-23 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78146a97-a7b1-3ca3-8ccc-1d21f368c773 | -17.39743 | -42.62661 | 2025-06-23 04:46:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce8e2dbe-07c2-3f5e-85fc-bbd0652847eb | -13.02556 | -42.67755 | 2025-06-23 04:46:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f33c6bfe-0858-3ae7-9eb0-2c07fabe19a8 | -13.08377 | -54.84565 | 2025-06-23 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 902d8cff-d2ce-3cb7-9d01-498b94991254 | -17.67084 | -46.75948 | 2025-06-23 04:46:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce5c8b7c-4b62-3b77-94d0-e19feba00d2e | -11.80659 | -56.9618 | 2025-06-23 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 606dc09c-2880-362d-ac78-ccf40ade1ce5 | -10.50588 | -53.57806 | 2025-06-23 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1be8daad-50b7-3f5a-a94e-ac8b30c2c87a | -11.10388 | -46.66334 | 2025-06-23 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b18c623-bc0b-3815-ae97-58369bfa6e57 | -11.50924 | -48.95717 | 2025-06-23 04:46:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b9be831-9e66-390d-b4fb-258435ef2c37 | -13.23737 | -49.8325 | 2025-06-23 04:46:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e35c95fa-ed1f-3eca-9a85-e7dc11c5a159 | -11.13487 | -53.91642 | 2025-06-23 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33a5d88c-d301-3400-b411-d4984a137ed6 | -11.31697 | -47.18229 | 2025-06-23 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c15b518-1ff8-35fd-baea-bde5aa09502d | -10.89305 | -56.46672 | 2025-06-23 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b9a96d0-9a68-3b69-82e9-bc0bfde5a9f9 | -10.50468 | -53.58542 | 2025-06-23 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 901d2583-8ecd-3c78-bb78-84f829aba4c0 | -11.61661 | -58.28957 | 2025-06-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1ca1c98-8b43-32ce-988f-e67e265bd553 | -15.07755 | -48.94598 | 2025-06-23 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4ca38f0-70dd-3036-8c4d-20da6fb72a5c | -16.6821 | -43.88694 | 2025-06-23 04:46:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d832233a-50e7-39a5-bf0b-01fe4797b0a0 | -11.13767 | -53.9207 | 2025-06-23 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3d446cd-be28-3d5e-90da-8e636989be2a | -11.10336 | -46.66713 | 2025-06-23 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c9ccf5f-5ced-3aba-b2b2-2c42bdbf2611 | -9.46006 | -56.05943 | 2025-06-23 04:46:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 908fc902-40f8-31ea-8964-af7e997806fc | -10.56823 | -51.89249 | 2025-06-23 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cbe3c32-3bad-3759-82e6-3d216381215e | -23.40721 | -46.55581 | 2025-06-23 04:49:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a8278111-c76c-31b9-8e97-8089d0fbca75 | -20.23245 | -46.17084 | 2025-06-23 04:49:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d5ea3f1-2a5f-31c3-ac78-e7c50596887b | -20.70593 | -50.06848 | 2025-06-23 04:49:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 365c6714-0c4f-3d52-b444-941ab24e6fda | -20.81265 | -55.73579 | 2025-06-23 04:49:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36cb08d1-ba30-35ae-80df-d435093fa61b | -19.23394 | -46.45947 | 2025-06-23 04:49:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcc53c02-a732-373d-a03f-229d8c24170f | -20.72518 | -49.43074 | 2025-06-23 04:49:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac447f22-6a99-30cd-b972-ccf4a3aea47b | -19.70033 | -54.61069 | 2025-06-23 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8f57a805-2962-3882-9ac8-cc7c09c7d276 | -22.53947 | -48.81424 | 2025-06-23 04:49:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aeb2e739-57b4-36e0-97cb-1ff248f45cfc | -21.39568 | -45.50719 | 2025-06-23 04:49:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2cc4f779-2f65-3b08-a548-388b12b0c7b0 | -23.59143 | -47.44045 | 2025-06-23 04:49:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cfbb18cd-26fb-3504-b3d3-e02678e5dc0c | -19.6937 | -54.60951 | 2025-06-23 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88a90e21-7590-32de-bc5d-da1f1bf03db4 | -19.51685 | -45.31459 | 2025-06-23 04:49:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53f1c55c-abd8-328e-a2c4-618ad11996f5 | -19.69701 | -54.6101 | 2025-06-23 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c75d7f35-4ce2-37f4-b944-a0c897987f76 | -21.44124 | -54.57988 | 2025-06-23 04:49:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 09456fcb-881f-37e8-b5bf-509a5d4912ba | -19.51145 | -45.31696 | 2025-06-23 04:49:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee33f8fb-7ea9-31c5-a816-31b9a858a7d8 | -20.23382 | -46.17055 | 2025-06-23 04:49:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 696c4763-54cb-35b9-a751-d6aa4751dd9c | -19.51178 | -45.31385 | 2025-06-23 04:49:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 692a8feb-cacb-38da-a2cc-fc28d37aa401 | -23.33804 | -46.77091 | 2025-06-23 04:49:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6a375a9f-e733-3c01-a573-db30967d7c72 | -19.70364 | -54.61129 | 2025-06-23 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa07fc9c-eb12-3ecf-acb2-7632d66179c6 | -22.25438 | -50.04047 | 2025-06-23 04:49:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 5de017f2-2395-3271-8ac4-64dc5f666dd8 | -19.2386 | -46.46033 | 2025-06-23 04:49:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README10.md)
