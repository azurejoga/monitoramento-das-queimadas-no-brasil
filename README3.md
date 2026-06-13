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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5127868-e6aa-3105-a920-a7ec4e8fb4fa | -10.0626 | -48.0758 | 2026-06-13 01:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9b32ee5c-ad85-31f1-8039-47472bcf5ac0 | -11.6497 | -48.5473 | 2026-06-13 01:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 8b1a2c98-edc2-3955-bd9d-621b49b81126 | -11.65 | -48.5253 | 2026-06-13 01:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 3687c46d-c04b-3e36-aa80-0d1cd52da5f0 | -11.6309 | -48.5277 | 2026-06-13 01:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 72cab14d-e7f6-3ecb-b25a-e98cf2251cc5 | -11.6306 | -48.5497 | 2026-06-13 01:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| d549cefc-c701-3f1c-8468-3c636c1f3fc4 | -11.6309 | -48.5277 | 2026-06-13 01:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c94dbe65-1b83-3447-96e8-2175d0fc7b77 | -10.0626 | -48.0758 | 2026-06-13 01:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 15987e71-5b32-3489-bf0e-57bdcdc27d63 | -10.0623 | -48.0978 | 2026-06-13 01:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| e6d47875-b9df-323d-9d22-fbed873d7aab | -11.6497 | -48.5473 | 2026-06-13 01:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ab28031d-c8bb-3a63-887a-bd8b37de1d55 | -11.1825 | -46.7874 | 2026-06-13 01:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7eb9fa32-dd5a-30e6-a8ea-3c6923fb104a | -11.6306 | -48.5497 | 2026-06-13 01:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 676a4d76-ef99-3426-bda0-aff407e88d44 | -12.269 | -57.4039 | 2026-06-13 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| d551e743-e1a1-30d5-9fec-a60e637947df | -10.0623 | -48.0978 | 2026-06-13 01:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 836a2ae4-e132-304c-b67a-1057a7d10830 | -10.0626 | -48.0758 | 2026-06-13 01:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 8df53dba-73cc-37fd-ba33-761c0ffc95f2 | -12.269 | -57.4039 | 2026-06-13 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| a070f2fb-7e68-31f6-81bc-5dc538e5a8f5 | -11.6497 | -48.5473 | 2026-06-13 01:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 83abeb35-d913-3287-83c8-6732e3e9cc45 | -11.6306 | -48.5497 | 2026-06-13 01:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 059c13bf-6bfa-3c5d-b97e-15bdf8326bb3 | -11.6309 | -48.5277 | 2026-06-13 01:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| ef664975-c97a-3c27-b462-66622a0c1d3b | -11.6306 | -48.5497 | 2026-06-13 01:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| f082deef-4343-35c4-b00a-88bd09c0f61d | -10.0626 | -48.0758 | 2026-06-13 01:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 08b513e4-e461-314b-ad85-8e82505ef82a | -10.0626 | -48.0758 | 2026-06-13 02:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| c7fddd8c-10c4-3719-bc03-eb5ef923481d | -10.0623 | -48.0978 | 2026-06-13 02:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| cc1a239e-2804-3fe7-bdaf-3dd4154f8ca1 | -11.6306 | -48.5497 | 2026-06-13 02:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| f11c22db-20e8-367f-9895-35f258e12211 | -10.0623 | -48.0978 | 2026-06-13 02:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| f55f4a05-f86f-36a8-9dfc-9ae764cf04c5 | -10.0626 | -48.0758 | 2026-06-13 02:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 2c806c2e-97a3-3b8d-94df-7431198e4615 | -11.6306 | -48.5497 | 2026-06-13 02:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 95f9bed6-c8d0-3db8-a87e-d7ac0e3639e8 | -10.0626 | -48.0758 | 2026-06-13 02:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 74e43acb-c3b4-353f-8a8a-b566bb9b99ac | -10.0623 | -48.0978 | 2026-06-13 02:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 70618084-829d-3a2e-8637-c5506eec0938 | -11.6306 | -48.5497 | 2026-06-13 02:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| c93ae6f3-ff38-36ca-86f4-1ab6a34f6b24 | -11.6309 | -48.5277 | 2026-06-13 02:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 5fcdb7e8-d674-328d-aa83-a538e4017d6f | -10.0626 | -48.0758 | 2026-06-13 02:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 3aad1626-8009-3de3-8d17-dbf92d58ba92 | -10.0623 | -48.0978 | 2026-06-13 02:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 81f22884-6bb5-38a7-aa6d-0a72f7a6a2ad | -11.6306 | -48.5497 | 2026-06-13 02:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| ed8d5422-36a5-3988-8c91-6900a57b3cf1 | -10.0623 | -48.0978 | 2026-06-13 02:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| b3745287-8213-3a3a-a43a-146ddf4d90c7 | -10.0626 | -48.0758 | 2026-06-13 02:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 3570e1d6-b571-3a5a-8d1a-2197e135b9d6 | -11.6306 | -48.5497 | 2026-06-13 02:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 83ecdb92-0deb-3ad1-a51f-2f6af8c2ff9b | -10.0626 | -48.0758 | 2026-06-13 02:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 59246ded-09b0-3dce-84b0-29bb815a0769 | -10.0626 | -48.0758 | 2026-06-13 03:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3414ef88-e71f-354c-a1f0-16d9433d28e4 | -10.0626 | -48.0758 | 2026-06-13 03:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 3754ba70-4435-31b0-b601-3103f6d60f2f | -10.0626 | -48.0758 | 2026-06-13 03:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 12664190-05b0-3b12-845a-570709b48ffc | -10.0626 | -48.0758 | 2026-06-13 03:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| a5559143-0260-391d-91ee-909cdf8cd59c | -10.0626 | -48.0758 | 2026-06-13 03:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 83b89894-7f08-3386-a7d2-a907d8d397ae | -10.0626 | -48.0758 | 2026-06-13 03:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 1f13714f-8cc6-3636-a37a-92b81f1b41ec | -11.6306 | -48.5497 | 2026-06-13 04:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| b2b6f2f7-ef67-3fb9-8d75-9caf7f3a6665 | -10.0626 | -48.0758 | 2026-06-13 04:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 5c2d0a9a-d684-3dfc-8098-64a60099f803 | -10.0626 | -48.0758 | 2026-06-13 04:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 3064be47-2b41-3848-a598-9fccd664bcbb | -10.0626 | -48.0758 | 2026-06-13 04:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |


