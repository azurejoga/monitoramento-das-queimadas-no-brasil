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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13ee9195-8aee-3f0b-a056-a016a55bd26f | -15.49722 | -53.89704 | 2026-08-21 04:49:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c3434fc-a481-3fbc-a3ee-d5a51d8349db | -12.74141 | -48.47246 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7140f5c3-e608-3a09-b309-69ef815fc102 | -12.44018 | -43.4045 | 2026-08-21 04:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78e6a58e-472b-300e-b410-f18a8560150b | -12.7499 | -48.46606 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bd64461-db13-3c00-971a-f9a86a672252 | -13.24881 | -51.6321 | 2026-08-21 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12904b9f-684d-326c-a8e0-46a883d86eba | -15.4431 | -41.38829 | 2026-08-21 04:49:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 853933d8-771b-3ac4-8585-b3450e5735af | -16.73133 | -49.27295 | 2026-08-21 04:49:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9774604a-6814-3a18-a37e-296b3199bd89 | -13.37531 | -54.37978 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 1540de48-35bd-3788-9380-a4e15304a6ad | -11.1698 | -54.01146 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0a4405ed-0f4a-34ca-a770-7172612a132d | -14.07029 | -58.87495 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eacbc7fd-001e-3baa-b480-b3852b70905b | -15.00484 | -52.67655 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5fba0da-0019-3dd2-bada-eacee4aae3bb | -12.51021 | -54.75285 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 507c64d0-f883-3c77-8ed9-34b6fd1e9d13 | -11.1828 | -54.01744 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f278c814-9bd7-3be2-a3a2-e3dde33f7b05 | -12.50675 | -54.75229 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 237a4cb4-c112-360e-88e8-46f4954ee37a | -13.40937 | -54.36972 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60571dad-8697-37b7-9948-b72a03ba93fd | -12.79442 | -48.45205 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 292f3641-8254-3f50-9e4d-7ffeeaf3d530 | -12.44057 | -43.4012 | 2026-08-21 04:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbd8c4c5-1564-323d-8c38-b3b86c6a8790 | -13.15529 | -42.41122 | 2026-08-21 04:49:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 12db0685-3dd4-3a6b-aadd-3730050151f8 | -11.87344 | -51.6499 | 2026-08-21 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdb366d9-9d99-35f1-99e5-22a2f4f99677 | -11.20284 | -54.00167 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb48dbd5-1668-33fb-8d1b-25e35f6ec3ae | -17.94492 | -44.39636 | 2026-08-21 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d52eba29-ca0c-39fb-aa67-295c66c6a796 | -11.21644 | -54.00393 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 773218b4-54b6-354d-9b60-d76b143b99f1 | -13.67729 | -48.76825 | 2026-08-21 04:49:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| efa00526-ddaf-37a2-98d5-d14ed0012d58 | -13.25994 | -51.62648 | 2026-08-21 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97fec80c-c488-3521-991f-466623a498f7 | -15.16653 | -48.77882 | 2026-08-21 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 548d710b-2838-3e87-85bb-b27a15ce0e57 | -12.75027 | -48.46457 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26aec57c-29c3-386c-8425-44f32d083933 | -12.00985 | -53.43103 | 2026-08-21 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 477e58ea-1e35-35bd-8f4b-2cf02bbf072e | -15.06053 | -48.7058 | 2026-08-21 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 002e6cc9-c1f5-3e10-a41f-3436494f5729 | -14.21924 | -51.92498 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbfc53ea-66b1-3b1c-bd29-12daf7712ce0 | -15.16522 | -48.7884 | 2026-08-21 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1bc7b26-fc35-3813-a1cc-7233a92475d2 | -14.55465 | -52.99345 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84038705-a34f-3a84-9517-f8ed629ac052 | -13.63961 | -51.76334 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 778960b2-7e97-31ed-8dcd-903c330f22c8 | -12.51177 | -54.76498 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83096fb3-682f-3bae-b31c-1c6c5c8aac9b | -13.3986 | -54.37174 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 85b0f9b7-c75d-3db9-b075-3c0c820668e1 | -14.33122 | -51.9024 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 011372af-e11b-306c-a529-9be303b0ceb4 | -11.68438 | -54.56211 | 2026-08-21 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7362906-b638-3c1f-8ceb-205d9fdcefb0 | -14.99766 | -52.67903 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73bd01bd-5233-3a7a-b76e-b9939d31841c | -12.23959 | -43.17454 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9470e668-9229-328d-8679-d30a05847a73 | -14.57672 | -53.00435 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f64b6261-4d88-3985-9f8a-8172c5b501fa | -13.25214 | -51.63266 | 2026-08-21 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00f6505c-0183-3224-a7db-32a8c36b169f | -14.72618 | -47.14017 | 2026-08-21 04:49:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2af6e9f1-8191-3982-bf98-85153e635dea | -10.38834 | -61.21078 | 2026-08-21 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 704998b1-ee2a-3c7f-9b74-7bf6a578abbe | -13.38999 | -54.38179 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 69dad0cd-7195-3377-881a-c5e6d6d39b4c | -13.38383 | -54.37694 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| ea76cc70-12de-3f4f-8ea3-f601c4f38470 | -11.81552 | -56.59743 | 2026-08-21 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35abf083-dac7-3dc1-843c-b3dbeadb7339 | -12.51805 | -54.76997 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b390a2a7-12cf-3393-9109-16cfc78a619b | -12.26914 | -43.1557 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f9f9cd80-3fd6-3362-8910-3716c6ea0307 | -12.75194 | -48.47933 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 059d8605-6cc5-3158-b1d4-ebd8d447543e | -12.27207 | -43.15828 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 974321f7-e35d-3166-89be-56d57ec4a89d | -12.50562 | -47.84613 | 2026-08-21 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d656a08-c6ac-37d0-b556-f5a98375d9b2 | -15.7177 | -47.79652 | 2026-08-21 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 812d1894-a82e-34c9-84e8-677200b11f06 | -13.09903 | -51.58653 | 2026-08-21 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71fc54f4-4fcf-3f37-ae40-42aa2defe7ae | -14.45742 | -45.61509 | 2026-08-21 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eddb420a-d52d-32a3-afef-cce7b764b9ba | -18.12054 | -43.74123 | 2026-08-21 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11b1ae96-9d34-3419-a88f-1310bf54d795 | -15.22088 | -52.79612 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6620f6e0-152e-321a-ae15-206f7a51a31c | -16.72202 | -47.68951 | 2026-08-21 04:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cc478aa-1154-3ef8-9059-2c7130e5e8f4 | -15.01256 | -52.6705 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51ba85f0-9bbf-3c5f-8620-946d6bc72887 | -12.85083 | -48.43716 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b27c9941-6755-3597-93ab-196e3c8225d6 | -15.71258 | -47.80368 | 2026-08-21 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca4510a8-8500-375a-bd57-a92243c1575e | -12.25062 | -43.17326 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 33c4ca13-607b-35d7-af01-28a94a6debe9 | -11.18341 | -54.01372 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fccc3682-54af-3381-b884-6d0b1b688d19 | -14.56238 | -52.98743 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a553da5-540a-3e1b-8bcc-635fb64ea88d | -13.40598 | -54.36916 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3131ea0a-02df-3584-a5dd-b03422d1c58c | -12.74812 | -48.47897 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e15c0ef5-8d59-3c7c-892a-58589d466be6 | -10.40074 | -61.20274 | 2026-08-21 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61e06950-72d5-3b02-a17c-e0baf061b7e0 | -12.75408 | -48.46504 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| daa4c3b6-ab4a-38c0-b8af-4b4f5d58f24e | -13.09674 | -58.18633 | 2026-08-21 04:49:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea404e26-1171-36f3-a8fc-7f796a4a27f5 | -15.00152 | -52.67601 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6df62a96-6707-3113-b85f-f7437cf755b4 | -11.16396 | -54.0258 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fa77ddd7-c3d9-35dd-b30b-7e8f3facb889 | -12.72125 | -48.47815 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82a36257-0dd5-38c6-808b-92a6eeb88150 | -11.20964 | -54.00281 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbccb012-a642-336f-b8d7-eada89ceca91 | -13.10238 | -51.58706 | 2026-08-21 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b44c685-8127-34e1-ace7-02a7c17deeee | -11.22378 | -54.86941 | 2026-08-21 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a04989e-6360-36dc-9c74-42f30f928065 | -12.84048 | -48.4555 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f44bdcee-8bf3-3324-b792-dd3ce432160b | -11.17381 | -54.00831 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9f7e93f5-2b84-3513-9f56-a12d4eb645af | -14.45274 | -45.61451 | 2026-08-21 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 637d8aa0-bb05-395d-bfd5-e982af85f566 | -12.79082 | -48.39378 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2467a82f-8199-3ef5-9f4a-ae3c8258deef | -14.32398 | -51.90496 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c080e00-aff9-31cb-83a8-11c452d4d058 | -11.17478 | -54.02377 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d618be9d-b0f3-3dd3-8326-5227388c1023 | -12.50492 | -47.85114 | 2026-08-21 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9204bfdd-253c-30f1-b0f6-06405c5661b7 | -14.57892 | -53.012 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcab5aa9-000e-3854-9013-26fbf5b92236 | -13.43933 | -43.84166 | 2026-08-21 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f702a1a5-bed7-37d8-866b-0fec6b27eead | -14.03253 | -58.86872 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33b01cb3-ea07-3e7a-88be-44bc324b4c29 | -13.41249 | -54.3932 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15407a67-ee38-33ca-a738-cfa5b59481d3 | -12.86437 | -48.42391 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e528539-9bc3-3643-b8bf-ae56592bf1bd | -12.79058 | -48.45179 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 709e1883-2b8f-301d-8606-6da26ab9015e | -13.38783 | -54.37378 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 02c1e4d8-0be0-3160-833e-ae014954936e | -12.44134 | -43.4006 | 2026-08-21 04:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d4a289e-b7b6-3482-a780-9da3b31c9303 | -14.99489 | -52.67492 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9c23432-1384-38f4-8e47-75f804b4e3fa | -12.76461 | -48.47158 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4b7a5b3-a9b2-34c1-861a-5a70abbb4618 | -13.64296 | -51.76386 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47428745-8d1b-32c7-b10d-23e38850ce9b | -11.20068 | -55.0556 | 2026-08-21 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1eeee92f-e93c-32e5-a7f4-fe3d842405a5 | -12.51649 | -54.75785 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2114bde-f374-31ad-9b30-31393f64ed1f | -14.03645 | -58.86866 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0264482c-2bf0-353d-b46f-900a4c71acc9 | -14.28383 | -47.41887 | 2026-08-21 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a70b43b-76f2-3082-94a3-6bf5fb992abb | -13.39582 | -54.36747 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| abfaf84b-e055-36f4-ab11-f9bfab9480d0 | -14.56013 | -53.04535 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44054c95-7a0f-3f42-8f43-704630dc1e78 | -12.85147 | -48.43268 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e83906db-f9e7-3d27-8fd8-d5ad680abc94 | -13.44183 | -51.79176 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1efcf19e-08e1-3dfb-bd74-09eda911814b | -11.17199 | -54.01946 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README49.md)
