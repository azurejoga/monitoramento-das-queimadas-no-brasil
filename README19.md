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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 661a00ee-f36d-352c-841a-3336452f15cd | -3.45236 | -45.59663 | 2025-10-08 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 47e5642a-8f5e-32e3-a92f-6ad4d11f2106 | -15.94026 | -42.6021 | 2025-10-08 03:49:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 984b82a4-6e37-3ebd-ad62-7bb594741734 | -13.49962 | -43.67098 | 2025-10-08 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b25b93b1-5f1b-353d-930a-efa4ead28ee7 | -11.4491 | -50.2114 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3af15b42-d087-310d-ab99-a5914e62bca6 | -8.19852 | -44.11367 | 2025-10-08 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50a59357-5b6d-3eed-a896-425e8caabee8 | -8.52136 | -46.23907 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4f64445d-b81e-3ecb-af45-da2f8ea7024d | -13.38615 | -47.56337 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4fd26b8a-0f0d-32c3-bb45-049f99d8fb6c | -8.10797 | -44.7725 | 2025-10-08 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d61e1cd1-e344-3f43-a051-31779e3b345e | -11.6957 | -50.95957 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3193640-28ec-364e-9e19-380a42eab804 | -15.79282 | -43.65539 | 2025-10-08 03:49:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4136100c-234c-3a66-b1b7-e56a61f88560 | -10.89413 | -43.82018 | 2025-10-08 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e9765fc-bd08-33af-99a9-376981799a31 | -9.09296 | -47.96462 | 2025-10-08 03:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ce8a3fd-a9a3-3c9a-8232-9d80a2a3db99 | -9.16159 | -43.01988 | 2025-10-08 03:49:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 11feb1b5-b215-37b2-814b-bd810d13077c | -4.45413 | -40.7676 | 2025-10-08 03:49:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eb9beb39-b3a3-34fc-8d85-3cbe5af48aab | -8.25587 | -50.09532 | 2025-10-08 03:49:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8695aa88-dc14-38e4-9d0b-deeceea3214c | -12.15635 | -51.43976 | 2025-10-08 03:49:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9cc234c-8eb9-3b66-b1e4-7b03bdc1889b | -10.87502 | -47.10226 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbf52a46-90d2-316c-af9c-b906bd076b30 | -11.05284 | -44.78269 | 2025-10-08 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d21aba64-e347-39c9-b3a7-073f0efc6eb3 | -14.93719 | -46.79474 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a672ca5d-91eb-3aee-bc5c-3fff4dfd6727 | -11.18896 | -49.78035 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17fbe97a-52c6-307d-8eda-edcac2329834 | -11.70231 | -50.96096 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e24cd14a-2737-33eb-8377-c89e9f9e693f | -3.13567 | -40.99293 | 2025-10-08 03:49:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 68910bb9-2303-3291-b9c0-30736d786ab0 | -13.72835 | -45.66986 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9a47d1d-35a4-38da-8b03-b1b09687c9d6 | -12.79077 | -48.81748 | 2025-10-08 03:49:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4246e587-c906-3e09-823f-9c19d0179b9e | -12.91885 | -46.82864 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fc24ad0-a6d3-35fd-a2ab-3d058b159c9c | -13.37511 | -47.22836 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fd340f9-0300-3b0a-9a18-729d8610ef67 | -13.30466 | -48.0308 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0bca63e-6812-3cbf-8ad0-d2319b2792a3 | -9.54807 | -47.76916 | 2025-10-08 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2e72888-4fdc-369e-8f47-259a08d197a1 | -15.19556 | -40.54709 | 2025-10-08 03:49:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5138e53a-cee2-3e47-9b68-3dfddb368a3a | -13.34918 | -47.55738 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 542e673c-a34c-3af3-b3e6-a34f187f2e0e | -9.39731 | -45.94825 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0461ccc1-fa57-376f-a5cc-56ef10bf3265 | -11.45651 | -50.20737 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d2a88c7-840d-3df4-aa23-2fd83b34aa50 | -11.99197 | -46.77316 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1ec723ba-38cc-3d17-82c0-2e55da7c9550 | -11.90494 | -46.20026 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa84c900-383c-3226-9f53-2dd494ee2ac9 | -14.52589 | -46.64329 | 2025-10-08 03:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 551fb571-a65a-395d-adcd-d16ef498c40a | -15.26476 | -46.33427 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0116099b-6d93-3987-965f-767880122a4f | -15.02861 | -41.00037 | 2025-10-08 03:49:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 478084a9-34ec-30e3-927f-55264e1de19b | -15.42341 | -41.26885 | 2025-10-08 03:49:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8f16d091-3526-311a-82a0-b0861898fdf0 | -8.55577 | -46.23122 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e900b40f-1f3f-3b03-8166-a3895766b8a4 | -8.18936 | -44.11253 | 2025-10-08 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc598eb3-1542-37c8-8585-cdfd1dba6f9b | -11.14347 | -47.75444 | 2025-10-08 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7e52bd0-4908-3515-b7b3-f2cf152049bd | -8.18828 | -43.3394 | 2025-10-08 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0fb20c0b-9334-3cce-ac0a-60b47b247a21 | -9.77668 | -48.28483 | 2025-10-08 03:49:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56a825ae-c97a-386f-8ef5-e143666ee7aa | -11.9883 | -46.77571 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36cf27c9-617b-36ee-831d-fe6be90270d2 | -8.61776 | -45.10109 | 2025-10-08 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0410e3a-309f-31ca-b725-2a149003dd01 | -13.26767 | -48.04768 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b617fe6-fcac-38a6-8162-45a8c161e9f6 | -11.4419 | -43.48056 | 2025-10-08 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d109bbd-c28f-368e-b2c8-23c6a9c983f8 | -8.19117 | -43.34832 | 2025-10-08 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0ffc7f30-ca78-3837-a1c1-fbbc55423a51 | -10.86439 | -47.10047 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 024a4204-020d-3db4-9fdd-f7f4ee972793 | -9.18874 | -46.90924 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 885defa9-05d4-339a-82b0-0a3c8f07bd13 | -8.52247 | -46.23661 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c38b1456-0729-3268-855a-9a892b2ac6af | -9.39837 | -45.94237 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a60fb7d-894b-3892-85b8-c0fb6700f0d9 | -13.37 | -47.22741 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5732f69a-adb2-3e18-a8c5-3248eda33327 | -7.91646 | -47.13734 | 2025-10-08 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 808b05a9-f534-3ab2-b2ce-faedf74722e1 | -9.54516 | -47.76771 | 2025-10-08 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16445374-9677-3e42-825a-b33689d452a0 | -11.90969 | -46.20195 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a2e92a5-42dd-3c7a-9d70-a3c466a92ed2 | -12.0033 | -46.76901 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b69b554-b0d7-3a58-a983-4fdb90feedac | -11.83848 | -44.90871 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cc5de20-6935-34b5-9443-97f5aefe8d65 | -11.73773 | -50.95611 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e12d9830-e11d-3cac-9849-5484e5c5bab9 | -1.40952 | -46.70466 | 2025-10-08 03:49:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2aa908ee-0e9c-3c53-a0d3-960498061e94 | -14.74067 | -47.86274 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 256bf852-8bc9-3ef8-9326-4393e562ed9b | -2.66408 | -47.8717 | 2025-10-08 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f418df30-772b-329f-96fd-8630809a575c | -13.80711 | -45.80264 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c28c009-de0e-3f33-9224-e8a6e0dee9a2 | -9.20745 | -46.89843 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa5ac852-5396-3ca4-8fc8-304ec6611c78 | -13.2237 | -47.18894 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 588ed531-49dc-347a-87ba-467d8c8e0cc8 | -11.81077 | -45.13737 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64cc28ee-c8b8-3902-8e78-aa4df0c0cd4d | -9.67111 | -49.95159 | 2025-10-08 03:49:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a374608-5ada-3c76-81d9-f771d634a61a | -7.91088 | -47.13626 | 2025-10-08 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a93b9546-83fe-3496-8e56-f645b98b6e32 | -14.79378 | -46.072 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85f7c5bc-778f-351d-be8d-0c2ce3fe66a4 | -11.44541 | -50.20676 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3acf3ef-2e5e-3500-ac28-9ea661a5c2ab | -9.7616 | -47.68761 | 2025-10-08 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d3e744a-4331-3e69-920c-959a6fe64d22 | -14.70602 | -46.08708 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1cfd9add-8d57-34ff-bff1-0a7147fdf855 | -12.0178 | -45.19518 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc47dffb-f3fc-3e7c-8d87-59876697240c | -15.07403 | -46.62785 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a34943b-bea4-345c-a501-7e69e83f3916 | -14.69123 | -48.4127 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9dbed490-a048-338d-bdd2-9fa2965af82c | -13.29251 | -48.03561 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d29acdf-ab34-34d1-a409-d6a1cf6fbace | -11.73113 | -50.94349 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 45290d14-332c-3195-a305-ee93d6eb32f5 | -13.45904 | -50.40766 | 2025-10-08 03:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 272fe0d5-baa2-3a8f-a842-96e78250f0cc | -9.02651 | -45.80183 | 2025-10-08 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7dbd26a-cc21-3d82-b60e-4c747c809406 | -14.25618 | -45.85934 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92851a71-7f8f-34d6-9d55-e68155da4590 | -14.95883 | -46.83798 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7c50396-773b-354b-a078-80f8fe36e66f | -8.22751 | -44.19313 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0df2c2e-5616-3d1f-88f6-928afc50fd8d | -15.24505 | -46.36119 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 231377dd-8e6c-305b-bcb6-4af74fd44e0c | -7.80297 | -46.0234 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64bea910-775f-3876-aa9e-39183d24a87b | -8.22126 | -44.20177 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 597940b8-0cc1-36a8-ae76-b828f6253183 | -12.29284 | -40.21053 | 2025-10-08 03:49:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24bf9735-ea4e-3b1c-bd64-cae5186f9ce4 | -11.9974 | -47.19131 | 2025-10-08 03:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a0bd416-ccad-33c1-b5ae-5bb64e6e3906 | -13.7238 | -45.6688 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ebad975-d36e-3768-bf50-b9cf525d3f19 | -13.23967 | -47.22915 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dc534c6a-2564-33c5-8be2-3e62c2e5b671 | -15.31935 | -46.17481 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 4a7b1a13-1275-3f56-83f0-fc341a81c79a | -14.14464 | -43.17377 | 2025-10-08 03:49:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 78e8f87d-eb2d-30fd-b8bd-b8690eb28b37 | -14.88873 | -42.264 | 2025-10-08 03:49:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2819720a-671e-3f32-8615-8d271bea32ee | -11.85493 | -44.92062 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c233fc38-0a01-3b37-a5b4-693e529d5405 | -11.7093 | -50.98191 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 78a3c7c0-1ba0-352e-81f5-0dc3b5297d71 | -13.23638 | -47.19171 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f32e7ce5-5afa-3a93-8871-1022d0dfadff | -14.71345 | -46.07305 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67869a8f-fee7-30e6-995e-a44b89f81b15 | -13.8021 | -45.78277 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e078ee9-f661-3c22-906b-f01fda965a2a | -15.53086 | -42.3385 | 2025-10-08 03:49:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b25be28-9e89-3bf0-be20-e9c82f7bb540 | -11.86679 | -44.93217 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12c0cc07-f486-3597-837a-c255354efb44 | -11.70111 | -50.96687 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README20.md)
