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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2288af0b-93cc-3c60-a4cf-d827b3eba0fd | -10.876 | -53.7614 | 2025-06-30 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 0e38b070-a46f-3818-b428-2bef2f935178 | -12.6316 | -54.2293 | 2025-06-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 091a2b62-7eff-3b3e-9c96-f7d259ff0f5a | -10.5579 | -52.0289 | 2025-06-30 00:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 4aea39db-e633-3a30-91ea-bed6df4c320c | -12.6128 | -54.2107 | 2025-06-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| d6fa65b5-8069-387d-bc0b-8a71b8fc9d72 | -12.6319 | -54.2087 | 2025-06-30 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 6c2afb11-78e4-3ea9-9bb2-6c14f61f3bb9 | -12.0708 | -48.4495 | 2025-06-30 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 04316b96-f47a-3f5a-a9a6-8173fa47a25c | -9.2337 | -58.74 | 2025-06-30 00:00:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| cea16b0c-6a95-3976-9a79-380d5fcecab6 | -9.2523 | -58.7389 | 2025-06-30 00:00:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e76263fc-5592-3113-a918-4f27d172eb5b | -10.5576 | -52.0499 | 2025-06-30 00:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 350bfb09-e278-3d3e-a139-eede2388fa3a | -9.1018 | -47.9575 | 2025-06-30 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 8d20b1ea-574b-3381-a08d-fc1cdf5a2e29 | -10.8762 | -53.7408 | 2025-06-30 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d2f70849-f6ca-3caf-aeb3-0698630b0716 | -11.9469 | -57.4503 | 2025-06-30 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 1849829a-674d-35a0-9924-083140254050 | -11.928 | -57.4518 | 2025-06-30 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ac87bde5-1a49-3d67-854f-f0447b948cc1 | -10.8571 | -53.7631 | 2025-06-30 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| d1c9deb9-2a57-3b48-b490-2893d8be279e | -10.1036 | -52.1967 | 2025-06-30 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 66b45437-386b-385c-ae9d-98fd2f02d359 | -10.8573 | -53.7425 | 2025-06-30 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 544d2ecb-97a1-30af-b7ee-3a695965eef0 | -12.0705 | -48.4716 | 2025-06-30 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| b6a5491c-d614-3ff0-a8ef-1876c92afc08 | -9.2522 | -58.7584 | 2025-06-30 00:00:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 52d13f23-bc5e-3408-9242-82def96e646e | -11.9469 | -57.4503 | 2025-06-30 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| d8ba320f-ad1a-3928-9db9-cf3903a9ff52 | -10.805 | -44.2319 | 2025-06-30 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 05169fbf-da01-3041-b691-8938d58c2e4f | -10.8573 | -53.7425 | 2025-06-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| b9a672d1-2136-397d-a489-d278e621f93e | -12.6128 | -54.2107 | 2025-06-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 2a1d0cea-3e95-3de8-9e63-2ee22b64dee1 | -9.2337 | -58.74 | 2025-06-30 00:10:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 89f405eb-6277-3cc5-8c54-6d1264cc4c2a | -10.876 | -53.7614 | 2025-06-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 9bb02026-c9bd-3978-bb92-b5fd1ba659ce | -10.8762 | -53.7408 | 2025-06-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| f98259e7-ec4e-387f-bce2-2ec71e290468 | -12.6316 | -54.2293 | 2025-06-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 4fb33693-d283-3524-b4d7-8e6d549a85b8 | -9.2522 | -58.7584 | 2025-06-30 00:10:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 50bbaf8d-f9e8-3be5-828c-1e19c760953d | -12.6126 | -54.2313 | 2025-06-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 282222b6-e273-35af-b2ac-101d1d330b62 | -9.2523 | -58.7389 | 2025-06-30 00:10:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| ab4c334c-e0e5-324a-b16d-0795d8908012 | -11.928 | -57.4518 | 2025-06-30 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 27069930-e279-31fb-b569-ac442f08dfa2 | -12.0705 | -48.4716 | 2025-06-30 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| e2d81179-1ab3-3458-9678-90dc3c3b6b11 | -12.6319 | -54.2087 | 2025-06-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 8953f516-557d-373a-b1f7-d025c96934a5 | -12.0708 | -48.4495 | 2025-06-30 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| aff476cf-0be4-350c-bd3b-e39231a239a3 | -12.6126 | -54.2313 | 2025-06-30 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d255bf88-48ca-377e-a844-2a0ece6daf79 | -9.2522 | -58.7584 | 2025-06-30 00:20:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d37796a9-7171-33e9-96eb-981fd9a0c9da | -12.6128 | -54.2107 | 2025-06-30 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ebd588ad-5fd1-3a1a-8cb0-7be32d8f466f | -12.6319 | -54.2087 | 2025-06-30 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| e15ce370-3f43-3af5-81d8-c21822153ac0 | -9.2523 | -58.7389 | 2025-06-30 00:20:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 7852e73e-aa49-3ed1-b3fc-790b24183590 | -11.928 | -57.4518 | 2025-06-30 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e3c1eb62-2f08-39b0-9d2f-bf23f71a1ff9 | -10.8762 | -53.7408 | 2025-06-30 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9a3705db-727d-35fd-8a30-89d15bc6c167 | -10.805 | -44.2319 | 2025-06-30 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| d760b365-0d6d-3166-bf4b-67a5aa82c561 | -12.0705 | -48.4716 | 2025-06-30 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ff7048f6-0d33-3fb1-b0a5-6600231b5c4e | -12.6316 | -54.2293 | 2025-06-30 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 7730ddbe-0ed3-3b58-8cd2-fc7927728679 | -9.2337 | -58.74 | 2025-06-30 00:20:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 7958f005-2be8-3f72-ba68-43ab22cba0c4 | -12.0708 | -48.4495 | 2025-06-30 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c2b0f6c4-fe48-3c1e-8007-8fcfe2346b7f | -10.8573 | -53.7425 | 2025-06-30 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| bd8bc631-0126-325c-b847-d24e7308abda | -11.9469 | -57.4503 | 2025-06-30 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 2ea5dd0f-e07f-33d3-a73b-a959d4c4c3f8 | -11.928 | -57.4518 | 2025-06-30 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 093ef063-9bf4-3c01-9d38-2e32a51f3945 | -12.0705 | -48.4716 | 2025-06-30 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ceedd039-8812-372f-bcc3-8acf689d6eeb | -9.2337 | -58.74 | 2025-06-30 00:30:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 274e4445-3c7a-3ea3-9383-3fbdaa6f1c3b | -10.5576 | -52.0499 | 2025-06-30 00:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3438ff04-72a0-3e33-99a8-28085f5a442e | -12.6319 | -54.2087 | 2025-06-30 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 2785e94b-f5d5-3933-8a9a-9caacdc9f0d9 | -10.8762 | -53.7408 | 2025-06-30 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a33c5781-2caa-374c-b829-e2144487e24d | -10.805 | -44.2319 | 2025-06-30 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ddaab3ca-9a3d-359a-8916-77e76b4b08e7 | -12.0708 | -48.4495 | 2025-06-30 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| bd470423-61aa-3518-85da-ca0d8ccfe7d1 | -12.6316 | -54.2293 | 2025-06-30 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| cd10fd39-779c-394a-98e1-fc2139180282 | -9.2522 | -58.7584 | 2025-06-30 00:30:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d02fcd4b-642f-3d2a-a0d8-b7f117db8f09 | -12.6128 | -54.2107 | 2025-06-30 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 900e305e-9ffe-3649-bba3-4154f1fe7140 | -9.1018 | -47.9575 | 2025-06-30 00:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b0308ba7-e6c9-3a22-888e-788f031b8ccd | -10.8573 | -53.7425 | 2025-06-30 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 5bd77f3e-5a09-3633-ab5a-dd91b086f0ec | -16.31115 | -48.90383 | 2025-06-30 00:39:00 | TERRA_M-M | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 030f21f2-d289-3de5-9cde-4f716168ea9d | -15.98964 | -41.98895 | 2025-06-30 00:39:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ea56526e-04e9-33d3-8461-e6727340d57c | -10.805 | -44.2319 | 2025-06-30 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 31585e70-46b9-3789-a490-c233a1f6ad33 | -12.0705 | -48.4716 | 2025-06-30 00:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 61e160b2-ab7b-37fe-a1b3-b8743c93428c | -12.6319 | -54.2087 | 2025-06-30 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 251fcce2-0263-3007-bd7c-1d7d85106fdd | -9.2522 | -58.7584 | 2025-06-30 00:40:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| fb456d1f-8830-3bc2-8f38-bc7a6e27d3df | -12.6128 | -54.2107 | 2025-06-30 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f6c08242-fd52-341d-9dbe-70cbc73874a1 | -11.928 | -57.4518 | 2025-06-30 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 04ea94a7-3298-390e-bd73-34992455d917 | -9.2337 | -58.74 | 2025-06-30 00:40:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 8ab2af2b-a06f-3484-8e9b-3f541964ab21 | -12.0708 | -48.4495 | 2025-06-30 00:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 36082569-2ca6-3901-a67d-bc89a198c3e6 | -9.1018 | -47.9575 | 2025-06-30 00:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| a8727dce-d940-3b85-87a4-86d00fa8e5b1 | -11.9469 | -57.4503 | 2025-06-30 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c2f7f786-f5db-3dda-ac0a-427a8e9d76e3 | -10.8573 | -53.7425 | 2025-06-30 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.4 |
| b1a0f2cd-bcd5-385c-bc73-599c4f7f8e47 | -10.876 | -53.7614 | 2025-06-30 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 96492a6c-babe-35e4-a333-9a0e6cc63366 | -12.6316 | -54.2293 | 2025-06-30 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ded6773a-6c7b-392b-b176-a4fe481828c7 | -10.8762 | -53.7408 | 2025-06-30 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 90af24c0-47ac-3f27-a770-3977b3bb4f7c | -9.23331 | -58.73287 | 2025-06-30 00:41:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f71d66fd-8dc6-3ed8-bc54-dc8f96b266dd | -10.8589 | -53.73951 | 2025-06-30 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| ec2dc227-c107-33a9-a5f2-0b67ef026093 | -10.55918 | -52.04982 | 2025-06-30 00:41:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 7304d6b3-f15b-3e51-a08d-90a472c74d30 | -10.09945 | -52.19985 | 2025-06-30 00:41:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| ee51deeb-170e-31ff-ac58-8349f0770097 | -9.08847 | -47.95882 | 2025-06-30 00:41:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0edc3b38-c224-3cab-bdf4-f0d1ce58e03b | -9.97888 | -47.80377 | 2025-06-30 00:41:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| baee5e55-c792-3a29-b780-acf03a6d2ae0 | -10.87212 | -53.75316 | 2025-06-30 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 0c849508-5a84-3023-8170-ff2bc581a989 | -12.61948 | -54.21304 | 2025-06-30 00:41:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 483ac613-78df-3105-91b3-86c1a4bd0c51 | -10.10941 | -52.19851 | 2025-06-30 00:41:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| ac70d1ab-5018-3a77-95eb-f3dfccb5ac6b | -11.49229 | -48.07957 | 2025-06-30 00:41:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 794e17ab-2d4f-329d-9ab1-1caa648e8a79 | -7.86006 | -47.87401 | 2025-06-30 00:41:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7a06649c-1d77-3956-924c-1de093beec90 | -9.2538 | -58.76621 | 2025-06-30 00:41:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d8ad9491-647e-3f69-8dac-25d87168bd5d | -14.03354 | -54.49282 | 2025-06-30 00:41:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 8a0039c1-cde3-3f10-84f0-62aaea63d65e | -13.08574 | -54.85575 | 2025-06-30 00:41:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| e69ffcea-14ad-3999-85cf-6263dc8abf9d | -10.09796 | -52.18842 | 2025-06-30 00:41:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2ea9ae98-6a99-3e1a-b171-be6846568960 | -12.07048 | -48.45411 | 2025-06-30 00:41:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| bb34ac61-927b-335b-a27e-fd25026fb85a | -11.9385 | -57.43063 | 2025-06-30 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 6ea160f3-20fa-3165-bdb0-665cbe490d2e | -12.07173 | -48.46309 | 2025-06-30 00:41:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| d38d822b-3a50-39e9-97cd-e867296e4dd1 | -12.07298 | -48.47207 | 2025-06-30 00:41:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 03f54d18-657b-308d-8e17-a202d0e1bd90 | -10.87282 | -53.76275 | 2025-06-30 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 5debfbc2-f0d3-3b8f-bd04-5dffae3f3dad | -13.43176 | -47.84105 | 2025-06-30 00:41:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 11cdd82d-524d-3845-9e36-9525e56a26d9 | -10.68215 | -49.13792 | 2025-06-30 00:41:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ea5237ed-7f1d-38af-ba7c-0cd142f7b640 | -7.25939 | -43.15681 | 2025-06-30 00:41:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 79607d53-be75-3108-b9cc-fae01be51d9c | -10.8702 | -53.73812 | 2025-06-30 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |


[Clique aqui para ver as próximas entradas](README2.md)
