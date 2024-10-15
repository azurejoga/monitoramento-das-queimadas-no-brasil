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
| 3bb08337-3f4c-3b3a-8afa-501107df630d | -9.4295 | -46.0103 | 2024-10-15 14:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| ddb367a7-50bd-3f2e-a758-2b743f738f9e | -9.4481 | -46.0308 | 2024-10-15 14:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 5d0375f1-3136-3c7f-9958-ebcf8af0c75d | -9.4513 | -45.8044 | 2024-10-15 14:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 0a20def7-6968-367e-ac86-008cb95a554d | -9.4503 | -45.8724 | 2024-10-15 14:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 4ad698ed-3a10-38ea-8fa9-09aa5b7e3ce6 | -9.5915 | -46.5989 | 2024-10-15 14:46:00 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 258bbd56-d30e-37cb-ac3d-e71db2996175 | -9.5912 | -46.6213 | 2024-10-15 14:46:00 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 01f638e2-5330-306e-9ace-34e115d07b65 | -9.888 | -47.0342 | 2024-10-15 14:46:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 6eaf6c50-992b-32c6-be0d-8c6053417ac0 | -9.9484 | -48.1322 | 2024-10-15 14:46:02 | GOES-16 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 76b02830-4372-3df6-8c78-47e7066cd737 | -9.8883 | -47.0119 | 2024-10-15 14:46:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 145.2 |
| da31f234-5fb7-3df6-bc7a-80644d080597 | -9.9597 | -47.315 | 2024-10-15 14:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 167.4 |
| b14b0448-8fb3-3475-9ba2-a15b8ac679df | -9.9411 | -47.2949 | 2024-10-15 14:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 03a7c318-287b-3da9-b080-415162869e5b | -9.96 | -47.2928 | 2024-10-15 14:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 0d21f994-253e-39e2-9933-6e691fe1ed65 | -9.997 | -47.3551 | 2024-10-15 14:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 5e1af932-e25e-396d-8fb1-26a532b959c4 | -9.9784 | -47.335 | 2024-10-15 14:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 152.6 |
| e61af7df-3596-3967-9bd0-92380d20cb09 | -10.0365 | -47.2397 | 2024-10-15 14:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| f2d79ec2-8b46-3180-919d-2c854df03d5d | -10.0495 | -47.6589 | 2024-10-15 14:46:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 156.7 |
| aba27b5f-8962-389d-a5ac-8a0490e2ee5e | -10.0498 | -47.6368 | 2024-10-15 14:46:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 158.7 |
| c8d8b3fb-682b-3c52-83ff-3e64b5ce9c8a | -10.0305 | -47.6611 | 2024-10-15 14:46:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 149.2 |
| a55fcc36-f323-391f-a08f-4c9b3f1dec8f | -10.2641 | -47.2134 | 2024-10-15 14:46:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 154.6 |
| e3bb3554-91b9-3765-a179-3cf1cd58a8e9 | -10.6795 | -47.3419 | 2024-10-15 14:46:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| fc8981e6-aa4c-37b5-9c0a-57b58c7a0d86 | -10.9358 | -45.5521 | 2024-10-15 14:46:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 2a05bad9-ff7e-3b11-810a-0bf0103afbb9 | -11.2637 | -44.213 | 2024-10-15 14:46:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 79b3f520-170f-3f31-a12a-93c6de797b1c | -11.7561 | -44.513 | 2024-10-15 14:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |


