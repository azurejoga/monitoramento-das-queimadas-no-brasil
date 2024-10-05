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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ebd40d8-daed-3c85-90f7-edea69f72836 | -12.82262 | -50.55412 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c63c956b-bf8e-318e-93fd-2e14243e1a3b | -12.82154 | -50.55945 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 57ab32ad-b3f0-3e64-a46a-dc9bdf73da7e | -12.81154 | -50.55317 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ebdbe7e2-ac29-3cef-8d1c-beaeb659ceb2 | -12.81042 | -50.55849 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 35ba4db1-a1b8-3c44-b31e-482fb4103ce5 | -12.80993 | -50.5514 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ad719115-fa5a-390c-a14e-1c528843c40a | -12.80884 | -50.55673 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| fec79350-9204-3e25-971e-9e3efa4beda3 | -12.80776 | -50.56206 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 91fbabff-6e5e-3cd1-bb93-90743ff4e3e2 | -12.80519 | -50.55183 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 88f7f181-5fdb-3a13-8ba6-aff10086595e | -12.80407 | -50.55716 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 31544629-0895-36ec-94c3-ee32a9abf477 | -12.80358 | -50.55004 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8e08f29a-19da-31df-8c42-641af528f97c | -12.80294 | -50.56249 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 01f5f81b-5410-31dd-8aa2-21d01e7e89d1 | -12.80249 | -50.55537 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 2fcd0266-1e13-30d8-86e2-c797ed4c92a2 | -12.8014 | -50.5607 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8346a0cb-687d-3c8f-9429-4802873796f4 | -12.79771 | -50.55583 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18ee8505-edc4-38a9-a260-2acbd86a63a4 | -12.79659 | -50.56116 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b7dd5943-5e16-36f2-a33b-db03067d3d17 | -12.7891 | -50.56516 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ee877bbb-1c14-32ef-b413-30191273f4bc | -12.78761 | -50.56332 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c4d2f6b5-596b-3d6f-b90d-b411b44f4f54 | -12.78727 | -50.54253 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| d41f241b-2d4b-3426-ac61-21e1033c0fcd | -12.78614 | -50.54785 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| e6b450c9-464a-3a03-8e1b-292a428a494a | -12.78501 | -50.55317 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 3c5d5fba-d4eb-38a3-b50d-0441397dcba4 | -12.78454 | -50.54598 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| d3cd0aae-877f-32be-8772-f26d6963817e | -12.78345 | -50.55131 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| d0d5f6d4-ad5b-3329-9748-edddd20ccd88 | -12.78275 | -50.56382 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| addaad85-a110-3549-ac93-79c74bc75ce6 | -12.78235 | -50.55663 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c81e49bd-2b15-35f1-b392-bfe291d94111 | -12.78126 | -50.56197 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| bd583d8a-126d-3381-bb76-abc28bf2794d | -12.78092 | -50.54121 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| d683d552-8d9a-342b-b9d2-474a37979e35 | -12.77979 | -50.54654 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 231ed6f5-6eeb-3957-85a1-e67e9e8d5277 | -12.77866 | -50.55185 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| b3b157fe-c3d1-32b2-a2cb-58f2b1fecae5 | -12.77819 | -50.54465 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 53c8880f-452a-3738-b71e-a594902bbac3 | -12.77752 | -50.55717 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 85c0657b-5395-34f3-b7b5-d7bd60689759 | -12.77709 | -50.54997 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| cc41d314-fa35-309b-8d49-c40a2c566f79 | -12.77639 | -50.56249 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 94be9813-95f0-3e59-9026-29506a5fa10a | -12.776 | -50.55528 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 49936c10-57f2-33c7-b525-ffd95225d2aa | -12.7749 | -50.56061 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6a685b1a-19df-3610-ba4c-369d74f3e4f8 | -12.7738 | -50.56595 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c2209d52-02f1-372e-aa45-49505e9544d2 | -12.7727 | -50.57131 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0750e553-b331-3372-9cbe-33402af8ad8d | -12.77074 | -50.54863 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| fb978abc-2bba-337b-a3b1-d16d0c3ca20d | -12.76964 | -50.55395 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 3e44c8cb-76c2-3de7-8912-163a8f9f4147 | -12.76855 | -50.55927 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2b3b1875-c9d6-3561-90fe-43a3b768498d | -12.76745 | -50.5646 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 433684d8-40a7-389b-8785-2728a5394831 | -12.76634 | -50.56995 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 89f11091-9038-318c-8ca6-dbd989e9a7bc | -12.76219 | -50.55793 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 81aba8ba-afb9-383a-9a0b-8577698cc05b | -12.76109 | -50.56325 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 06703fa6-71ef-3076-a480-567d5d7f2333 | -12.75999 | -50.56857 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 161ba341-0f80-35e2-a86e-bac0c9f71942 | -12.37235 | -50.97771 | 2024-10-05 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21fbd7af-f43d-3cad-95b1-ef8e97a5eff4 | -16.1285 | -50.44788 | 2024-10-05 03:51:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2b8a52a5-53b8-3d12-b8a7-60b6d9a7ad19 | -16.12743 | -50.45287 | 2024-10-05 03:51:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 310c8c21-7624-380d-a633-164815a5924c | -16.10561 | -50.46739 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 845cbadd-3d33-30a7-a1bb-f0713f0f1785 | -16.09967 | -50.466 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e9646b2-cec7-365b-9913-e169140ea9cb | -16.09369 | -50.46483 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9ff91473-93c5-3745-aa51-7aad42ac734a | -16.08912 | -50.44456 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 606cce00-96fc-3b32-92da-da85fda5d3b9 | -16.08791 | -50.45037 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19f54f69-2ac0-337e-a953-4985107d759f | -16.08679 | -50.45572 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 037f98aa-82a0-3dc1-8c33-fd69a3e71321 | -16.08613 | -50.44218 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6ebd8aa0-50ae-3664-9447-82861ca1aa3b | -16.08494 | -50.44767 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b303a09-ead5-3652-971f-1cac70be22f3 | -16.08381 | -50.45287 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57340152-0a04-3ab4-8a25-e706d183b164 | -16.08293 | -50.44444 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a01c5670-212e-3d07-aa2d-9635e3508147 | -16.07886 | -50.44694 | 2024-10-05 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fae5f3e-aceb-3cae-988a-28c317d712c9 | -17.13254 | -51.72218 | 2024-10-05 03:51:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 41.6 |
| a3a948d9-b51a-35d4-8cd3-29d0764a835d | -17.13131 | -51.72765 | 2024-10-05 03:51:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 9d269b47-593e-3ff7-bb3c-2d753f6153d1 | -17.13008 | -51.73311 | 2024-10-05 03:51:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 54418eb2-d4d0-3b0b-83b5-b99f579e0059 | -17.12887 | -51.73848 | 2024-10-05 03:51:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ead897c4-edac-308e-b149-b5901feac2b4 | -17.12628 | -51.72061 | 2024-10-05 03:51:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 41.6 |
| c12774ea-3747-3e92-98ca-96cdeb092c09 | -17.12503 | -51.72618 | 2024-10-05 03:51:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| cc7ec64a-37a0-3d0e-8187-57a4c96ca25f | -17.12381 | -51.73162 | 2024-10-05 03:51:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 764d6c0f-99f6-3aa6-b983-d5d5433264d5 | -17.12265 | -51.73674 | 2024-10-05 03:51:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cb9dda7d-4470-3bc4-bdc7-f91e92123e2a | -12.93408 | -51.46567 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc1214f3-426d-39ab-900d-4ad089ca3438 | -12.93278 | -51.4717 | 2024-10-05 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 116d64db-1d70-315b-9f01-9d2716e80759 | -18.78456 | -52.63341 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eb121d8b-472c-3e35-83f2-89533478106e | -18.50464 | -52.84307 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1a4959c5-3ac0-37b9-a0c8-12ae7c2a32dc | -18.50325 | -52.84903 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 703e1cf6-6897-3907-9b8e-36afc0ba5ba6 | -18.50026 | -52.77892 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d312e609-afeb-3103-bbbe-c6e8c9361fe9 | -18.5002 | -52.77412 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d037d37-ea82-388e-8ec4-c900f7d8b6e5 | -18.49883 | -52.77995 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d504f7cd-26f6-32d4-87b6-add9f5701efc | -18.49673 | -52.84748 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b38c20fc-07b1-3998-960d-fd6290f068de | -18.49535 | -52.85335 | 2024-10-05 03:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 28e3440a-ef5a-37ae-8df1-29b840729586 | -18.49397 | -52.8592 | 2024-10-05 03:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7f3464e4-fe73-36bf-a311-94334f75213f | -18.49378 | -52.77731 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32b65fe0-444e-33ae-a784-a0f14acbad76 | -18.49244 | -52.78318 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 29bd5d69-8666-3432-bd3f-52ad9b8fa60c | -18.49236 | -52.77829 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 41434195-8dc4-3450-83c2-a2ac98da0324 | -18.49097 | -52.78417 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce38a698-20f8-3d94-a369-05fd72e029f8 | -18.49074 | -52.85078 | 2024-10-05 03:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5dc6f1d3-8445-390e-b3cb-f52e4c2dc399 | -18.48941 | -52.85664 | 2024-10-05 03:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| caf9370f-3708-3a45-bf56-2fa0253d8926 | -18.48753 | -52.85732 | 2024-10-05 03:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1111bc4f-0bcb-3733-8309-3a73a1199a53 | -18.88588 | -54.48611 | 2024-10-05 03:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eaa36fad-304d-3485-8671-745543c60102 | -18.88018 | -54.47881 | 2024-10-05 03:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 12452c69-c65c-38f9-b519-259c78ea1f4a | -18.8785 | -54.48566 | 2024-10-05 03:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2af74ecb-1fbf-3273-97be-38d03561ba81 | -18.85863 | -54.52175 | 2024-10-05 03:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 541d5123-4124-3144-a5c1-95d508fd3bf9 | -18.85688 | -54.52906 | 2024-10-05 03:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0ce937ca-b5bd-30e0-9817-9f9055d36d25 | -18.85321 | -54.52756 | 2024-10-05 03:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 98ed35d3-7fe6-3e1e-8a01-0c1703dd5559 | -18.85246 | -54.46971 | 2024-10-05 03:51:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a0427a0-c3af-326b-abf8-1ebd004f5e52 | -18.85076 | -54.47659 | 2024-10-05 03:51:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d33e5ce6-9f44-3e99-8ee1-a0a1c17b851f | -20.48334 | -42.36095 | 2024-10-05 03:51:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 11b7e1bc-2b61-3fc7-92d3-cf1c076b8ee1 | -20.47991 | -42.36026 | 2024-10-05 03:51:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 624b5c3b-5bec-3cfd-9fdc-773424dc0936 | -20.64632 | -44.80099 | 2024-10-05 03:51:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 981596aa-a38c-33d0-8d9e-ddc5e1bb1852 | -19.71308 | -43.24918 | 2024-10-05 03:51:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7f5e8aa6-dfd8-3d4b-8dd5-d5a0c7935127 | -19.70946 | -43.24856 | 2024-10-05 03:51:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5d2a81f3-7d16-328a-839c-0a54411fd78b | -19.67136 | -43.2324 | 2024-10-05 03:51:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3aa16bc-baa8-3782-8c7b-e0353dd5b7af | -14.04535 | -45.18071 | 2024-10-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 3c61d7c7-5b9e-3176-85a0-eb06c334ed26 | -14.04454 | -45.18514 | 2024-10-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |


[Clique aqui para ver as próximas entradas](README50.md)
