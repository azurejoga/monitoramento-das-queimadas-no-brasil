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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f84105ac-3452-3f0c-badb-54cf5d5cbb3a | -17.88714 | -55.25407 | 2026-05-02 12:04:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.0 |
| 17cb89a4-f68f-3254-9b44-bf750c1c5047 | -20.1989 | -46.45562 | 2026-05-02 12:04:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 781d7768-3be4-320b-a009-2b68c824790f | -19.61711 | -47.62851 | 2026-05-02 12:04:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| aed2a439-789e-378f-aec8-83eb2c8c1c35 | -19.43436 | -46.89286 | 2026-05-02 12:04:00 | TERRA_M-T | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 51af04b1-7567-3128-9fb8-2b441b42df2c | -17.88395 | -55.25947 | 2026-05-02 12:04:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 3f637340-fe3c-3117-ad62-dde8991eea37 | -12.3696 | -50.0459 | 2026-05-02 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 75c02e12-d309-38e9-a327-a808a52b338a | -12.3696 | -50.0459 | 2026-05-02 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 8f7a637a-1df2-3a34-8614-f0f63402646e | -12.3887 | -50.0435 | 2026-05-02 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 4e7ee0ad-7c0c-3a9a-8da1-1d62099858d5 | -12.3696 | -50.0459 | 2026-05-02 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 8eb3ded3-ec46-32cf-8bdf-8fe20b337193 | -12.3696 | -50.0459 | 2026-05-02 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| ff14519b-06f5-3ed6-bd2b-c85c44230b6f | -10.9815 | -45.0874 | 2026-05-02 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 4b7f8df8-1fbb-3f75-980d-f93d364852f5 | -12.3887 | -50.0435 | 2026-05-02 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| eb58b301-e529-3b70-955f-7af41190f1ff | -12.3696 | -50.0459 | 2026-05-02 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| a7150b64-c202-3aef-8caf-70a4c53611a5 | -12.3887 | -50.0435 | 2026-05-02 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 871bb552-97a5-324b-b789-c2cd25666339 | -12.3696 | -50.0459 | 2026-05-02 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| e1a28ce8-45e6-36b9-bffb-fb09ac63da20 | -10.9815 | -45.0874 | 2026-05-02 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 84afbb82-170b-338d-8912-739d5f06f4c1 | -18.0062 | -52.9861 | 2026-05-02 13:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| a764a5f7-2fe9-3d1c-9adc-b5ae0b590948 | -12.3696 | -50.0459 | 2026-05-02 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 6d6e4db6-0749-359e-ac76-8c53584830e0 | -12.3887 | -50.0435 | 2026-05-02 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e913c57f-7fd7-3ec0-ace2-5120adefad82 | -10.9815 | -45.0874 | 2026-05-02 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| a5f78bbf-45f1-34bd-891d-96b2120f1aa1 | -10.7136 | -46.3526 | 2026-05-02 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| abf1fb8c-5fa7-3291-bfe2-5379997b9e06 | -10.9815 | -45.0874 | 2026-05-02 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 1f877c85-1175-355a-b9a4-dc24246e87cd | -10.7136 | -46.3526 | 2026-05-02 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 8240aba0-04e1-392e-b6a9-fff0f3392b4f | -12.3696 | -50.0459 | 2026-05-02 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| d23cf6ce-b055-394a-a020-6915bfc6ee1b | -12.3887 | -50.0435 | 2026-05-02 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 01304bc0-24a8-3d04-bc45-f1d67e0c1850 | -18.0261 | -52.9829 | 2026-05-02 14:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| fe639e92-3830-349d-844c-3997e9b8c405 | -12.3887 | -50.0435 | 2026-05-02 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| d4890452-f8b0-3223-83da-538433da759f | -10.7136 | -46.3526 | 2026-05-02 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 88000c98-ceab-34ce-a9ac-ac523603056d | -18.0062 | -52.9861 | 2026-05-02 14:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 3bf9ae61-b328-3aa1-9926-65360c5cc7de | -12.3696 | -50.0459 | 2026-05-02 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| bfba7ed6-1b55-3bcc-992d-8bc8671a5421 | -12.3887 | -50.0435 | 2026-05-02 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| e730c3e2-f84f-3acb-98b2-ab22c7fe4351 | -12.3696 | -50.0459 | 2026-05-02 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 2e35d961-a254-32c8-ab33-e6e5476319b2 | -18.0062 | -52.9861 | 2026-05-02 14:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 8e649b20-f16b-3d8a-b681-5f169cf6b41f | -18.0261 | -52.9829 | 2026-05-02 14:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 05f9efd4-e9a9-31f9-9da1-8a22a3bcb337 | -10.7136 | -46.3526 | 2026-05-02 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 154.7 |
| fd23fc72-830e-3f7e-b7e6-e2b8b13236f5 | -12.3696 | -50.0459 | 2026-05-02 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 9c13d5cb-67d6-3621-be45-2a43019aba07 | -18.0062 | -52.9861 | 2026-05-02 14:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 4ff089f4-1d55-3767-a299-2b4b57297552 | -18.0261 | -52.9829 | 2026-05-02 14:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 9ef9e010-1cd1-39a5-bb17-8f7be19d0ed4 | -12.3887 | -50.0435 | 2026-05-02 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 284bfda8-2607-3015-84fe-27984c7a9c97 | -12.3887 | -50.0435 | 2026-05-02 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b27cd5ac-0cdc-33b8-a59b-aa1af378ab23 | -12.3696 | -50.0459 | 2026-05-02 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d59f3391-5352-3a76-afe6-c29447cf5aab | -10.7136 | -46.3526 | 2026-05-02 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |


