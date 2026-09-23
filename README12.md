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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64de165c-f93c-3904-9540-88b222b56af9 | -6.3761 | -55.278801 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d8e6bd1-49f8-343c-9e91-6b3705bd6d86 | -3.75 | -59.307701 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4f319b4-fba1-3bfb-90da-1328f2fa3432 | -8.9307 | -61.479599 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2d8d041-bb6d-3f9f-ab16-9b39ea0f8b27 | -8.4967 | -57.6105 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f437a6b-dafd-311e-825a-e53d0258e1ac | -11.6888 | -50.931999 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 81f6108c-b804-3a6e-9d10-73e4f61afca2 | -4.2765 | -55.430801 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 067b380d-9729-3f82-9b97-0de46848ecb4 | -7.8716 | -61.160198 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 817a572a-33d2-397d-89f1-4c1c04a61c65 | -7.3935 | -55.218601 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bac9f7d9-a822-3fa5-9e73-7e3db08f2c8a | -3.0548 | -61.1703 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef1cbb18-341c-3489-9070-0b8bd7852b25 | -6.7292 | -55.063801 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6870f5fe-d9c4-35fa-ac17-0ff056713f8a | -8.2793 | -54.762299 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8c62409-69c2-3a6c-8e9c-eb1b42608527 | 3.6745 | -61.860401 | 2026-09-23 00:36:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 422e60cf-f754-31a6-99a8-9f83b8553658 | -4.3817 | -60.947498 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86292393-316e-3362-b61a-209e3e73f185 | -3.2088 | -46.929901 | 2026-09-23 00:36:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 855efa34-8990-36cc-bbcd-a77804130850 | -8.5977 | -54.6213 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed8ce1af-67a2-3ea7-990e-f69c7a422774 | -5.8046 | -57.722801 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92790020-a6cf-3d57-8396-fb6a4cfda481 | -11.2889 | -51.333698 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da8fca5f-f6e8-3df3-8f42-3a9cad2d0190 | -3.9768 | -59.770802 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bfbfa12a-6411-3a43-81ac-323b46534b53 | -6.4588 | -59.982498 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 162c6254-a1bf-365d-88f4-ccbf38fb7554 | -8.1977 | -54.720798 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c33964a-56d6-3914-b8a0-6bb4fb40c5f2 | -5.761 | -45.1119 | 2026-09-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c8b42cf-e94c-3dac-9f0d-4f004d7a98cc | -8.8357 | -50.490002 | 2026-09-23 00:36:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e252efe5-aa09-3884-9307-59883484b646 | -3.1798 | -57.868801 | 2026-09-23 00:36:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29ac5fd7-192b-327b-94d9-1d679f877b5f | 1.5673 | -55.8316 | 2026-09-23 00:36:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42587972-b6db-33f0-8a11-bd06d910dfc0 | -3.9358 | -59.633099 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03d5eb37-eb1b-3b2f-97a4-8bbf823a2267 | -7.8836 | -61.168598 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6199e867-c337-3d29-be58-2f868c0d4cdd | -3.2991 | -57.849602 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f14e0c77-9e2f-3cca-a1d9-de3733e1831e | -6.6058 | -59.950699 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6740ba6e-4049-37ef-ae05-1eca033b3140 | -11.6767 | -50.924702 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d1610a0-06f4-3dec-abc8-640be68a4cae | -3.1075 | -61.084 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83c66678-2ffa-33b7-b320-e4a78d11d90e | -4.2051 | -56.340599 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38696dde-8380-31db-b7b2-0d91bab8393d | 0.6093 | -55.969898 | 2026-09-23 00:36:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1369b325-d445-3961-94d5-a973593a0f1e | -3.247 | -53.951401 | 2026-09-23 00:36:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 988b710b-6f34-315c-9b2e-eb61f27a8a91 | -5.8685 | -52.0611 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 771b2aae-121b-3fb2-8e84-7c804892d1ef | -3.4783 | -59.564899 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c26f3e35-65ea-3248-802f-a7265c4da140 | -6.7751 | -48.664101 | 2026-09-23 00:36:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2b7eba8c-0057-329c-94c3-e6a851e2a579 | -3.7431 | -58.862598 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed6c2262-7cf7-3620-b400-c25d119d8dc2 | -3.4786 | -59.612801 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47f728f5-87d6-3b49-985e-cdfdbbca22a5 | -3.2243 | -46.951801 | 2026-09-23 00:36:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 996726c0-1645-3c83-a3c1-d34464961292 | -3.032 | -54.406601 | 2026-09-23 00:36:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 644e5c86-8d37-3a75-bf1d-856982e67407 | -3.7905 | -58.844601 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8cb7a37e-f2f5-3349-82ce-8fdfc276ba8a | -6.1589 | -57.695702 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9470be91-1d0a-336b-bd67-2828c731c5e0 | -2.4129 | -57.8951 | 2026-09-23 00:36:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed4ebcf6-a37f-33d8-891f-40198a671e5c | -6.0922 | -57.673698 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 283c46e9-154d-301a-8b03-f10e4be85b00 | -4.4518 | -55.069801 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8befee1b-2dee-3c97-a020-3c117b9f04e6 | -3.7415 | -58.8554 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4d4985d-7723-3412-9fc1-4235dba00a00 | -6.1389 | -59.9277 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b381b0be-feb3-3862-a6f1-e89779a2f7c9 | -12.8199 | -50.865398 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 739b3142-70f3-3bc7-950c-624c80599d01 | -6.8151 | -59.452301 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92b851a7-99d5-3232-9275-09d0fccd6516 | -6.457 | -59.973999 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e153b336-b380-3202-ae4d-6387cfacf2b3 | -4.2808 | -56.265598 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 449f30df-70f2-37b0-8b9b-75cd526ad9eb | -4.5116 | -54.970798 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2335d23b-b236-365a-8fc0-68887e958793 | 1.173 | -60.3563 | 2026-09-23 00:36:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1b60443e-8c24-39c9-8e84-bb94c0d07c15 | -3.7683 | -60.728699 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 25fd0244-3552-325d-b58b-51c73057ab1d | -6.6695 | -58.557598 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 41e52771-0011-3e6f-ad81-ea3a43c269e7 | -9.8533 | -48.326401 | 2026-09-23 00:36:00 | METOP-B | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76d7bd7e-0c2e-35c5-91dc-94b063353eff | -3.4289 | -60.4044 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f07be95-31b6-3161-9270-54d6f02db724 | -10.7086 | -48.695301 | 2026-09-23 00:36:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0367ee1a-1fdd-37f3-8d18-879a2166feba | -3.1961 | -60.420799 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd7d9da9-bd80-3385-a3f1-0bac05dff7d5 | -12.7764 | -50.855999 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a1332e9-db83-3701-9212-faf9e6843b6e | -8.1808 | -61.1712 | 2026-09-23 00:36:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0dfe50ea-a99d-3ec6-9c5a-46d38c29d5a6 | -9.8457 | -48.296001 | 2026-09-23 00:36:00 | METOP-B | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 984a797d-e968-3963-a946-a75027dc5bfa | -6.1275 | -57.739498 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f174bd0-4271-374e-b981-19825e0ebaa9 | -3.0713 | -58.393398 | 2026-09-23 00:36:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0547288-48eb-365e-80be-6fc24036ddd5 | -1.9174 | -58.256599 | 2026-09-23 00:36:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 137eb515-1a46-32f5-9a7e-b3b7a3900d71 | -12.4073 | -46.957199 | 2026-09-23 00:36:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ec2c24f-63f5-3b3f-bbf5-8a4a82dcb291 | -3.6453 | -59.2995 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f991440-2ed8-3f6e-a45a-8c8b8420a3ab | -8.8302 | -50.4673 | 2026-09-23 00:36:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76237b9b-14b4-37a9-9be2-4707b0868559 | -4.4463 | -47.9077 | 2026-09-23 00:36:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fe34200-c204-37fb-b632-cd4d9facc825 | -6.338 | -59.9464 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8bfa3111-0b29-3bb2-9df4-23cbe532d2ae | -4.2679 | -56.254002 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d6e3c94-477b-3e9b-8d75-920f6c0025d7 | -8.4503 | -48.696098 | 2026-09-23 00:36:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 411eb733-ba9a-347e-87dd-5d209305dfdd | -8.8585 | -62.4016 | 2026-09-23 00:36:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d8829a2a-acee-38bd-8d2f-bc941327f789 | -3.511 | -59.573601 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da83ef3c-e776-376a-ae8c-37318ff28f45 | -3.4569 | -59.2397 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e84ff6b-4874-3863-b961-07c55dfb0a3a | -6.6119 | -59.931599 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a1c9f2d-d92d-3a3d-a7c9-3d38f4e8d53f | -3.8658 | -58.812801 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d99ec51e-b99b-3f59-8e6d-9d6d4f1b2de3 | -13.9254 | -47.840698 | 2026-09-23 00:36:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e826950b-6652-38b9-8a53-a2e363b676df | -3.2254 | -53.947498 | 2026-09-23 00:36:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03655c07-c74d-3bfc-b399-9d61dbd403df | -6.8807 | -59.8466 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2974abc1-ecef-358d-94a4-72819c993403 | -1.6288 | -55.119701 | 2026-09-23 00:36:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f60c633-dbd4-3f4e-b759-9b89e16eb35b | -3.4406 | -60.4105 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e586b2a1-1f73-3836-8db8-5d52caed88b9 | -2.2341 | -48.758801 | 2026-09-23 00:36:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b229354f-243f-3f8b-83fd-5d86106649c7 | 4.1109 | -61.306301 | 2026-09-23 00:36:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6739650f-8f0a-39c3-8fa2-543ccf64a8b8 | -3.2878 | -57.844898 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ec27f71-afc1-369b-b3b9-ba33ec4f39c7 | -11.301 | -51.340698 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b07b29ee-7d76-3b3f-a731-8a9b394cb8c8 | -6.6217 | -59.929501 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd75abf2-3a1e-3d7f-82e4-66ee287afe57 | -2.9678 | -50.3997 | 2026-09-23 00:36:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd6c194a-67c2-35cf-a9d4-a444fe08e3ab | -5.7671 | -47.149601 | 2026-09-23 00:36:00 | METOP-B | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 715c61f5-2520-3869-bce4-256ced1b5c5c | -7.8814 | -61.158199 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1105536b-d669-3380-9d19-1e2ed93682f5 | -6.6334 | -59.935902 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 817fd8f4-e04b-3545-8c32-630b1965e5ec | -8.183 | -61.181702 | 2026-09-23 00:36:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 41a750d9-4ebb-3971-bc8a-bee141acb5d3 | -6.1974 | -57.7757 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c7f5765-b9a7-381b-9d86-87db879b4b0b | -6.1958 | -57.7686 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65ddf270-a122-32a6-b96d-93de74e34c14 | -3.3038 | -59.429401 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a558d3cf-51d6-381d-8c1f-ad18f13b41b1 | -6.186 | -57.770699 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7bdf6bd-0612-33ab-b8c0-afff1f647edd | -6.6493 | -59.9146 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 540c9789-699f-3322-9f78-c36fe7d2b64d | -7.4017 | -55.2094 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9373b20-14df-374b-9714-1e19af806e2c | -3.337 | -59.853802 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b89f95b-ec28-37f6-8c6e-5227b34ec936 | -8.9457 | -50.9044 | 2026-09-23 00:36:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
