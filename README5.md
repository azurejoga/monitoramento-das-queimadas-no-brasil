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
| 0428f248-6bd5-37ec-bc93-bdbf84312d39 | -12.37 | -50.0242 | 2026-04-30 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| b7594107-6873-37ff-a7eb-028e29218512 | -10.9815 | -45.0874 | 2026-04-30 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a242407f-eff2-381c-81d8-e0e61125ddb7 | -12.3696 | -50.0459 | 2026-04-30 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| aef983b7-1107-353a-b020-364e5454f66e | -12.37 | -50.0242 | 2026-04-30 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| cc3159da-14fd-36ee-83cc-dd0e09e35ce7 | -10.9815 | -45.0874 | 2026-04-30 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 57c0bc11-d937-398c-a257-4f03f88db6ff | -12.3696 | -50.0459 | 2026-04-30 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 32973f65-366d-3850-9e65-d4f9dee3e909 | -9.4655 | -46.1415 | 2026-04-30 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 63d0a86e-fb22-3d21-aa44-81efd674c874 | -17.2478 | -47.0825 | 2026-04-30 14:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 10a00b03-f0f9-38e7-9a2e-12987669d79e | -12.37 | -50.0242 | 2026-04-30 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e2e310bb-8b3b-3bbd-b132-869dcb393979 | -12.37 | -50.0242 | 2026-04-30 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 4b1e803d-8cff-3d13-958a-e98e4a5a6939 | -9.4655 | -46.1415 | 2026-04-30 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 7b575c6b-ab9f-3d93-8821-14ca07031505 | -12.3696 | -50.0459 | 2026-04-30 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 4ccd94d3-f8b1-3219-9c85-c11777527b44 | -17.2478 | -47.0825 | 2026-04-30 14:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 111.8 |
| b99f025f-910c-3550-9696-6a3f4eb7089c | -17.2677 | -47.0785 | 2026-04-30 14:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 74.2 |
| bffc72c4-5f38-3bf2-af6a-1bcc9fd7d980 | -10.9815 | -45.0874 | 2026-04-30 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b09c6dc5-a602-3fdb-9e00-3a70d6feab8f | -17.2478 | -47.0825 | 2026-04-30 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 132.9 |
| ae3769ec-ee28-3fb1-8945-4118c95c1ab5 | -12.37 | -50.0242 | 2026-04-30 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 48407c64-0467-3095-9ec8-40f3867e7644 | -12.3696 | -50.0459 | 2026-04-30 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 2e12f519-110c-360c-924f-18747c017f9f | -10.9815 | -45.0874 | 2026-04-30 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 077ffbad-0b07-314a-bae2-24c40b923915 | -11.0006 | -45.0847 | 2026-04-30 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 88cd2e7a-b0ab-35c8-8b97-177a1c611e94 | -12.37 | -50.0242 | 2026-04-30 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| c6cc1f95-9e07-3dde-ada6-9f1997d840b4 | -12.3696 | -50.0459 | 2026-04-30 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| fd85e27f-4076-3100-9844-3d2765ed9542 | -17.2478 | -47.0825 | 2026-04-30 14:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 120.6 |
| bc7be9f5-58c6-3b65-aa61-735c6314b2a9 | -12.3696 | -50.0459 | 2026-04-30 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| be3fc0b2-f8ad-33ff-a7d5-1e8a12eaba68 | -10.9815 | -45.0874 | 2026-04-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| e55327fc-f6c5-3270-a0b9-7ec21493c8e6 | -17.2478 | -47.0825 | 2026-04-30 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 2eab0d10-f55b-3002-b460-d420945db060 | -12.37 | -50.0242 | 2026-04-30 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 3e21f5e5-81b9-34c5-8d86-8fab212a6456 | -11.0006 | -45.0847 | 2026-04-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| af41234f-8360-3d3a-b8d2-abe00291f1e0 | -10.8364 | -49.5788 | 2026-04-30 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| e430227d-9d73-31b0-8b0e-df0303bf85c9 | -10.9624 | -45.09 | 2026-04-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 642924b8-00e9-3102-b5db-748d8c6f3d6b | -11.0006 | -45.0847 | 2026-04-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 7cb8937c-91dd-3896-aaec-1d6568b297b6 | -12.3696 | -50.0459 | 2026-04-30 14:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 00d614f6-ca5d-3099-a1df-3debfd62ae72 | -12.37 | -50.0242 | 2026-04-30 14:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 98928f57-d5eb-3301-89b0-277f8c4582e6 | -10.8364 | -49.5788 | 2026-04-30 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| ab6dd6e9-4bb9-3c7c-8f38-6fec63e3f905 | -12.37 | -50.0242 | 2026-04-30 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a7a75e8c-d3b9-3180-b3a7-b73e93ee0c7c | -10.9815 | -45.0874 | 2026-04-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 5540863f-0da8-3d74-8f5d-ee8e36377222 | -10.9624 | -45.09 | 2026-04-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 9bd42ee5-3f18-3c93-9689-edd4671f2881 | -10.9624 | -45.09 | 2026-04-30 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| ced7d679-fcf3-318d-a7d3-75aec4a72edc | -12.37 | -50.0242 | 2026-04-30 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| a0ac9d0c-08ea-3e01-850a-f4e3ed9f00f6 | -11.0006 | -45.0847 | 2026-04-30 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1512c908-c78a-3268-89bb-ff99fe4f2e79 | -10.9815 | -45.0874 | 2026-04-30 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 719ed5e5-4d0a-3ffb-a839-0a5e4bc01a17 | -11.0006 | -45.0847 | 2026-04-30 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |


