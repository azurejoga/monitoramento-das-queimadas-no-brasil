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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ea51556-6482-3c8f-a421-1771722c3072 | -14.75849 | -46.7691 | 2025-09-01 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 6e20c394-9d28-373b-b450-02bcc9e7fdd9 | -10.6128 | -44.3284 | 2025-09-01 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 0fb7f5b6-83d0-37c3-9a3f-c200f6e98c9c | -10.5937 | -44.331 | 2025-09-01 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 1cd9427d-9b97-3e59-a897-c400899cef55 | -15.6063 | -48.3177 | 2025-09-01 01:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 7154e290-314e-38d2-abb2-5bb54e5b71e0 | -12.2287 | -43.8772 | 2025-09-01 01:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 4bed4424-d367-39f2-80b0-93410bf6f25d | -15.7112 | -48.9032 | 2025-09-01 01:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 119.1 |
| af853c3a-f45e-3d9e-9f02-0276585e0457 | -15.6058 | -48.3402 | 2025-09-01 01:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 2695e0ea-c296-3c1d-b923-4b3ee8dc05e9 | -9.2825 | -47.1007 | 2025-09-01 01:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 0484588b-2d82-30aa-bafc-8d0147160358 | -19.0724 | -48.3148 | 2025-09-01 01:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 50.7 |
| fc22b86a-d247-3a52-8f12-7422b09e6763 | -15.5867 | -48.321 | 2025-09-01 01:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| cddf6421-36de-3312-ba07-37994aa97f31 | -14.7618 | -46.7667 | 2025-09-01 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 0efc3e5e-9192-399f-a402-2ade11013e2c | -17.5956 | -46.6648 | 2025-09-01 01:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 1ff78dde-f682-3b7f-95e5-9882ab071b6e | -11.3709 | -43.5631 | 2025-09-01 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 5024807b-ed70-3e60-b622-9893be4b5219 | -17.595 | -46.6882 | 2025-09-01 01:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 114.7 |
| e33c28d2-f392-3f41-a7ed-4d59b19117fb | -12.2094 | -43.8803 | 2025-09-01 01:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 51583988-c58c-34de-a445-1d0dd27f0043 | -7.2744 | -60.6677 | 2025-09-01 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 01a765a4-3eb3-33b7-8a85-3a00a4733290 | -7.0946 | -44.3589 | 2025-09-01 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| a5fbc3d0-4c62-3802-ab30-3756d793aa21 | -19.0522 | -48.3191 | 2025-09-01 01:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 176bd2ba-1690-3204-912d-e3b64782e788 | -7.076 | -44.3376 | 2025-09-01 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 87da3300-5052-323b-ab71-cadaa4b858bd | -6.8466 | -52.8132 | 2025-09-01 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 9cf933dd-66a7-37d1-bb78-bf39abebf24b | -7.0965 | -63.0437 | 2025-09-01 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 492d42d9-fb15-395d-a0e5-a368139d1f9f | -6.8281 | -52.8143 | 2025-09-01 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 024a9ceb-0adf-34c0-8afa-3c8a3153018d | -17.6155 | -46.6607 | 2025-09-01 01:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 268.5 |
| 428633f4-03a0-35b9-b58e-2d78af31b767 | -9.135 | -65.5453 | 2025-09-01 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f550f5dd-d20c-3259-9a34-204f3bd5ad45 | -6.8279 | -52.8348 | 2025-09-01 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 13e69cd5-37fe-3a02-8a51-d9794abef571 | -6.7438 | -43.7898 | 2025-09-01 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 4810ecff-2a52-3180-a0f6-0070134d8f9a | -17.615 | -46.684 | 2025-09-01 01:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 239.0 |
| ec70e66a-fff2-3ace-95ab-0f42c851dcbd | -15.6916 | -48.9065 | 2025-09-01 01:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| b6e4ac6f-0b41-385e-9bd8-3b6d6e03da69 | -10.0434 | -48.0998 | 2025-09-01 01:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 30ff3ea4-c639-370c-811c-3b34b17cd841 | -7.9335 | -73.0052 | 2025-09-01 01:10:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 195968d9-fa49-3988-b939-a3bd8bc0dd01 | -15.5862 | -48.3435 | 2025-09-01 01:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 1d3960c5-4f29-32ec-a7a2-cca1b3261814 | -7.2745 | -60.6486 | 2025-09-01 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5ea05568-c616-38ba-890c-0d4792da64e5 | -9.1165 | -65.5459 | 2025-09-01 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 4a0d0076-9a6a-38f6-8216-35ec4610f1ea | -7.2929 | -60.667 | 2025-09-01 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 552b78bf-b267-3ce4-9121-a1ea202562cd | -7.6783 | -61.0908 | 2025-09-01 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 21ae7d90-e85e-314d-a3bb-1732787f657b | -7.0757 | -44.3606 | 2025-09-01 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| e06b5c76-4406-3c28-852b-0a7966b5abc9 | -6.8095 | -52.8154 | 2025-09-01 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| c3a7ce93-2497-343c-b5cd-c868c751e3cf | -13.1644 | -45.2897 | 2025-09-01 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| f759be6c-d29b-3ea0-b73d-7fc9ab5c432c | -11.3701 | -43.6104 | 2025-09-01 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 28b10445-d158-380c-9b84-4a09c697e780 | -11.026 | -47.0538 | 2025-09-01 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a6afb70b-2f4b-365e-9aed-fa4b256987d1 | -12.5722 | -48.2059 | 2025-09-01 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 31a01a7f-b2e9-3eb9-9080-887dadf85b7a | -11.3696 | -43.6341 | 2025-09-01 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 720ec205-443f-306e-b27d-901a71fdaf87 | -7.0948 | -44.3358 | 2025-09-01 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 246fa937-2273-32cc-808f-e42dc53e9188 | -13.1648 | -45.2665 | 2025-09-01 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 6d1c9cc9-93ac-3be6-8c28-2ea55be8401b | -11.0263 | -47.0314 | 2025-09-01 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c717b429-244c-300e-93de-c0faae697fb0 | -11.3705 | -43.5868 | 2025-09-01 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3369698b-60d7-3049-99f2-518c9c18dd0a | -11.3888 | -43.6312 | 2025-09-01 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 430e8c26-ee81-30b9-8ce6-35de1539ba64 | -4.09045 | -55.80527 | 2025-09-01 01:11:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d0e8724e-f7bc-307d-a551-51a62329b970 | -4.09195 | -55.81575 | 2025-09-01 01:11:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cc47697a-fc52-321a-89da-c239397ae8ec | -10.5937 | -44.331 | 2025-09-01 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e9584ac2-6ce8-38ed-81bd-83495b771414 | -11.3709 | -43.5631 | 2025-09-01 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 98e5b7c0-9871-3bc3-b885-4a262bb0e661 | -6.4605 | -43.9532 | 2025-09-01 01:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 64f1aa9f-f9d5-3d46-afb6-8b1b0de9a5f6 | -9.135 | -65.5453 | 2025-09-01 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| fa9c1257-31c0-3055-b59d-1d0fa514b2fa | -7.076 | -44.3376 | 2025-09-01 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 58c4f389-73b5-385d-9034-556ecbc480c0 | -11.026 | -47.0538 | 2025-09-01 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 2fbdb731-d487-3b93-8f05-2d26e8039111 | -12.5722 | -48.2059 | 2025-09-01 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| aa75850e-6e5a-34c0-a878-a7e5e3b84922 | -6.8466 | -52.8132 | 2025-09-01 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| b4b0d69f-03a2-3fdf-ab8c-997b6961b352 | -13.1648 | -45.2665 | 2025-09-01 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 6e46d856-96ea-3984-af5f-3735337e11c6 | -12.9197 | -56.9471 | 2025-09-01 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 280.6 |
| c1c2de9c-a85e-38fb-a3e7-1238834cef0c | -11.3701 | -43.6104 | 2025-09-01 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 3413d59e-5373-3826-934b-13e8be4707b8 | -13.1837 | -45.2865 | 2025-09-01 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 4ae059aa-67e0-3caa-be2c-8c017f0ad1f2 | -12.9194 | -56.9672 | 2025-09-01 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 187.7 |
| 7ae7faf1-b6b6-361c-afee-4a22d0182602 | -7.0946 | -44.3589 | 2025-09-01 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 07fe30ee-3882-39a2-9308-bcf951956c89 | -6.4602 | -43.9764 | 2025-09-01 01:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 014ed8b6-4c0a-34a5-af25-831d51b63c23 | -15.6916 | -48.9065 | 2025-09-01 01:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 95914254-5573-3929-ba13-7d071a1f42b7 | -19.0724 | -48.3148 | 2025-09-01 01:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 95838ff4-c631-3f8e-bd21-e57abd0bb549 | -7.9335 | -72.987 | 2025-09-01 01:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 81ba9ddb-a40a-3bc4-9556-c722ac4797be | -7.2744 | -60.6677 | 2025-09-01 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 190c01c7-293a-36cf-b4e3-1aa8c321edcf | -12.9385 | -56.9655 | 2025-09-01 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 8d96d04d-33b7-31b3-b43e-b197aa2a058f | -7.0948 | -44.3358 | 2025-09-01 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| ef305f2a-dbbe-3400-915d-f1798aa8e073 | -15.6063 | -48.3177 | 2025-09-01 01:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ea71a37d-69fd-3906-9ad9-b76fc54a75e3 | -7.0965 | -63.0437 | 2025-09-01 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 780797ae-fec5-3510-81a4-4b74bbe311f6 | -9.1165 | -65.5459 | 2025-09-01 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 3aeaa249-03f1-3ff1-a2d0-6459c74f9ec5 | -7.6967 | -61.09 | 2025-09-01 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 95035c7f-e038-3d02-85f4-366573db761b | -19.0522 | -48.3191 | 2025-09-01 01:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 80.1 |
| bd7de0f5-a214-33db-9a49-fee2e6bf95d5 | -11.0263 | -47.0314 | 2025-09-01 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| dcf83261-f173-39eb-a440-37e3b3747664 | -11.3696 | -43.6341 | 2025-09-01 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 88f99397-893b-3099-9166-7f7b60e8a924 | -10.0434 | -48.0998 | 2025-09-01 01:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8e785a40-3126-359d-a5cf-e5ef298f937a | -10.6128 | -44.3284 | 2025-09-01 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e4582822-438d-3c54-af4f-b55d54cf64fb | -11.3705 | -43.5868 | 2025-09-01 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 1b8fc445-efa3-3110-b4ee-722a0b37a8c2 | -13.1644 | -45.2897 | 2025-09-01 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 1b9d5141-fcc2-3a5a-b9c5-0160df19e80f | -7.2745 | -60.6486 | 2025-09-01 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9f48d5e6-ac40-3826-a801-08a7a53e8ef0 | -15.5862 | -48.3435 | 2025-09-01 01:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e11f034c-694b-35f1-8f48-6156f79018b6 | -6.8279 | -52.8348 | 2025-09-01 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 098a9203-3de8-33f6-b389-d6e24b090379 | -7.0757 | -44.3606 | 2025-09-01 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 3b28c992-ea3a-30ef-af78-e21d1e07a7ec | -7.2929 | -60.667 | 2025-09-01 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| f1319b0b-577f-3817-a2d2-54b95e04ac73 | -7.9335 | -73.0052 | 2025-09-01 01:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4db7fa13-36ea-3681-b926-729b917e0ab7 | -15.6058 | -48.3402 | 2025-09-01 01:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 26c550ae-d4c4-32d5-a1b5-40445183d0d9 | -12.9387 | -56.9454 | 2025-09-01 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 835116d3-5169-374c-bcfa-69eddbfe9620 | -12.9006 | -56.9488 | 2025-09-01 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| d9df04f1-2887-3c38-b40e-1f7e7a8047c9 | -6.8281 | -52.8143 | 2025-09-01 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 18063b4c-4359-3c80-af8c-0ffd2ff13746 | -6.8095 | -52.8154 | 2025-09-01 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a4709a67-3fc9-33ee-b33a-d512acbf6031 | -7.6783 | -61.0908 | 2025-09-01 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a1f78b48-51a6-319b-9706-3828be8b34a9 | -14.7618 | -46.7667 | 2025-09-01 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 3b0b1f9e-d114-3d59-bea4-62c0cd0ff841 | -9.1351 | -65.5266 | 2025-09-01 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 8a825a2c-56dc-38b0-b680-65d8174f0dff | -9.2825 | -47.1007 | 2025-09-01 01:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b2952b15-3a06-3655-ae9c-81e09683caa9 | -15.7112 | -48.9032 | 2025-09-01 01:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 110.5 |
| aac8942d-48ad-3fa6-9768-90ce00867a49 | -6.7626 | -43.7881 | 2025-09-01 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 79f351c4-144c-354e-a862-51ce60a222b2 | -7.0965 | -63.0437 | 2025-09-01 01:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b077d056-adba-3c9e-9787-60912ce5fb93 | -7.076 | -44.3376 | 2025-09-01 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 170.1 |


[Clique aqui para ver as próximas entradas](README7.md)
