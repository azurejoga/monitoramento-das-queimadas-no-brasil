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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a7c50cc-bdc9-312f-9f56-b949835e274c | -19.76883 | -57.95388 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| eeab9ca3-453f-3af6-9db7-fda217db5dd0 | -19.75457 | -57.95614 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8c3d1bba-f16d-331c-8fda-843049164218 | -22.67487 | -43.47765 | 2026-08-19 04:23:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 73220fdb-39e7-3ffe-9a23-6160a80edf31 | -19.73157 | -57.93764 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ef515290-918e-3fc9-a366-155a2de9eae8 | -19.75502 | -57.96191 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ec96b1c0-8991-3d33-b7d2-35da3d2148d8 | -25.46264 | -49.99868 | 2026-08-19 04:23:00 | NPP-375D | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 54123fe6-2c19-3a94-b3f3-8227218f0ec9 | -23.75623 | -46.80183 | 2026-08-19 04:23:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 99a8e9dc-d43e-3b17-96bb-e8df9ea3c02f | -19.75595 | -57.95038 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 31912e20-52e1-38ab-bf24-5a63539324fc | -19.75089 | -57.94287 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1d7a2cc1-755d-335f-bc0c-a6efdfa14da4 | -22.98479 | -50.02301 | 2026-08-19 04:23:00 | NPP-375D | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| d791dec7-860a-3878-9828-f3777b40c095 | -19.74445 | -57.94113 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1bfd7ff2-41cb-3e83-818a-75d6b59abcc0 | -23.7556 | -46.80565 | 2026-08-19 04:23:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 755ed607-5a15-34d5-886b-db12914ea8f9 | -19.7403 | -57.95842 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bd863f7a-ee95-3382-b330-1b3bb381b639 | -19.73019 | -57.94339 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7195bd45-b07f-32f8-bd85-497b6c0b0fdf | -21.44656 | -48.51215 | 2026-08-19 04:23:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c576d58d-aab8-3614-bb86-fee5fa7c89fe | -21.52868 | -52.00785 | 2026-08-19 04:23:00 | NPP-375D | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 694728e4-9def-3f7d-8e3a-c24bb474059c | -19.75637 | -57.95613 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cbb77842-13b7-3360-ac34-7659047538b1 | -22.981 | -50.02216 | 2026-08-19 04:23:00 | NPP-375D | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 3779e6b9-8a99-3d99-b384-7cccca874737 | -21.5243 | -52.00686 | 2026-08-19 04:23:00 | NPP-375D | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 7f36554c-bd3c-358a-b61a-6867226fcae9 | -19.75319 | -57.96191 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f194636f-ec7d-39fb-83ee-e3df8061784e | -19.75964 | -57.96366 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 44725c65-3c1b-3eed-988e-29da87466259 | -23.29198 | -46.16348 | 2026-08-19 04:23:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bc7cb523-6b25-3ca3-9167-8be5f1bda65e | -21.44577 | -48.51659 | 2026-08-19 04:23:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9bed840f-d332-3335-83c8-199f9f581c63 | -19.73839 | -57.94505 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4dfd81ef-2419-3b1a-a936-15ed771b50b2 | -19.74675 | -57.96016 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0c5842ea-3abc-321b-9ea3-e78477fed1cc | -19.73196 | -57.94326 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 816b8b4a-bcdf-343a-8054-e1c556bbcd1d | -19.74858 | -57.96014 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3ff32da2-9347-38d6-96c2-c5638ec20acb | -23.31148 | -47.53522 | 2026-08-19 04:23:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6630d661-9534-31b5-9520-8a75e845a2db | -22.36412 | -46.90733 | 2026-08-19 04:23:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3bbe6c78-113d-33e5-b0ba-24271ce8fe7d | -19.74169 | -57.95265 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b3f3345c-48b8-3e49-8454-4979f13c7570 | -19.74618 | -57.94105 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| fd092d86-4a8c-335b-8172-7588169c193c | -19.74349 | -57.95259 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a5d4952e-cae2-3270-9948-a9d36b82d472 | -21.44938 | -48.51731 | 2026-08-19 04:23:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3613bd3d-5211-3b20-98ca-dff1cf218e2a | -24.76615 | -49.08878 | 2026-08-19 04:23:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c78e3503-6e78-335f-81d6-f12dfabf818b | -23.71078 | -46.82191 | 2026-08-19 04:23:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 100a20a3-fdeb-3a92-b3b2-5bbc37b9d614 | -19.75261 | -57.94281 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3c1f6a4f-d0bc-3c4c-9b6b-3ebfd0629104 | -19.73801 | -57.9394 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a43b517f-c804-3501-9f8d-c90aa2545972 | -19.74813 | -57.9544 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0358eabf-2d78-3ceb-bee9-6aeeabda8994 | -19.75771 | -57.95036 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4eb70d8f-8223-3250-b998-6a98b8572e43 | -19.76609 | -57.9654 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 20c288f9-4877-3970-82dc-0470e52d3125 | -22.91349 | -47.21892 | 2026-08-19 04:23:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 205c83e4-cd82-3ed5-bc05-3903331a8d49 | -23.80763 | -47.16563 | 2026-08-19 04:23:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8af1da12-72d1-3dc4-a376-ec2c82cedb6a | -19.7333 | -57.93752 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2e6b272d-9eb9-30a3-aa12-6ca2117c13c8 | -19.73974 | -57.93929 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 88423545-8fdc-3fd8-8cd9-6bdf22954131 | -21.40342 | -48.71218 | 2026-08-19 04:23:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cd444f3-edc2-3179-8e06-51f7aa450550 | -23.75895 | -46.8063 | 2026-08-19 04:23:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 82d5ef92-c3b8-377e-b23d-a881f1a4ea70 | -19.76239 | -57.95213 | 2026-08-19 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e9a41396-685b-316c-a9b5-bd3874179047 | -29.1402 | -50.39508 | 2026-08-19 04:25:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| dae984da-221b-32d2-9059-ad962b24848e | -29.14103 | -50.39054 | 2026-08-19 04:25:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| e1b8d876-19f9-3aee-8b5c-01bd17a44a4a | -28.59649 | -49.87258 | 2026-08-19 04:25:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3bef292a-3504-3637-8c41-86a2469a22b2 | -9.4257 | -60.416 | 2026-08-19 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 5cad319d-9714-3557-9331-17701d654288 | -8.5787 | -54.7364 | 2026-08-19 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2c0561b2-df00-39ee-a7dc-5006f6e21181 | -5.4317 | -48.4212 | 2026-08-19 04:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| dd63d00b-c76e-3f44-978a-9482aeff1ede | -8.5413 | -54.7389 | 2026-08-19 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 9fbebe64-a434-3ee5-a7f4-213d1686fc59 | -8.5412 | -54.7591 | 2026-08-19 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 5298c5ff-094f-352f-891f-31511f36c05c | -8.56 | -54.7377 | 2026-08-19 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 59f4128d-6f0d-322b-8598-04c019b13e96 | -5.9198 | -43.6264 | 2026-08-19 04:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 03f06f90-ccb3-3e67-bbec-b6122ab6022e | -9.406 | -60.5711 | 2026-08-19 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| ba16054e-8d87-3990-a8e3-a8916fd97b4a | -8.5785 | -54.7566 | 2026-08-19 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| ea4f68a3-b7a4-37f0-b302-b09a208a162c | -8.5598 | -54.7579 | 2026-08-19 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 0cb8ddd6-eafe-3ebe-9198-bfa27efc6f0c | -9.4256 | -60.4353 | 2026-08-19 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 47e18324-b191-32e9-945a-352f8e8d7883 | -5.9994 | -57.8639 | 2026-08-19 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f441c5b1-0b7b-397e-8628-4a841f32de54 | -6.0912 | -57.9187 | 2026-08-19 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 4c2a56a2-08b5-3771-958d-6ec04c392559 | -5.4319 | -48.3996 | 2026-08-19 04:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 8a165a9d-01b5-3729-8311-fcd19cc800cb | -6.0728 | -57.9194 | 2026-08-19 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 5182a19c-4c11-3b51-a1c2-808681b03358 | -9.4061 | -60.5518 | 2026-08-19 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| aed3916f-064f-3418-b9c7-3bfc2a015f55 | -9.3875 | -60.5528 | 2026-08-19 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 11032e26-a857-3e17-bd1e-d8d99efed67e | -0.98038 | -47.49972 | 2026-08-19 04:36:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d48dbdb6-90e5-3c22-a144-aeecbb984c45 | 2.79812 | -50.93309 | 2026-08-19 04:36:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e01b00e-1717-3b5c-8011-89176aa3dd2e | 2.80214 | -50.93247 | 2026-08-19 04:36:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7a1afdd-aea9-3b52-90e4-d1728126051f | 2.8016 | -50.92898 | 2026-08-19 04:36:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c88aa13d-219d-3bee-83a6-88c722fbb427 | 0.71716 | -51.37386 | 2026-08-19 04:36:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b9ee178-f695-3e3d-9ac4-5cc59e9b6651 | -6.80247 | -59.4505 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da0f69b4-2734-34c0-b35a-86e893f1a299 | -6.75625 | -59.15908 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8664a7b6-e877-335d-81c4-9b8a33e7bd01 | -6.88849 | -59.05965 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbc24cd1-e4c2-38c0-bbce-a69ed70ea54e | -6.00293 | -57.84296 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e7d8d27-db2b-366c-925a-598b96fcb7c7 | -1.26398 | -55.66475 | 2026-08-19 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 487571bd-55cc-3f25-b536-3d7ec26eeb08 | -6.13766 | -57.85159 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ddaf265-15db-35c2-a808-5629fab8c296 | -6.14122 | -57.85634 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b84b6ed7-13fc-333c-9874-9b25583ba0c8 | -2.82478 | -52.29407 | 2026-08-19 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ce3213a-5446-3608-9f2f-2d8be8efa3de | -7.6153 | -49.92569 | 2026-08-19 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aee6566a-2aef-330b-bb5d-315ffff73c53 | -9.11627 | -46.04553 | 2026-08-19 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2dc875d-2b8a-3011-b5d9-835b02e49e20 | -6.70202 | -58.93845 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 434c1116-aa8d-3634-bd1e-ccabab9530e9 | -6.84151 | -58.998 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b68a1fda-d14f-3bed-91c6-bd8a80290e97 | -6.13847 | -57.87143 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e103a9da-ce12-3266-ae5c-b66fbbd0c738 | -6.02125 | -57.80412 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b8ff9a9-b4c4-30b7-9a8e-ca0932a976ea | -7.25347 | -44.21437 | 2026-08-19 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab2fffec-9f25-31cc-8bce-a5802cdfed2f | -7.05291 | -41.43414 | 2026-08-19 04:38:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c7a511ff-a1bf-3481-8362-a6467732adea | -6.14065 | -57.86742 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d70630d3-e77d-39ac-9b89-3a0fd9f65a76 | -6.88087 | -59.05116 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e678629c-9f52-3dcb-826c-74a9241d5d36 | -5.91411 | -43.63194 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f2cc2f6-d1ac-3b7d-9764-45f61673585b | -7.62965 | -45.71867 | 2026-08-19 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 760c1d8d-a82f-359c-9e98-e477b58fada0 | -6.9519 | -59.0485 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45e0b339-ea00-3869-9ac0-fa63f07f9066 | -7.09437 | -41.37007 | 2026-08-19 04:38:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 13d02a96-1908-33e9-a60b-00576424e377 | -7.02297 | -45.89725 | 2026-08-19 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c67ee16b-dcf3-333f-ab16-c80a967bdfa9 | -9.11337 | -46.04089 | 2026-08-19 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ede9c1c6-1ec3-39d5-9c38-2cf795ad37c8 | -7.18613 | -43.45107 | 2026-08-19 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ad7c7298-7ffd-3a68-b7b2-722ba5f0b17b | -6.13698 | -57.84803 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84142b95-09c8-3aef-8a68-4d28054c1a31 | -6.00095 | -57.85423 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38cc09a5-c069-3080-9bf2-97e18ad7cf00 | -3.97537 | -47.21022 | 2026-08-19 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README32.md)
