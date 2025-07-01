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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a687fc9-b71d-38bf-933a-f3b15a5a512f | -12.6632 | -45.3008 | 2025-07-01 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a0a17cde-7b78-3fc2-a04f-b1bd03dfc639 | -6.2226 | -43.3459 | 2025-07-01 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 0875d04d-29fa-350c-828f-e36996fcd839 | -7.7133 | -47.8453 | 2025-07-01 13:40:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 40c68152-0cdf-3e40-a34e-b3733a5f5ea4 | -7.732 | -47.8437 | 2025-07-01 13:50:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| fb8f4f27-a96c-3bce-a7a4-57aa307a1fee | -7.7133 | -47.8453 | 2025-07-01 13:50:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 400f6879-8ab9-3504-9aa5-feef1f4f46ca | -12.6632 | -45.3008 | 2025-07-01 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 6fa7c8a6-ae62-3273-b1d4-c5157ec3eb04 | -12.427 | -50.0387 | 2025-07-01 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 56699c4e-4f00-363a-bb60-e0341878a316 | -12.6632 | -45.3008 | 2025-07-01 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 372d0074-0f8b-3f66-bc8f-80f07f2f38f8 | -7.0752 | -44.4066 | 2025-07-01 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 8f3d0478-2186-3db4-bb95-238eeda86e12 | -12.427 | -50.0387 | 2025-07-01 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| ee2520a4-3049-33e7-b694-3ff4b787944f | -7.7133 | -47.8453 | 2025-07-01 14:00:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 5a520036-3e7c-3e94-9cdd-5dbf48498e4a | -7.7133 | -47.8453 | 2025-07-01 14:10:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 2e8a1c59-92c7-33b2-bdeb-e24dd3bce4a9 | -12.6632 | -45.3008 | 2025-07-01 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| edd6fdc0-0f8a-32c8-8c15-d0145fb15ada | -12.0708 | -48.4495 | 2025-07-01 14:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c22fae4b-ca6e-3328-a3f4-5dc6aaf90da4 | -7.732 | -47.8437 | 2025-07-01 14:10:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 1ff2f200-6cf3-3af4-895e-83bf14cfd1a9 | -12.0708 | -48.4495 | 2025-07-01 14:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 294f0397-370b-392f-8c0a-a05078810bde | -13.8667 | -45.9344 | 2025-07-01 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| b90c9180-9b38-3d63-b3ad-1d932ec9785b | -12.427 | -50.0387 | 2025-07-01 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| a51f0b4d-5081-3250-9012-4a5c46693d30 | -9.577 | -49.107 | 2025-07-01 14:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 9da823b9-183d-3fd7-960d-fe55436b7683 | -7.7133 | -47.8453 | 2025-07-01 14:20:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a16e0046-07ce-3713-b492-bd0975736ca0 | -12.6443 | -45.2806 | 2025-07-01 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 06f82804-0f53-3598-b211-5b0d6d7f39e1 | -12.6632 | -45.3008 | 2025-07-01 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 3bae1605-3fa4-3e17-8090-a16ddcacf7de | -12.0705 | -48.4716 | 2025-07-01 14:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 2c6d75f4-f322-316f-8053-ac259eccd5ca | -9.577 | -49.107 | 2025-07-01 14:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 2a08ebf8-3c5c-37fd-9346-e2d9e270f55e | -10.8832 | -56.4367 | 2025-07-01 14:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| bc4402f6-df66-33e1-9d8e-6f1628969098 | -12.0708 | -48.4495 | 2025-07-01 14:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 955a6be1-bfa2-3fa0-8186-865eb8c9692b | -12.6632 | -45.3008 | 2025-07-01 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| bb6a1510-0ea3-347c-be44-6efe9eb3fdfd | -10.9018 | -56.4552 | 2025-07-01 14:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 47326741-f947-3385-a8a7-7fa73ab4d15e | -12.427 | -50.0387 | 2025-07-01 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 4cdfcb13-cd12-314a-b532-bc1a761f6903 | -12.6443 | -45.2806 | 2025-07-01 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| a752e099-5640-3264-903d-2df19b87e1a0 | -7.7133 | -47.8453 | 2025-07-01 14:30:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| de11d514-d962-3f77-9b1a-565dba8068b5 | -10.876 | -53.7614 | 2025-07-01 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 14b12862-42ca-3600-b06a-b88586731614 | -12.6632 | -45.3008 | 2025-07-01 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 222791be-4837-3f06-841e-23716549ceb1 | -7.0755 | -44.3836 | 2025-07-01 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 4abe764b-b1ee-35ab-b856-d42721c4de5c | -12.427 | -50.0387 | 2025-07-01 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2d002278-3bec-39b5-ad23-1fcfb2fd2d16 | -9.577 | -49.107 | 2025-07-01 14:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 408d4a1f-d896-39b4-bb7f-440daa28cd5a | -12.0705 | -48.4716 | 2025-07-01 14:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 2812c085-591c-3acc-9a03-b852a9b27e52 | -10.9018 | -56.4552 | 2025-07-01 14:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| eefedd92-9045-3a77-b12a-7e2a296751f2 | -12.6443 | -45.2806 | 2025-07-01 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| f7ce6f3a-7ade-32b4-a5c8-831819a3f829 | -12.0708 | -48.4495 | 2025-07-01 14:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 7a9c89a7-c3fb-3696-ad53-4f4be18bad88 | -10.883 | -56.4567 | 2025-07-01 14:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 200.1 |
| c0110168-20b4-3425-834b-b03acb5265ac | -7.7133 | -47.8453 | 2025-07-01 14:40:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 44538911-6f43-3a79-9f5c-71da1af8b337 | -10.8832 | -56.4367 | 2025-07-01 14:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |


