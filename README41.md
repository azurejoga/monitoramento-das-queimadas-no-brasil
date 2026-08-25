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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9dde3ee-81ef-36c3-8ded-4c7e5f8dc913 | -10.58301 | -50.40832 | 2026-08-25 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 143f13bc-57e5-3f6f-90b2-fe64f79e976c | -12.71163 | -48.39206 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d1dfab2-b116-3b99-a101-a906dfb24bf8 | -11.49254 | -52.92144 | 2026-08-25 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9097e5ea-712a-373b-bbbf-2629c624af42 | -16.3996 | -49.93522 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72ec3a48-8322-37d5-80a2-0f9559e1b0d7 | -12.64249 | -47.79288 | 2026-08-25 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58e15dfb-2516-35de-9139-0733f89d1d92 | -14.39802 | -52.95466 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85d6a37c-5812-3486-8716-44f5dd678c6f | -16.378 | -42.97767 | 2026-08-25 04:27:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb8340df-04c2-3dbf-b91b-bdb9362f7428 | -15.29986 | -52.80998 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08546b44-b78e-39b3-b7ed-046c9f618c54 | -11.56322 | -46.97492 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 30d2cd2d-b16e-3bf1-9ad5-ba411537ab61 | -12.22849 | -43.12758 | 2026-08-25 04:27:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d4d1ff2d-4353-31d1-8137-54e0aa0e8c27 | -14.38228 | -51.96445 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d553b928-62a3-3d15-955c-b398065c7cda | -16.06505 | -50.46783 | 2026-08-25 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 793a77c5-e66d-37ad-a10d-a06b915ea6c2 | -10.77136 | -50.92765 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f660cc3-9f97-3eb9-b4c3-ad78730b8e44 | -11.7731 | -47.24882 | 2026-08-25 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d759158-5e56-315b-9214-8c6c03a6c81e | -13.35685 | -48.20499 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90edf98d-42d2-3df5-a29a-532a06e9be74 | -11.43809 | -44.54878 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 932f54ba-33c6-398d-a130-56298df1a540 | -9.67706 | -55.08857 | 2026-08-25 04:27:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 837e6837-f635-37b0-9cf4-23cccbd6d7e3 | -11.98306 | -45.91551 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ed6299b-dd9c-3bb0-b2cb-6dd7ab7c4311 | -12.78195 | -44.26817 | 2026-08-25 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 29bf0a72-59c4-37dc-9b6d-cc020599a4e9 | -12.7552 | -46.4453 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ed74e42-278d-3b91-9958-e86a8eb3fbbf | -14.53998 | -52.29742 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 707b210e-101b-39a9-aebf-1805e6c7ce88 | -14.38849 | -51.76848 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e32a349-922e-3b04-ab4e-96a6a318e1fd | -13.35906 | -48.2127 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7be10bc-6040-3e85-a119-5370acc234ad | -14.87192 | -52.65193 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f264b24-9710-3bfa-b09c-9d118d258efb | -14.30388 | -53.16771 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c66d4a6a-508a-3637-9d7f-880421dddf59 | -14.35476 | -52.92427 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 794418ae-3a95-3da4-86cf-b16ca443b860 | -12.77922 | -48.36455 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad387638-2b94-3ba9-a1fc-dac101cc154d | -10.91004 | -51.06969 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 5d1bddfc-79ce-3b15-b7de-b43e84cd1842 | -13.99878 | -44.04987 | 2026-08-25 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dc21e0d-4ae3-34ea-b165-4a8e93ca2542 | -12.74635 | -46.4583 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4009686a-3dc7-39cb-8bf2-4a750657e759 | -13.86785 | -54.04313 | 2026-08-25 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98da4a2d-cf2d-3095-af47-7832fa6d2025 | -10.85536 | -50.55599 | 2026-08-25 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e263c07d-0efc-39cd-a46e-ddc7882bfd68 | -14.62029 | -42.53368 | 2026-08-25 04:27:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7a11d977-68c7-3401-a0da-f3968dbfee81 | -11.56908 | -46.97572 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e61a3183-ef23-3913-8c5a-c099b754df67 | -11.09269 | -46.15528 | 2026-08-25 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e02e8c7-92f6-34ea-a2f7-73692d6e4d15 | -14.2793 | -53.20316 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 019fac93-c015-30bd-a062-467147e943ad | -13.36246 | -48.21327 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9ace378-415b-37ad-a48f-5defc0e923b1 | -16.39609 | -49.93455 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 06db1211-31b8-379d-9a49-f2491f72da0d | -10.56241 | -50.43354 | 2026-08-25 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11326524-5c46-3f49-b4b3-53c186857c3a | -12.58912 | -47.92033 | 2026-08-25 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71d9fb83-1595-3639-b058-8b05e7e9b889 | -11.82065 | -47.64514 | 2026-08-25 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1eb0474b-3fa8-3d47-858c-3b6c75a878e3 | -15.24204 | -52.79409 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 645fb2b2-8c18-3f34-9889-0820e2eed992 | -16.06143 | -50.46716 | 2026-08-25 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79aef576-f5f9-3776-8ef0-5a77cd24b25b | -14.54986 | -49.11486 | 2026-08-25 04:27:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe8b5f70-5eff-300c-bad1-e4151a0189e9 | -10.91834 | -51.0935 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8d660bb-e687-38d4-acf9-e3e1a498a9aa | -14.97128 | -52.7028 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96f9193a-d5c0-3693-81ae-c1393b0c4c22 | -10.79806 | -50.9246 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| b47e1e8b-de6a-313a-8450-c7fb44291fff | -11.99354 | -45.93524 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 572ab89d-5730-313b-aea1-7756d970f4c3 | -13.09245 | -43.3672 | 2026-08-25 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c44bc44-5b39-3f63-bd78-970c0e254718 | -9.15471 | -59.40041 | 2026-08-25 04:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5411b94-b52f-310a-a0d6-f72c00e9f5d7 | -11.56656 | -46.97547 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24e991e7-d0fb-3d64-ae40-4510e0f5bae2 | -11.43412 | -44.5294 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ada663bb-398e-3f21-a19e-3e91e7fe2302 | -11.39328 | -45.15125 | 2026-08-25 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3602c4ce-c04a-3e9c-9d5f-365161e57d73 | -14.90826 | -52.64248 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e7faf556-f346-3878-b3dd-5ac51ac2775c | -12.70756 | -48.39525 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 539bbfea-9082-3ca5-86eb-508de1910abc | -18.44561 | -48.41967 | 2026-08-25 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 571446e9-c630-314e-b62c-78a3ddae1145 | -12.69946 | -48.40154 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4af54c42-8cd1-31db-9145-706488d8115a | -12.70717 | -48.41901 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1fa6f3f-c7a2-333e-92b4-bae8c707b3ed | -10.47703 | -50.4389 | 2026-08-25 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 925be2ce-10db-35b2-b26a-dc0bfef8aed8 | -12.77794 | -44.27146 | 2026-08-25 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| af945b2a-4951-3951-ac9c-3b88e278e83a | -11.98086 | -45.90794 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3658c043-c00b-3312-abb2-9bd8ae416563 | -11.43471 | -44.54824 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6da31e4a-5c35-3a5a-a427-a96f3b22889a | -12.20914 | -43.18427 | 2026-08-25 04:27:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ad4bd3ab-6e37-392f-9b04-f8bf8d738c9e | -12.70161 | -48.40987 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 704ad289-64da-366f-902a-5f20323e6f62 | -12.8831 | -48.47832 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f1d9853-bbfd-3546-a124-a7ce924c8238 | -15.28049 | -52.79739 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 22900e6d-ec2c-3bc4-bc07-09f91adf8e14 | -14.72477 | -47.1535 | 2026-08-25 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db54f63f-5b20-37c0-9cb3-53746e24b5bc | -12.45093 | -43.40352 | 2026-08-25 04:27:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 564c5dce-7127-3d4c-8424-7142e198fe34 | -14.98334 | -52.68444 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a93cd2e-cd1d-3ca7-91cd-fdb8ad7df5e1 | -10.81871 | -50.92467 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e790c5a-3ed1-3dd6-92a4-3556968dd675 | -12.70782 | -48.41507 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 580d3366-4214-34c5-9781-2e59c785dcc8 | -11.43074 | -44.52887 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8853a3bc-c973-3c7b-add2-6f1bba15b13c | -14.54477 | -52.29443 | 2026-08-25 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a98e5300-7f7b-3f1d-9986-ec01bf91621c | -12.75464 | -46.44883 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a0907a5-0e80-3345-8774-c19a1ea140a4 | -12.88174 | -48.48647 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f05c19d4-bbc8-32ab-b792-f29d32eced72 | -12.75021 | -46.45533 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5b2fb53-0907-3ff3-9ed6-fed083f9ab9c | -16.41726 | -51.83795 | 2026-08-25 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8fe1eb1-36ed-382b-bf49-5a18883147a9 | -12.74242 | -46.48299 | 2026-08-25 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5b254df-3343-3433-869f-651cde58509c | -12.74741 | -46.47295 | 2026-08-25 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d737a75-38b9-3e05-9824-ea9b0d42547b | -11.16717 | -54.00101 | 2026-08-25 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a29f238-91bb-3f05-a36e-74449a27d5e9 | -10.78338 | -50.92984 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 581ed34c-c172-3519-b3d7-df04a7c69822 | -10.5305 | -50.77826 | 2026-08-25 04:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 633913f3-e86e-30bd-ba3a-d5878e41283f | -12.61189 | -44.63131 | 2026-08-25 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f92883e3-5386-38c1-9163-9c2da0fa1139 | -10.8027 | -50.92179 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6f671501-98f7-3a2b-9833-04e8ce4660ca | -14.36122 | -52.90075 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53f63c34-4581-3a48-ac73-1e1f3279c2ba | -14.35844 | -52.89159 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3038c427-2eef-3bdd-9bbc-1eb8cd8b9bb3 | -11.60185 | -46.75512 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc1d6255-08b1-3009-bfb8-22a5f234c42b | -12.879 | -48.4817 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 325d0038-6223-30f4-9dd1-880b86a703e8 | -13.16377 | -51.35984 | 2026-08-25 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec238ed7-0845-3503-a9c4-1fd96f6c5beb | -12.77965 | -44.25999 | 2026-08-25 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2b10c781-74ea-3eea-b210-d3c82b1604b3 | -10.79217 | -50.93449 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 3ef4b891-cb1e-36f7-88c0-9ae15e71fa0c | -10.7954 | -50.93202 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 41b19904-579c-329e-b883-908f667422ee | -10.93084 | -51.06978 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b939407c-ebfd-3c21-8329-207e305a98b9 | -11.43189 | -44.54405 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74ef7347-88a2-3447-960e-5eeda18dcd07 | -11.44091 | -44.55297 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2f9979c-a7b9-3a2d-bc70-d21d0be28442 | -11.90807 | -50.00437 | 2026-08-25 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c77f1888-a6db-3fc5-bdfb-37ad18a643ad | -14.35597 | -52.92981 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 695e3d27-91ce-33aa-8bf6-7e6ebb805b4f | -10.7928 | -50.93096 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c68446a9-35f4-380a-848f-cf3ae6b24cf2 | -12.711 | -48.39582 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4fc1990-0f9a-3314-bdaa-a1bb50513970 | -12.41147 | -40.92276 | 2026-08-25 04:27:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README42.md)
