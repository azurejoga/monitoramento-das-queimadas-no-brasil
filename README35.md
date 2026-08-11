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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5f7a09b-b717-33f4-ac1c-fb8cc1a6b468 | -9.3714 | -47.5119 | 2026-08-11 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| d26c947a-c04f-312a-bfb7-c2a8f8dd2650 | -13.5498 | -46.3074 | 2026-08-11 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 270.4 |
| e4674a44-ad70-3de3-ac4a-7cec5560ca9d | -15.0736 | -52.7309 | 2026-08-11 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 4d281396-b3bd-3696-921a-564d0bbe30d2 | -10.1084 | -46.2018 | 2026-08-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 8490e6b8-ca98-3920-9ca7-7f34952db162 | -11.0294 | -45.6536 | 2026-08-11 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 268.5 |
| b94a168d-5717-39b0-8614-bbdd31dc1e79 | -14.2877 | -45.2835 | 2026-08-11 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 18d32eec-4bb3-3cd8-9ebb-3fa48c2a8533 | -11.7905 | -51.84 | 2026-08-11 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 379.9 |
| bb608633-f5c4-3424-a0e1-e0d033586a75 | -9.3717 | -47.4897 | 2026-08-11 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 195.9 |
| b20e4de9-77bd-3213-bd24-503ef2facc1f | -14.351 | -52.0412 | 2026-08-11 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| d34a12e2-9e9c-353b-b5b5-dfb1335ce81a | -10.2271 | -45.8708 | 2026-08-11 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 880.3 |
| d43e3dac-e100-323d-bb83-70aebf333bd3 | -13.8211 | -53.8931 | 2026-08-11 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 150.5 |
| bb6d5cb1-5997-329b-90f7-279dca3536de | -10.2458 | -45.8912 | 2026-08-11 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 8ec91719-e948-3e51-92db-a7cd204af42c | -11.7908 | -51.8189 | 2026-08-11 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 186.9 |
| c542ec89-b747-3d43-bf81-cccd8b691c7d | -10.8259 | -50.3315 | 2026-08-11 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| ff6ec3bb-5091-3327-92d5-98d97da1f347 | -17.9949 | -44.3787 | 2026-08-11 14:30:00 | GOES-19 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| faec450d-f3b1-35b2-94c7-8053786a2e2a | -11.0107 | -45.6333 | 2026-08-11 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 277.7 |
| 5d964847-489b-3822-a83f-739003caab15 | -11.8669 | -48.0791 | 2026-08-11 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 9edfe07f-73f9-3ca4-bde8-729819a975c2 | -8.9596 | -60.5934 | 2026-08-11 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 1268807d-8b16-31a6-9771-988d2c9761fc | -13.84 | -53.9117 | 2026-08-11 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 1491ebd8-cf31-391f-a3f7-67ba07d8293a | -10.2462 | -45.8684 | 2026-08-11 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 171.5 |
| fdc22a73-37af-33dd-adbd-9d7838425df5 | -13.8403 | -53.8909 | 2026-08-11 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |


