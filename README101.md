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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f847d8a2-a2e1-3505-84a5-3056d45c5200 | -11.73822 | -47.75679 | 2025-09-04 12:17:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 181.0 |
| d3650fc7-21f8-3ca2-83ed-3b61a7db0df5 | -13.85644 | -47.9642 | 2025-09-04 12:17:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2d735bd3-012f-3979-8bd3-ae479ab3abb1 | -10.15679 | -46.25001 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5b486771-cb5a-34be-a1f0-0853893baca8 | -11.8614 | -51.43653 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 87c77234-bd94-3360-9072-a65e65f7b7e1 | -15.00405 | -50.03361 | 2025-09-04 12:17:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8176417a-a846-3e7c-a2f9-5658d002cd78 | -15.19691 | -52.36208 | 2025-09-04 12:17:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 0cc650c9-662e-35c0-ac7f-e76cddee025d | -14.53983 | -48.08852 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 394859f2-c066-38e0-8d9a-3978048e7c42 | -15.05891 | -50.05245 | 2025-09-04 12:17:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 1a42b652-1bfc-31b5-81b3-da1495ebe131 | -10.49094 | -46.75742 | 2025-09-04 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 630a3b91-0cd8-3964-9d74-2356a22fcc8d | -10.98967 | -49.72579 | 2025-09-04 12:17:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8c89f79f-a5bd-3383-bf9d-2a848da2f7b4 | -8.19963 | -49.60065 | 2025-09-04 12:17:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 2eca7bcc-9470-3607-b784-d3e3bb128a57 | -14.80302 | -48.30507 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e8d7291f-8bb0-3f0d-9569-bdda93fdf941 | -11.85704 | -51.46417 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| afb501ce-a1c5-362a-b8d7-38fa91f0265a | -13.00958 | -48.07943 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 418fa9f8-2303-3aea-84b0-41c5f0f0c724 | -8.87028 | -47.93376 | 2025-09-04 12:17:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f763fd71-9156-3705-96b4-4f92dead6784 | -8.35823 | -48.33918 | 2025-09-04 12:17:00 | TERRA_M-T | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 33.6 |
| a36eaa20-4558-3e46-b910-7293501007b0 | -12.90641 | -48.02954 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bdcd4ab0-f733-3a6f-b826-d037be2e8613 | -12.48265 | -48.0852 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| d59e455b-b217-3e40-af25-033f2194598f | -14.56897 | -49.13344 | 2025-09-04 12:17:00 | TERRA_M-T | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e106626b-8810-33b6-8461-3d13c4289707 | -14.80167 | -48.31428 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 1e41c0ed-5ff6-3384-94d5-b819217455e4 | -9.54556 | -48.35672 | 2025-09-04 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 2794c090-b8e7-3d97-9a5a-e103c64e5cba | -14.78192 | -48.12783 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7a1be3fe-e890-3981-ac66-ff5aedb26de3 | -11.80252 | -51.52709 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 503c058b-3fce-3fe9-8bbe-821fa7e82eb2 | -11.79025 | -50.64552 | 2025-09-04 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5ee82e4a-ba88-3d2b-9d4b-99c640f572dc | -12.51353 | -48.06802 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5e473b23-384c-3652-b535-14d180eb621b | -11.8788 | -50.60358 | 2025-09-04 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d3a3c4be-a041-345f-bff5-1601a65ccab9 | -11.35814 | -46.87406 | 2025-09-04 12:17:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d204d5d6-51ec-3e35-bc50-6db8755daab9 | -12.23725 | -50.14423 | 2025-09-04 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 98016439-1903-3cf0-9afa-854a3c712395 | -9.72676 | -48.31633 | 2025-09-04 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| dd3d16ea-3b9e-3a4c-9bf1-77f1dbd50844 | -12.00379 | -46.74498 | 2025-09-04 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0c4380a5-5758-3bfe-ac49-fe61b5ac2840 | -15.04785 | -50.06194 | 2025-09-04 12:17:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 12008ebe-e3fd-3e75-9a1f-5f07b55b9723 | -11.73688 | -47.7659 | 2025-09-04 12:17:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 87fd2dee-8f4a-38ad-93fe-1ee39fcbbf7d | -9.30601 | -47.09835 | 2025-09-04 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 1c41acbb-ce02-31c2-86c7-8b03336e7ae2 | -12.50461 | -48.06669 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| dea7ed68-315b-37dc-8d4b-c85c94d76f59 | -8.57577 | -44.3271 | 2025-09-04 12:17:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7452d2c1-0b64-3b15-b782-d53364b7d26d | -8.0571 | -47.56772 | 2025-09-04 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 944f1abd-91e6-3b02-ba89-ac8ca2275387 | -13.85246 | -47.99148 | 2025-09-04 12:17:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 8053548f-4340-396c-adc9-68aeebeef984 | -11.5813 | -52.11238 | 2025-09-04 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5440629a-eb89-3389-88d8-611022b8e7b1 | -13.31087 | -51.76758 | 2025-09-04 12:17:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| de4b706f-d914-3c98-bb94-352d81ea0d97 | -12.50598 | -48.05745 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ce34b039-f0d1-39ec-a16e-9fd6409a8580 | -10.75722 | -48.27592 | 2025-09-04 12:17:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7010feaa-09de-3f25-9da5-0a2dfae92b6b | -11.72933 | -47.75549 | 2025-09-04 12:17:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 84104a49-46bb-38fc-942d-c056936d932d | -11.96427 | -45.78313 | 2025-09-04 12:17:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 0897bd5d-5797-3664-a2cb-ccc1813feeef | -9.66376 | -46.0943 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 103758b2-cdb1-3c09-839b-dd305e6458e1 | -12.65627 | -45.30247 | 2025-09-04 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| b872f456-7507-352a-86df-f7e285bc9751 | -10.53513 | -46.76375 | 2025-09-04 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b81b36be-adf2-3376-81fa-1279a68a3d2b | -9.30731 | -47.08938 | 2025-09-04 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| f16f729b-29bb-347a-a253-c870c47989b8 | -10.4649 | -50.40447 | 2025-09-04 12:17:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6c13c43c-7d91-3bb4-b770-c9d588d57d70 | -13.85511 | -47.97327 | 2025-09-04 12:17:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 6465e530-4fb0-3b58-a1fb-8d5069b4dfc4 | -13.23487 | -40.94187 | 2025-09-04 12:17:00 | TERRA_M-T | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 11508f74-3488-3323-b2a6-9d9035c5cdfe | -12.51099 | -44.72836 | 2025-09-04 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d47ed421-cf2e-31cd-9130-20a95bfe131a | -8.37829 | -48.33194 | 2025-09-04 12:17:00 | TERRA_M-T | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| a8843f18-5c2f-3cc1-9f92-5f6494578a5d | -13.28297 | -46.8226 | 2025-09-04 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e13a8e8-df3f-37eb-b340-6488071b0116 | -12.30185 | -50.00161 | 2025-09-04 12:17:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 95a5465f-e8f1-332f-9e22-1b9ffd3fcffc | -10.15424 | -46.26792 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| aeddc8c7-76e2-36b7-a18f-f89dcdb01185 | -10.99702 | -45.91668 | 2025-09-04 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| a0064d6f-8b8d-37c3-8db7-d4fc9644e6fa | -14.53364 | -48.06892 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1d8799f4-9a65-3753-9282-69b4a8858e5b | -8.88093 | -49.83792 | 2025-09-04 12:17:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 0aa21b67-90b8-3cf8-bef2-cbd293bc3eb9 | -11.81693 | -48.15903 | 2025-09-04 12:17:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 789a6e93-2d05-38db-af43-4db7482be5db | -15.49719 | -43.55664 | 2025-09-04 12:17:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 88d2e0ef-d1cb-3be5-bfa6-c85261f9f1c5 | -9.66249 | -46.10328 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 660ec62d-bad8-39b2-ae64-b47963a2ea6d | -10.99602 | -49.74921 | 2025-09-04 12:17:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| f26d0b0c-98e7-3035-83d5-687c4070b5a8 | -10.66248 | -51.58392 | 2025-09-04 12:17:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 343.5 |
| c85fff4f-c305-3aaa-8c2f-82f5b5680679 | -9.84402 | -46.12302 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 02e208ca-ae52-31d9-8778-fd8e72ee7bdb | -11.96558 | -45.77372 | 2025-09-04 12:17:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 1c6c866b-493f-3b78-9ea8-232a69cc014c | -14.81809 | -48.32609 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 42a05974-e83a-377b-9130-a0f1613bb93a | -12.30013 | -50.01258 | 2025-09-04 12:17:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 37a1c222-846c-3d07-be5d-fbbaa57a478a | -10.66019 | -51.59866 | 2025-09-04 12:17:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| c0a9da36-4e7e-36ed-885a-3f0df3f0b740 | -14.78059 | -48.13697 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7a6acb9b-61b6-3435-bed4-b8d29ccebb8d | -10.16397 | -47.22985 | 2025-09-04 12:17:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 3de8c6f2-6d81-38db-b226-07db927b9746 | -12.66418 | -45.31369 | 2025-09-04 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 29d09f6d-8af5-3567-aca8-4a9de8f1a4b0 | -8.90026 | -45.82077 | 2025-09-04 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 1e119faa-1760-3663-b120-27d483e7be61 | -9.87368 | -46.56159 | 2025-09-04 12:17:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 1583e0e4-c1d5-32ac-8c39-a192df5d238e | -22.27118 | -49.56818 | 2025-09-04 12:19:00 | TERRA_M-T | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 286ac0aa-912c-3e98-8f66-c0335674822d | -19.38664 | -45.65959 | 2025-09-04 12:19:00 | TERRA_M-T | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f0981a99-8ec9-3633-b92b-9b3e852057d1 | -21.3524 | -46.87166 | 2025-09-04 12:19:00 | TERRA_M-T | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 8e3b1100-61bd-346b-af55-8d873b39c65a | -20.96345 | -44.91022 | 2025-09-04 12:19:00 | TERRA_M-T | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 42687a4d-d472-3409-bcdc-c31e2a59da9b | -18.7673 | -47.64483 | 2025-09-04 12:19:00 | TERRA_M-T | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0ce76fc-ae1f-3aa6-b063-bc11b900850d | -20.16677 | -46.58974 | 2025-09-04 12:19:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7ba43726-a51e-3a06-9db1-5a29ca66c1cf | -17.14581 | -46.24689 | 2025-09-04 12:19:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 85a6c4a9-0c9a-34ca-9f0c-f233b3f9a9f1 | -23.11683 | -52.08163 | 2025-09-04 12:19:00 | TERRA_M-T | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 63b2e76a-d90d-3f9f-9433-65cda3c4b456 | -16.20679 | -48.73264 | 2025-09-04 12:19:00 | TERRA_M-T | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 273f1e73-f4ad-3908-8f8c-464dfe303390 | -16.30141 | -45.68787 | 2025-09-04 12:19:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 90664965-dd7d-382a-ab06-68a917edf88a | -17.5846 | -49.07965 | 2025-09-04 12:19:00 | TERRA_M-T | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 63a83e8a-50b3-35aa-abd0-126a28408a7c | -24.95814 | -50.54998 | 2025-09-04 12:19:00 | TERRA_M-T | IPIRANGA | PARANÁ | Brasil | 4110508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f1f4e39f-cd19-36f3-a889-0ec055804c81 | -15.73448 | -53.63608 | 2025-09-04 12:19:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 53a77c4c-d6ea-3ff7-910b-01e4dce4fe83 | -16.70221 | -44.96272 | 2025-09-04 12:19:00 | TERRA_M-T | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5c954332-cb7e-3025-91ac-20dc7ac0d8e6 | -17.53172 | -49.12896 | 2025-09-04 12:19:00 | TERRA_M-T | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c9fa679e-1f13-3a4e-aa14-662d9aed7c4d | -18.22478 | -52.61927 | 2025-09-04 12:19:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2a370a0c-d3af-3432-b5a8-20805ac3acd5 | -23.39429 | -46.83782 | 2025-09-04 12:19:00 | TERRA_M-T | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| c4cd4b4d-3ddf-3246-be25-6f7f706f7bb0 | -18.86227 | -47.3557 | 2025-09-04 12:19:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 29cfa4f9-2d9f-31c9-9d4b-3f690f717f00 | -20.10364 | -50.00728 | 2025-09-04 12:19:00 | TERRA_M-T | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.3 |
| 16edbf9b-b292-36e4-b249-f4139000e6b6 | -20.75377 | -45.22201 | 2025-09-04 12:19:00 | TERRA_M-T | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 4a57d96f-ad85-344c-a272-3a2b4a4347e2 | -18.7686 | -47.63538 | 2025-09-04 12:19:00 | TERRA_M-T | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 90fe4f0a-75e4-3fc6-995c-d5093df0cdc3 | -22.99943 | -50.44546 | 2025-09-04 12:19:00 | TERRA_M-T | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 65495f6b-ef1a-3576-bb3b-a5b206643f1f | -23.29888 | -46.6297 | 2025-09-04 12:19:00 | TERRA_M-T | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| c26415ad-764b-3f4e-86a9-4567f95c9cd9 | -22.29104 | -52.04487 | 2025-09-04 12:19:00 | TERRA_M-T | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 2855a42e-40d2-3dd7-b04e-7d5f33cf57ec | -17.06211 | -46.45039 | 2025-09-04 12:19:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 21beab6d-c23e-3bb8-9aa8-92b6b41c681d | -17.5228 | -49.12753 | 2025-09-04 12:19:00 | TERRA_M-T | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| f44ba2e0-6878-34d7-a875-4aa49b5a455c | -19.12247 | -46.44229 | 2025-09-04 12:19:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README102.md)
