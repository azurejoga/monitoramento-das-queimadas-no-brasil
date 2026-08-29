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
| fa4902d1-bc43-3151-aafb-9ed2b555d6bf | -12.19702 | -50.54647 | 2026-08-29 00:07:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3eb8ba0f-d5be-3c7c-9aa6-ef1f163ddb2a | -11.20815 | -51.28349 | 2026-08-29 00:07:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c665c1d2-13a1-359b-b378-5bdc572b2d85 | -12.4337 | -43.41173 | 2026-08-29 00:07:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| ebe929f1-70ec-343a-802e-6fcafc5f6366 | -8.97616 | -50.78639 | 2026-08-29 00:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a1df4e48-b37a-38cd-9590-fa07b87ac164 | -14.20296 | -52.83709 | 2026-08-29 00:07:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 4f091e3b-2b58-3673-8588-7477c4834bf9 | -7.27503 | -45.85497 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 43dcddf5-d608-3c30-be71-a2515ad86bb4 | -8.53462 | -55.35234 | 2026-08-29 00:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| e4c832f4-1539-3ca9-b04b-e6bfc3d2b2f4 | -8.60039 | -54.77341 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 9d2086a3-ec0d-394a-8fc8-a538998cfc56 | -9.21003 | -51.55951 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f93e868d-2212-3d85-a5ab-782caa985e64 | -12.1903 | -50.57265 | 2026-08-29 00:07:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3c713762-6cb9-3e55-88bf-3802cf95fc0a | -11.17834 | -51.26481 | 2026-08-29 00:07:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 968e8b12-3806-324d-b609-26544ffab4ac | -11.26734 | -54.04058 | 2026-08-29 00:07:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| d7d56374-4e66-3e45-b4a6-60db76c58e5e | -8.79999 | -50.50032 | 2026-08-29 00:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 77c1cb8c-6af8-38ac-9826-d2bb4f7a7157 | -5.59902 | -44.19271 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 7fd915e4-e011-3f36-a56e-dcf549dd3b76 | -10.82952 | -50.51569 | 2026-08-29 00:07:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cf2ab044-1d8c-332f-8b9e-f57f174365f1 | -11.26556 | -54.02675 | 2026-08-29 00:07:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| a6e85d14-52cd-30dd-9177-598c63390a97 | -8.11891 | -51.66029 | 2026-08-29 00:07:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8869fca5-62f0-334c-a71d-c8c3b559de0b | -8.97859 | -50.80423 | 2026-08-29 00:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b44fdc21-909a-368b-88df-cd33bf58e8a5 | -13.31918 | -48.19222 | 2026-08-29 00:07:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c7dd1cb1-fbde-3968-af16-3ecc7172a0ee | -8.59308 | -54.82288 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 730b7ea6-defa-35f9-92dc-728a1f5db13f | -8.53435 | -55.25829 | 2026-08-29 00:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 038a080b-1448-39c5-b84f-e85e90f7ae8b | -11.4932 | -45.10667 | 2026-08-29 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4870a5c7-ece9-355d-9c6a-30644279a160 | -11.27216 | -54.04816 | 2026-08-29 00:07:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 393ee7c0-baf0-32d5-9e28-d7b6bcd16dc4 | -14.26523 | -57.04165 | 2026-08-29 00:07:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 9db7c15b-2935-3d7e-8431-d98acf0b7a14 | -7.49755 | -55.30486 | 2026-08-29 00:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 7612ab7c-1202-3d83-b330-c711fc3f9d0d | -7.29757 | -49.97291 | 2026-08-29 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| ddb929a2-6781-3171-9dff-d93e90854198 | -10.83716 | -50.5054 | 2026-08-29 00:07:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 42f47662-b56b-3636-ae5e-61236f6f9cb7 | -10.75391 | -54.03996 | 2026-08-29 00:07:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3880cfc3-fe85-32e3-924d-b678d46d2fc7 | -9.20099 | -51.5607 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1c645dd7-dbcd-3bc1-8682-2122fd485c07 | -8.9862 | -50.79401 | 2026-08-29 00:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 83142548-f364-384c-bd4e-c0852e0f6070 | -7.2803 | -49.84834 | 2026-08-29 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 84fc7a11-24c2-3cb6-8090-faff06cb055d | -11.79377 | -47.66039 | 2026-08-29 00:07:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5b7a0b08-cf5a-3460-b7ca-95548e241965 | -11.20941 | -51.29303 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b5b0ed04-be07-3b77-8361-3a661e6f63db | -13.66002 | -47.73671 | 2026-08-29 00:07:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 8fd49794-847b-3413-9d06-5a5adf42a4c1 | -12.42759 | -43.40051 | 2026-08-29 00:07:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 8abd9aa8-2229-340c-9bbc-f1b8b5310f6d | -8.58946 | -54.79493 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 4f0f1c55-4af3-3e98-a3ca-612f172cc044 | -5.97688 | -43.75091 | 2026-08-29 00:07:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 6243d93a-2296-31e2-bf93-792d61917f43 | -7.53286 | -44.46455 | 2026-08-29 00:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d8643542-4fc2-37bf-9981-a4199b5acb56 | -11.02371 | -57.2225 | 2026-08-29 00:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e99a6ab7-83fe-3115-83a0-beefe56b18a5 | -9.43118 | -51.69951 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9d70baf0-ad3a-32c7-9741-913dab9de50f | -6.48682 | -49.90133 | 2026-08-29 00:07:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4b39212b-6518-31fd-9856-dd66d4251d31 | -10.80914 | -50.64454 | 2026-08-29 00:07:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 45e0c479-15d4-38f0-9b0d-ef01726d781d | -9.93342 | -60.42823 | 2026-08-29 00:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 702dd7d1-7cad-39c0-97c2-5a4e1dc18103 | -11.03486 | -57.26348 | 2026-08-29 00:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 239d0684-7e8a-3388-9b1e-b79c11e79297 | -9.15013 | -49.97478 | 2026-08-29 00:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2357c356-01dc-39aa-b4a0-61f4125dec75 | -9.40294 | -51.62601 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 75b8ab52-d89a-3dda-9211-bfaed1e10e99 | -8.58579 | -54.76664 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d450c1be-b6fd-3ab5-a584-05e4557a3abc | -11.17962 | -51.27434 | 2026-08-29 00:07:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1bd7e8c2-879c-3d71-a8cc-c6aee770dc55 | -10.80572 | -54.01956 | 2026-08-29 00:07:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e78d8276-d7f5-3c84-ab09-548ae43c60fc | -8.66865 | -49.55109 | 2026-08-29 00:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| eeba00fc-3d6e-3bc0-997a-dcb193d885b3 | -10.31403 | -49.9812 | 2026-08-29 00:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a19c402e-3d78-3860-a2cb-341f530aaf67 | -10.89936 | -46.6272 | 2026-08-29 00:07:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| e3018d5e-3da2-36d4-a550-9299ac0e1cd9 | -11.02846 | -49.68414 | 2026-08-29 00:07:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8b1453dc-4c77-304b-8601-9148bff73bf5 | -9.16015 | -49.98238 | 2026-08-29 00:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5dffb591-feae-369e-88fd-b3d0a9145cd8 | -7.34255 | -55.17265 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c70a4b51-ead7-33ae-9d11-1603f86c33fe | -10.89771 | -46.61589 | 2026-08-29 00:07:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5ac58ae7-73a1-333d-bc18-5f4d572959f7 | -10.3392 | -49.96852 | 2026-08-29 00:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 964ef465-2852-31b6-b963-fd03fc142eef | -7.2861 | -45.85327 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| b7b8b4a7-b317-343b-8fdb-9289c3372ec4 | -12.43046 | -43.41867 | 2026-08-29 00:07:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| f4e5bf9a-5b54-312a-9899-dcada1646762 | -11.19485 | -55.1 | 2026-08-29 00:07:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| d4ca8dd0-e7ed-3c27-a5c3-f420ddd0279d | -9.40419 | -51.63544 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6621c60c-a2e3-3613-bcc6-a64f91df355a | -14.20457 | -52.85005 | 2026-08-29 00:07:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 35.6 |
| e8a8fd08-557b-3200-848e-d4ab840a75cb | -9.40545 | -51.64495 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ca936f57-01e1-3b57-946b-edb4592b6af1 | -7.50879 | -55.30346 | 2026-08-29 00:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 6af59f7e-0c54-31bf-b8f3-e3bbdd032ebe | -8.6674 | -49.54213 | 2026-08-29 00:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 28f81636-f306-3a44-8744-64d471fc14ae | -7.27558 | -45.8484 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 79402d5a-2dea-31bd-898d-a586ff3c124d | -6.49691 | -49.90888 | 2026-08-29 00:07:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d1314375-a6f7-338b-adfd-808475733300 | -11.18218 | -51.2934 | 2026-08-29 00:07:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 0e4d56bd-b4d6-3396-ae34-7ecddd92a4d7 | -7.2863 | -49.95653 | 2026-08-29 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| fa7e7352-335f-3a1e-8815-7591c102c2f6 | -9.68983 | -46.54913 | 2026-08-29 00:07:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 23ac8d04-9812-3379-87da-b98f66d1b871 | -8.53659 | -55.36803 | 2026-08-29 00:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bec62b33-d7e8-390d-9287-1418f3dd4194 | -13.3205 | -48.20158 | 2026-08-29 00:07:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| aeb705fe-4861-3589-8948-8990b760a3de | -6.75166 | -52.45509 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7c782029-d3f0-3c41-90dd-283b36dd4f3a | -8.77085 | -50.50126 | 2026-08-29 00:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f7267ec2-2012-32d4-9d25-ea21adbc28ee | -14.48937 | -58.49706 | 2026-08-29 00:07:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| d136e896-64cb-335f-a588-9c3ebbd2111d | -11.02958 | -57.27103 | 2026-08-29 00:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c65c8571-816b-3b18-9add-b2d3556aeaed | -8.60739 | -54.83024 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 3c4ba17d-077b-3d17-a108-f83e1ee67852 | -11.25804 | -54.02201 | 2026-08-29 00:07:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 0242a953-1d91-36bf-801a-a3254d3e6da5 | -8.9533 | -50.81694 | 2026-08-29 00:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1dc8817a-4f58-367b-aa66-443ae12ac146 | -6.34535 | -44.09316 | 2026-08-29 00:07:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 41e661ea-44e4-3160-8e1b-a46ae5cdb960 | -5.65483 | -44.30504 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| cbd75361-3d8a-354e-9eb5-9a73941e986b | -5.33942 | -45.15718 | 2026-08-29 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 1b5c00a9-14e1-3f59-8152-f9939254fe76 | -11.01817 | -57.24084 | 2026-08-29 00:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 2e137745-c912-30ef-a50f-7b664488c3fa | -9.8672 | -60.31067 | 2026-08-29 00:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 94e70b0f-b73e-3607-a3bd-33075898301e | -6.75037 | -52.44542 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| c0fd77be-9723-3e00-b46e-6f2bbddd76ee | -9.97455 | -53.93506 | 2026-08-29 00:07:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 32961c2a-5a20-35dc-b319-bdbbd2152024 | -11.03209 | -57.23907 | 2026-08-29 00:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 902d69c2-af5e-38de-84bd-e0d8920067fb | -8.79878 | -50.49145 | 2026-08-29 00:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6a18a791-2231-38a1-985e-d956baaa286c | -11.48012 | -45.09407 | 2026-08-29 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 6eb81c5e-9769-3777-81a5-89699a1825ec | -7.27022 | -49.84064 | 2026-08-29 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bd7b39b0-0fe8-3579-bce5-deeb0116244c | -7.5069 | -55.28852 | 2026-08-29 00:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 6748e39d-3e33-3e00-931b-cf79ddbb8320 | -9.17924 | -56.98177 | 2026-08-29 00:07:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 9e8fe030-2092-395c-973d-be20685af214 | -12.76937 | -44.2639 | 2026-08-29 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0016c5ba-6e65-3331-af73-a298e7084631 | -12.42147 | -43.41384 | 2026-08-29 00:07:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| b6ac9037-848b-3961-b8f9-8e776b4ff821 | -11.2597 | -54.0358 | 2026-08-29 00:07:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b78fd422-429e-3f3d-b86c-67bdcba7f3cc | -11.70735 | -54.52686 | 2026-08-29 00:07:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2cd80585-a88e-3822-bcce-4bc2066a22ba | -8.95208 | -50.80796 | 2026-08-29 00:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 65e2bb62-c758-30fa-a482-dc24790cbc39 | -9.86911 | -60.30371 | 2026-08-29 00:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| ed5149fa-f3a6-366e-a37c-708f48297842 | -7.27147 | -49.84973 | 2026-08-29 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 15916360-c7dc-3d89-b459-9c2d51a7c09c | -6.50053 | -53.2687 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README4.md)
