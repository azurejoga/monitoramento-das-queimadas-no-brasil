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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44c233c9-6157-3bc8-bdf6-fd64bb7a7143 | -10.79724 | -44.24855 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| f2625b2c-3994-3cfc-9787-5f2dd28a9af6 | -12.2011 | -49.63572 | 2025-06-30 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1d0774f8-dffd-399a-b436-772a8ec4958a | -12.06157 | -48.46232 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 665340a4-a670-3159-9cd8-26742e25d591 | -9.09454 | -47.95975 | 2025-06-30 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ac090be0-a8f9-38cf-99ac-6106c0fba214 | -14.54278 | -46.62056 | 2025-06-30 04:14:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a692bc8a-4a98-320c-9140-7017e0f23625 | -10.55715 | -52.0461 | 2025-06-30 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 756e4bc4-2c6a-3749-82c2-521ecd794328 | -9.09251 | -47.9669 | 2025-06-30 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97359af3-2a1f-3f8f-b574-8144f4c4cdd6 | -12.62571 | -54.21518 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8cdb0c78-217c-39ca-99e8-c1f9860e06f3 | -10.10558 | -51.56863 | 2025-06-30 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e0515b0-a2ab-3f49-822b-1ff731227632 | -10.87409 | -53.74676 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adbd7ee1-6a13-3655-bf90-413b20da9bc2 | -11.20633 | -55.92473 | 2025-06-30 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46585d7c-5ba3-397a-b419-b314f17dae5e | -10.55214 | -52.0361 | 2025-06-30 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 894821b7-44af-3786-8e64-678c9be12ad8 | -7.63844 | -44.66472 | 2025-06-30 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 857be53d-58b9-32bb-bbeb-6d32d631523e | -11.02462 | -56.26778 | 2025-06-30 04:14:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a572d5f-c7b2-3b51-8567-cebca24b7d86 | -8.54583 | -48.26073 | 2025-06-30 04:14:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 80e72b4d-ca54-3783-9a0c-bcbf94f3f27d | -12.19773 | -49.63133 | 2025-06-30 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4483c662-278d-3cd5-b8a6-e77487d0e073 | -10.55495 | -52.0479 | 2025-06-30 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba37e5ea-ef16-3318-9001-63e7cabe2d15 | -10.79417 | -44.24417 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c350aa8f-845a-34f3-9b99-ca717776b88d | -10.65022 | -44.48962 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 186d0544-e7f0-3404-99b0-2b22c5887100 | -10.12974 | -57.77674 | 2025-06-30 04:14:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 920ab0fe-1f56-39bb-8517-3915669c7461 | -12.62823 | -54.23067 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29698379-9a44-348a-9aff-5fcd6046fa7d | -11.59122 | -44.66113 | 2025-06-30 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bb7cd43-f324-359b-98b2-bb2c353b59b2 | -10.55597 | -52.04244 | 2025-06-30 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1cf2e3c-c28c-3d27-83f0-fdc133726c90 | -12.60589 | -57.87268 | 2025-06-30 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c858129e-3243-3ea2-9df9-b35ddf20713a | -12.6239 | -54.21516 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5f3aceb1-a8a5-3c2c-8e4e-f0c38d44e52f | -13.432 | -47.83232 | 2025-06-30 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55aec20d-9b22-39ca-b31d-4cad134ca8d6 | -10.86331 | -53.74455 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d951bed-b7e5-3068-86f0-60f1664e6cd7 | -11.92868 | -57.44617 | 2025-06-30 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f469385e-03f4-3011-ac5f-5906c3406da5 | -8.71208 | -47.85326 | 2025-06-30 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92f43a87-5649-3f34-86b8-d07723aa758f | -12.62652 | -54.23069 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15aa0c5b-86f9-3a9d-bace-d5f635b8ecf6 | -8.08931 | -46.85307 | 2025-06-30 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b30fca37-bcc3-3e4f-a0ea-9ceeac7b9360 | -10.87107 | -53.77255 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| adf1fde1-338e-3a0e-ba2e-e5ed9684c8d6 | -10.85664 | -53.75033 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15df4dff-346a-35fa-befd-f33022d176f3 | -10.79775 | -44.24511 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 37576e8e-0cd4-3e2a-aad3-ea4c28d69524 | -12.62252 | -54.22238 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| fdd3d678-f51b-372f-935b-a00b02f4a980 | -8.09441 | -46.86709 | 2025-06-30 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72b40651-3068-3bc7-af65-9a0540e66e8c | -9.77959 | -47.80685 | 2025-06-30 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 831ad2fd-2413-3315-95ff-1fc7cb0b997a | -12.08356 | -43.35796 | 2025-06-30 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff9af070-defb-32b2-a2a0-6e6b9deae9d7 | -12.06611 | -48.45834 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 644a847b-51fe-3adb-979e-eeab6d2b95f4 | -12.76017 | -44.40131 | 2025-06-30 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| af8b65be-149f-3efb-9140-4a63003d5c92 | -10.86946 | -53.77151 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb53789b-c01c-3358-b75f-b048f45efc22 | -12.62459 | -54.21157 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 03ba1788-9145-38be-aca8-0a89e41ebd4a | -7.63232 | -44.6601 | 2025-06-30 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3635bf7-c073-3055-97f2-219e0db4ed67 | -12.19709 | -49.63494 | 2025-06-30 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| df86af8c-95ca-318d-850b-1b25f4bd345a | -10.65409 | -44.48666 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fd9cbe32-96d9-3470-ab17-c25fab04f122 | -12.06832 | -48.47108 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d615a3c7-c585-343f-b9d7-b9273db11500 | -13.00915 | -53.41372 | 2025-06-30 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f62527e1-1f20-3a6f-84ac-189417a8dc41 | -10.12277 | -57.77535 | 2025-06-30 04:14:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c67f9b7-b59d-30e2-a4eb-89236be4256d | -11.93534 | -57.44746 | 2025-06-30 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5c65ad97-dc89-34bd-babc-03ba316bedca | -9.15764 | -48.30627 | 2025-06-30 04:14:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fabc45f6-b77f-3650-a43a-4296f6fab9f1 | -8.8586 | -47.95388 | 2025-06-30 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2738da1-d006-3fce-9aa5-4376c13a343b | -12.62113 | -54.22963 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f536e9ce-6b70-3ff3-90de-dff439109c68 | -11.20689 | -55.91685 | 2025-06-30 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df06681a-12c5-3b08-8092-2e1216691576 | -11.20112 | -55.91874 | 2025-06-30 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d00640fe-44b9-33bd-89f5-c3c604e52422 | -13.00857 | -53.41677 | 2025-06-30 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 372dbf52-bccc-3e8e-a0a8-3d0ef0577c97 | -12.62861 | -54.21983 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 13995685-ba98-3b5d-b558-da4b5b4f99eb | -10.85382 | -53.73555 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 312ec948-71a6-3a57-9792-00bf9f48770e | -10.80547 | -44.23918 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3b8e2e0b-8a9a-3c14-8da3-b93be86adf5c | -10.87382 | -53.75838 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c94d14e-bbc8-31d0-b990-f4de1cc1b27b | -10.86267 | -53.74799 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d20db1e-2181-3b04-b32b-c8b8bdcecf98 | -13.0125 | -53.42393 | 2025-06-30 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce182309-a103-3c84-a52b-707849531ebd | -9.08997 | -47.96375 | 2025-06-30 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69a29b20-748e-306c-9a47-aefe90390431 | -10.15866 | -53.92387 | 2025-06-30 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43c7f27b-b728-3b68-bd10-96dc9f80a69b | -12.76348 | -44.40185 | 2025-06-30 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f33c2a52-f1d0-3ca2-a2c8-400044b5ce02 | -12.63398 | -54.221 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fce84bf6-41ac-3c93-a1ee-06fd632e01ce | -10.86202 | -53.75145 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3085c08d-fbb6-36e1-b2e5-d4d95d15aa82 | -7.62788 | -44.64491 | 2025-06-30 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e18c2754-bc6b-38eb-8a1d-61b8384a834d | -10.85986 | -53.73319 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f883ac23-ff11-3d55-b1c6-8f1c986ce20f | -9.14235 | -46.36638 | 2025-06-30 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1de083a5-7584-357c-95ec-8051244cbbd9 | -8.01161 | -47.40268 | 2025-06-30 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72a587c0-a2ca-36ac-9fad-5927974ddba2 | -9.09332 | -47.96224 | 2025-06-30 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b3ea8eeb-fb54-3f08-b9ac-f564cf80102c | -7.63067 | -44.64897 | 2025-06-30 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 158558f0-b38d-36f8-995f-e27d2114b338 | -9.15888 | -48.30342 | 2025-06-30 04:14:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb4321be-77c2-320a-84b7-d47a51076568 | -11.84561 | -43.79808 | 2025-06-30 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16c12d5a-6896-3e89-90a8-35bac52c13a1 | -12.62182 | -54.22601 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35831eda-ac5e-3f46-a7a2-62a34e8fc98b | -8.08718 | -46.86572 | 2025-06-30 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08489d49-bde5-3840-9ef4-4ca6b7fd03a1 | -10.54746 | -52.04424 | 2025-06-30 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 271ff7b0-209d-3f01-9234-429d1c2acd13 | -12.01978 | -47.77388 | 2025-06-30 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2d0ffff-3b80-3499-a752-6b872db78815 | -10.87062 | -53.73538 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f564cd09-e06d-385d-a3a0-5c11ca47ee41 | -12.61921 | -54.21048 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 127a0cc0-2dbb-3c44-8eb2-4913af0a5cd6 | -10.86137 | -53.75493 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee2fbf6e-eff8-32dd-b65d-7722646c6815 | -12.06699 | -48.45657 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b998022e-fb24-3875-b220-83f6596b66ec | -10.55112 | -52.04153 | 2025-06-30 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19958353-1bd1-34be-a037-5dcfb27a1248 | -10.84713 | -53.74141 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4a2c651-eb3c-3d5f-b453-3f6fb8d83cde | -11.19403 | -55.92233 | 2025-06-30 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b00b256e-e4b8-3cc8-9f9e-3e1eafd0488b | -10.87713 | -53.77018 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdb35188-5b77-3ed5-8dfd-eef0d4c68d20 | -12.06455 | -48.4676 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6753f670-a159-3397-ba9c-3145b4cf36b3 | -14.43394 | -45.16053 | 2025-06-30 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b03bf6ae-2402-3a3f-849f-0510d68c04e5 | -13.23643 | -49.83366 | 2025-06-30 04:14:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de1a287c-7194-30b9-b587-3f212ff9d876 | -12.62355 | -54.226 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd4acaa5-a32e-3be5-8dcf-86d328e2aa20 | -11.02359 | -56.27296 | 2025-06-30 04:14:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e97c2f14-8a71-3e4d-8aa4-5654821abacd | -8.54497 | -48.26573 | 2025-06-30 04:14:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8258edd-3a68-38e1-a5af-e7cd46d11efa | -10.44622 | -47.44843 | 2025-06-30 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cef2a1e2-042e-30b6-b4e2-2275533ca2fd | -12.09272 | -54.66708 | 2025-06-30 04:14:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dabe0f15-b08c-3329-b3d8-d93d0547f2d2 | -10.85857 | -53.74007 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e57fcfa-6696-33f3-9afd-333593466eaa | -7.8666 | -47.13048 | 2025-06-30 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36329f2f-7873-3fb5-a0b9-e38d3320541e | -11.2002 | -55.92345 | 2025-06-30 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e175780-290a-3770-a004-23f4ca68a6af | -12.10352 | -54.58134 | 2025-06-30 04:14:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55b1cff5-7bab-3279-9b28-d81060771319 | -10.85792 | -53.74348 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6afaf1e9-22fd-3707-b8a6-17e35b2ce510 | -12.06001 | -48.4716 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README8.md)
