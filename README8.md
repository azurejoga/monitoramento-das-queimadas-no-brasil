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
| 33755d17-4d0d-357f-a3f0-1ebc777eb666 | -12.4651 | -58.5009 | 2026-06-28 02:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 458cffb9-e9a5-3a8f-be09-8a7ebe574cb7 | -11.2279 | -54.3036 | 2026-06-28 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| ee09e622-6cc1-3cdb-958a-bde885c3e3ba | -9.0796 | -59.4098 | 2026-06-28 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 5bd27e3c-5256-3324-b248-0bb2b148718a | -11.5243 | -54.7872 | 2026-06-28 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2052a099-e0ad-3e7e-92ab-6ad2f583da67 | -10.2942 | -57.1182 | 2026-06-28 02:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 83823b23-1c49-3ab2-bcc7-49ae5939d2a6 | -12.6048 | -57.8743 | 2026-06-28 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 59521179-0cf2-3894-9d61-567e709bbf12 | -10.2941 | -57.138 | 2026-06-28 02:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b11530e4-9969-3240-8549-a3a1f00a7a74 | -10.313 | -57.1169 | 2026-06-28 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| aa97062b-e21a-3324-93ad-d3cd22b3205d | -11.2088 | -54.3258 | 2026-06-28 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| fc8287f2-a711-391d-ba1c-feaa62fc0488 | -12.4654 | -58.481 | 2026-06-28 02:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 00f32aef-7013-3364-8330-c48c3769f6d5 | -9.4761 | -40.3862 | 2026-06-28 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 3b6cd16d-2bff-3c13-996a-b68906291315 | -11.209 | -54.3053 | 2026-06-28 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 186.8 |
| f872fb65-b8b6-32b9-9896-fd040bdc7fb8 | -17.3041 | -42.643 | 2026-06-28 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 73.6 |
| d6e65b86-d1b8-33e9-b75b-8ffc970d628f | -12.6046 | -57.8942 | 2026-06-28 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 76a04f79-a97b-38c3-9277-b7d217a09b2c | -10.3128 | -57.1367 | 2026-06-28 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3fd941b8-a354-373a-bf69-cd43d4835dfb | -11.6657 | -57.2536 | 2026-06-28 02:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 4208d88f-5c31-3086-89d0-b249d95c6df4 | -18.4795 | -54.1105 | 2026-06-28 02:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 03af722d-35b4-373d-b460-00dee610f15e | -12.1775 | -57.1319 | 2026-06-28 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1ebba64c-464d-38f4-9372-84ce3d2d1566 | -17.3034 | -42.6678 | 2026-06-28 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| df22c55f-0c09-3544-8520-b6f1b7ed7471 | -12.1773 | -57.1519 | 2026-06-28 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 0d1c60f2-cb28-3610-9478-5b2dc9905944 | -12.092 | -52.0176 | 2026-06-28 02:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 6353fedc-6042-3698-893c-ea76a4ab153d | -9.457 | -40.3889 | 2026-06-28 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 12166943-b475-3c59-b596-76677ad7a0da | -12.092 | -52.0176 | 2026-06-28 02:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 7e9e0799-7953-3623-9ff7-f628eac56ccf | -11.6657 | -57.2536 | 2026-06-28 02:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e037d60b-c866-3e6c-892a-5e3662f8fa30 | -18.4795 | -54.1105 | 2026-06-28 02:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 3749a87c-8521-30cc-b3a1-3f26a3e4f660 | -12.6046 | -57.8942 | 2026-06-28 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| bd21d868-edc9-3596-b148-764825953d49 | -17.3041 | -42.643 | 2026-06-28 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 20af9017-10fa-3c46-a9da-093215545376 | -11.2279 | -54.3036 | 2026-06-28 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 20a56fd4-8fa3-356c-afe4-35449f34f610 | -9.457 | -40.3889 | 2026-06-28 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 141.5 |
| 50873875-e8e3-3580-ab57-d961c510abfb | -12.4651 | -58.5009 | 2026-06-28 02:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| cd748b17-a23a-3309-a945-8b83ca7eebfa | -12.6048 | -57.8743 | 2026-06-28 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| d92e4222-5fc1-393b-be84-3736097fc55a | -11.209 | -54.3053 | 2026-06-28 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 172.4 |
| f1841120-5d3e-3ee8-928e-a6efef4f5f56 | -12.1773 | -57.1519 | 2026-06-28 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 02772935-96e7-31cd-ac53-1fb7f95be40e | -12.1775 | -57.1319 | 2026-06-28 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 1ddbeab7-c12e-3472-8b47-7906acf56852 | -17.3242 | -42.6381 | 2026-06-28 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 2ce69f2d-7e3b-3b6e-bbf9-6fa0e54aa309 | -9.4761 | -40.3862 | 2026-06-28 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 160.6 |
| be6618b8-7cae-3fdb-9a74-3ec44a5f8eea | -12.092 | -52.0176 | 2026-06-28 02:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 4316a4bf-73a5-38b8-a33d-d568daa37f80 | -17.3041 | -42.643 | 2026-06-28 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 73.1 |
| cd04aad6-d1b6-39bf-bc09-ae685670e50c | -11.5243 | -54.7872 | 2026-06-28 02:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| da746a7b-285e-38c4-bec8-cf0fc4a8841b | -17.3034 | -42.6678 | 2026-06-28 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 9ed70ab7-9153-35b8-89f9-e6aa35274662 | -18.4795 | -54.1105 | 2026-06-28 02:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b519e9fa-1bfa-34fd-9a2e-a9b686887366 | -12.6046 | -57.8942 | 2026-06-28 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 57492365-03f8-382f-8473-a064fd717dc0 | -11.209 | -54.3053 | 2026-06-28 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 59d65aa0-8359-3c6a-8a8c-d6e3cf50ca37 | -11.2088 | -54.3258 | 2026-06-28 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 301d0648-f1b1-3cdc-a83d-31298ae11a32 | -12.1775 | -57.1319 | 2026-06-28 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4441081e-f1e0-3c1d-9819-70aa77d5bb50 | -12.4651 | -58.5009 | 2026-06-28 02:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 573572bd-702c-3e9d-8f64-52670c33b73e | -11.2279 | -54.3036 | 2026-06-28 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 7ca8807b-6a6f-3b67-985a-af708390a88c | -12.6048 | -57.8743 | 2026-06-28 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 33c25a96-9140-37c3-8f03-4c5145ff39d8 | -11.2093 | -54.2848 | 2026-06-28 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 45f9278d-8dee-35da-b759-e2a8964ed6a2 | -17.3041 | -42.643 | 2026-06-28 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| cf317374-72c6-3eaa-b988-a4bf5f76efd5 | -12.4651 | -58.5009 | 2026-06-28 02:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 7ad88ea2-8b43-3c0d-8bd8-876cab5ca97c | -12.6048 | -57.8743 | 2026-06-28 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 4c568da4-9d6d-3ba8-93f9-58decce6d6ad | -11.2279 | -54.3036 | 2026-06-28 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 38266ef8-7bb6-33f3-8d88-261819e6a9a3 | -11.209 | -54.3053 | 2026-06-28 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 187.3 |
| 7c3985ad-ad04-33d9-9147-5385a31d103d | -12.092 | -52.0176 | 2026-06-28 02:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 38db3f16-f276-37e2-b27b-a8fab38c97a5 | -11.2093 | -54.2848 | 2026-06-28 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6c33a97a-e791-3e97-9bdc-2fafbb4b7327 | -9.457 | -40.3889 | 2026-06-28 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 1d165c42-db98-37e8-b239-26399ebe0b25 | -17.3034 | -42.6678 | 2026-06-28 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 31489251-658d-3ffc-81cf-7aaa50fdcc76 | -12.6046 | -57.8942 | 2026-06-28 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 1b7f225f-2725-30cb-a67f-3a51d1400d57 | -18.4795 | -54.1105 | 2026-06-28 02:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 54.5 |
| fc9ccc67-547b-38e4-8b57-fc0bd863799b | -12.4651 | -58.5009 | 2026-06-28 02:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 36bdb63b-0459-3767-b6a3-683161ee97fe | -11.2279 | -54.3036 | 2026-06-28 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 9fffd197-a620-329d-9331-492baba313d5 | -12.092 | -52.0176 | 2026-06-28 02:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 853f0938-d3a4-3956-88ed-be5e3854b0c4 | -9.457 | -40.3889 | 2026-06-28 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 161.0 |
| 53da9644-ab55-3404-9ce0-b746207edb16 | -9.4761 | -40.3862 | 2026-06-28 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 141.9 |
| 8881d14e-3c81-321a-afa3-b440a9b7131f | -11.2088 | -54.3258 | 2026-06-28 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 05e71cd9-d496-3acb-9c2a-1ec6ff45916f | -10.2942 | -57.1182 | 2026-06-28 02:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| cfe5f4ab-cfa0-3f07-9424-4cce907f59d2 | -17.3041 | -42.643 | 2026-06-28 02:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 65.0 |
| d7e06b2b-fd83-3117-bddd-6326d69e3113 | -12.6048 | -57.8743 | 2026-06-28 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| c09186ba-73b8-33a5-b333-194767747786 | -11.2093 | -54.2848 | 2026-06-28 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 0fb45b76-5306-3a95-81ae-974707f154fb | -10.313 | -57.1169 | 2026-06-28 02:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e1f2c391-9b65-3dbf-bc94-671d69d4b02e | -11.209 | -54.3053 | 2026-06-28 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 205.8 |
| f74b8d04-db1d-317f-995b-66576a494ee2 | -12.4651 | -58.5009 | 2026-06-28 02:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| b1267157-3a6c-3512-a0cb-a729c0178b59 | -10.2941 | -57.138 | 2026-06-28 02:50:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 180eaaad-4840-3828-9143-cd52953f9684 | -11.2093 | -54.2848 | 2026-06-28 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 38c5fa91-2e4f-3529-8cb1-2e8cfa744f08 | -17.3041 | -42.643 | 2026-06-28 02:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| dadacc8e-bbda-3d4e-af19-b104f3499744 | -11.209 | -54.3053 | 2026-06-28 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 179.2 |
| 7018b90d-180c-30e9-8e8e-a3cdfe0f8107 | -12.6046 | -57.8942 | 2026-06-28 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 7cf31b41-2d4f-3758-b46f-9b2c679cd92b | -17.3242 | -42.6381 | 2026-06-28 02:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 1d9ea49e-53b3-355c-95b6-2e018944afc4 | -10.2942 | -57.1182 | 2026-06-28 02:50:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 64f2a2f9-08a2-3466-83cf-31f65d92e1b4 | -12.6048 | -57.8743 | 2026-06-28 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| f5077c9c-e63c-3084-a9af-727def50477b | -12.092 | -52.0176 | 2026-06-28 02:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f56349e4-c7c7-3613-905c-93ff1bda67b2 | -11.2279 | -54.3036 | 2026-06-28 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 5f4c9db2-abc1-3514-ab2e-215ecbc03b57 | -12.4651 | -58.5009 | 2026-06-28 03:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 6a5a99cd-a8bb-3f7c-8c74-fab40c456711 | -12.092 | -52.0176 | 2026-06-28 03:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 92036e36-56b5-3ddd-81d5-a4a15e9a4726 | -10.3128 | -57.1367 | 2026-06-28 03:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| bbe47c2e-980d-3ca7-abc2-35f5875d6be5 | -17.3041 | -42.643 | 2026-06-28 03:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2d4e7e4e-bd84-3bc0-b15f-fe49f854c271 | -12.6046 | -57.8942 | 2026-06-28 03:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 911617cb-b9bb-38e9-9c78-7bb07124aac1 | -17.3034 | -42.6678 | 2026-06-28 03:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 53.3 |
| b4a75eee-28b1-34b1-83db-88e75c1efa31 | -10.2941 | -57.138 | 2026-06-28 03:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a0d75c1a-7c65-3830-99bc-771889b0ee85 | -11.5243 | -54.7872 | 2026-06-28 03:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 80a1aa3a-0023-307e-83de-80fce171b8c9 | -11.209 | -54.3053 | 2026-06-28 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 229.9 |
| ee7baed5-8a0c-32b9-9258-ab5930aa82a3 | -11.2093 | -54.2848 | 2026-06-28 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c1da7f1d-93b6-317d-9d37-795bbb543486 | -10.313 | -57.1169 | 2026-06-28 03:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 94e1bd98-a595-3574-9a41-bac127b64975 | -10.2942 | -57.1182 | 2026-06-28 03:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3811fb11-0bd6-36de-8f93-88e38c18ba2c | -11.2279 | -54.3036 | 2026-06-28 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| f48c6278-3b2c-3fff-9646-725c71198d10 | -12.2131 | -52.8637 | 2026-06-28 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a0aadba6-d91d-3971-96db-42e681f7a088 | -11.209 | -54.3053 | 2026-06-28 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 190.7 |
| c97159a8-ea4c-3024-935a-64735e29aea5 | -17.3041 | -42.643 | 2026-06-28 03:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 09825adf-557b-31fa-8f02-1e6adcc2a0e5 | -12.1747 | -52.8886 | 2026-06-28 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |


[Clique aqui para ver as próximas entradas](README9.md)
