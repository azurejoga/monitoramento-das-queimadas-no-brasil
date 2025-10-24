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
| d583b343-ba21-3e53-b9fb-5546608cf5bf | -13.04433 | -43.37852 | 2025-10-24 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a507b132-cef0-3b51-a736-b44f54bafc74 | -10.89729 | -48.04488 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b053679-25d2-3a34-bd1e-5975aa91748c | -10.9798 | -50.36363 | 2025-10-24 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9e3245e4-1269-3a7a-ba46-345c6fe2d9af | -2.42946 | -49.27756 | 2025-10-24 03:49:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4dfd802d-f4f4-3732-83c9-065854faf180 | -10.47008 | -49.10107 | 2025-10-24 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86590119-2cbe-3e86-93dc-67320e0a3df5 | -12.05956 | -46.41523 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 919552c6-00ff-3b3d-8e18-8fec2448a895 | -12.82178 | -50.96959 | 2025-10-24 03:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df028dd2-d5bd-3ada-8026-413d90706e5a | -10.01065 | -47.10368 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 537d275c-ce5b-35ea-83c3-d3132d47f81d | -3.02373 | -49.45143 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c4ac0d1a-7b94-31e5-8b31-85e2bf7b30d0 | -9.60673 | -46.88771 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a23d117-2c49-3bcc-9de4-76f52d0047d7 | -3.57812 | -43.37668 | 2025-10-24 03:49:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1aae0716-d161-370d-8ca9-f15bbc7b5a93 | -9.24094 | -45.58767 | 2025-10-24 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 641e1a34-c87e-39f2-895a-0b605778df5a | -12.84889 | -48.55472 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd98755a-e5ff-35de-83cb-5a40b607ff3b | -12.05744 | -46.42643 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b8ec33c5-fa18-3ace-988b-28ab486263a1 | -13.35679 | -47.97412 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| adcd3f89-616f-3a07-9064-ac58478bf15c | -9.09225 | -46.53358 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7298064-a256-3032-aa36-cd4adf9dfbd8 | -9.64013 | -46.88762 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9b8fa45b-a22c-3f83-b9e8-96fa67dc22d6 | -9.63764 | -46.90123 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05ab7d3e-bff8-3755-b719-25c6410f543f | -13.18719 | -48.48973 | 2025-10-24 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2abc186a-ddc8-3da3-a04c-9bbb34efe458 | -10.90315 | -48.045 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82320cb8-6abc-3a0c-a5ad-69abf46eb6c7 | -15.57311 | -47.71545 | 2025-10-24 03:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18a9c585-3f2c-3352-a1f8-d3e6a6ba18e4 | -13.26411 | -47.8919 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ff9ffd6-9537-30b9-a39b-b97f06c759bb | -13.40443 | -47.35967 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8908639d-6eae-3b88-bdf3-c74e936f6681 | -15.44475 | -48.5744 | 2025-10-24 03:49:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c7d793e-8ccc-3529-a705-ac7448a9c17c | -13.66861 | -47.95776 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b596289-bca5-371e-abe3-b8667b1ab11b | -12.95649 | -48.50014 | 2025-10-24 03:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c487c67e-2ed6-3d8b-bd80-f188d0af3079 | -12.88818 | -43.43157 | 2025-10-24 03:49:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 039939e9-e9f7-3252-bcf9-91fe363e0e60 | -9.26155 | -46.46975 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c447e945-de6a-3fd1-99f8-985ebcdb3265 | -10.86998 | -44.41428 | 2025-10-24 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55bed218-e7b8-3799-bbca-89b0c081a88b | -13.1912 | -47.752 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ea94b65-50ad-3037-8ed1-057a0a7e2cac | -10.87227 | -44.41086 | 2025-10-24 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3849b52f-263c-3b8e-b45a-682f881d2a99 | -11.05969 | -45.39326 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b46cabcc-7e52-3772-8289-d388f4c5d737 | -10.04168 | -47.08742 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 532ae393-539a-374c-81b2-5460ddc88ea2 | -5.0479 | -41.19725 | 2025-10-24 03:49:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1274d337-279e-3e3a-88f4-8590ec11a57d | -15.61391 | -45.91785 | 2025-10-24 03:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c24c66a0-7fc0-3774-a02e-f4923a1285d0 | -11.35427 | -45.95873 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| dbddb1a5-d5fd-338a-8198-3326b5df82ad | -4.91454 | -47.32603 | 2025-10-24 03:49:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ce024d6-c917-3503-a905-c905ab484d4c | -3.47266 | -43.24523 | 2025-10-24 03:49:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d66625c-ea2e-3d4d-8e69-0de21eb7cc76 | -15.95477 | -49.60706 | 2025-10-24 03:49:00 | NOAA-21 | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e87cee76-06ea-3e5b-9c8e-e97d6eac307f | -15.56958 | -47.71941 | 2025-10-24 03:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac04c75b-f84e-31c0-977d-bad4bde567e1 | -5.54984 | -41.35106 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36cfb401-6d1c-3d8d-9c16-46b908ac7b45 | -3.13317 | -49.51807 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7a9c0e52-7e4e-3af0-980a-cc8d612d24a7 | -4.81295 | -42.75144 | 2025-10-24 03:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 16c629ea-a152-3984-9945-6c40c0438793 | -4.85639 | -46.73005 | 2025-10-24 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24581bec-7e89-3da5-b898-97018810ace0 | -15.95161 | -49.60094 | 2025-10-24 03:49:00 | NOAA-21 | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49bef528-48e7-38ca-87a2-09dcc31223e0 | -9.60405 | -46.90217 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d49773b3-4fd7-31b9-a056-070468d50844 | -3.13105 | -49.519 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c193c4b4-6573-3a88-820f-16314acc9cd6 | -15.13254 | -47.9395 | 2025-10-24 03:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f8dc63a-cf34-3d24-931a-96b88469a030 | -14.46969 | -47.90834 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14c0e46b-ed1c-33c2-8ce8-8e47bad3d94f | -13.53603 | -47.54805 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55c716cc-bace-3112-8ff0-123e1f60bbb2 | -15.84036 | -49.10333 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76222b14-73e2-3fa6-affe-1c3fff10fb32 | -5.55042 | -41.34761 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 77088bd0-6d0a-364c-bb98-e460ead23fda | -15.61296 | -45.92278 | 2025-10-24 03:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79e51f7c-d8c6-3c90-a1a4-3a485f3c153f | -4.85053 | -46.72955 | 2025-10-24 03:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3f3efaf-ca56-3698-a436-033511b5ada5 | -13.89782 | -48.3923 | 2025-10-24 03:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a99d81ca-f482-370b-a7f8-67511e9af9db | -14.43809 | -50.95355 | 2025-10-24 03:49:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 71bbe65f-ba44-3aaa-9387-b4b20ad31a8d | -12.03347 | -46.91836 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93953ed4-fb3f-3aaf-84de-7bc60883a619 | -2.42822 | -49.27705 | 2025-10-24 03:49:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0a911ac9-6e83-31bd-a19e-24df26898700 | -3.02495 | -49.48632 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab0291ed-186d-3cce-8349-bd6d5004cc3a | -12.82115 | -50.9677 | 2025-10-24 03:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f42a7832-9ea5-3cad-9431-9080bff6fd71 | -9.25684 | -46.46571 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5efac807-f623-3025-b597-ca8e492a1948 | -5.8396 | -40.7989 | 2025-10-24 03:49:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| df2635a7-6dbd-34d7-b6bf-c8683483740e | -13.34679 | -47.9678 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af391234-c14e-3e29-a7c6-6ed4c733cb35 | -9.24041 | -45.59054 | 2025-10-24 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fdcd64e-df9c-37f4-9306-a2fad193d7b2 | -12.80485 | -48.62749 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29c1252f-5fa5-351b-997c-7bed803c529f | -9.27777 | -46.97138 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 370c55f6-0acc-3bc4-9cee-5eab476ddcd3 | -15.84119 | -49.09924 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54a22889-a7f0-3e6b-bb28-38be53c2b812 | -15.52122 | -50.01278 | 2025-10-24 03:49:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1223dac-da54-3e4d-a41b-53ae0d5498a5 | -13.28138 | -47.48889 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac6467ff-6793-3b8c-bdc1-ee3b3aa595e7 | -16.0968 | -45.10211 | 2025-10-24 03:49:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50d3ac8a-0654-3cdb-bfc2-982162a1c85b | -12.83121 | -48.64349 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9242201-37c3-335f-8be3-e4db015d5bb0 | -12.07056 | -46.43923 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2146adc0-4f80-3500-aff9-418644c8fedd | -10.88995 | -48.05247 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f8cde31b-0121-34b0-b055-4f1310ad988e | -14.47535 | -47.90745 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ce6e566-a61e-3122-a399-7a55df69713e | -4.00174 | -43.75618 | 2025-10-24 03:49:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81f1fd5e-8bb1-3454-905c-9c4119e11018 | -12.06621 | -46.40743 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf3f09d7-1a91-3a16-ba08-63ab01b4b0a8 | -10.04446 | -47.10278 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a8dd922-7d1e-364f-ad22-498e405a7a9d | -10.62666 | -48.08186 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3e4e7948-dc10-3c4c-895c-b22bed4562af | -12.15492 | -47.0256 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff708fe4-57d4-3d09-aa85-7ca37b141d37 | -11.37221 | -45.94426 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3110c548-d716-3cf1-a9d5-2624e7913587 | -10.0447 | -47.08117 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8b41243-b205-3a7d-8910-461be59eb553 | -2.47243 | -49.22943 | 2025-10-24 03:49:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7f2eca02-96ca-36b6-8e10-2c239f30f445 | -9.80291 | -45.76246 | 2025-10-24 03:49:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abb59c33-4426-38b5-8aae-0516a31f4a67 | -9.80843 | -45.76041 | 2025-10-24 03:49:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60822f02-0abb-3d6c-8f1e-a8b7f61667b0 | -6.10136 | -39.19169 | 2025-10-24 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8fd1e250-761e-32c4-8542-44285cce7792 | -5.61707 | -41.11595 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| beb5ebc3-ca8f-31df-951b-8913ef85e564 | -9.6061 | -46.9099 | 2025-10-24 03:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 891c16ef-f0f7-3747-8f91-17cf4a75711e | -9.6058 | -46.9322 | 2025-10-24 03:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 70422a57-c933-34c9-9416-7d495c18ad42 | -9.5872 | -46.912 | 2025-10-24 03:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 1f2f6f47-9f62-3446-9999-bbe194135299 | -21.17975 | -46.40547 | 2025-10-24 03:51:00 | NOAA-21 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 75a4e98a-f5f5-393c-bd4e-f370bfc6113d | -19.32909 | -46.49137 | 2025-10-24 03:51:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de5f38f0-4ac7-3674-b4cb-59f9eb195f38 | -18.36188 | -51.70224 | 2025-10-24 03:51:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 571edb7d-944f-39f2-a6d9-b9481902e3a8 | -19.98998 | -44.22962 | 2025-10-24 03:51:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cd3a54ca-769a-3fb0-b035-70ab4561b8df | -19.98707 | -44.22406 | 2025-10-24 03:51:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dc70f9c2-9b14-3482-872f-2b2f6bbbbebe | -17.31449 | -43.6034 | 2025-10-24 03:51:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a54ba662-392f-322e-b113-623e9179edce | -20.36082 | -45.79705 | 2025-10-24 03:51:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cff503ec-86da-377b-9896-c9a7aca4d09c | -18.83366 | -47.12237 | 2025-10-24 03:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abad1efe-345b-3bc7-b944-aa19934fce38 | -22.74184 | -47.16472 | 2025-10-24 03:51:00 | NOAA-21 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee95a8c9-3e33-3cf8-82e9-bce1426993fd | -20.49069 | -44.37287 | 2025-10-24 03:51:00 | NOAA-21 | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 81e091e1-60ec-3533-aff9-dab265d79599 | -21.03976 | -44.05608 | 2025-10-24 03:51:00 | NOAA-21 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README13.md)
