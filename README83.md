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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03f7a1d3-3d99-3a12-9f6f-8764a1d03797 | -11.3436 | -54.1086 | 2026-09-28 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| fb964f7f-9084-3fa4-bfa1-ad8ca1a77684 | -10.8375 | -57.2178 | 2026-09-28 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 805626a0-1b26-33df-9dbe-c8da258f7ba9 | -7.9898 | -45.0065 | 2026-09-28 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| fc968497-1624-3990-81bf-2b95c7cd191e | 1.6381 | -56.0214 | 2026-09-28 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 8be01b23-fb6c-3303-8bf2-0dd157298fe6 | -10.6094 | -53.9902 | 2026-09-28 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 940d0bdb-0641-30d3-bd72-f3f9985b0456 | -11.9964 | -50.7563 | 2026-09-28 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 048325d2-3df9-34e1-81fc-126e00ce171e | 1.6749 | -55.9422 | 2026-09-28 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| df1643ab-5ca5-3dbd-a819-2378ec0fff95 | -10.9536 | -50.6805 | 2026-09-28 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 324.5 |
| 6976fc3c-8b5d-3c62-998a-95b43c520a05 | -10.6827 | -54.1679 | 2026-09-28 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 5d82a10a-2f28-35d1-82d4-1ca07ffc2935 | -12.1672 | -50.8004 | 2026-09-28 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 486977af-708d-3f72-b8a2-c5c5270fdde3 | -9.1525 | -49.9639 | 2026-09-28 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a8345add-5228-331f-a2f9-6be2f7750155 | -10.7115 | -60.7312 | 2026-09-28 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| ae55d5a2-8e35-38c3-bb50-5a4174d704df | -10.8187 | -57.2192 | 2026-09-28 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 777f429a-3a86-3e1a-bc85-9bed5a8eee56 | -11.6551 | -50.6887 | 2026-09-28 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 7d587410-b34d-3c4f-81f8-5be696aeed0e | -8.3617 | -45.4013 | 2026-09-28 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 174a8a4b-0601-3d28-a8c3-27e79b4a48f9 | 1.6749 | -55.9225 | 2026-09-28 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 21f9b05e-3e26-33ef-b74a-63f97140bb4b | -12.289 | -50.3143 | 2026-09-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| b7d8e6b7-f23f-3980-b17e-4e332f378be8 | -12.2508 | -50.3189 | 2026-09-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 7f6c95d6-9a92-3fc1-a150-8788cba1163a | -7.4869 | -44.5751 | 2026-09-28 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 99f548ef-0eea-3040-85a6-0fb884e2795a | -12.6463 | -47.2598 | 2026-09-28 15:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 4e3ef9dd-a503-3ea8-a904-28f468689d08 | -8.2807 | -54.7158 | 2026-09-28 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| aaaa745d-dd74-37cd-98b2-31ad9e048ce5 | -10.4229 | -53.8424 | 2026-09-28 15:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 748c5c26-81e9-3c3e-8c0c-548df1eb8446 | -12.3488 | -50.1563 | 2026-09-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| eeefb985-5b6e-33e6-9e32-9f331041993c | -11.8665 | -50.5362 | 2026-09-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 0f6d6990-e70c-3762-8c47-537de20804de | -10.9154 | -50.7059 | 2026-09-28 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 890bf3db-a2dd-30af-987f-5a75cf90335f | -12.8847 | -44.8015 | 2026-09-28 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| a6f7a4d9-c6ec-33e6-b866-051de57c6357 | -9.7874 | -44.8289 | 2026-09-28 15:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 148.6 |
| a80e4d1f-315f-340c-9c0a-e7191bb73562 | -7.449 | -44.6016 | 2026-09-28 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 7f41fce4-a4cd-395b-8686-29d5833f2c60 | -12.8851 | -44.7782 | 2026-09-28 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| bea4c40d-58fe-37e9-b3f9-3246b16ced9a | 3.7868 | -60.3155 | 2026-09-28 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a7bd2ebe-fe65-334e-ba1f-287fa6b8823f | -12.2699 | -50.3166 | 2026-09-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f14cfbb3-fe69-30c2-b5be-d2dbef073f1f | -11.1183 | -54.0062 | 2026-09-28 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 134fbb42-e1a8-3b31-8ece-ea0fdbf59226 | -10.8532 | -54.0916 | 2026-09-28 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fbb67b33-3bcc-3748-a12e-36cc99e9e81b | -20.1966 | -48.5773 | 2026-09-28 15:00:00 | GOES-19 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 5bb5e42e-454a-3e34-b3a2-aecbaa0eaae5 | -12.9649 | -51.0671 | 2026-09-28 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ebbad37d-72fb-3f5f-b706-01c5396dacba | -10.2067 | -49.9898 | 2026-09-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 205.5 |
| 31ac0173-b45a-338e-b972-35bf541ec306 | -15.4003 | -47.9035 | 2026-09-28 15:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 3695b0aa-103a-3cb3-91c2-e5d496c2579d | 1.6566 | -55.903 | 2026-09-28 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 32f29236-4343-37df-a184-d3e0035b9bf8 | -13.4325 | -57.061 | 2026-09-28 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 97046e71-cb1b-35bf-895a-a54e2e0b99c1 | -10.9538 | -50.6592 | 2026-09-28 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| c6678df5-ba58-35b5-8f97-00567133b448 | -10.8001 | -57.2007 | 2026-09-28 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 4db51a5c-bfbe-3ca2-abbd-8f8049577b2e | -10.11 | -50.1708 | 2026-09-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 2a2b4b56-5703-3cbb-87d8-b618a00371aa | -8.3608 | -45.4695 | 2026-09-28 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 1eca5295-5442-3ca3-9716-a52f7ae7b701 | -7.4974 | -55.0256 | 2026-09-28 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 474.6 |
| e344928d-d74a-38f7-bf04-ef351dd8f37d | -12.6836 | -47.3217 | 2026-09-28 15:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 9f57fee9-024c-375d-9663-a088eba5b4f5 | -10.9595 | -50.2529 | 2026-09-28 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 6ddb584d-d9f4-338c-99bc-17ce1c2df867 | -13.161 | -48.5437 | 2026-09-28 15:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| cdde95ad-337c-3b8a-b5af-399dfb3ffa68 | -8.6171 | -54.6126 | 2026-09-28 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 29cb3402-5d1c-39ad-a33e-ca8a507500df | -8.2291 | -45.4602 | 2026-09-28 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 195.3 |
| c4a277e0-d059-396f-94f2-75cea94724f9 | -11.9971 | -50.7135 | 2026-09-28 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d1ba6f49-9c54-3c7f-a5ff-a35335111d92 | -15.0616 | -54.5988 | 2026-09-28 15:00:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 131.1 |
| f46a8598-2f6e-3cee-a0bd-ad7c2c8f333d | -10.9156 | -50.6845 | 2026-09-28 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 055d8cf2-a54a-34d7-85c3-5f55acb65723 | 1.5835 | -55.8251 | 2026-09-28 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| c2dc7ace-aa29-3313-90de-e97338de2f0f | -11.0422 | -54.0542 | 2026-09-28 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f7e7fb4d-3af9-339c-8c29-57705728f98a | -11.3739 | -43.3972 | 2026-09-28 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 6f77c83f-1dd9-380d-9804-f67f2180254c | -8.2623 | -54.6969 | 2026-09-28 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 7a2f4157-103d-375f-b629-ece909821f05 | -10.8187 | -57.2192 | 2026-09-28 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 36186c0c-e606-3591-8e94-794acf749902 | -12.0609 | -50.2773 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 8cc30e68-c8c0-3366-9247-0cac8bf5318f | -11.6199 | -50.5004 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 30892427-5962-30db-a19e-286f8e14758b | 2.1266 | -50.8788 | 2026-09-28 15:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 80.4 |
| bd6b4dfc-ea5b-39ae-8ac8-b26238064e6e | 1.6018 | -55.8643 | 2026-09-28 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 3207f387-0550-35eb-b6f3-b892b3fda0e7 | -12.0984 | -50.3158 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| c80645bd-6fe0-37ad-a5b4-adc6aeb8483b | -15.112 | -53.8838 | 2026-09-28 15:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| db1fab03-2537-3655-85ff-621836714e43 | 1.5835 | -55.8448 | 2026-09-28 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| b2eeab6f-31cc-32bb-9389-fc3006901e6e | -12.3283 | -50.2449 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a19effaf-7689-3a8f-9e3e-74f2207b92d0 | -12.1952 | -52.7821 | 2026-09-28 15:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e0a4d136-47b0-327a-ae6e-d7a3da60f659 | -12.6836 | -47.3217 | 2026-09-28 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 0c2afb50-1610-3a9c-8c23-bc5574c43d37 | -16.3585 | -41.6045 | 2026-09-28 15:10:00 | GOES-19 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 124.6 |
| 9f11789a-55b7-3495-96df-a1d30123337b | -11.7522 | -50.5494 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 979ae773-b853-3535-b3d9-558be1a503d5 | 3.7868 | -60.3155 | 2026-09-28 15:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| a8a9dedd-7051-321f-afd9-839d6b0e0d16 | -12.2502 | -50.362 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 3b65b092-28d4-34a3-8d85-fd465a21bb2a | -13.161 | -48.5437 | 2026-09-28 15:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 1fe5cc8c-0978-3f28-b117-8ff5d315da96 | -10.8191 | -57.1795 | 2026-09-28 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a2e0e624-4234-35c6-a7fa-153fc12380fb | -7.7037 | -54.7722 | 2026-09-28 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 0aaf7cad-7868-335a-be3b-fd4cb0e35cbd | -7.7086 | -44.92 | 2026-09-28 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 65b2cf69-733d-3d5c-8205-bedd182a73f9 | -8.2291 | -45.4602 | 2026-09-28 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 5bc76659-241d-3a97-a6ed-cdf2ce3b664b | -10.8185 | -57.2391 | 2026-09-28 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| c67fa61d-d039-355b-a413-f6218020c47c | -11.7122 | -50.6822 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b9bc4062-9368-326c-9a7c-24e4f07a351a | -11.0991 | -54.0285 | 2026-09-28 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 68e3fd7f-ebd6-355e-84db-7128b868c87d | -15.3998 | -47.9261 | 2026-09-28 15:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7b4c13fe-d67b-37f0-bfad-172b44203a43 | -9.1057 | -60.9511 | 2026-09-28 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 22cb233f-7b23-36e6-a33c-7c0d26232f4a | -15.1847 | -46.141 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 124.0 |
| c7784629-2144-3d56-bf43-b5e77ded7a90 | 1.2613 | -50.6845 | 2026-09-28 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3dbf408e-002b-38b0-ad7b-25a3aec8bcde | -12.9649 | -51.0671 | 2026-09-28 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 43844fb9-1c0e-36e6-a27d-13dff908db3f | -15.4003 | -47.9035 | 2026-09-28 15:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 78e1c289-5811-3e2d-a069-745f1e18c4ed | -12.2498 | -50.3835 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c01e0ca5-fc22-3d89-adbb-3b6ce0de2789 | -11.809 | -50.5642 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 39641d35-0523-3671-9b48-760ce574efe6 | -11.3436 | -54.1086 | 2026-09-28 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a25918e7-02ea-37e2-b8c6-1f04ea1d5b00 | -9.9779 | -50.184 | 2026-09-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| e39e5aef-86ed-3e0b-8e63-d21ef381cad1 | -12.2311 | -50.3643 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| fb4db666-a1df-3498-b77a-db844064ad5a | -11.0235 | -54.0354 | 2026-09-28 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| ced31e81-1d12-3697-869c-180124369e79 | 3.7504 | -60.2782 | 2026-09-28 15:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 5eacddd2-57e1-3537-af94-9a3a99c30216 | -11.5628 | -50.5069 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 4215ca50-3ede-3b79-99c5-2350f99c3e0f | -8.206 | -54.7408 | 2026-09-28 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| b60ae52d-44af-3064-8c6c-fbb1deb75828 | -13.4325 | -57.061 | 2026-09-28 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6192c460-a5ae-3518-bfb9-4bc56e659009 | -9.1771 | -61.3882 | 2026-09-28 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 57bd70bb-7ac7-3c05-99df-03f03b3c8420 | -10.7115 | -60.7312 | 2026-09-28 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 42780106-630c-3a58-9f7b-f5fde2762c6d | -11.0396 | -51.3079 | 2026-09-28 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 790d7abe-1b84-3cc0-bc4d-f7101b1f9aeb | -12.6704 | -46.9866 | 2026-09-28 15:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 159.8 |
| f86d7cda-dc72-35ee-9e4c-bb5373bc9d7f | -9.0838 | -61.4499 | 2026-09-28 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |


[Clique aqui para ver as próximas entradas](README84.md)
